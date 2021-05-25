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

    with self.argument_context("ez") as c:
        c.argument("tags", tags_type)

    with self.argument_context("ez destroy") as c:
        c.argument("confirm", options_list=["--yes", "-y"], action="store_false")

    with self.argument_context("ez init") as c:
        c.argument("location", get_location_type(self.cli_ctx))
        c.argument("name", project_name_type)

    with self.argument_context("ez app create") as c:
        c.argument(
            "runtime",
            options_list=["--runtime", "-r"],
            validator=validate_runtime_choice,
            help='The name of the runtime you want to use, e.g. "python", "node", or "dotnet".',
        )
        c.argument(
            "version",
            options_list=["--version", "-v"],
            help="The version of the runtime to provision on the application service.",
        )
        c.argument(
            "sku",
            options_list=["--sku", "-s"],
            validator=validate_sku_choice,
            help="The SKU to provision, defaults to F1 (free).",
        )

    with self.argument_context("ez app domain") as c:
        c.argument(
            "domain",
            options_list=["--domain", "-d"],
            help="The domain name to configure.",
        )

    with self.argument_context("ez app scale") as c:
        c.argument(
            "sku",
            options_list=["--sku", "-s"],
            validator=validate_sku_choice,
            help="The SKU to provision, defaults to B1.",
        )
