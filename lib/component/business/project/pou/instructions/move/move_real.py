#!/usr/bin/env python

from lib.component.business.project.pou.instructions.move.move_base import MoveBase


class MoveReal(MoveBase):
    """The "Move Real" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-10
    """

    def __init__(self, own_software, params=None):
        super(MoveReal, self).__init__(own_software, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-10
        """

        public = super(MoveReal, self).properties_config
        local = {'id': 418, 'locations': [{'row_add': 1, 'col_add': 0, 'id': 0}, {'row_add': 1, 'col_add': 2, 'id': 0}]}
        config = {**public, **local}

        return config
