#!/usr/bin/env python

from lib.component.business.project.pou.instructions.instruction_base import InstructionBase


class ConvertBase(InstructionBase):
    """The "Convert" instructions base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-05
    """

    def __init__(self, own_software, params=None):
        super(ConvertBase, self).__init__(own_software, params)
