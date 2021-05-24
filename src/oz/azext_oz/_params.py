# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type, get_location_type
    from ._validators import validate_runtime_choice, validate_sku_choice

    project_name_type = CLIArgumentType(
        options_list="--name", help="Name of the project", id_part="name"
    )

    with self.argument_context("oz") as c:
        c.argument("tags", tags_type)

    with self.argument_context("oz init") as c:
        c.argument("location", get_location_type(self.cli_ctx))
        c.argument("name", project_name_type)

    with self.argument_context("oz app create") as c:
        c.argument("runtime", options_list=['--runtime', '-r'],
                   validator=validate_runtime_choice,
                   help='The name of the runtime you want to use, e.g. "python", "node", or "dotnet".')
        c.argument("version", options_list=['--version', '-v'],
                   help='The version of the runtime to provision on the application service.')
        c.argument("sku", options_list=['--sku', '-s'],
                   validator=validate_sku_choice,
                   help='The SKU to provision, defaults to F1 (free).')