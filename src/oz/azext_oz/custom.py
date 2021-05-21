# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_oz(cmd, resource_group_name, oz_name, location=None, tags=None):
    raise CLIError('TODO: Implement `oz create`')


def list_oz(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `oz list`')


def update_oz(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance