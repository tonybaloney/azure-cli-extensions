# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azext_oz._client_factory import cf_oz, app_client_factory
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):
    oz_sdk = CliCommandType(operations_tmpl="azext_oz.custom#{}", client_factory=cf_oz)

    with self.command_group("oz", command_type=oz_sdk, client_factory=cf_oz) as g:
        g.custom_command("init", "init_oz")
        g.custom_command("destroy", "destroy_oz")

    with self.command_group("oz app", command_type=oz_sdk, client_factory=app_client_factory) as g:
        g.custom_command("create", "create_app")


