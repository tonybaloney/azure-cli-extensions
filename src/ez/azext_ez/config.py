# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from dataclasses import dataclass
import json
import pathlib
from knack.util import CLIError

DEFAULT_CONFIG_PATH = ".azure"
DEFAULT_CONFIG_NAME = "settings.json"


class NoProjectSettingsError(CLIError):
    message = "No project settings file exists in {0}/{1}".format(
        DEFAULT_CONFIG_PATH, DEFAULT_CONFIG_NAME
    )


@dataclass
class EzConfig:
    resource_group_name: str
    region: str
    app_service: bool = False
    app_name: str = None
    git_url: str = None
    database: bool = False

    def save(self, file):
        with open(file, "w+") as f:
            json.dump(self.__dict__, f)

    @classmethod
    def load(cls, file):
        with open(file) as f:
            settings = json.load(f)
        return cls(**settings)


def init_project_settings(resource_group_name: str, region: str):
    config = EzConfig(resource_group_name=resource_group_name, region=region)
    config_root = pathlib.Path() / DEFAULT_CONFIG_PATH
    if not config_root.exists():
        config_root.mkdir()

    config.save(config_root / DEFAULT_CONFIG_NAME)


def get_project_settings() -> EzConfig:
    config_root = pathlib.Path() / DEFAULT_CONFIG_PATH
    if not config_root.exists():
        raise NoProjectSettingsError
    config_file_path = config_root / DEFAULT_CONFIG_NAME
    if not config_file_path.exists():
        raise NoProjectSettingsError

    return EzConfig.load(config_file_path)


def destroy_project_settings():
    config_root = pathlib.Path() / DEFAULT_CONFIG_PATH
    if not config_root.exists():
        return
    config_file_path = config_root / DEFAULT_CONFIG_NAME
    if config_file_path.exists():
        config_file_path.unlink()
    config_root.rmdir()  # This will fail if there are other files in the directory,  but thats ok because I don't know what they are


def update_project_settings(**kwargs):
    settings = get_project_settings()
    for k, v in kwargs.items():
        setattr(settings, k, v)
    settings.save(pathlib.Path() / DEFAULT_CONFIG_PATH / DEFAULT_CONFIG_NAME)