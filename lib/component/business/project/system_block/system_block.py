#!/usr/bin/env python

import re

from lib.exceptions.check_exception import CheckException
from lib.component.business.business_base import BusinessBase
from lib.exceptions.not_found_exception import NotFoundException


class SystemBlock(BusinessBase):
    """System block class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-23
    """

    def __init__(self, own_software, params=None):
        super(SystemBlock, self).__init__(own_software, params)

    @property
    def cpu_mode_config(self):
        """CPU mode config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        config = {
            'stop': 'eDEVICECOMPASS_POWER_UP_IN_STOP',
            'run': 'eDEVICECOMPASS_POWER_UP_IN_RUN',
            'last': 'eDEVICECOMPASS_POWER_UP_IN_LAST'
        }

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

        data = self.own_software.dispatch('get_system_block_data')['rData']
        params = {'obj': data['obj']}
        element_data = self.own_software.dispatch('get_system_block_element_data', params)['rElement']
        data.update(element_data)

        return data

    @property
    def own_project(self):
        """Get own project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        return self.params['own_business']

    def set_module_info(self, params):
        """Set module information
        Args:
            params             type(dict)          the parameters for set the module information of the system block
            ------------------------------------------------------------------------------------------------
            params details:
            cpu                type(dict)          CPU information
            ************************************************************************************************
            cpu details:
            cpu_type           type(str)           enum: ST30, SR30, ST20 ...
            cpu_version        type(str)           enum: 02.04, 02.05 ...
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-31
        """

        config_data = self.config_data
        if 'cpu' in params:
            if 'cpu_type' in params['cpu']:
                if not params['cpu']['cpu_type']:
                    params['cpu']['cpu_type'] = self.own_software.conn_plc.cpu_type
                params['cpu']['cpu_type'] = self.cpu_type_config[params['cpu']['cpu_type']]

            if 'cpu_version' in params['cpu']:
                if not params['cpu']['cpu_version']:
                    params['cpu']['cpu_version'] = self.own_software.conn_plc.version
                params['cpu']['cpu_version'] = self.get_cpu_version_to_set(params['cpu']['cpu_version'])

        params['obj'] = config_data['obj']
        params = {'rData': params}
        result = self.set_config_data(params)

        return result

    def get_cpu_version_to_set(self, target_version=''):
        """Get the specified cpu version to set
        Args:
            target_version         type(str)          enum: V02.04, V02.05 ...
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-18
        """

        config_data = self.config_data
        versions = config_data['versions']

        if not target_version:
            return versions.GetAt(0)

        if not isinstance(target_version, str):
            target_version = target_version
        elif target_version[0].isdigit():
            target_version = 'V' + target_version
        else:
            target_version = 'V' + target_version[1:]

        size = versions.GetSize()
        for i in range(size):
            if self.compare.compare_c_str(target_version, versions.GetAt(i), 6) == 0:
                return versions.GetAt(i)

        raise NotFoundException('Not found specified version: %s, length of versions: %s.' % (target_version, size))

    def set_communication(self, params):
        """Set communication information
        Args:
            params             type(dict)          the parameters for set the communication of the system block
            ------------------------------------------------------------------------------------------------
            params details:
            ************************************************************************************************
            Ethernet Port details:
            fixed_ip           type(bool)          is fixed ip.
            ip                 type(str)           "IP Address" when network_type is fixed_ip
            subnet_mask        type(str)           "Subnet Mask" when network_type is fixed_ip
            default_gateway    type(str)           "Default Gateway" when network_type is fixed_ip
            station_name       type(str)           "Station Name" when network_type is fixed_ip
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-31
        """
        if params.get('fixed_ip'):
            if not params.get('ip'):
                params['ip'] = self.own_software.conn_ip
            if not params.get('subnet_mask'):
                params['subnet_mask'] = '255.255.255.0'
            if not params.get('default_gateway'):
                params['default_gateway'] = '0.0.0.0'
            if not params.get('station_name'):
                if params.get('role'):
                    params['station_name'] = '%s%s' % (re.sub('[-_]', '', params['role']), params['ip'].split('.')[-1])
                else:
                    params['station_name'] = re.sub('\\.', '', params['ip'])
            self.add_properties({'fixed_ip': params['fixed_ip'], 'ip': params['ip'],
                                 'station_name': params['station_name']})

        config_data = self.config_data
        params['obj'] = config_data['obj']
        params = {'rData': params}
        result = self.set_config_data(params)

        return result

    def set_startup(self, params):
        """Set Startup information
        Args:
            params             type(dict)          the parameters for set the communication of the system block
            ------------------------------------------------------------------------------------------------
            params details:
            ************************************************************************************************
            CPU Mode details:
            cpu_mode           type(int)           enum(stop, start, last)
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-31
        """

        config_data = self.config_data
        if params.get('cpu_mode'):
            params['cpu_mode'] = self.cpu_mode_config[params['cpu_mode']]

        params['obj'] = config_data['obj']
        params = {'rData': params}
        result = self.set_config_data(params)

        return result

    def set_config_data(self, params):
        """Set config data
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-31
        """

        result = self.own_software.dispatch('set_system_block_data', params)
        self.validate()

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

        result = True
        info = self.own_software.dispatch('validate_system_block')
        if info['pErrorCount'] or info['pWarningCount']:
            result = False

        if is_raise and (not result):
            raise CheckException('Validate system block not pass.')

    def check_after_clear(self):
        """Check the system block of the project on PLC after reset PLC
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-23
        """

        result = True
        config_data = self.config_data

        # check password level
        if config_data['password_level'] != 1:
            self.logger.info('After reset factory, password level is %s not 1.' % config_data['password_level'])
            result = False
        # check background time
        if config_data['back_ground_time'] != 10:
            self.logger.info(
                'After reset factory, background time is %s not 10.' % config_data['back_ground_time'])
            result = False
        # check retentive ranges
        if config_data['retentive_ranges'] != 0:
            self.logger.info(
                'After reset factory, retentive ranges is %s not 0.' % config_data['retentive_ranges'])
            result = False
        # check cpu mode
        if config_data['cpu_mode'] != 0:
            self.logger.info('After reset factory, PLC mode is %s not 0.' % config_data['cpu_mode'])
            result = False
        # check fixed ip
        if config_data['fixed_ip'] != 0:
            self.logger.info('After reset factory, fixed ip is %s not 0.' % config_data['fixed_ip'])
            result = False
        # check ip
        if config_data['ip'] != '192.168.2.1':
            self.logger.info('After reset factory, ip is %s.' % config_data['ip'])
            result = False
        # check station name
        if self.compare.compare_c_str(config_data['station_name'], ''):
            self.logger.info('After reset factory, station name is %s not "".' % config_data['station_name'])
            result = False

        return result
