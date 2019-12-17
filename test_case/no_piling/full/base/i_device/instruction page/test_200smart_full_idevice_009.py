#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice009(CaseMW):
    """Controller&I-Device
    No.: test_200smart_full_idevice_009
    Preconditions:
        1. Open Micro/WIN V2.5;  
        2. Connect to a plc with V2.5 FW;
    Step actions:
        1. Open PN wizard, select plc role as "Controller&I-Device";
    Expected results:
        1. "Paraneter assignment..." is grey and unchecked, Only "Fixed IP address and name" checked and displayed
        under "Ethernet Port"; a controller page and an idevice pageunder PROFINET network;
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
        super(Test200SmartFullIdevice009, self).prepare()

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
        super(Test200SmartFullIdevice009, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Open PN wizard, select plc role as "Controller&I-Device";')
        controller_params = {'role': 'controller', 'fixed_ip': False}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': 'SR30',
                            'fixed_ip': True,
                            'device_ip': '192.168.2.151',
                            'station_name': 'idevice151',
                            'areas_info': [{'io_type': 'output', 'address': 128, 'sub_slot_number': 1000},
                                           {'io_type': 'input', 'address': 128, 'sub_slot_number': 1001}]}
        i_device_params = {'areas_info': [{'io_type': 'input', 'address': 1152},
                                          {'io_type': 'output', 'address': 1152}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        result = wizard_pn.config_controller_i_device(controller_params, io_device_params, i_device_params)
        config_data = wizard_pn.config_data

        self.logger.info('Expected results:')
        self.logger.info('1. "Paraneter assignment..." is grey and unchecked, Only "Fixed IP address and name" '
                         'checked and displayed under "Ethernet Port"; a controller page and an idevice pageunder '
                         'PROFINET network;')
        if result['result'] or config_data['i-device']['parameter_assignment']:
            raise CheckException('Not only "Fixed IP" or "Parameter assignment..." is not grey;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice009, self).cleanup()

        self.file_options.remove_file_dir(self.prj_file, is_project=True)
