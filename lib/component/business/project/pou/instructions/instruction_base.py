#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.component.business.business_base import BusinessBase


class InstructionBase(BusinessBase):
    """The instructions base class.
    Args:
        params          type(dict)           instruction parameters
        -----------------------------------------------------------
        params details:
        row_id          type(int)            row id of the network
        col_id          type(int)            col id of the network
        values          type(list, tuple)    values for config instruction locations
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-20
    """

    def __init__(self, own_software, params=None):
        super(InstructionBase, self).__init__(own_software, params)

    @property
    def own_network(self):
        """Get own network
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        return self.params['own_business'].params['own_business']

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

        return self.own_network.own_pou

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        config = {'sub_id': 0}

        return config

    def initialize(self):
        """Initialize the instruction.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        # check whether can drop instruction
        self.check_whether_can_drop()
        # insert the instruction into the network
        self.insert()
        # set the value of the instruction
        self.set_instruction_value()

    def check_whether_can_drop(self):
        """Check whether can drop the instruction
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        cell_location = self.own_network.get_cell_location(
            **{'row_id': self.params['row_id'], 'col_id': self.params['col_id']})
        params = {
            'cell_location': cell_location,
            'instruction_id': self.params['id'],
            'instruction_sub_id': self.params['sub_id']
        }
        self.own_network.check_whether_can_drop(**params)
        self.add_properties({'cell_location': cell_location})

    def insert(self):
        """Insert the instruction into the network
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        operand_location = self.get_operand_location()
        params = {
            'cell_location': self.params['cell_location'],
            'operand_location': operand_location,
            'instruction_id': self.params['id'],
            'instruction_sub_id': self.params['sub_id']
        }
        self.own_network.insert_instruction(**params)

    def get_operand_location(self, location=None, col_offset=0):
        """Get the GRID CELL OPERAND LOCATION of the instruction.
        Args:
            location           type(dict)
            col_offset         type(int)
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        if not location:
            location = {'row_add': 0, 'col_add': 0, 'id': 1}

        params = {'row_id': self.params['row_id'] + location['row_add'],
                  'col_id': self.params['col_id'] + location['col_add'] + col_offset, 'location': location['id']}
        operand_location = self.own_software.dispatch('grid_operand_location', params)['code']

        return operand_location

    def set_instruction_value(self):
        """set the value of the instruction
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        col_offset = 0
        values = self.params.get('values', None) or list()
        for i, v in enumerate(values):
            operand_location = self.get_operand_location(self.params['locations'][i], col_offset)
            params = {
                'pouId': self.own_pou.get_mw_id(),
                'netNumber': self.own_network.params['id'],
                'opLoc': operand_location,
                'pOperand': v
            }
            for n in range(2):
                try:
                    self.own_software.dispatch('set_instruction_value', params)
                except CheckException:
                    self.logger.info('Has been set value %s times.' % (n + 1))
                    col_offset = -1
                    params['opLoc'] = self.get_operand_location(self.params['locations'][i], col_offset)
                else:
                    break
