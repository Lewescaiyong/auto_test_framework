#!/usr/bin/env python

from lib.component.business.project.pou.instructions.counters.counters_base import CountersBase


class HighSpeedCounter(CountersBase):
    """The "High Speed Counter" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-06
    """

    def __init__(self, own_software, params=None):
        super(HighSpeedCounter, self).__init__(own_software, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-06
        """

        public = super(HighSpeedCounter, self).properties_config
        local = {'id': 314, 'locations': [{'row_add': 1, 'col_add': 0, 'id': 0}]}
        config = {**public, **local}

        return config
