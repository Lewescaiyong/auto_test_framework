#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice013(CaseMW):
    """Add and remove
    No.: test_200smart_full_idevice_013
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "I-Device" and click "Next";
    Step actions:
        1. Add 1~8 input transfer areas, remove 1~8 transfer areas;
        2. Add 1~8 output transfer areas, remove 1~8 transfer areas;
        3. Add 4 input and 4 output transfer areas, remove 1~8 transfer areas;
        4. Add 9th transfer areas;
    Expected results:
        1. Add successful, remove successful;
        2. Add successful, remove successful;
        3. Add successful, remove successful;
        4. Add failed, has reasonable prompt;
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
        super(Test200SmartFullIdevice013, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. In PN wizard, select plc role is "I-Device" and click "Next";')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice013, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add 1~8 input transfer areas, remove 1~8 transfer areas;')
        self.logger.info('2. Add 1~8 output transfer areas, remove 1~8 transfer areas;')
        self.logger.info('3. Add 4 input and 4 output transfer areas, remove 1~8 transfer areas;')
        self.logger.info('4. Add 9th transfer areas;')

        self.logger.info('Expected results:')
        self.logger.info('1. Add successful, remove successful;')
        self.logger.info('2. Add successful, remove successful;')
        self.logger.info('3. Add successful, remove successful;')
        self.logger.info('4. Add failed, has reasonable prompt;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice013, self).cleanup()
