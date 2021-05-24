# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from .name_generator import app_name
from .config import init_project_settings

logger = get_logger(__name__)


def init_oz(client, location, name=None, tags=None):
    if not name:
        name = app_name()

    logger.info("Creating project %s.", name)
    params = {
        "location": location,
        "tags": tags,
    }
    client.resource_groups.create_or_update(
        resource_group_name=name, parameters=params
    )
    init_project_settings(resource_group_name=name, region=location)
    logger.info("Project created %s.", name)
    logger.info("Your Azure settings have been written to .azure/settings.json")


def get_app_oz(
    cmd,
):
    raise CLIError("TODO: Implement `oz list`")
