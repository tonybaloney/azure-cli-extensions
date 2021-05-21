# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.client_factory import get_mgmt_service_client


def cf_oz(cli_ctx, *args, **kwargs):
    from azure.mgmt.resource import ResourceManagementClient

    return get_mgmt_service_client(cli_ctx, ResourceManagementClient)
