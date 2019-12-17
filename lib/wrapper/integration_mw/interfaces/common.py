#!/usr/bin/env python


def compare_with_plc(self, params=None):
    """Compare the project between MicroWin and PLC device
    Args:
        params              type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rOptions            type(dict)
        pResults            type(int)
        bCheckPouOrder      type(int)
        bIgnoreTimestamps   type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-08
    """

    template = {
        'rOptions': {'to_type': 'compare_options', 'option': False},
        'pResults': {'to_type': 'compare_results', 'default': 0, 'option': True},
        'bCheckPouOrder': {'to_type': 'p_type', 'default': False, 'option': True},
        'bIgnoreTimestamps': {'to_type': 'p_type', 'default': True, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_ExecuteCompare}


def get_micro_win_version(self, params=None):
    """Compare the project between MicroWin and PLC device
    Args:
        params              type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rRevisionType            type(int)
        rMajVer                  type(int)
        MinVer                   type(int)
        rSP                      type(int)
        rHF                      type(int)
        rIncNo                   type(int)
        rBldNo                   type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-08
    """

    template = {
        'rRevisionType': {'to_type': 'word_pointer', 'default': 1, 'option': True},
        'rMajVer': {'to_type': 'word_pointer', 'default': 1, 'option': True},
        'MinVer': {'to_type': 'word_pointer', 'default': 1, 'option': True},
        'rSP': {'to_type': 'word_pointer', 'default': 1, 'option': True},
        'rHF': {'to_type': 'word_pointer', 'default': 1, 'option': True},
        'rIncNo': {'to_type': 'word_pointer', 'default': 1, 'option': True},
        'rBldNo': {'to_type': 'word_pointer', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.test_GetMicroWinVersion}
