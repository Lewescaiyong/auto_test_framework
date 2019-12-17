#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase


class PNDeviceBase(BusinessBase):
    """PN Device base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-24
    """

    def __init__(self, own_software, params=None):
        super(PNDeviceBase, self).__init__(own_software, params)

    @property
    def own_wizard(self):
        """Get own wizard pn
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        return self.params['own_business']

    def get_compile_result(self):
        """Get the project compile result
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20 create
        """

        compile_result = self.own_wizard.own_project.project_compile()

        return compile_result
