#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.interrupt.enable_interrupt import EnableInterrupt
from lib.component.business.project.pou.instructions.interrupt.attach_interrupt import AttachInterrupt
from lib.component.business.project.pou.instructions.interrupt.detach_interrupt import DetachInterrupt
from lib.component.business.project.pou.instructions.interrupt.disable_interrupt import DisableInterrupt
from lib.component.business.project.pou.instructions.interrupt.clear_interrupt_event import ClearInterruptEvent
from lib.component.business.project.pou.instructions.interrupt.conditional_return_from_interrupt import \
    ConditionalReturnFromInterrupt


class InterruptCollector(BusinessBase):
    """Interrupt instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-06
    """

    def __init__(self, own_software, params=None):
        super(InterruptCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-06
        """

        config = {
            'enable_interrupt': EnableInterrupt,
            'disable_interrupt': DisableInterrupt,
            'conditional_return_from_interrupt': ConditionalReturnFromInterrupt,
            'attach_interrupt': AttachInterrupt,
            'detach_interrupt': DetachInterrupt,
            'clear_interrupt_event': ClearInterruptEvent
        }

        return config
