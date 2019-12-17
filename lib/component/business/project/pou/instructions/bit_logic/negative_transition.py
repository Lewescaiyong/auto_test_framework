#!/usr/bin/env python

from lib.component.business.project.pou.instructions.bit_logic.bit_logic_base import BitLogicBase


class NegativeTransition(BitLogicBase):
    """The "Negative Transition" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-02
    """

    def __init__(self, own_software, params=None):
        super(NegativeTransition, self).__init__(own_software, params)

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

        public = super(NegativeTransition, self).properties_config
        local = {'id': 26}
        config = {**public, **local}

        return config
