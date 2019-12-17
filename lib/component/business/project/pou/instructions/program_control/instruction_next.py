#!/usr/bin/env python

from lib.component.business.project.pou.instructions.program_control.program_control_base import ProgramControlBase


class InstructionNext(ProgramControlBase):
    """The "Next" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-12
    """

    def __init__(self, own_software, params=None):
        super(InstructionNext, self).__init__(own_software, params)

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

        public = super(InstructionNext, self).properties_config
        local = {'id': 430}
        config = {**public, **local}

        return config
