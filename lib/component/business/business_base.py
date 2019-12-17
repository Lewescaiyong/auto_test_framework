# !/usr/bin/env python

from lib.component.component_base import ComponentBase


class BusinessBase(ComponentBase):
    """Business parent class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-20
    """

    def __init__(self, own_software, params=None):
        self.__own_software = own_software
        super(BusinessBase, self).__init__(params)

    @property
    def own_software(self):
        """Get own software to invoke the interface
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """

        return self.__own_software

    @property
    def cpu_type_config(self):
        """CPU type config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-31
        """

        config = {
            'ST20': 'CPU ST20 (DC/DC/DC)',
            'ST30': 'CPU ST30 (DC/DC/DC)',
            'ST40': 'CPU ST40 (DC/DC/DC)',
            'ST60': 'CPU ST60 (DC/DC/DC)',

            'SR20': 'CPU SR20 (AC/DC/Relay)',
            'SR30': 'CPU SR30 (AC/DC/Relay)',
            'SR40': 'CPU SR40 (AC/DC/Relay)',
            'SR60': 'CPU SR60 (AC/DC/Relay)',

            'CR20s': 'CPU CR20s (AC/DC/Relay)',
            'CR30s': 'CPU CR30s (AC/DC/Relay)',
            'CR40s': 'CPU CR40s (AC/DC/Relay)',
            'CR60s': 'CPU CR60s (AC/DC/Relay)',

            'CR40': 'CPU CR40 (AC/DC/Relay)',
            'CR60': 'CPU CR60 (AC/DC/Relay)',
        }

        return config
