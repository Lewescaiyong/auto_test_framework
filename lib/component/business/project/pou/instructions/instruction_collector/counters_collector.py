#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.counters.count_up import CountUp
from lib.component.business.project.pou.instructions.counters.count_down import CountDown
from lib.component.business.project.pou.instructions.counters.pulse_output import PulseOutput
from lib.component.business.project.pou.instructions.counters.count_up_or_down import CountUpOrDown
from lib.component.business.project.pou.instructions.counters.high_speed_counter import HighSpeedCounter
from lib.component.business.project.pou.instructions.counters.high_speed_counter_definition import \
    HighSpeedCounterDefinition


class CountersCollector(BusinessBase):
    """Counters instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-06
    """

    def __init__(self, own_software, params=None):
        super(CountersCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-06
        """

        config = {
            'count_up': CountUp,
            'count_down': CountDown,
            'count_up_or_down': CountUpOrDown,
            'high_speed_counter_definition': HighSpeedCounterDefinition,
            'high_speed_counter': HighSpeedCounter,
            'pulse_output': PulseOutput
        }

        return config
