#!/usr/bin/env python

from lib.component.business.project.pou.instructions.compare.compare_base import CompareBase


class GreaterThanOrEqualByte(CompareBase):
    """The "Greater Than Or Equal Byte" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-04
    """

    def __init__(self, own_software, params=None):
        super(GreaterThanOrEqualByte, self).__init__(own_software, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-04
        """

        public = super(GreaterThanOrEqualByte, self).properties_config
        local = {'id': 172, 'locations': [{'row_add': 0, 'col_add': 0, 'id': 0}, {'row_add': 0, 'col_add': 0, 'id': 2}]}
        config = {**public, **local}

        return config
