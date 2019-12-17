#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice024(CaseMW):
    """IP Setting
    No.: test_200smart_full_idevice_024
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Import two gsdml files, fixed and dcp;
        3. In PN wizard, config plc as controller and add the two devices;
    Step actions:
        1. View the "IP Setting" and "IP Address" of the fixed device in device table;
        2. View the "IP Setting" and "IP Address" of the dcp device in device table;
        3. Add a catalog device, View the "IP Setting" and "IP Address" of the dcp device in device table;
    Expected results:
        1. The "IP Setting" of fixed device is "Fixed" and cannot be modifyed, the "IP Address" is
           grey and cannot be edited.
        2. The "IP Setting" of dcp device is "Set by user" and can be modifyed, the "IP Address" can be edited.
        3. The "IP Setting" of catalog device is "Set by user" and can be modifyed, the "IP Address" can be edited.
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-12-13 create
    """

    io_device_01 = '192.168.2.151'
    io_device_02 = '192.168.2.152'
    device_name_02 = 'idevice152'
    io_device_03 = '192.168.2.153'
    device_name_03 = 'idevice153'

    gsd_files = ('GSDML-V2.34-#Siemens-PLC200smart_CPU SR30-20191213-140021.xml',
                 'GSDML-V2.34-#Siemens-PLC200smart_CPU SR30-20191213-140041.xml')

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice024, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Import two gsdml files, fixed and dcp;')
        self.logger.info('3. In PN wizard, config plc as controller and add the two devices;')
        # copy gsd file
        self.gsd_file_options.copy_gsd_file(self.gsd_files)
        # create a new project
        time_str = self.converter.convert_time_to_str()
        self.prj_file = 'new_%s.smart' % time_str
        self.PROJECT.project_new(self.prj_file)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice024, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. View the "IP Setting" and "IP Address" of the fixed device in device table;')
        # config a controller, add io device by gsd file
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_gsd', 'io_device_type': 'i-device', 'gsd_file': self.gsd_files[1],
                            'fixed_ip': False, 'device_ip': self.io_device_01}
        wizard_pn = self.PROJECT.find('wizard_pn')
        wizard_pn.config_controller(controller_params, io_device_params)
        wizard_data_01 = wizard_pn.config_data

        self.logger.info('2. View the "IP Setting" and "IP Address" of the dcp device in device table;')
        # config a controller, add io device by gsd file
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_gsd', 'io_device_type': 'i-device', 'gsd_file': self.gsd_files[0],
                            'fixed_ip': False, 'device_ip': self.io_device_02, 'device_name': self.device_name_02}
        wizard_pn = self.PROJECT.find('wizard_pn')
        wizard_pn.config_controller(controller_params, io_device_params)
        wizard_data_02 = wizard_pn.config_data

        self.logger.info('3. Add a catalog device, View the "IP Setting" and "IP Address" of the dcp device '
                         'in device table;')
        # config a controller, add io device by catalog
        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR40',
                            'fixed_ip': False,
                            'device_ip': self.io_device_03,
                            'station_name': self.device_name_03,
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        wizard_pn.config_controller(controller_params, io_device_params)
        wizard_data_03 = wizard_pn.config_data

        self.logger.info('Expected results:')
        self.logger.info('1. The "IP Setting" of fixed device is "Fixed" and cannot be modifyed, the "IP Address" '
                         'is grey and cannot be edited.')

        self.logger.info('2. The "IP Setting" of dcp device is "Set by user" and can be modifyed, the "IP Address" '
                         'can be edited.')

        self.logger.info('3. The "IP Setting" of catalog device is "Set by user" and can be modifyed, the "IP Address" '
                         'can be edited.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice024, self).cleanup()
        # clear gsd file
        self.gsd_file_options.gsd_file_reduction()
