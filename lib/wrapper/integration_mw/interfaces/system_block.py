#!/usr/bin/env python


def get_system_block_data(self, params=None):
    """Get the configuration of system block
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rData          type(dict)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-23
    """

    template = {
        'rData': {'to_type': 'sdb_data', 'default': dict(), 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_GetSystemBlockData}


def get_system_block_element_data(self, params=None):
    """Get the configuration of element in system block
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rElement       type(int)
        obj            type(object)       system block
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-23
    """

    template = {
        'rElement': {'to_type': 'compass_element', 'default': 0, 'option': True}
    }
    system_block = params.pop('obj')
    self.check_params(params, template)

    return {'params': params, 'interface': system_block.m_cpu.GetSDBElement, 'check_function': self.check_function}


def set_system_block_data(self, params=None):
    """Set the configuration of system block
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rData          type(dict)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-23
    """

    template = {
        'rData': {'to_type': 'sdb_data', 'option': False}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_SetSystemBlockData}


def validate_system_block(self, params=None):
    """Validate system block
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rData          type(dict)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-31
    """

    template = {
        'pErrorCount': {'to_type': 'word_pointer', 'default': 0, 'option': True},
        'pWarningCount': {'to_type': 'word_pointer', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_ValidateSystemBlock}
