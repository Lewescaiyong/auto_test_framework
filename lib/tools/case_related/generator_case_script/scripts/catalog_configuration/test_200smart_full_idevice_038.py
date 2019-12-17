#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice038(CaseMW):
    """Start Address of submodule
    No.: test_200smart_full_idevice_038
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "Controller", add a catalog device in device table and go to next page;
    Step actions:
        1. Add one input submodule, modify the start address to 127;
        2. Modify start address to 256/0;
        3. Size is 10, then add another input submodule, Modify start address to 130;
    Expected results:
        1. Modify failed, prompt user out of range, and the address is automatically restored to 128;
        2. Modify failed, prompt user out of range, and the address is automatically changed to 128;
        3. Modify failed, prompt user that the address has been used, and the address is automatically restored to 138;
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
        super(Test200SmartFullIdevice038, self).prepare()

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
        super(Test200SmartFullIdevice038, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add one input submodule, modify the start address to 127;')
        self.logger.info('2. Modify start address to 256/0;')
        self.logger.info('3. Size is 10, then add another input submodule, Modify start address to 130;')

        self.logger.info('Expected results:')
        self.logger.info('1. Modify failed, prompt user out of range, and the address is automatically restored to 128;')
        self.logger.info('2. Modify failed, prompt user out of range, and the address is automatically changed to 128;')
        self.logger.info('3. Modify failed, prompt user that the address has been used, and the address is automatically restored to 138;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice038, self).cleanup()
