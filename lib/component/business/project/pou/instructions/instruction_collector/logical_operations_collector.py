#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.logical_operations.or_byte import OrByte
from lib.component.business.project.pou.instructions.logical_operations.or_word import OrWord
from lib.component.business.project.pou.instructions.logical_operations.and_byte import AndByte
from lib.component.business.project.pou.instructions.logical_operations.and_word import AndWord
from lib.component.business.project.pou.instructions.logical_operations.invert_byte import InvertByte
from lib.component.business.project.pou.instructions.logical_operations.invert_word import InvertWord
from lib.component.business.project.pou.instructions.logical_operations.or_double_word import OrDoubleWord
from lib.component.business.project.pou.instructions.logical_operations.and_double_word import AndDoubleWord
from lib.component.business.project.pou.instructions.logical_operations.exclusive_or_byte import ExclusiveOrByte
from lib.component.business.project.pou.instructions.logical_operations.exclusive_or_word import ExclusiveOrWord
from lib.component.business.project.pou.instructions.logical_operations.invert_double_word import InvertDoubleWord
from lib.component.business.project.pou.instructions.logical_operations.exclusive_or_double_word import \
    ExclusiveOrDoubleWord


class LogicalOperationsCollector(BusinessBase):
    """Logical Operations instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-06
    """

    def __init__(self, own_software, params=None):
        super(LogicalOperationsCollector, self).__init__(own_software, params)

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
            'invert_byte': InvertByte,
            'invert_word': InvertWord,
            'invert_double_word': InvertDoubleWord,
            'and_byte': AndByte,
            'and_word': AndWord,
            'and_double_word': AndDoubleWord,
            'or_byte': OrByte,
            'or_word': OrWord,
            'or_double_word': OrDoubleWord,
            'exclusive_or_byte': ExclusiveOrByte,
            'exclusive_or_word': ExclusiveOrWord,
            'exclusive_or_double_word': ExclusiveOrDoubleWord
        }

        return config
