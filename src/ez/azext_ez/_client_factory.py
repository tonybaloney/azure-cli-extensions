# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import namedtuple
from azure.cli.core.commands.client_factory import get_mgmt_service_client


def mgmt_client_factory(cli_ctx, *args, **kwargs):
    from azure.mgmt.resource import ResourceManagementClient

    return get_mgmt_service_client(cli_ctx, ResourceManagementClient)


def app_client_factory(cli_ctx, *args, **kwargs):
    from azure.mgmt.web import WebSiteManagementClient

    return get_mgmt_service_client(cli_ctx, WebSiteManagementClient)


def db_client_factory(cli_ctx, *args, **kwargs):
    # TODO : this seems like overkill. refactor.
    Client = namedtuple("Client", "mysql postgres")

    from azure.mgmt.rdbms.postgresql_flexibleservers import (
        PostgreSQLManagementClient,
    )
    from azure.mgmt.rdbms.mysql_flexibleservers import MySQLManagementClient

    return Client(
        get_mgmt_service_client(cli_ctx, MySQLManagementClient),
        get_mgmt_service_client(cli_ctx, PostgreSQLManagementClient),
    )
