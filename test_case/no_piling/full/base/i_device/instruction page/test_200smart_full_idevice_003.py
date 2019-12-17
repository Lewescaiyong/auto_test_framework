#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice003(CaseMW):
    """FW version is V2.5
    No.: test_200smart_full_idevice_003
    Preconditions:
        1. Open Micro/WIN V2.5;  
        2. Connect to a plc with V2.5 FW;
    Step actions:
        1. In system block, select the CPU module is "ST60", version is V02.05.00, click "PROFINET" in wizard;
    Expected results:
        1. The "PROFINET" is not grey, in PN wizard,  "Controller" and "I-Device" under "PLC Role";
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
        super(Test200SmartFullIdevice003, self).prepare()

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
        super(Test200SmartFullIdevice003, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. In system block, select the CPU module is "ST60", version is V02.05.00, '
                         'click "PROFINET" in wizard;')
        system_block = self.PROJECT.find('system_block')
        system_block.set_module_info({'cpu': {'cpu_type': 'ST60', 'cpu_version': '02.05'}})

        # get is support
        wizard_pn = self.PROJECT.find('wizard_pn')
        i_device = wizard_pn.find('i_device')
        controller = wizard_pn.find('controller')
        pn_support = wizard_pn.is_support
        i_device_support = i_device.is_support
        controller_support = controller.is_support

        self.logger.info('Expected results:')
        self.logger.info('1. The "PROFINET" is not grey, in PN wizard,  "Controller" and "I-Device" under "PLC Role";')
        if not (pn_support and i_device_support and controller_support):
            self.logger.info('pn_support: %s, i_device_support: %s, controller_support: %s.' % (
                pn_support, i_device_support, controller_support))
            raise CheckException(
                '1. The "PROFINET" is grey or in PN wizard, not "Controller" and "I-Device" under "PLC Role";')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice003, self).cleanup()
