#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice037(CaseMW):
    """Add/Delete submodule
    No.: test_200smart_full_idevice_037
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "Controller", add a catalog device in device table and go to next page;
    Step actions:
        1. Add 1~8 input submodule;
        2. Delete all submodule, add 1~8 output submodule;
        3. Delete all submodule, add 4 input and 4 output submodules;
        4. Add 9th submodule;
    Expected results:
        1. Add successful;
        2. Add successful;
        3. Add successful;
        4. Add failed, has resonable prompt message;
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
        super(Test200SmartFullIdevice037, self).prepare()

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
        super(Test200SmartFullIdevice037, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add 1~8 input submodule;')
        self.logger.info('2. Delete all submodule, add 1~8 output submodule;')
        self.logger.info('3. Delete all submodule, add 4 input and 4 output submodules;')
        self.logger.info('4. Add 9th submodule;')

        self.logger.info('Expected results:')
        self.logger.info('1. Add successful;')
        self.logger.info('2. Add successful;')
        self.logger.info('3. Add successful;')
        self.logger.info('4. Add failed, has resonable prompt message;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice037, self).cleanup()
