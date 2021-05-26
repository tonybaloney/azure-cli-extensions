# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
import knack.prompting as prompting
from knack.util import CLIError
from .name_generator import app_name
from .config import (
    init_project_settings,
    get_project_settings,
    destroy_project_settings,
    load_dot_env,
    update_project_settings,
    save_dot_env,
    NoProjectSettingsError,
)
from .localgit import init_local_folder
from .runtimes import RUNTIME_GROUPS, get_runtime_versions, map_version_dict
from .skus import WEBAPP_SKUS, DB_SKUS, DB_ENGINES, DB_STORAGE_SIZES
from ._client_factory import app_client_factory
from azure.mgmt.web.models import (
    AppServicePlan,
    Site,
    SiteConfig,
    SkuDescription,
    HostNameBinding,
)
from azure.cli.command_modules.appservice.custom import (
    config_diagnostics,
    get_streaming_log,
)
from secrets import token_hex, token_urlsafe
from urllib.parse import quote_plus
from webbrowser import open as browse

DEFAULT_LOCATION = "westus"

logger = get_logger(__name__)


def ez_init(client, location, name=None, tags=None):
    if not name:
        name = app_name()
    logger.info("Creating project %s.", name)
    params = {
        "location": location,
        "tags": tags,
    }
    rg = client.resource_groups.create_or_update(
        resource_group_name=name, parameters=params
    )
    init_project_settings(resource_group_name=name, region=location)
    logger.info("Project created %s.", name)
    logger.info("Your Azure settings have been written to .azure/settings.json")
    return rg


def ez_destroy(client, confirm=True):
    try:
        project = get_project_settings()
    except NoProjectSettingsError:
        logger.warning("Can't find a project settings directory. Nothing to destroy.")
        return

    logger.info("Destroying project %s.", project.resource_group_name)
    job = None
    if not confirm or prompting.prompt_y_n(
        "Do you want to destroy the resource group on Azure too?"
    ):
        job = client.resource_groups.begin_delete(project.resource_group_name)

    destroy_project_settings()
    logger.info("Your Azure settings removed from .azure/settings.json")
    return job


def app_create(cmd, client, runtime=None, version=None, sku=None):
    project = get_project_settings()

    if not runtime:
        runtime = RUNTIME_GROUPS[
            prompting.prompt_choice_list("Select a runtime", RUNTIME_GROUPS)
        ]
    if not sku:
        sku = WEBAPP_SKUS[0]["name"]

    _plan_name = "{0}-plan".format(project.resource_group_name)
    _app_name = "{0}-app".format(project.resource_group_name)

    _version_options = get_runtime_versions(runtime)
    if not version:
        version = _version_options[
            prompting.prompt_choice_list(
                "Select a version", _version_options, default=1
            )
        ]
    else:
        if version not in _version_options:
            raise CLIError(
                "Version %s is not a valid option for runtime %s." % (version, runtime)
            )

    logger.info("Creating %s %s app named %s.", runtime, version, _app_name)

    # Create service plan
    plan_task = client.app_service_plans.begin_create_or_update(
        resource_group_name=project.resource_group_name,
        name=_plan_name,
        app_service_plan=AppServicePlan(
            location=project.region,
            sku=SkuDescription(
                name=sku,
            ),
        ),
    )
    plan = plan_task.result()
    logger.info("Created plan %s.", plan.name)
    logger.info("Creating webapp %s.", _app_name)
    # create a web app
    webapp_task = client.web_apps.begin_create_or_update(
        project.resource_group_name,
        _app_name,
        site_envelope=Site(
            location=project.region,
            server_farm_id=plan.id,
            site_config=SiteConfig(
                scm_type="LocalGit", **map_version_dict(runtime, version)
            ),
        ),
    )

    webapp = webapp_task.result()
    logger.info("Created webapp %s.", webapp.name)

    update_project_settings(
        app_service=True, app_name=_app_name, app_plan_name=_plan_name
    )

    creds_task = client.web_apps.begin_list_publishing_credentials(
        resource_group_name=project.resource_group_name, name=_app_name
    )
    creds = creds_task.result()
    git_url = "https://{0}:{1}@{2}.scm.azurewebsites.net/{3}.git".format(
        quote_plus(creds.publishing_user_name),
        quote_plus(creds.publishing_password),
        creds.name,
        creds.name,
    )
    init_local_folder(git_url)
    update_project_settings(git_url=git_url)
    config_diagnostics(
        cmd,
        resource_group_name=project.resource_group_name,
        name=_app_name,
        level="info",
        application_logging="filesystem",
        web_server_logging="filesystem",
        docker_container_logging="filesystem",
        detailed_error_messages=True,
    )

    logger.info("When you're ready to deploy, do `git push azure`.")
    return webapp


def app_settings(client):
    project = get_project_settings()
    settings = client.web_apps.list_application_settings(
        resource_group_name=project.resource_group_name, name=project.app_name
    )
    return settings.properties


def app_logs(cmd):
    project = get_project_settings()
    get_streaming_log(cmd, project.resource_group_name, project.app_name)


def app_set_domain(client, domain):
    project = get_project_settings()
    logger.info("Setting domain to %s.", domain)

    # Check the plan first
    plan = client.app_service_plans.get(
        resource_group_name=project.resource_group_name,
        name=project.app_plan_name,
    )
    if plan.sku.family == "F":
        logger.error(
            "Cannot set custom domain names for Free tier web apps. Upgrade before setting."
        )
        return

    client.web_apps.create_or_update_host_name_binding(
        project.resource_group_name,
        project.app_name,
        domain,
        HostNameBinding(site_name=project.app_name),
    )
    update_project_settings(app_domain_name=domain)
    logger.info("Domain configured successfully", domain)


def app_scale(client, sku=None):
    project = get_project_settings()
    if not sku:
        choice = prompting.prompt_choice_list("Select a SKU", WEBAPP_SKUS)
        sku = WEBAPP_SKUS[choice]["name"]

    logger.info("Setting SKU to %s.", sku)
    plan_task = client.app_service_plans.begin_create_or_update(
        resource_group_name=project.resource_group_name,
        name=project.app_plan_name,
        app_service_plan=AppServicePlan(
            location=project.region,
            sku=SkuDescription(
                name=sku,
            ),
        ),
    )
    plan_task.result()
    logger.info("SKU changed to %s.", sku)


def app_open():
    project = get_project_settings()
    if project.app_domain_name:
        url = "https://{0}/".format(project.app_domain_name)
    else:
        url = "https://{0}.azurewebsites.net/".format(project.app_name)
    browse(url)


def app_oryx():
    project = get_project_settings()
    url = "https://{0}.scm.azurewebsites.net/".format(project.app_name)
    browse(url)


def app_get(client, overwrite=False):
    # TODO : Spec out the overwrite method
    webapps = list(client.web_apps.list())
    webapp_names = [webapp.name for webapp in webapps]
    webapp = webapps[prompting.prompt_choice_list("Select a web app", webapp_names)]
    init_project_settings(webapp.resource_group, region=webapp.location)
    _plan_name = "{0}-plan".format(webapp.resource_group)
    update_project_settings(
        app_service=True,
        app_name=webapp.name,
        app_plan_name=_plan_name,
        app_domain_name=webapp.default_host_name,
    )
    app_settings_task = client.web_apps.list_application_settings(
        resource_group_name=webapp.resource_group, name=webapp.name
    )
    app_settings_dict = app_settings_task.properties
    save_dot_env(app_settings_dict)
    creds_task = client.web_apps.begin_list_publishing_credentials(
        resource_group_name=webapp.resource_group, name=webapp.name
    )
    creds = creds_task.result()
    git_url = "https://{0}:{1}@{2}.scm.azurewebsites.net/{3}.git".format(
        quote_plus(creds.publishing_user_name),
        quote_plus(creds.publishing_password),
        creds.name,
        creds.name,
    )
    init_local_folder(git_url)
    update_project_settings(git_url=git_url)

    if "DATABASE_URL" not in app_settings_dict:
        return
    _db_name = "{0}-db".format(webapp.resource_group)
    update_project_settings(
        database=True, db_name=_db_name, db_engine=app_settings_dict["DATABASE_NAME"]
    )


def db_create(cmd, client, engine=None, sku=None, size=None):
    from azure.mgmt.rdbms.mysql.models import (
        ServerForCreate,
        ServerPropertiesForDefaultCreate,
        StorageProfile,
        Sku,
        FirewallRule,
    )
    from azure.mgmt.rdbms.mysql_flexibleservers.models import (
        ServerVersion as MySQLVersion,
    )
    from azure.mgmt.rdbms.postgresql_flexibleservers.models import (
        ServerVersion as PostgresVersion,
    )
    from requests import get

    public_ip = get("https://api.ipify.org").text

    project = get_project_settings()
    if not engine:
        engine = DB_ENGINES[
            prompting.prompt_choice_list("Select a DB engine", DB_ENGINES)
        ]
    if not sku:
        sku = DB_SKUS[engine][0]
    if not size:
        size = DB_STORAGE_SIZES[0]["name"]
    ADMIN_USER = "admin_{0}".format(token_hex(8))
    ADMIN_PASSWORD = token_urlsafe(20)

    # TODO : Allow choice of version.
    if engine == "mysql":
        DB_VERSION = MySQLVersion.EIGHT0
    elif engine == "postgres":
        DB_VERSION = PostgresVersion.TWELVE
    else:
        raise NotImplementedError

    _db_name = "{0}-db".format(project.resource_group_name)

    client = getattr(client, engine)
    logger.info("Creating database server %s.", _db_name)

    server_creation_poller = client.servers.begin_create(
        project.resource_group_name,
        _db_name,
        ServerForCreate(
            properties=ServerPropertiesForDefaultCreate(
                administrator_login=ADMIN_USER,
                administrator_login_password=ADMIN_PASSWORD,
                version=DB_VERSION,
                storage_profile=StorageProfile(storage_mb=size),
            ),
            location=project.region,
            sku=Sku(
                name=sku, tier="Burstable"
            ),  # TODO : allow for choice of [Burstable, GeneralPurpose, MemoryOptimized]
        ),
    )

    server = server_creation_poller.result()
    logger.info("Created database server %s.", _db_name)

    update_project_settings(database=True, db_name=_db_name, db_engine=engine)

    env_dict = {
        "DATABASE_URL": f"{engine}://{ADMIN_USER}%40{_db_name}.{engine}.database.azure.com:{ADMIN_PASSWORD}@{_db_name}.{engine}.database.azure.com/{engine}",
        "DATABASE_HOST": f"{_db_name}.{engine}.database.azure.com",
        "DATABASE_USER": f"{ADMIN_USER}@{_db_name}.{engine}.database.azure.com",
        "DATABASE_PASSWORD": ADMIN_PASSWORD,
        "DATABASE_NAME": engine,
    }

    # Write .env
    save_dot_env(env_dict)

    # Save settings to web app
    app_client = app_client_factory(cmd.cli_ctx)
    logger.info("Updating web app settings.")

    preview_app_settings = app_client.web_apps.list_application_settings(
        resource_group_name=project.resource_group_name, name=project.app_name
    )
    preview_app_settings.properties.update(env_dict)
    app_client.web_apps.update_application_settings(
        resource_group_name=project.resource_group_name,
        name=project.app_name,
        app_settings=preview_app_settings,
    )
    logger.info("Updated web app settings.")

    logger.info("Adding a firewall rule for your IP, %s.", public_ip)
    # Open access to this server for IPs
    rule_creation_poller = client.firewall_rules.begin_create_or_update(
        resource_group_name=project.resource_group_name,
        server_name=_db_name,
        firewall_rule_name="allow_local_connection",
        parameters=FirewallRule(
            start_ip_address=public_ip,
            end_ip_address=public_ip,
        ),
    )

    rule_creation_poller.result()
    logger.info("Added a firewall rule for your IP, %s.", public_ip)

    return server


def db_scale(client, sku=None):
    from azure.mgmt.rdbms.mysql_flexibleservers.models import (
        ServerForUpdate,
        Sku,
    )

    project = get_project_settings()
    assert project.database
    engine = project.db_engine
    if not sku:
        choice = prompting.prompt_choice_list("Select a SKU", DB_SKUS[engine])
        sku = DB_SKUS[engine][choice]
    client = getattr(client, engine)
    logger.info("Setting SKU to %s.", sku)

    server_update = client.servers.begin_update(
        project.resource_group_name,
        project.db_name,
        ServerForUpdate(
            sku=Sku(name=sku, tier="Burstable"),
        ),
    )
    server_update.result()
    logger.info("SKU changed to %s.", sku)
    return


def db_connect():
    from os import spawnvpe, P_WAIT, environ

    project = get_project_settings()
    assert project.database
    if project.db_engine == "postgres":
        shell = "psql"
    elif project.db_engine == "mysql":
        shell = "mysql"
    else:
        raise NotImplementedError

    env = load_dot_env()
    res = spawnvpe(P_WAIT, shell, [env["DATABASE_URL"]], environ)
    if res != 0:
        raise Exception(
            "Could not run {0}, make sure you have it installed".format(shell)
        )
