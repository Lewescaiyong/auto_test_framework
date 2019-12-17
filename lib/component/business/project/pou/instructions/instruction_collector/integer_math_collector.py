#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.integer_math.add_integer import AddInteger
from lib.component.business.project.pou.instructions.integer_math.divide_integer import DivideInteger
from lib.component.business.project.pou.instructions.integer_math.decrement_byte import DecrementByte
from lib.component.business.project.pou.instructions.integer_math.decrement_word import DecrementWord
from lib.component.business.project.pou.instructions.integer_math.increment_byte import IncrementByte
from lib.component.business.project.pou.instructions.integer_math.increment_word import IncrementWord
from lib.component.business.project.pou.instructions.integer_math.multiply_integer import MultiplyInteger
from lib.component.business.project.pou.instructions.integer_math.subtract_integer import SubtractInteger
from lib.component.business.project.pou.instructions.integer_math.add_double_integer import AddDoubleInteger
from lib.component.business.project.pou.instructions.integer_math.divide_double_integer import DivideDoubleInteger
from lib.component.business.project.pou.instructions.integer_math.increment_double_word import IncrementDoubleWord
from lib.component.business.project.pou.instructions.integer_math.decrement_double_word import DecrementDoubleWord
from lib.component.business.project.pou.instructions.integer_math.subtract_double_integer import SubtractDoubleInteger
from lib.component.business.project.pou.instructions.integer_math.multiply_double_integer import MultiplyDoubleInteger
from lib.component.business.project.pou.instructions.integer_math.multiply_integer_to_double_integer import \
    MultiplyIntegerToDoubleInteger
from lib.component.business.project.pou.instructions.integer_math.divide_integer_to_quotient_or_remainder import \
    DivideIntegerToQuotientOrRemainder


class IntegerMathCollector(BusinessBase):
    """Integer Math instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-05
    """

    def __init__(self, own_software, params=None):
        super(IntegerMathCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-05
        """

        config = {
            'add_integer': AddInteger,
            'add_double_integer': AddDoubleInteger,
            'subtract_integer': SubtractInteger,
            'subtract_double_integer': SubtractDoubleInteger,
            'multiply_integer_to_double_integer': MultiplyIntegerToDoubleInteger,
            'multiply_integer': MultiplyInteger,
            'multiply_double_integer': MultiplyDoubleInteger,
            'divide_integer_to_quotient_or_remainder': DivideIntegerToQuotientOrRemainder,
            'divide_integer': DivideInteger,
            'divide_double_integer': DivideDoubleInteger,
            'increment_byte': IncrementByte,
            'increment_word': IncrementWord,
            'increment_double_word': IncrementDoubleWord,
            'decrement_byte': DecrementByte,
            'decrement_word': DecrementWord,
            'decrement_double_word': DecrementDoubleWord
        }

        return config
