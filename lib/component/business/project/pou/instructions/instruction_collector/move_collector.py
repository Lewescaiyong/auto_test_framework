#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.move.move_byte import MoveByte
from lib.component.business.project.pou.instructions.move.move_word import MoveWord
from lib.component.business.project.pou.instructions.move.move_real import MoveReal
from lib.component.business.project.pou.instructions.move.swap_bytes import SwapBytes
from lib.component.business.project.pou.instructions.move.block_move_byte import BlockMoveByte
from lib.component.business.project.pou.instructions.move.block_move_word import BlockMoveWord
from lib.component.business.project.pou.instructions.move.move_double_word import MoveDoubleWord
from lib.component.business.project.pou.instructions.move.block_move_double_word import BlockMoveDoubleWord
from lib.component.business.project.pou.instructions.move.move_byte_immediate_read import MoveByteImmediateRead
from lib.component.business.project.pou.instructions.move.move_byte_immediate_write import MoveByteImmediateWrite


class MoveCollector(BusinessBase):
    """Move instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-29
    """

    def __init__(self, own_software, params=None):
        super(MoveCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        config = {
            'move_byte': MoveByte,
            'move_word': MoveWord,
            'move_double_word': MoveDoubleWord,
            'move_real': MoveReal,
            'block_move_byte': BlockMoveByte,
            'block_move_word': BlockMoveWord,
            'block_move_double_word': BlockMoveDoubleWord,
            'swap_bytes': SwapBytes,
            'move_byte_immediate_read': MoveByteImmediateRead,
            'move_byte_immediate_write': MoveByteImmediateWrite
        }

        return config
