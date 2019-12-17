#!/usr/bin/env python

from lib.component.business.project.pou.instructions.instruction_base import InstructionBase


class CompareBase(InstructionBase):
    """The "Compare" instructions base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-04
    """

    def __init__(self, own_software, params=None):
        super(CompareBase, self).__init__(own_software, params)
