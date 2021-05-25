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
    update_project_settings,
    NoProjectSettingsError,
)
from .localgit import init_local_folder
from .runtimes import RUNTIME_GROUPS, get_runtime_versions, map_version_dict
from .skus import WEBAPP_SKUS
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
from urllib.parse import quote_plus


logger = get_logger(__name__)


def init_ez(client, location, name=None, tags=None):
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


def destroy_ez(client, confirm=True):
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


def create_app(cmd, client, runtime=None, version=None, sku="F1"):
    project = get_project_settings()

    if not runtime:
        runtime = RUNTIME_GROUPS[
            prompting.prompt_choice_list("Select a runtime", RUNTIME_GROUPS)
        ]

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
    plan = plan_task.result()
    logger.info("SKU changed to %s.", sku)
