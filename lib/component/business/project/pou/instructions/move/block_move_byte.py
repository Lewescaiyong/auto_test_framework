#!/usr/bin/env python

from lib.component.business.project.pou.instructions.move.move_base import MoveBase


class BlockMoveByte(MoveBase):
    """The "Block Move Byte" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-12
    """

    def __init__(self, own_software, params=None):
        super(BlockMoveByte, self).__init__(own_software, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-12
        """

        public = super(BlockMoveByte, self).properties_config
        local = {'id': 419, 'locations': [{'row_add': 1, 'col_add': 0, 'id': 0}, {'row_add': 1, 'col_add': 0, 'id': 1},
                                          {'row_add': 1, 'col_add': 2, 'id': 0}]}
        config = {**public, **local}

        return config
