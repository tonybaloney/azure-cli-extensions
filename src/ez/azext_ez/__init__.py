# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azext_ez._help import helps  # pylint: disable=unused-import


class EzCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_ez._client_factory import mgmt_client_factory

        oz_custom = CliCommandType(
            operations_tmpl="azext_ez.custom#{}", client_factory=mgmt_client_factory
        )
        super(EzCommandsLoader, self).__init__(
            cli_ctx=cli_ctx, custom_command_type=oz_custom
        )

    def load_command_table(self, args):
        from azext_ez.commands import load_command_table

        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_ez._params import load_arguments

        load_arguments(self, command)


COMMAND_LOADER_CLS = EzCommandsLoader
