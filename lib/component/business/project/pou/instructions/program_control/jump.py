#!/usr/bin/env python

from lib.component.business.project.pou.instructions.program_control.program_control_base import ProgramControlBase


class Jump(ProgramControlBase):
    """The "Jump" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-12
    """

    def __init__(self, own_software, params=None):
        super(Jump, self).__init__(own_software, params)

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

        public = super(Jump, self).properties_config
        local = {'id': 431, 'locations': [{'row_add': 0, 'col_add': 0, 'id': 0}]}
        config = {**public, **local}

        return config
