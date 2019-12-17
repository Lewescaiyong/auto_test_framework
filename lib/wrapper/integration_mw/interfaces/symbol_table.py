#!/usr/bin/env python


def create_s7200_symbol_table(self, params=None):
    """Create S7200 SymbolTable
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rSymId         type(dict)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-08
    """

    template = {
        'rSymId': {'to_type': 'mw_id', 'default': dict(), 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.SYM_CreateS7200SymbolTable}


def create_io_symbol_table(self, params=None):
    """Create IO SymbolTable
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rSymId         type(dict)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-08
    """

    template = {
        'rSymId': {'to_type': 'mw_id', 'default': dict(), 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.SYM_CreateIOSymbolTable}


def tab_insert(self, params=None):
    """Tab insert
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rType          type(str)          enum: POU_SBR, POU_INT, POU_MAIN, SYM_USER, CHT_USER, DB_USER
        rId            type(dict)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-08
    """

    template = {
        'rType': {'to_type': 'struct_arg', 'option': False},
        'rId': {'to_type': 'mw_id', 'default': dict(), 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.TAB_Insert}
