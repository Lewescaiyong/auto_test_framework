#!/usr/bin/env python

from lib.wrapper.wrapper_base import WrapperBase


class IntegrationMW(WrapperBase):
    """Integration test interfaces collection class of Micro WIN.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    view = 'IntegrationMW'

    def get_public_interface(self):
        """Create a socket object.
        Args:
            ip                  type(str)           ip address
            port                type(str)           port number
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        modules = ['lib.wrapper.integration_mw.interfaces.common',
                   'lib.wrapper.integration_mw.interfaces.instruction',
                   'lib.wrapper.integration_mw.interfaces.memory_options',
                   'lib.wrapper.integration_mw.interfaces.network',
                   'lib.wrapper.integration_mw.interfaces.plc_option',
                   'lib.wrapper.integration_mw.interfaces.pou',
                   'lib.wrapper.integration_mw.interfaces.project',
                   'lib.wrapper.integration_mw.interfaces.session',
                   'lib.wrapper.integration_mw.interfaces.symbol_table',
                   'lib.wrapper.integration_mw.interfaces.system_block',
                   'lib.wrapper.integration_mw.interfaces.upgrade',
                   'lib.wrapper.integration_mw.interfaces.wizard_pn']
        other_modules = super(IntegrationMW, self).get_public_interface()

        return modules + other_modules

    def get_version_interface(self, version=''):
        """Create a socket object.
        Args:
            version         type(str)         the version of micro win
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        modules = self.version_config.get(version)
        other_modules = super(IntegrationMW, self).get_version_interface(version)

        return modules + other_modules
