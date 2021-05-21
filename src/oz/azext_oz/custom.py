# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError

from .name_generator import app_name

logger = get_logger(__name__)


def init_oz(cmd, name=None, location=None, tags=None):
    if not name:
        name = app_name()
    logger.info("Creating project %s.", name)


def get_app_oz(
    cmd,
):
    raise CLIError("TODO: Implement `oz list`")
