#!/usr/bin/env python

from lib.component.business.project.pou.instructions.instruction_base import InstructionBase


class MoveBase(InstructionBase):
    """The "Move" instructions base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-28
    """

    def __init__(self, own_software, params=None):
        super(MoveBase, self).__init__(own_software, params)
