#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase


class WizardBase(BusinessBase):
    """Wizard base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-23
    """

    def __init__(self, own_software, params=None):
        super(WizardBase, self).__init__(own_software, params)

    @property
    def own_project(self):
        """Get own project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        return self.params['own_business']

    @property
    def own_system_block(self):
        """Get own project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        system_block = self.own_project.find('system_block')

        return system_block
