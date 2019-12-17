#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase


class IODeviceBase(BusinessBase):
    """IO Device base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-26
    """

    def __init__(self, own_software, params=None):
        super(IODeviceBase, self).__init__(own_software, params)

    @property
    def own_controller(self):
        """Get own controller device
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        return self.params['own_business'].params['own_business']

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        config = {'device_number': 1, 'device_ip': '', 'sub_slot_number': 1000}

        return config
