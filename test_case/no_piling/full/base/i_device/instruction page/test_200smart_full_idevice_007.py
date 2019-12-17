#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice007(CaseMW):
    """Controller
    No.: test_200smart_full_idevice_007
    Preconditions:
        1. Open Micro/WIN V2.5;  
        2. Connect to a plc with V2.5 FW;
    Step actions:
        1. Open PN wizard, select plc role as "Control";
    Expected results:
        1. "Paraneter assignment..." is grey and unchecked, Only "Fixed IP address and name" checked and
            displayed  under "Ethernet Port"; a controller page under PROFINET network;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-11-18 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice007, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;  ')
        self.logger.info('2. Connect to a plc with V2.5 FW;')
        time_str = self.converter.convert_time_to_str()
        self.prj_file = 'new_%s.smart' % time_str
        self.PROJECT.project_new('self.prj_file')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice007, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Open PN wizard, select plc role as "Control";')
        wizard_pn = self.PROJECT.find('wizard_pn')
        controller_params = {'role': 'controller', 'fixed_ip': False}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': 'idevice151',
                            'areas_info': [{'io_type': 'output', 'address': 128, 'sub_slot_number': 1000},
                                           {'io_type': 'input', 'address': 128, 'sub_slot_number': 1001}]}
        result = wizard_pn.config_controller(controller_params, io_device_params)

        self.logger.info('Expected results:')
        self.logger.info('1. "Paraneter assignment..." is grey and unchecked, Only "Fixed IP address and name" '
                         'checked and displayed  under "Ethernet Port"; a controller page under PROFINET network;')
        if result['result']:
            raise CheckException('Not only "Fixed IP";')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice007, self).cleanup()
