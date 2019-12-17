#!/usr/bin/env python

import re

from lib.exceptions.check_exception import CheckException
from lib.component.business.project.wizard.wizard_base import WizardBase
from lib.component.business.project.wizard.wizard_pn.pn_device.i_device.i_device_base import IDeviceBase
from lib.component.business.project.wizard.wizard_pn.pn_device.controller.controller_base import ControllerBase


class WizardPN(WizardBase):
    """PN wizard class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-23
    """

    def __init__(self, own_software, params=None):
        super(WizardPN, self).__init__(own_software, params)

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

        business = ('i_device', 'controller')

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

        config = {'i_device': IDeviceBase, 'controller': ControllerBase}

        return config

    @property
    def config_data(self):
        """Config data
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-23
        """

        data = self.own_software.dispatch('pn_get_configuration')['rData']
        data['role'] = self.get_role_from_role_config(data['role'])

        return data

    @property
    def is_support(self):
        """Whether can configuration pn wizard
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-18 create
        """

        compile_result = self.own_project.project_compile()
        is_support = self.own_software.dispatch('pn_is_support')['rIsSupported']
        result = 0 if compile_result['rErrorCount'] else is_support

        return result

    @property
    def role_config(self):
        """Role type config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        config = {'controller': 2, 'i-device': 4, 'controller_i-device': 8}

        return config

    def get_role_from_role_config(self, role_number):
        """Get role from role type config dict.
        Args:
            role_number         type(int)          role type: 2, 4, 8
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-12
        """

        config = self.role_config
        for k, v in config.items():
            if int(role_number) == v:
                return k

    def config_controller(self, controller_params, io_device_params, is_set_role=True, is_complete=True, is_raise=True):
        """Configure PN controller
        Args:
            controller_params          type(dict)          parameters information of the controller device
            io_device_params           type(dict, list)    parameters information of the io device
            is_set_role                type(bool)          whether to set role information
            is_complete                type(bool)          whether PN configuration was completed
            is_raise                   type(bool)          whether to raise the exception if validate is not pass
            ----------------------------------------------------------------------------------------------
            controller_params detail:
            role                       type(str)           enum(controller, controller_i-device)
            fixed_ip                   type(bool)          is fixed ip, default True.
            ip                         type(str)           "IP Address", default current ip
            station_name               type(str)           "Station Name", default [role + 'end ip number']
            startup_time               type(int)           Start Up Time, default 10000 ms
            **********************************************************************************************
            io_device_params detail:
            add_type                   type(str)           io device add type: by_gsd, by_catalog
            io_device_type             type(str)           io device type: i-device
            device_number              type(int)           device number, default 1

            gsd_file                   type(str)           the full path of GSD file if add_type=='by_gsd'

            cpu_type                   type(object)        CPU type, enum(SR30, ST30...) if add_type=='by_catalog'
            fixed_ip                   type(bool)          whether fixed ip if add_type=='by_catalog'
            ip                         type(str)           "IP Address" if add_type=='by_catalog'
            station_name               type(str)           "Station Name" if add_type=='by_catalog'
            areas_info                 type(list)          areas information if add_type=='by_catalog'
            **********************************************************************************************
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
        ChangeInfo: cai, yong 2019-12-05
        """

        result = dict()

        # config role information
        if is_set_role:
            self.set_network_info(**controller_params)
        # add io device
        controller = self.find('controller')
        if isinstance(io_device_params, dict):
            io_device_params = [io_device_params]
        for i in io_device_params:
            controller.add_io_device(i)
        # validate pn wizard and generate
        if is_complete:
            result = self.pn_teardown(is_raise)

        return result

    def config_i_device(self, i_device_params, is_set_role=True, is_complete=True):
        """Configure PN i-device
        Args:
            params                     type(dict)          parameters information of the i-device
            is_set_role                type(bool)          whether to set role information
            is_complete                type(bool)          whether PN configuration was completed
            ----------------------------------------------------------------------------------------------
            params detail:
            role                       type(str)           enum(i-device,)
            fixed_ip                   type(bool)          is fixed ip, default True.
            ip                         type(str)           "IP Address", default current ip
            station_name               type(str)           "Station Name", default [role + 'end ip number']
            startup_time               type(int)           Start Up Time, default 10000 ms
            areas_info                 type(list)          transfer areas information
            **********************************************************************************************
            single transfer area information is a dictionary, details:
            io_type                    type(str)           io type, enum(input, output)
            address                    type(int)           area address, QB: 1152+, IB: 1152+
            length                     type(int)           length of the area, default 1
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-05
        """

        areas_info = i_device_params.pop('areas_info', list())

        # config role information
        if is_set_role:
            self.set_network_info(**i_device_params)
        # add transfer areas
        i_device = self.find('i_device')
        i_device.add_transfer_areas(areas_info)
        # validate pn wizard and generate
        if is_complete:
            self.pn_teardown()

    def config_controller_i_device(self, controller_params, io_device_params, i_device_params):
        """Configure PN controller
        Args:
            controller_params          type(dict)          parameters information of the controller device
            io_device_params           type(dict, list)    parameters information of the io device
            i_device_params            type(dict)          parameters information of the i-device
            ----------------------------------------------------------------------------------------------
            controller_params detail:
            role                       type(str)           enum(controller, controller_i-device)
            fixed_ip                   type(bool)          is fixed ip, default True.
            ip                         type(str)           "IP Address", default current ip
            station_name               type(str)           "Station Name", default [role + 'end ip number']
            startup_time               type(int)           Start Up Time, default 10000 ms
            **********************************************************************************************
            io_device_params detail:
            add_type                   type(str)           io device add type: by_gsd, by_catalog
            io_device_type             type(str)           io device type: i-device
            device_number              type(int)           device number, default 1

            gsd_file                   type(str)           the full path of GSD file if add_type=='by_gsd'

            cpu_type                   type(object)        CPU type, enum(SR30, ST30...) if add_type=='by_catalog'
            fixed_ip                   type(bool)          whether fixed ip if add_type=='by_catalog'
            ip                         type(str)           "IP Address" if add_type=='by_catalog'
            station_name               type(str)           "Station Name" if add_type=='by_catalog'
            areas_info                 type(list)          areas information if add_type=='by_catalog'
            **********************************************************************************************
            single area information details:
            device_number              type(int)           device number, default 1
            slot_number                type(int)           slot number, default 1
            sub_slot_number            type(int)           Sub slot number, 1000+
            io_type                    type(str)           io type, enum(input, output)
            address                    type(int)           area address, QB: 128+, IB: 128+
            length                     type(int)           length of the area, default 1
            **********************************************************************************************
            i_device_params detail:
            areas_info                 type(list)          transfer areas information
            **********************************************************************************************
            single transfer area information is a dictionary, details:
            io_type                    type(str)           io type, enum(input, output)
            address                    type(int)           area address, QB: 1152+, IB: 1152+
            length                     type(int)           length of the area, default 1
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-12
        """

        # config controller
        self.config_controller(controller_params, io_device_params, is_set_role=True, is_complete=False)
        # config i-device
        self.config_i_device(i_device_params, is_set_role=False, is_complete=True)

    def set_network_info(self, role, fixed_ip=True, ip='', station_name='', startup_time=10000):
        """Set the network information of pn wizard
        Args:
            role               type(str)           enum(controller, i-device, controller_i-device)
            fixed_ip           type(bool)          is fixed ip.
            ip                 type(str)           "IP Address" when network_type is fixed_ip
            station_name       type(str)           "Station Name" when network_type is fixed_ip
            startup_time       type(int)           Start Up Time
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-25 create
        """

        role_new = self.role_config[role]

        if not ip:
            ip = self.own_software.conn_plc.ip
        if not station_name:
            station_name = '%s%s' % (re.sub('[-_]', '', role), ip.split('.')[-1])

        cpu_type = self.own_software.conn_plc.cpu_type
        cpu_version = self.own_system_block.get_cpu_version_to_set()
        self.add_properties({'fixed_ip': fixed_ip, 'ip': ip, 'station_name': station_name,
                             'cpu_type': self.own_software.conn_plc.cpu_type})
        params = {'plcRole': role_new, 'isFixedIP': fixed_ip, 'plcIP': ip, 'plcName': station_name,
                  'startupTime': startup_time, 'strType': cpu_type, 'strVer': cpu_version}
        result = self.own_software.dispatch('pn_set_network_info', params)

        return result

    def set_network_info_by_config_data(self, role, ethernet_port=None, communication=None):
        """Set the network information by configuration data of the pn wizard
        Args:
            role               type(int)          enum(controller, i-device, controller_i-device)
            ethernet_port      type(dict)         Ethernet Port information
            communication      type(dict)         Communication information
            ---------------------------------------------------------------------------------------------------
            ethernet_port detail:
            network_type       type(str)          enum(fixed_ip, obtain_by_other)

            communication detail:
            send_clock         type(str)          Send Clock, enum(1.000,)
            startup_time       type(str)          Start Up Time

        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-25 create
        """

        role_new = self.role_config[role]

        ethernet_port = ethernet_port or dict()
        if not ethernet_port.get('network_type'):
            ethernet_port['network_type'] = 'fixed_ip'

        communication = communication or dict()
        if not communication.get('send_clock'):
            communication['send_clock'] = 1.000
        if not communication.get('startup_time'):
            communication['startup_time'] = 10000

        config_data = self.config_data
        params = {'rData': {'role': role_new, 'ethernet_port': ethernet_port, 'communication': communication,
                            'obj': config_data['obj']}}
        result = self.set_config_data(params)

        return result

    def set_config_data(self, params):
        """Set config data
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-25
        """

        result = self.own_software.dispatch('pn_set_configuration', params)

        return result

    def pn_teardown(self, is_raise=True):
        """Validate PN configuration and generator binary data
        Args:
            is_raise           type(bool)             whether to raise the exception if validate is not pass
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-05 create
        """

        # correction sdb data
        self.own_system_block.set_module_info({'cpu': {'cpu_type': ''}})
        # validate pn wizard
        result = self.validate(is_raise=is_raise)
        # generator
        if result['result']:
            self.config_complete()

        return result

    def validate(self, is_raise=True):
        """Validate system block
        Args:
            is_raise           type(bool)             whether to raise the exception if validate is not pass
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-31
        """

        result = {'result': True, 'error_code': None, 'error_description': None}
        config_data = self.config_data
        info = self.own_software.dispatch('validate_wizard_pn', {'rData': config_data['obj']})
        self.logger.info('Wizard validation result: %s' % info)
        if info['code']:
            result['result'] = False
            result['error_code'] = info['code']
            result['error_description'] = self.error_code.error_code_config.get(info['code'], '')

        if is_raise and (not result['result']):
            raise CheckException('Validate pn configuration not pass.')

        return result

    def config_complete(self):
        """PN configuration complete
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-31
        """

        self.own_software.dispatch('pn_config_complete')

    def check_after_clear(self):
        """Check the PN of the project on PLC after reset PLC
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-23
        """

        result = True
        data = self.config_data
        if data['is_enabled']:
            self.logger.info('After reset factory, the configuration of PN has not been cleaned up.')
            result = False

        return result
