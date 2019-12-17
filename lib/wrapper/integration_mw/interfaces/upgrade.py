#!/usr/bin/env python


def upgrade_fw(self, params=None):
    """Upgrade firmware
    Args:
        params           type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        strFilePath      type(str)          the path of the cell
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-23
    """

    template = {
        'strFilePath': {'to_type': 'c_str', 'option': False}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.UpdateFW}
