#!/usr/bin/env python

from lib.component.business.project.wizard.wizard_pn.pn_device.io_device.by_catalog.by_catalog_base import ByCatalogBase


class CatalogIDevice(ByCatalogBase):
    """Add [io device: i-device] by catalog.
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
    ChangeInfo: cai, yong 2019-12-10
    """

    def __init__(self, own_software, params=None):
        super(CatalogIDevice, self).__init__(own_software, params)

    @property
    def io_type_config(self):
        """IO type configuration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29 create
        """

        config = {'input': {'id': 1, 'dap_id': 'TransferAreaInput', 'i_dent_number': '0x20000000'},
                  'output': {'id': 2, 'dap_id': 'TransferAreaOutput', 'i_dent_number': '0x10000000'}}

        return config

    def initialize(self):
        """Initialize the io device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-10
        """

        # add pn device
        self.add_io_device_to_controller()
        # set pn device properties
        self.set_io_device_properties()
        # add transfer area
        self.add_transfer_areas()

    def add_io_device_to_controller(self):
        """Add io device to controller device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-10
        """

        dap_info = self.dap_config[self.params['cpu_type']]
        dap_id = dap_info['dap_id']
        i_dent_number = self.converter.convert_to_int(dap_info['i_dent_number'], 16)

        params = {'strGSDFullPathName': '', 'nDapModuleIDstr': dap_id,
                  'dapModuleIdentNumber': i_dent_number, 'deviceNumber': self.params['device_number']}
        self.own_software.dispatch('add_io_device', params)

    def set_io_device_properties(self):
        """Set IO device properties.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-10
        """

        is_fixed = self.params['fixed_ip']
        device_ip = self.params['device_ip']
        device_name = self.params['station_name']

        params = {'deviceNumber': self.params['device_number'], 'isIPFixed': is_fixed, 'deviceIP': device_ip,
                  'deviceName': device_name}
        self.own_software.dispatch('set_io_device_properties', params)

    def add_transfer_areas(self):
        """Add transfer area to i-device.
        Args:
            area_info                  type(list)          area information
            ------------------------------------------------------
            single area information details:
            device_number              type(int)           device number, default 1
            slot_number                type(int)           slot number, default 1
            sub_slot_number            type(int)           Sub slot number, 1000+
            io_type                    type(str)           io type, enum(input, output)
            address                    type(int)           area address, QB: 128+, IB: 128+
            length                     type(int)           length of the area, default 1
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        for area_info in self.params['areas_info']:
            self.add_transfer_area(**area_info)

    def add_transfer_area(self, io_type='input', address=128, length=1, slot_number=1, sub_slot_number=None):
        """Add transfer area to i-device.
        Args:
            io_type                    type(str)           io type, enum(input, output)
            address                    type(int)           area address, QB: 128+, IB: 128+
            length                     type(int)           length of the area, default 1
            slot_number                type(int)           slot number, default 1
            sub_slot_number            type(int)           Sub slot number, 1000+
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        # process io_type
        dap_id = self.io_type_config[io_type]['dap_id']
        i_dent_number = self.converter.convert_to_int(self.io_type_config[io_type]['i_dent_number'], 16) + length
        io_type = self.io_type_config[io_type]['id']
        # process sub_slot_number
        if sub_slot_number is None:
            sub_slot_number = self.params['sub_slot_number']
        if self.params['sub_slot_number'] >= sub_slot_number:
            self.params['sub_slot_number'] += 1
        else:
            self.params['sub_slot_number'] = sub_slot_number + 1
        params = {'deviceId': self.params['device_number'], 'slotNum': slot_number, 'subslotNubmer': sub_slot_number,
                  'submoduleIDstr': dap_id, 'submoduleIdentNumber': i_dent_number, 'ioType': io_type,
                  'address': address, 'length': length}
        self.own_software.dispatch('add_transfer_area_to_controller', params)
