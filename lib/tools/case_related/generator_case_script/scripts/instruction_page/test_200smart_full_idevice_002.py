#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice002(CaseMW):
    """FW version is V2.4
    No.: test_200smart_full_idevice_002
    Preconditions:
        1. Open Micro/WIN V2.5;
    Step actions:
        1. In system block, select the CPU module is "ST60", version is V02.04.00, click "PROFINET" in wizard;
    Expected results:
        1. The "PROFINET" is not grey, in PN wizard, only "Controller" under "PLC Role";
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
        super(Test200SmartFullIdevice002, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice002, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. In system block, select the CPU module is "ST60", version is V02.04.00, click "PROFINET" in wizard;')

        self.logger.info('Expected results:')
        self.logger.info('1. The "PROFINET" is not grey, in PN wizard, only "Controller" under "PLC Role";')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice002, self).cleanup()
