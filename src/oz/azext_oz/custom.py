# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
import knack.prompting as prompting
from knack.util import CLIError
from .name_generator import app_name
from .config import (init_project_settings,
                     get_project_settings,
                     destroy_project_settings,
                     NoProjectSettingsError)
from .runtimes import RUNTIME_GROUPS, get_runtime_versions


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


def destroy_oz(client):
    try:
        project = get_project_settings()
    except NoProjectSettingsError:
        logger.warning("Can't find a project settings directory. Nothing to destroy.")
        return

    logger.info("Destroying project %s.", project.resource_group_name)
    job = None
    if prompting.prompt_y_n("Do you want to destroy the resource group on Azure too?"):
        job = client.resource_groups.begin_delete(project.resource_group_name)
    destroy_project_settings()
    logger.info("Your Azure settings removed from .azure/settings.json")
    return job


def create_app(client, runtime=None, version=None, sku="F1"):
    try:
        project = get_project_settings()
    except NoProjectSettingsError:
        raise CLIError("Can't find a project settings directory. Run `init` first.")

    if not runtime:
        runtime = RUNTIME_GROUPS[prompting.prompt_choice_list("Select a runtime", RUNTIME_GROUPS)]
    app_name = "{0}-app".format(project.resource_group_name)
    
    _version_options = get_runtime_versions(runtime)
    if not version:
        version = _version_options[prompting.prompt_choice_list("Select a version", _version_options, default=1)]
    else:
        if version not in _version_options:
            raise CLIError("Version %s is not a valid option for runtime %s." % (version, runtime))

    _runtime_internal = "{0}|{1}".format(runtime.upper(), version)
    logger.info("Creating %s %s app named %s.", runtime, version, app_name)