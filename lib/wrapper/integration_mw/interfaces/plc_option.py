#!/usr/bin/env python


def set_plc_mode(self, params=None):
    """set plc mode
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        Mode           type(int)          PLC mode: {0: stop, 1: run}
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'Mode': {'to_type': 'p_int', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.COM_SetOpMode}


def get_plc_mode(self, params=None):
    """get plc mode
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        pMode           type(int)          PLC mode: {0: stop, 1: run}
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    template = {
        'pMode': {'to_type': 'word_pointer', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.COM_GetOpMode}


def get_plc_info(self, params=None):
    """get plc information
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rcInfo         type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-24
    """

    template = {
        'rcInfo': {'to_type': 'plc_info', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.COM_GetDeviceInformation}


def plc_power_up_reset(self, params=None):
    """power up reset
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-24
    """

    self.check_params(params, dict())

    return {'params': params, 'interface': self.interface.COM_PowerUpReset}


def plc_clear(self, params=None):
    """clear project on plc
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        eBlockType     type(int)          upload type: BLOCK_TYPE_INVALID, BLOCK_TYPE_OB, BLOCK_TYPE_DB,
                                                       BLOCK_TYPE_SDB, BLOCK_TYPE_ALL
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-11
    """

    template = {
        'eBlockType': {'to_type': 'struct_arg', 'default': 'BLOCK_TYPE_ALL', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_ClearPLC}


def read_memory_data(self, params=None):
    """Read plc specified address data
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rcInfo         type(dict)         network information
        asMemory       type(dict)         memory information
        nElements      type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    template = {
        'rcInfo': {'to_type': 'network_info', 'option': False},
        'asMemory': {'to_type': 'memory_info', 'option': False},
        'nElements': {'to_type': 'p_int', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.COM_DataRead}


def plc_get_clock(self, params=None):
    """Get the clock of PLC device.
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        pTimeDate      type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-24
    """

    template = {
        'pTimeDate': {'to_type': 'clock_struct', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.COM_GetTimeDate}


def plc_set_clock(self, params=None):
    """Set the clock of PLC device.
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        pTimeDate      type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-24
    """

    template = {
        'pTimeDate': {'to_type': 'clock_struct', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.COM_SetTimeDate}
