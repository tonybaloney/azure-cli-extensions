# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azext_ez._client_factory import mgmt_client_factory, app_client_factory
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):
    ez_sdk = CliCommandType(
        operations_tmpl="azext_ez.custom#{}", client_factory=mgmt_client_factory
    )

    with self.command_group(
        "ez", command_type=ez_sdk, client_factory=mgmt_client_factory
    ) as g:
        g.custom_command("init", "init_ez")
        g.custom_command("destroy", "destroy_ez")

    with self.command_group(
        "ez app", command_type=ez_sdk, client_factory=app_client_factory
    ) as g:
        g.custom_command("create", "create_app")
        g.custom_command("settings", "app_settings")