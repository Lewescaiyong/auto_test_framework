#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice001(CaseMW):
    """FW version less than V2.4
    No.: test_200smart_full_idevice_001
    Preconditions:
        1. Open Micro/WIN V2.5;
    Step actions:
        1. In system block, select the CPU module is "CR60",  View the "PROFINET" in wizard;
    Expected results:
        1. The "PROFINET" is grey and cannot be clicked;
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
        super(Test200SmartFullIdevice001, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
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
        super(Test200SmartFullIdevice001, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. In system block, select the CPU module is "CR60",  View the "PROFINET" in wizard;')
        system_block = self.PROJECT.find('system_block')
        system_block.set_module_info({'cpu': {'cpu_type': 'CR60', 'cpu_version': '02.02'}})

        # get is support
        wizard_pn = self.PROJECT.find('wizard_pn')
        is_support = wizard_pn.is_support

        self.logger.info('Expected results:')
        self.logger.info('1. The "PROFINET" is grey and cannot be clicked;')
        if is_support:
            raise CheckException('1. The "PROFINET" is not grey;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice001, self).cleanup()
