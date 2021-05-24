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


def get_app_oz(
    cmd,
):
    raise CLIError("TODO: Implement `oz list`")
