#!/usr/bin/env python

from lib.component.business.project.wizard.wizard_pn.pn_device.io_device.io_device_base import IODeviceBase


class ByCatalogBase(IODeviceBase):
    """Add IO Device by catalog.
    Args:
        params                     type(dict)          io-device parameters
        -----------------------------------------------------------
        params details:
        device_number              type(int)           device number, default 1
        cpu_type                   type(object)        CPU type, enum(SR30, ST30...)
        fixed_ip                   type(bool)          whether fixed ip
        device_ip                  type(str)           "IP Address" of the io device
        station_name               type(str)           "Station Name"  of the io device
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-26
    """

    def __init__(self, own_software, params=None):
        super(ByCatalogBase, self).__init__(own_software, params)

    @property
    def dap_config(self):
        """Dap fields configuration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-10
        """

        config = {
            'SR20': {'dap_id': 'DAP1', 'i_dent_number': '0x80000201'},
            'SR30': {'dap_id': 'DAP2', 'i_dent_number': '0x80000301'},
            'SR40': {'dap_id': 'DAP3', 'i_dent_number': '0x80000401'},
            'SR60': {'dap_id': 'DAP4', 'i_dent_number': '0x80000601'},
            'ST20': {'dap_id': 'DAP5', 'i_dent_number': '0x80000200'},
            'ST30': {'dap_id': 'DAP6', 'i_dent_number': '0x80000300'},
            'ST40': {'dap_id': 'DAP7', 'i_dent_number': '0x80000400'},
            'ST60': {'dap_id': 'DAP8', 'i_dent_number': '0x80000600'}
        }

        return config
