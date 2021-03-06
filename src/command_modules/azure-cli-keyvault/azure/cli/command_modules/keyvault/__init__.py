# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

import azure.cli.command_modules.keyvault._help  # pylint: disable=unused-import


class KeyVaultCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azure.cli.command_modules.keyvault._client_factory import keyvault_client_factory
        from azure.cli.command_modules.keyvault._command_type import KeyVaultCommandGroup, KeyVaultArgumentContext
        keyvault_custom = CliCommandType(
            operations_tmpl='azure.cli.command_modules.keyvault.custom#{}',
            client_factory=keyvault_client_factory
        )
        super(KeyVaultCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                     custom_command_type=keyvault_custom,
                                                     command_group_cls=KeyVaultCommandGroup,
                                                     argument_context_cls=KeyVaultArgumentContext)

    def load_command_table(self, args):
        from azure.cli.command_modules.keyvault.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azure.cli.command_modules.keyvault._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = KeyVaultCommandsLoader
