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
from azure.mgmt.web.models import AppServicePlan, Site, SiteConfig, SkuDescription
from azure.cli.command_modules.appservice.custom import config_diagnostics


logger = get_logger(__name__)


def init_oz(client, location, name=None, tags=None):
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


def destroy_oz(client, confirm=True):
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
    try:
        project = get_project_settings()
    except NoProjectSettingsError:
        raise CLIError("Can't find a project settings directory. Run `init` first.")

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

    _runtime_internal = "{0}|{1}".format(runtime.upper(), version)
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

    update_project_settings(app_service=True, app_name=_app_name)

    creds_task = client.web_apps.begin_list_publishing_credentials(
        resource_group_name=project.resource_group_name, name=_app_name
    )
    creds = creds_task.result()
    init_local_folder(creds.scm_uri)
    update_project_settings(git_url=creds.scm_uri)
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
    return
