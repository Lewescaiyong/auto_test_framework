#!/usr/bin/env python


def grid_operand_location(self, params=None):
    """Create a operand location
    Args:
        params           type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        row_id           type(int)          the row number of the cell
        col_id           type(int)          the col number of the cell
        location         type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-23
    """

    template = {
        'row_id': {'to_type': 'p_int', 'option': False},
        'col_id': {'to_type': 'p_int', 'option': False},
        'location': {'to_type': 'p_int', 'default': 0, 'option': True}
    }
    self.check_params(params, template)
    args_order = ('row_id', 'col_id', 'location')

    return {'params': params, 'interface': self.interface.GRID_OPERAND_LOCATION, 'check_function': self.check_function,
            'args_order': args_order}


def set_instruction_value(self, params=None):
    """set the value of the instruction
    Args:
        params             type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        pouId              type(c_type)
        netNumber          type(int)          the network id
        opLoc              type(c_type)
        pOperand           type(str)          the value of the location
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-23
    """

    template = {
        'pouId': {'to_type': 'c_type', 'option': False},
        'netNumber': {'to_type': 'p_int', 'option': False},
        'opLoc': {'to_type': 'c_type', 'option': False},
        'pOperand': {'to_type': 'p_str', 'option': False}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.GRID_SetOperand}
