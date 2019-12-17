#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.instruction_collector.move_collector import MoveCollector
from lib.component.business.project.pou.instructions.instruction_collector.clock_collector import ClockCollector
from lib.component.business.project.pou.instructions.instruction_collector.convert_collector import ConvertCollector
from lib.component.business.project.pou.instructions.instruction_collector.compare_collector import CompareCollector
from lib.component.business.project.pou.instructions.instruction_collector.counters_collector import CountersCollector
from lib.component.business.project.pou.instructions.instruction_collector.bit_logic_collector import BitLogicCollector
from lib.component.business.project.pou.instructions.instruction_collector.interrupt_collector import InterruptCollector
from lib.component.business.project.pou.instructions.instruction_collector.integer_math_collector import \
    IntegerMathCollector
from lib.component.business.project.pou.instructions.instruction_collector.communications_collector import \
    CommunicationsCollector
from lib.component.business.project.pou.instructions.instruction_collector.program_control_collector import \
    ProgramControlCollector
from lib.component.business.project.pou.instructions.instruction_collector.floating_point_math_collector import \
    FloatingPointMathCollector
from lib.component.business.project.pou.instructions.instruction_collector.logical_operations_collector import \
    LogicalOperationsCollector


class InstructionCollector(BusinessBase):
    """The instruction collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-20
    """

    def __init__(self, own_software, params=None):
        super(InstructionCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        config = dict()
        for i in (BitLogicCollector, ClockCollector, CommunicationsCollector, CompareCollector, ConvertCollector,
                  CountersCollector, FloatingPointMathCollector, IntegerMathCollector, InterruptCollector,
                  LogicalOperationsCollector, MoveCollector, ProgramControlCollector):
            config.update(i(self.own_software).add_config)

        return config
