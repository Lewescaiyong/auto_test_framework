#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.instruction_collector.instruction_collector import \
    InstructionCollector


class NetworkBase(BusinessBase):
    """The network base class.
    Args:
        params          type(dict)           network parameters
        -----------------------------------------------------------
        params details:
        id              type(int)            network id
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-18
    """

    def __init__(self, own_software, params=None):
        super(NetworkBase, self).__init__(own_software, params)

    @property
    def business_config(self):
        """Config the businesses type that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-18
        """

        business = ('instruction_collector',)

        return business

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-18
        """

        config = {'instruction_collector': InstructionCollector}

        return config

    @property
    def own_pou(self):
        """Get own pou
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        return self.params['own_business'].params['own_business']

    def get_cell_location(self, row_id, col_id):
        """Get the GRID CELL LOCATION of the instruction.
        Args:
            row_id                 type(int)          the row id in the network where add instruction
            col_id                 type(int)          the col id in the network where add instruction
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        params = {'row_id': row_id, 'col_id': col_id}
        cell_location = self.own_software.dispatch('grid_cell_location', params)['code']

        return cell_location

    def check_whether_can_drop(self, cell_location, instruction_id, instruction_sub_id):
        """Check whether can drop instruction
        Args:
            cell_location         type(int)
            instruction_id        type(int)          the instruct id
            instruction_sub_id    type(int)          the instruct sub id
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        params = {
            'mw_id': self.own_pou.get_mw_id(),
            'network_id': self.params['id'],
            'cell_location': cell_location,
            'instruction_id': instruction_id,
            'instruction_sub_id': instruction_sub_id
        }
        result = self.own_software.dispatch('check_whether_can_drop', params)
        if result['result'] != 1:
            raise CheckException('The instruction is not can be inserted into the project.')

    def insert_instruction(self, cell_location, operand_location, instruction_id, instruction_sub_id):
        """Insert the instruction into the project
        Args:
            cell_location         type(c_type)
            operand_location      type(c_type)
            instruction_id        type(int)          the instruct id
            instruction_sub_id    type(int)          the instruct sub id
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        params = {
            'mw_id': self.own_pou.get_mw_id(),
            'network_id': self.params['id'],
            'cell_location': cell_location,
            'operand_location': operand_location,
            'instruction_id': instruction_id,
            'instruction_sub_id': instruction_sub_id,
            'rectangle': self.own_pou.get_rectangle()
        }
        self.own_software.dispatch('insert_instruction', params)
