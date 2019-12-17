#!/usr/bin/env python


def grid_rectangle(self, params=None):
    """Create a grid rectangle
    Args:
        params           type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-23
    """

    self.check_params(params, dict())

    return {'params': params, 'interface': self.interface.GRID_RECTANGLE, 'check_function': self.check_function}


def pou_set_password(self, params=None):
    """Set the password for pou page.
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rPouId         type(dict)         the mw_id of pou
        rPassword      type(str)          password str
        rStyle         type(str)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'rPouId': {'to_type': 'mw_id', 'option': False},
        'rPassword': {'to_type': 'c_str', 'option': False},
        'rStyle': {'to_type': 'struct_arg', 'default': 'DISPLAY_INVISIBLE', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.TAB_SetDisplayProtection}


def pou_is_protected(self, params=None):
    """Whether th pou is protected.
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rId            type(dict)         the mw_id of pou
        rStyle         type(str)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'rId': {'to_type': 'mw_id', 'option': False},
        'rStyle': {'to_type': 'int_pointer', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.test_GetDisplayProtection}


def pou_authorize(self, params=None):
    """POU authorize.
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rPouId         type(dict)         the mw_id of pou
        rPassword      type(str)          password str
        bPermanent     type(int)          whether to remove the password
        bIsSha512      type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'rPouId': {'to_type': 'mw_id', 'option': False},
        'rPassword': {'to_type': 'c_str', 'option': False},
        'bPermanent': {'to_type': 'p_int', 'default': 0, 'option': True},
        'bIsSha512': {'to_type': 'p_int', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.TAB_AuthorizePassword}
