# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type, get_location_type
    from azure.cli.core.commands.validators import (
        get_default_location_from_resource_group,
    )

    project_name_type = CLIArgumentType(
        options_list="--name", help="Name of the project", id_part="name"
    )

    with self.argument_context("oz") as c:
        c.argument("tags", tags_type)

    with self.argument_context("oz init") as c:
        c.argument("location", get_location_type(self.cli_ctx))
        c.argument("name", project_name_type)
