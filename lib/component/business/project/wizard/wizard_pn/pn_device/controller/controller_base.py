#!/usr/bin/env python

from lib.component.business.project.wizard.wizard_pn.pn_device.pn_device_base import PNDeviceBase
from lib.component.business.project.wizard.wizard_pn.pn_device.io_device.io_device_collector import IODeviceCollector


class ControllerBase(PNDeviceBase):
    """Controller base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-24
    """

    def __init__(self, own_software, params=None):
        super(ControllerBase, self).__init__(own_software, params)

    @property
    def business_config(self):
        """Config the businesses type that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        business = ('io_device_collector',)

        return business

    @property
    def add_config(self):
        """[pou type -- pou class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        config = {'io_device_collector': IODeviceCollector}

        return config

    @property
    def is_support(self):
        """Whether can configuration controller in pn wizard
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-18 create
        """

        compile_result = self.get_compile_result()
        is_support = self.own_software.dispatch('controller_is_support')['rIsSupported']
        result = 0 if compile_result['rErrorCount'] else is_support

        return result

    def add_io_device(self, params=None):
        """Add io device
        Args:
            params                     type(dict)          parameters information of io device
            **********************************************************************************************
            params detail:
            add_type                   type(str)           io device add type: by_gsd, by_catalog
            io_device_type             type(str)           io device type: i-device
            gsd_file                   type(str)           the full path of GSD file if add_type=='by_gsd'
            i_device_pn                type(object)        wizard_pn object if add_type=='by_catalog'
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-05
        """

        add_type = params.pop('add_type')
        io_device_type = params.pop('io_device_type')

        if add_type == 'by_gsd':
            if io_device_type == 'i-device':
                self.add_i_device_by_gsd(params)

        if add_type == 'by_catalog':
            if io_device_type == 'i-device':
                self.add_i_device_by_catalog(params)

    def add_i_device_by_gsd(self, params=None):
        """Add i-device by gsd file
        Args:
            params             type(int)          parameters information of io device
            ----------------------------------------------------------------------------
            params detail:
            device_number      type(int)          device number, default 1
            gsd_file           type(str)          the full path of GSD file if add_type=='by_gsd'
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-04
        """

        # add io device: i-device
        collector = self.find('io_device_collector')
        collector.add('gsd_i_device', params, True)

    def add_i_device_by_catalog(self, params=None):
        """Add i-device by catalog config
        Args:
            params                     type(int)           parameters information of io device
            ----------------------------------------------------------------------------
            params detail:
            device_number              type(int)           device number, default 1
            cpu_type                   type(object)        CPU type, enum(SR30, ST30...)
            fixed_ip                   type(bool)          whether fixed ip
            device_ip                  type(str)           "IP Address" of the io device
            station_name               type(str)           "Station Name"  of the io device
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-04
        """

        # add io device: i-device
        collector = self.find('io_device_collector')
        collector.add('catalog_i_device', params, True)
