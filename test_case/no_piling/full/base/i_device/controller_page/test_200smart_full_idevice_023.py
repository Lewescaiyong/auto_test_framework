#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice023(CaseMW):
    """Device name
    No.: test_200smart_full_idevice_023
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "Controller", click "Next";
        3. Two devices have been added;
    Step actions:
        1. Modify device name to 63 characters with lower case letters, digits, "-" and ".";
        2. Modify device name to 64 characters;
        3. Modify device name with capital letters;
        4. Modify device name with Chinese characters;
        5. Modify device name to "device192.168.0.2";
        6. Modify device name begin with port-123 or port-123-45678;
        7. Modify device name begin with  "-" or ".".
        8. Modify device name end with  "-" or ".".
    Expected results:
        1. Modify successful;
        2. Modify failed with reasonable prompt;
        3. Modify failed with reasonable prompt;
        4. Modify successful;
        5. Modify failed with reasonable prompt;
        6. Modify failed with reasonable prompt;
        7. Modify failed with reasonable prompt;
        8. Modify failed with reasonable prompt;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-12-13 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice023, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        # new a project
        time_str = self.converter.convert_time_to_str()
        self.prj_file = 'new_%s.smart' % time_str
        self.PROJECT.project_new(self.prj_file)

        self.logger.info('2. In PN wizard, select plc role is "Controller", click "Next";')
        self.logger.info('3. Two devices have been added;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice023, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Modify device name to 63 characters with lower case letters, digits, "-" and ".";')
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': 'aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdde1_.e',
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        result1 = wizard_pn.config_controller(controller_params, io_device_params, is_raise=False)

        self.logger.info('2. Modify device name to 64 characters;')
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': 'aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddee1234',
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        result2 = wizard_pn.config_controller(controller_params, io_device_params, is_raise=False)

        self.logger.info('3. Modify device name with capital letters;')
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': 'aabbccddEE',
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        result3 = wizard_pn.config_controller(controller_params, io_device_params, is_raise=False)

        self.logger.info('4. Modify device name with Chinese characters;')
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': 'aabb中文ccdd',
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        result4 = wizard_pn.config_controller(controller_params, io_device_params, is_raise=False)

        self.logger.info('5. Modify device name to "device192.168.0.2";')
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': 'device192.168.0.2',
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        result5 = wizard_pn.config_controller(controller_params, io_device_params, is_raise=False)

        self.logger.info('6. Modify device name begin with port-123 or port-123-45678;')
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': self.common.get_random_element(('port-123', 'port-123-45678')),
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        result6 = wizard_pn.config_controller(controller_params, io_device_params, is_raise=False)

        self.logger.info('7. Modify device name begin with  "-" or ".".')
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': '%saabbcc' % self.common.get_random_element(('-', '.')),
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        result7 = wizard_pn.config_controller(controller_params, io_device_params, is_raise=False)

        self.logger.info('8. Modify device name end with  "-" or ".".')
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': 'aabbcc%s' % self.common.get_random_element(('-', '.')),
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        result8 = wizard_pn.config_controller(controller_params, io_device_params, is_raise=False)

        self.logger.info('Expected results:')
        self.logger.info('1. Modify successful;')
        self.logger.info('result1: %s.' % str(result1))
        if not result1['result']:
            raise CheckException('1. Modify failed;')

        self.logger.info('2. Modify failed with reasonable prompt;')
        self.logger.info('result2: %s.' % str(result2))
        if result2['result'] or (result2['error_code'] != -1610610847):
            raise CheckException('2. Modify successfully, or error code is incorrect;')

        self.logger.info('3. Modify failed with reasonable prompt;')
        self.logger.info('result3: %s.' % str(result3))
        if result3['result'] or (result3['error_code'] != -1610610847):
            raise CheckException('3. Modify successfully, or error code is incorrect;')

        self.logger.info('4. Modify successful;')
        self.logger.info('result4: %s.' % str(result4))
        if not result4['result']:
            raise CheckException('4. Modify failed;')

        self.logger.info('5. Modify failed with reasonable prompt;')
        self.logger.info('result5: %s.' % str(result5))
        if result5['result'] or (result5['error_code'] != -1610610847):
            raise CheckException('5. Modify successfully, or error code is incorrect;')

        self.logger.info('6. Modify failed with reasonable prompt;')
        self.logger.info('result6: %s.' % str(result6))
        if result6['result'] or (result6['error_code'] != -1610610847):
            raise CheckException('6. Modify successfully, or error code is incorrect;')

        self.logger.info('7. Modify failed with reasonable prompt;')
        self.logger.info('result7: %s.' % str(result7))
        if result7['result'] or (result7['error_code'] != -1610610847):
            raise CheckException('7. Modify successfully, or error code is incorrect;')

        self.logger.info('8. Modify failed with reasonable prompt;')
        self.logger.info('result8: %s.' % str(result8))
        if result8['result'] or (result8['error_code'] != -1610610847):
            raise CheckException('8. Modify successfully, or error code is incorrect;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice023, self).cleanup()
