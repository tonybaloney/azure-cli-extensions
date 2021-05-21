# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azext_oz._client_factory import cf_oz
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):
    oz_sdk = CliCommandType(operations_tmpl="azext_oz.custom#{}", client_factory=cf_oz)

    with self.command_group("oz", command_type=oz_sdk, client_factory=cf_oz) as g:
        g.custom_command("init", "init_oz")
        g.custom_command("app:get", "get_app_oz")

    with self.command_group("oz", is_preview=True):
        pass
