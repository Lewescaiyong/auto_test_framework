#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.compare.equal_real import EqualReal
from lib.component.business.project.pou.instructions.compare.equal_byte import EqualByte
from lib.component.business.project.pou.instructions.compare.equal_string import EqualString
from lib.component.business.project.pou.instructions.compare.equal_integer import EqualInteger
from lib.component.business.project.pou.instructions.compare.not_equal_real import NotEqualReal
from lib.component.business.project.pou.instructions.compare.not_equal_byte import NotEqualByte
from lib.component.business.project.pou.instructions.compare.less_than_real import LessThanReal
from lib.component.business.project.pou.instructions.compare.less_than_byte import LessThanByte
from lib.component.business.project.pou.instructions.compare.not_equal_string import NotEqualString
from lib.component.business.project.pou.instructions.compare.less_than_integer import LessThanInteger
from lib.component.business.project.pou.instructions.compare.greater_than_byte import GreaterThanByte
from lib.component.business.project.pou.instructions.compare.not_equal_integer import NotEqualInteger
from lib.component.business.project.pou.instructions.compare.greater_than_real import GreaterThanReal
from lib.component.business.project.pou.instructions.compare.greater_than_integer import GreaterThanInteger
from lib.component.business.project.pou.instructions.compare.equal_double_integer import EqualDoubleInteger
from lib.component.business.project.pou.instructions.compare.less_than_or_equal_real import LessThanOrEqualReal
from lib.component.business.project.pou.instructions.compare.less_than_or_equal_byte import LessThanOrEqualByte
from lib.component.business.project.pou.instructions.compare.less_than_double_integer import LessThanDoubleInteger
from lib.component.business.project.pou.instructions.compare.not_equal_double_integer import NotEqualDoubleInteger
from lib.component.business.project.pou.instructions.compare.greater_than_or_equal_real import GreaterThanOrEqualReal
from lib.component.business.project.pou.instructions.compare.greater_than_or_equal_byte import GreaterThanOrEqualByte
from lib.component.business.project.pou.instructions.compare.less_than_or_equal_integer import LessThanOrEqualInteger
from lib.component.business.project.pou.instructions.compare.greater_than_double_integer import GreaterThanDoubleInteger
from lib.component.business.project.pou.instructions.compare.greater_than_or_equal_integer import \
    GreaterThanOrEqualInteger
from lib.component.business.project.pou.instructions.compare.greater_than_or_equal_double_integer import \
    GreaterThanOrEqualDoubleInteger
from lib.component.business.project.pou.instructions.compare.less_than_or_equal_double_integer import \
    LessThanOrEqualDoubleInteger


class CompareCollector(BusinessBase):
    """Compare instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-04
    """

    def __init__(self, own_software, params=None):
        super(CompareCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-04
        """

        config = {
            'equal_byte': EqualByte,
            'not_equal_byte': NotEqualByte,
            'greater_than_or_equal_byte': GreaterThanOrEqualByte,
            'less_than_or_equal_byte': LessThanOrEqualByte,
            'greater_than_byte': GreaterThanByte,
            'less_than_byte': LessThanByte,
            'equal_integer': EqualInteger,
            'not_equal_integer': NotEqualInteger,
            'greater_than_or_equal_integer': GreaterThanOrEqualInteger,
            'less_than_or_equal_integer': LessThanOrEqualInteger,
            'greater_than_integer': GreaterThanInteger,
            'less_than_integer': LessThanInteger,
            'equal_double_integer': EqualDoubleInteger,
            'not_equal_double_integer': NotEqualDoubleInteger,
            'greater_than_or_equal_double_integer': GreaterThanOrEqualDoubleInteger,
            'less_than_or_equal_double_integer': LessThanOrEqualDoubleInteger,
            'greater_than_double_integer': GreaterThanDoubleInteger,
            'less_than_double_integer': LessThanDoubleInteger,
            'equal_real': EqualReal,
            'not_equal_real': NotEqualReal,
            'greater_than_or_equal_real': GreaterThanOrEqualReal,
            'less_than_or_equal_real': LessThanOrEqualReal,
            'greater_than_real': GreaterThanReal,
            'less_than_real': LessThanReal,
            'equal_string': EqualString,
            'not_equal_string': NotEqualString
        }

        return config
