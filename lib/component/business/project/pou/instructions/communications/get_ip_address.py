#!/usr/bin/env python

from lib.component.business.project.pou.instructions.communications.communications_base import CommunicationsBase


class GetIPAddress(CommunicationsBase):
    """The "Get IP Address" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-03
    """

    def __init__(self, own_software, params=None):
        super(GetIPAddress, self).__init__(own_software, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-03
        """

        public = super(GetIPAddress, self).properties_config
        local = {'id': 166, 'locations': [{'row_add': 1, 'col_add': 2, 'id': 0}, {'row_add': 1, 'col_add': 2, 'id': 1},
                                          {'row_add': 1, 'col_add': 2, 'id': 2}]}
        config = {**public, **local}

        return config
