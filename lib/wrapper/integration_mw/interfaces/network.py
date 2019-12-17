#!/usr/bin/env python


def grid_cell_location(self, params=None):
    """Create a grid cell location
    Args:
        params           type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        row_id           type(int)          the row number of the cell
        col_id           type(int)          the col number of the cell
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-20
    """

    template = {
        'row_id': {'to_type': 'p_int', 'option': False},
        'col_id': {'to_type': 'p_int', 'option': False}
    }
    self.check_params(params, template)
    args_order = ('row_id', 'col_id')

    return {'params': params, 'interface': self.interface.GRID_CELL_LOCATION, 'check_function': self.check_function,
            'args_order': args_order}


def check_whether_can_drop(self, params=None):
    """Check whether can drop instruction
    Args:
        params                type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        mw_id                 type(c_type)
        network_id            type(int)          the network id
        cell_location         type(c_type)
        instruction_id        type(int)          the instruct id
        instruction_sub_id    type(int)          the instruct sub id
        edit_mode             type(int)          the edit mode
        result                type(int)          used to record the check result
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-20
    """

    template = {
        'mw_id': {'to_type': 'c_type', 'option': False},
        'network_id': {'to_type': 'p_int', 'option': False},
        'cell_location': {'to_type': 'c_type', 'option': False},
        'instruction_id': {'to_type': 'p_int', 'option': False},
        'instruction_sub_id': {'to_type': 'p_int', 'default': 0, 'option': True},
        'edit_mode': {'to_type': 'struct_arg', 'default': 'INSERT_MODE', 'option': True},
        'result': {'to_type': 'bool_pointer', 'default': False, 'option': True}
    }
    self.check_params(params, template)
    args_order = ('mw_id', 'network_id', 'cell_location', 'instruction_id', 'instruction_sub_id', 'edit_mode', 'result')

    return {'params': params, 'interface': self.interface.GRID_CanDropInstruction, 'args_order': args_order}


def insert_instruction(self, params=None):
    """Insert the instruction into the project
    Args:
        params             type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        mw_id                 type(c_type)
        network_id            type(int)          the network id
        operand_location      type(c_type)
        instruction_id        type(int)          the instruct id
        instruction_sub_id    type(int)          the instruct sub id
        edit_mode             type(int)          the edit mode
        cell_location         type(c_type)
        rectangle             type(c_type)       used to record the insert result
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-20
    """

    template = {
        'mw_id': {'to_type': 'c_type', 'option': False},
        'network_id': {'to_type': 'p_int', 'option': False},
        'operand_location': {'to_type': 'p_type', 'option': False},
        'instruction_id': {'to_type': 'p_int', 'option': False},
        'instruction_sub_id': {'to_type': 'p_int', 'default': 0, 'option': True},
        'edit_mode': {'to_type': 'struct_arg', 'default': 'INSERT_MODE', 'option': True},
        'cell_location': {'to_type': 'c_type', 'option': False},
        'rectangle': {'to_type': 'c_type', 'option': False}
    }
    self.check_params(params, template)
    args_order = ('mw_id', 'network_id', 'operand_location', 'instruction_id', 'instruction_sub_id', 'edit_mode',
                  'cell_location', 'rectangle')

    return {'params': params, 'interface': self.interface.GRID_SetElementInst, 'args_order': args_order}
