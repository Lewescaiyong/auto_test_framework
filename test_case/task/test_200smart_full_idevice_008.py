#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice008(CaseMW):
    """I-Device
    No.: test_200smart_full_idevice_008
    Preconditions:
        1. Open Micro/WIN V2.5;  
        2. Connect to a plc with V2.5 FW;
    Step actions:
        1. Open PN wizard, select plc role as "I-Device";
    Expected results:
        1. "Paraneter assignment..." is not grey and can be checked, "Fixed IP address and name" and  "Obtain IP
        address by other services" displayed under "Ethernet Port", you can select any but only one; an idevice page
        under PROFINET network;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-11-18 create
    """

    prj_file_01 = ''
    prj_file_02 = ''
    i_device_pn = None
    controller_pn = None

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice008, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;  ')
        self.logger.info('2. Connect to a plc with V2.5 FW;')

        self.PLC['2'].create_session()
        time_str = self.converter.convert_time_to_str()
        self.prj_file_01 = 'new_%s.smart' % time_str
        self.PROJECT.project_new(self.prj_file_01)
        self.i_device_pn = self.PROJECT.find('wizard_pn')

        params = {'role': 'i-device', 'areas_info': [{'io_type': 'input', 'address': 1152},
                                                     {'io_type': 'output', 'address': 1152}]}
        self.i_device_pn.config_i_device(params)
        self.PROJECT.project_save_as(self.prj_file_01)
        self.PROJECT.project_add_instruction(pou_type='pou_main', network_id=0, row_id=0, col_id=0,
                                             instruction_type='normally_open', instruction_values=('Always_On',))
        self.PROJECT.project_add_instruction(pou_type='pou_main', network_id=0, row_id=0, col_id=1,
                                             instruction_type='move_byte', instruction_values=('IB1152', 'QB0'))
        self.PROJECT.project_save()
        self.PROJECT.project_download()
        self.PLC['2'].set_plc_mode(1)
        self.MicroWIN.test_prepare(is_download=False)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice008, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Open PN wizard, select plc role as "I-Device";')

        self.reset_test_resource()
        self.PLC['1'].create_session()
        time_str = self.converter.convert_time_to_str()
        self.prj_file_02 = 'new_%s.smart' % time_str
        self.PROJECT.project_new(self.prj_file_02)
        self.controller_pn = self.PROJECT.find('wizard_pn')

        controller_params = {'role': 'controller'}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': self.i_device_pn.params['cpu_type'],
                            'fixed_ip': self.i_device_pn.params['fixed_ip'],
                            'device_ip': self.i_device_pn.params['ip'],
                            'station_name': self.i_device_pn.params['station_name'],
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        self.controller_pn.config_controller(controller_params, io_device_params)
        self.PROJECT.project_save_as(self.prj_file_02)
        # system_block = self.PROJECT.find('system_block')
        # system_block.set_module_info({'cpu': {'cpu_type': ''}})
        # system_block.set_communication({'fixed_ip': True, 'station_name': self.controller_pn.params['station_name']})
        self.PROJECT.project_add_instruction(pou_type='pou_main', network_id=0, row_id=0, col_id=0,
                                             instruction_type='normally_open', instruction_values=('Always_On',))
        self.PROJECT.project_add_instruction(pou_type='pou_main', network_id=0, row_id=0, col_id=1,
                                             instruction_type='move_byte', instruction_values=(1, 'QB128'))
        self.PROJECT.project_save()
        self.PROJECT.project_download()
        self.PLC['1'].set_plc_mode(1)

        self.logger.info('Expected results:')
        self.logger.info('1. "Paraneter assignment..." is not grey and can be checked, "Fixed IP address and name" '
                         'and  "Obtain IP address by other services" displayed under "Ethernet Port", you can select'
                         ' any but only one; an idevice page under PROFINET network;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice008, self).cleanup()

        self.file_options.remove_file_dir(self.prj_file_01, is_project=True)
        self.file_options.remove_file_dir(self.prj_file_02, is_project=True)
        self.PLC['2'].set_plc_mode(0)
        self.PLC['1'].set_plc_mode(0)
