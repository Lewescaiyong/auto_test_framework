#!/usr/bin/env python

from lib.component.business.project.pou.instructions.clock.clock_base import ClockBase


class SetRealTimeClockExtended(ClockBase):
    """The "Set Real Time Clock Extended" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-03
    """

    def __init__(self, own_software, params=None):
        super(SetRealTimeClockExtended, self).__init__(own_software, params)

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

        public = super(SetRealTimeClockExtended, self).properties_config
        local = {'id': 153, 'locations': [{'row_add': 1, 'col_add': 0, 'id': 0}]}
        config = {**public, **local}

        return config
