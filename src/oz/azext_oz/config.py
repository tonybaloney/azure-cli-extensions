# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from dataclasses import dataclass
import json
from logging.config import DEFAULT_LOGGING_CONFIG_PORT
import pathlib
import os

DEFAULT_CONFIG_PATH = '.azure'
DEFAULT_CONFIG_NAME = 'settings.json'

@dataclass
class OzConfig:
    resource_group_name: str
    region: str
    app_service: bool = False
    database: bool = False

    def save(self, file):
        with open(file, 'w+') as f:
            json.dump(self.__dict__, f)

    @classmethod
    def load(cls, file):
        with open(file) as f:
            settings = json.load(f)
        return cls(**settings)


def init_project_settings(resource_group_name: str, region: str):
    config = OzConfig(resource_group_name=resource_group_name, region=region)
    config_root = pathlib.Path() / DEFAULT_CONFIG_PATH
    if not config_root.exists():
        config_root.mkdir()

    config.save(config_root / DEFAULT_CONFIG_NAME)
