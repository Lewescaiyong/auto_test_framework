#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice022(CaseMW):
    """Delete device
    No.: test_200smart_full_idevice_022
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "Controller", click "Next";
        3. Two devices have been added;
    Step actions:
        1. Delete device by "Delete" button;
        2. Delete device by Tab key;
    Expected results:
        1. Delete successful, display correctly in network topology;
        2. Delete successful, display correctly in network topology;
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
        super(Test200SmartFullIdevice022, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. In PN wizard, select plc role is "Controller", click "Next";')
        self.logger.info('3. Two devices have been added;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice022, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Delete device by "Delete" button;')
        self.logger.info('2. Delete device by Tab key;')

        self.logger.info('Expected results:')
        self.logger.info('1. Delete successful, display correctly in network topology;')
        self.logger.info('2. Delete successful, display correctly in network topology;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice022, self).cleanup()
