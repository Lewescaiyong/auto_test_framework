#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.clock.set_real_time_clock import SetRealTimeClock
from lib.component.business.project.pou.instructions.clock.read_real_time_clock import ReadRealTimeClock
from lib.component.business.project.pou.instructions.clock.set_real_time_clock_extended import SetRealTimeClockExtended
from lib.component.business.project.pou.instructions.clock.read_real_time_clock_extended import \
    ReadRealTimeClockExtended


class ClockCollector(BusinessBase):
    """Clock instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-03
    """

    def __init__(self, own_software, params=None):
        super(ClockCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-03
        """

        config = {
            'read_real_time_clock': ReadRealTimeClock,
            'set_real_time_clock': SetRealTimeClock,
            'read_real_time_clock_extended': ReadRealTimeClockExtended,
            'set_real_time_clock_extended': SetRealTimeClockExtended
        }

        return config
