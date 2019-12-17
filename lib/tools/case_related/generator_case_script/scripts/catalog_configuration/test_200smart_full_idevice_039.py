#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice039(CaseMW):
    """Size of submodule
    No.: test_200smart_full_idevice_039
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "Controller", add a catalog device in device table and go to next page;
    Step actions:
        1. Add one input submodule, modify the size to 129;
        2. Modify size to 0;
        3. Modify size to 128;
        4. Add another input submodule;
    Expected results:
        1. Modify failed, prompt user out of range, and the size is automatically restored to 1;
        2. The address is automatically changed to 1;
        3. Modify successful;
        4. Add failed, prompt user can not exceed 128 bytes.
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
        super(Test200SmartFullIdevice039, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Plc role is "Controller", add a catalog device in device table and go to next page;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice039, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add one input submodule, modify the size to 129;')
        self.logger.info('2. Modify size to 0;')
        self.logger.info('3. Modify size to 128;')
        self.logger.info('4. Add another input submodule;')

        self.logger.info('Expected results:')
        self.logger.info('1. Modify failed, prompt user out of range, and the size is automatically restored to 1;')
        self.logger.info('2. The address is automatically changed to 1;')
        self.logger.info('3. Modify successful;')
        self.logger.info('4. Add failed, prompt user can not exceed 128 bytes.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice039, self).cleanup()
