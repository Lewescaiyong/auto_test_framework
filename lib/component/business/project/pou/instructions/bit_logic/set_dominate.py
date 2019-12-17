#!/usr/bin/env python

from lib.component.business.project.pou.instructions.bit_logic.bit_logic_base import BitLogicBase


class SetDominate(BitLogicBase):
    """The "Set Dominate" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-02
    """

    def __init__(self, own_software, params=None):
        super(SetDominate, self).__init__(own_software, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-02
        """

        public = super(SetDominate, self).properties_config
        local = {'id': 140, 'locations': [{'row_add': 0, 'col_add': 1, 'id': 0}]}
        config = {**public, **local}

        return config