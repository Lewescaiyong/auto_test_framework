#!/usr/bin/env python

from lib.component.business.project.pou.instructions.interrupt.interrupt_base import InterruptBase


class DisableInterrupt(InterruptBase):
    """The "Disable Interrupt" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-06
    """

    def __init__(self, own_software, params=None):
        super(DisableInterrupt, self).__init__(own_software, params)

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

        public = super(DisableInterrupt, self).properties_config
        local = {'id': 366}
        config = {**public, **local}

        return config
