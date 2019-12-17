#!/usr/bin/env python


def force(self, params=None):
    """Force a value to a memory on PLC
    Args:
        params           type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rcInfo           type(dict)         network information
        asMemory         type(dict)         memory information
        nElements        type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-22
    """

    template = {
        'rcInfo': {'to_type': 'network_info', 'option': False},
        'asMemory': {'to_type': 'memory_info', 'option': False},
        'nElements': {'to_type': 'p_int', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.COM_Force, 'check_function': self.check_function}


def unforce_all(self, params=None):
    """UnForce all memory on PLC
    Args:
        params           type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-22
    """

    self.check_params(params, dict())

    return {'params': params, 'interface': self.interface.PRJ_UnforceAll}
