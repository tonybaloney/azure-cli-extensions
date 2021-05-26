# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azext_ez._client_factory import (
    mgmt_client_factory,
    app_client_factory,
    db_client_factory,
)
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
        g.custom_command("logs", "app_logs")
        g.custom_command("domain", "app_set_domain")
        g.custom_command("scale", "app_scale")
        g.custom_command("open", "app_open")
        g.custom_command("oryx", "app_oryx")

    with self.command_group(
        "ez db", command_type=ez_sdk, client_factory=db_client_factory
    ) as g:
        g.custom_command("create", "create_db")
        g.custom_command("scale", "db_scale")
        g.custom_command("connect", "db_connect")
