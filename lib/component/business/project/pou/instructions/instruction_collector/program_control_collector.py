#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.program_control.stop import Stop
from lib.component.business.project.pou.instructions.program_control.jump import Jump
from lib.component.business.project.pou.instructions.program_control.label import Label
from lib.component.business.project.pou.instructions.program_control.end_scr import EndSCR
from lib.component.business.project.pou.instructions.program_control.load_scr import LoadSCR
from lib.component.business.project.pou.instructions.program_control.get_error import GetError
from lib.component.business.project.pou.instructions.program_control.transition_scr import TransitionSCR
from lib.component.business.project.pou.instructions.program_control.watchdog_reset import WatchdogReset
from lib.component.business.project.pou.instructions.program_control.instruction_for import InstructionFor
from lib.component.business.project.pou.instructions.program_control.instruction_next import InstructionNext
from lib.component.business.project.pou.instructions.program_control.conditional_end_of_program import \
    ConditionalEndOfProgram
from lib.component.business.project.pou.instructions.program_control.conditional_return_from_subroutine import \
    ConditionalReturnFromSubroutine


class ProgramControlCollector(BusinessBase):
    """Program Control instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-12
    """

    def __init__(self, own_software, params=None):
        super(ProgramControlCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-12
        """

        config = {
            'instruction_for': InstructionFor,
            'instruction_next': InstructionNext,
            'jump': Jump,
            'label': Label,
            'load_scr': LoadSCR,
            'transition_scr': TransitionSCR,
            'end_scr': EndSCR,
            'conditional_return_from_subroutine': ConditionalReturnFromSubroutine,
            'conditional_end_of_program': ConditionalEndOfProgram,
            'stop': Stop,
            'watchdog_reset': WatchdogReset,
            'get_error': GetError
        }

        return config
