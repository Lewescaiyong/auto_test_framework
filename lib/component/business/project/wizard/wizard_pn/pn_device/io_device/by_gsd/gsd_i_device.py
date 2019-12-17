#!/usr/bin/env python

import os

from lib.tools.xml.xml_parser import XMLParser
from lib.component.business.project.wizard.wizard_pn.pn_device.io_device.by_gsd.by_gsd_base import ByGSDBase


class GSDIDevice(ByGSDBase):
    """Add [io device: i-device] by GSD file.
    Args:
        gsd_file        type(str)            the full path of GSD file
        device_number   type(int)            device number, default 1
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-26
    """

    def __init__(self, own_software, params=None):
        super(GSDIDevice, self).__init__(own_software, params)

    def initialize(self):
        """Initialize the io device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-26
        """

        # parse GSD file
        self.parse_gsd_file()
        # add pn device
        self.add_io_device_to_controller()
        # set pn device properties
        self.set_io_device_properties()

    def parse_gsd_file(self):
        """Parse the gsd file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-26
        """

        if ':' not in self.params['gsd_file']:
            self.params['gsd_file'] = os.path.join(self.gsd_file_options.gsd_file_path, self.params['gsd_file'])

        parser = XMLParser(self.params['gsd_file'])
        data = parser.xml_parser()
        self.add_properties({'gsd_data': data})

    def add_io_device_to_controller(self):
        """Add io device to controller device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-28
        """

        info = self.params['gsd_data']['ISO15745Profile']['ProfileBody']['ApplicationProcess']['DeviceAccessPointList']
        dap_id = info['DeviceAccessPointItem']['ID']
        i_dent_number = info['DeviceAccessPointItem']['ModuleIdentNumber']
        i_dent_number = self.converter.convert_to_int(i_dent_number, 16)

        params = {'strGSDFullPathName': self.params['gsd_file'], 'nDapModuleIDstr': dap_id,
                  'dapModuleIdentNumber': i_dent_number, 'deviceNumber': self.params['device_number']}
        self.own_software.dispatch('add_io_device', params)

    def set_io_device_properties(self):
        """Set IO device properties.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-28
        """

        info = self.params['gsd_data']['ISO15745Profile']['ProfileBody']['ApplicationProcess']['DeviceAccessPointList']
        if 'fixed_ip' in self.params:
            is_fixed = self.params['fixed_ip']
        else:
            is_fixed = ('LOCAL' == info['DeviceAccessPointItem']['AddressAssignment'])
        device_name = self.params.get('device_name') or info['DeviceAccessPointItem']['DNS_CompatibleName']

        params = {'deviceNumber': self.params['device_number'], 'isIPFixed': is_fixed,
                  'deviceIP': self.params['device_ip'], 'deviceName': device_name}
        self.own_software.dispatch('set_io_device_properties', params)
