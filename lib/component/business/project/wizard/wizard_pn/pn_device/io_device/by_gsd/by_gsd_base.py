#!/usr/bin/env python

from lib.component.business.project.wizard.wizard_pn.pn_device.io_device.io_device_base import IODeviceBase


class ByGSDBase(IODeviceBase):
    """Add IO Device by GSD file.
    Args:
        params          type(dict)           i-device parameters
        -----------------------------------------------------------
        params details:
        gsd_file        type(str)            the full path of GSD file
        device_number   type(int)            device number, default 1
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-26
    """

    def __init__(self, own_software, params=None):
        super(ByGSDBase, self).__init__(own_software, params)
