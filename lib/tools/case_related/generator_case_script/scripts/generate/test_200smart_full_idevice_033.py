#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice033(CaseMW):
    """Re-generate
    No.: test_200smart_full_idevice_033
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Select plc role is "I-Device" in PN wizard, add transfer area and generate;
    Step actions:
        1. Modify the CPU module is system block, click "OK" button;
        2. Open PN wIzard, check the CPU type in Designation, generate;
    Expected results:
        1. There is a prompt message for user to regenerate in PN Wizard;
        2. The CPU type in Designation is automatically changed, genearte successful;
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
        super(Test200SmartFullIdevice033, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Select plc role is "I-Device" in PN wizard, add transfer area and generate;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice033, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Modify the CPU module is system block, click "OK" button;')
        self.logger.info('2. Open PN wIzard, check the CPU type in Designation, generate;')

        self.logger.info('Expected results:')
        self.logger.info('1. There is a prompt message for user to regenerate in PN Wizard;')
        self.logger.info('2. The CPU type in Designation is automatically changed, genearte successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice033, self).cleanup()
