#!/usr/bin/env python

from lib.component.business.project.pou.instructions.instruction_base import InstructionBase


class ClockBase(InstructionBase):
    """The "Clock" instructions base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-03
    """

    def __init__(self, own_software, params=None):
        super(ClockBase, self).__init__(own_software, params)
