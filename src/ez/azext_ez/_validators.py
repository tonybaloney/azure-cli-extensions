# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .runtimes import RUNTIME_GROUPS
from knack.util import CLIError


def validate_runtime_choice(cmd, namespace):
    if namespace.runtime:
        if namespace.runtime not in RUNTIME_GROUPS:
            raise CLIError("Invalid runtime %s." % namespace.runtime)


def validate_sku_choice(cmd, namespace):
    if namespace.sku:
        # TODO : Compare namespace.sku with list of available skus
        pass