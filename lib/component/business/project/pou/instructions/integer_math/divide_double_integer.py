#!/usr/bin/env python

from lib.component.business.project.pou.instructions.integer_math.integer_math_base import IntegerMathBase


class DivideDoubleInteger(IntegerMathBase):
    """The "Divide Double Integer" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-06
    """

    def __init__(self, own_software, params=None):
        super(DivideDoubleInteger, self).__init__(own_software, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-06
        """

        public = super(DivideDoubleInteger, self).properties_config
        local = {'id': 354, 'locations': [{'row_add': 1, 'col_add': 0, 'id': 0}, {'row_add': 1, 'col_add': 0, 'id': 1},
                                          {'row_add': 1, 'col_add': 2, 'id': 0}]}
        config = {**public, **local}

        return config
