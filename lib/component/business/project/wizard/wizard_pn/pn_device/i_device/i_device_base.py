#!/usr/bin/env python

from lib.component.business.project.wizard.wizard_pn.pn_device.pn_device_base import PNDeviceBase


class IDeviceBase(PNDeviceBase):
    """I-Device base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-24
    """

    def __init__(self, own_software, params=None):
        super(IDeviceBase, self).__init__(own_software, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        config = {'sub_slot_number': 1000}

        return config

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

        config = {'input': 1, 'output': 2}

        return config

    @property
    def is_support(self):
        """Whether can configuration i-device in pn wizard
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-18 create
        """

        compile_result = self.get_compile_result()
        is_support = self.own_software.dispatch('i_device_is_support')['rIsSupported']
        result = 0 if compile_result['rErrorCount'] else is_support

        return result

    def add_transfer_areas(self, areas_info):
        """Add transfer area to i-device.
        Args:
            areas_info              type(list)         area information
            ------------------------------------------------------
            single area information details:
            io_type                 type(str)          io type, enum(input, output)
            address                 type(int)          area address, QB: 1152+, IB: 1152+
            length                  type(int)          length of the area, default 1
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        for area_info in areas_info:
            self.add_transfer_area(**area_info)

    def add_transfer_area(self, io_type, address, length=1, sub_slot_number=None):
        """Add transfer area to i-device.
        Args:
            sub_slot_number         type(int)          Sub slot number, 1000+
            io_type                 type(str)          io type, enum(input, output)
            address                 type(int)          area address, QB1152+/IB1152+
            length                  type(int)          length of the area, default 1
            sub_slot_number         type(int)          Sub slot number, 1000+
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        # process io_type
        io_type = self.io_type_config[io_type]
        # process sub_slot_number
        if sub_slot_number is None:
            sub_slot_number = self.params['sub_slot_number']
        if self.params['sub_slot_number'] >= sub_slot_number:
            self.params['sub_slot_number'] += 1
        else:
            self.params['sub_slot_number'] = sub_slot_number + 1
        params = {'subslotNubmer': sub_slot_number, 'ioType': io_type, 'address': address, 'length': length}
        self.own_software.dispatch('add_transfer_area_to_i_device', params)
