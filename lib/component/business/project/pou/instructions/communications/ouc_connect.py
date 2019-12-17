#!/usr/bin/env python

from lib.component.business.project.pou.instructions.communications.communications_base import CommunicationsBase


class OUCConnect(CommunicationsBase):
    """The "OUC Connect" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-04
    """

    def __init__(self, own_software, params=None):
        super(OUCConnect, self).__init__(own_software, params)

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

        public = super(OUCConnect, self).properties_config
        local = {'id': 155, 'locations': [{'row_add': 1, 'col_add': 0, 'id': 0}]}
        config = {**public, **local}

        return config
