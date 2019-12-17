#!/usr/bin/env python

from lib.component.business.project.pou.instructions.instruction_base import InstructionBase


class BitLogicBase(InstructionBase):
    """The "Bit Logic" instructions base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-20
    """

    def __init__(self, own_software, params=None):
        super(BitLogicBase, self).__init__(own_software, params)
