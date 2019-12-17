#!/usr/bin/env python

from lib.component.business.project.pou.instructions.instruction_base import InstructionBase


class FloatingPointMathBase(InstructionBase):
    """The "Floating-Point Math" instructions base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-06
    """

    def __init__(self, own_software, params=None):
        super(FloatingPointMathBase, self).__init__(own_software, params)
