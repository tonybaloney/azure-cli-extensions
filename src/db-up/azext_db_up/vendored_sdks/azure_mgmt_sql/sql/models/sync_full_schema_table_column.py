# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SyncFullSchemaTableColumn(Model):
    """Properties of the column in the table of database full schema.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar data_size: Data size of the column.
    :vartype data_size: str
    :ivar data_type: Data type of the column.
    :vartype data_type: str
    :ivar error_id: Error id of the column.
    :vartype error_id: str
    :ivar has_error: If there is error in the table.
    :vartype has_error: bool
    :ivar is_primary_key: If it is the primary key of the table.
    :vartype is_primary_key: bool
    :ivar name: Name of the column.
    :vartype name: str
    :ivar quoted_name: Quoted name of the column.
    :vartype quoted_name: str
    """

    _validation = {
        'data_size': {'readonly': True},
        'data_type': {'readonly': True},
        'error_id': {'readonly': True},
        'has_error': {'readonly': True},
        'is_primary_key': {'readonly': True},
        'name': {'readonly': True},
        'quoted_name': {'readonly': True},
    }

    _attribute_map = {
        'data_size': {'key': 'dataSize', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'str'},
        'error_id': {'key': 'errorId', 'type': 'str'},
        'has_error': {'key': 'hasError', 'type': 'bool'},
        'is_primary_key': {'key': 'isPrimaryKey', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'quoted_name': {'key': 'quotedName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SyncFullSchemaTableColumn, self).__init__(**kwargs)
        self.data_size = None
        self.data_type = None
        self.error_id = None
        self.has_error = None
        self.is_primary_key = None
        self.name = None
        self.quoted_name = None