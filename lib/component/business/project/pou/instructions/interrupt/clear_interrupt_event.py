#!/usr/bin/env python

from lib.component.business.project.pou.instructions.interrupt.interrupt_base import InterruptBase


class ClearInterruptEvent(InterruptBase):
    """The "Clear Interrupt Event" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-06
    """

    def __init__(self, own_software, params=None):
        super(ClearInterruptEvent, self).__init__(own_software, params)

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

        public = super(ClearInterruptEvent, self).properties_config
        local = {'id': 377, 'locations': [{'row_add': 1, 'col_add': 0, 'id': 0}]}
        config = {**public, **local}

        return config
