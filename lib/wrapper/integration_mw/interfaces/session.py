#!/usr/bin/env python


def create_session(self, params=None):
    """create connection with plc
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        ipAddress      type(str)          plc ip
        subNetMask     type(str)          mask
        errorMsg       type(str)          The error message after a connection error
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'ipAddress': {'to_type': 'c_str', 'option': False},
        'subNetMask': {'to_type': 'c_str', 'default': '255.255.255.0', 'option': True},
        'errorMsg': {'to_type': 'c_str', 'default': '', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.test_CreateSession}


def test_env_init(self, params=None):
    """check whether the communication module is started
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        strErrMsg       type(str)         The error message after a connection error
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'strErrMsg': {'to_type': 'c_str', 'default': 'communication module start error', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.test_InitEnv}


def load_instruction_libs(self, params=None):
    """load instruction libs
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-20
    """

    self.check_params(params, dict())

    return {'params': params, 'interface': self.interface.PRJ_LoadInstructionLibs}
