#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.bit_logic.reset import Reset
from lib.component.business.project.pou.instructions.bit_logic.output import Output
from lib.component.business.project.pou.instructions.bit_logic.no_operation import NoOperation
from lib.component.business.project.pou.instructions.bit_logic.set_dominate import SetDominate
from lib.component.business.project.pou.instructions.bit_logic.set_immediate import SetImmediate
from lib.component.business.project.pou.instructions.bit_logic.normally_open import NormallyOpen
from lib.component.business.project.pou.instructions.bit_logic.reset_dominate import ResetDominate
from lib.component.business.project.pou.instructions.bit_logic.reset_immediate import ResetImmediate
from lib.component.business.project.pou.instructions.bit_logic.instruction_not import InstructionNot
from lib.component.business.project.pou.instructions.bit_logic.normally_closed import NormallyClosed
from lib.component.business.project.pou.instructions.bit_logic.instruction_set import InstructionSet
from lib.component.business.project.pou.instructions.bit_logic.output_immediate import OutputImmediate
from lib.component.business.project.pou.instructions.bit_logic.negative_transition import NegativeTransition
from lib.component.business.project.pou.instructions.bit_logic.positive_transition import PositiveTransition
from lib.component.business.project.pou.instructions.bit_logic.normally_open_immediate import NormallyOpenImmediate
from lib.component.business.project.pou.instructions.bit_logic.normally_closed_immediate import NormallyClosedImmediate


class BitLogicCollector(BusinessBase):
    """Bit logic instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-29
    """

    def __init__(self, own_software, params=None):
        super(BitLogicCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        config = {
            'normally_open': NormallyOpen,
            'normally_closed': NormallyClosed,
            'normally_open_immediate': NormallyOpenImmediate,
            'normally_closed_immediate': NormallyClosedImmediate,
            'not': InstructionNot,
            'positive_transition': PositiveTransition,
            'negative_transition': NegativeTransition,
            'output': Output,
            'output_immediate': OutputImmediate,
            'set': InstructionSet,
            'set_immediate': SetImmediate,
            'reset': Reset,
            'reset_immediate': ResetImmediate,
            'set_dominate': SetDominate,
            'reset_dominate': ResetDominate,
            'no_operation': NoOperation
        }

        return config
