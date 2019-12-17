#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice040(CaseMW):
    """Update time and data hold
    No.: test_200smart_full_idevice_040
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "Controller", add a catalog device in device table and go to next page;
    Step actions:
        1. Modify the Update Time;
        2. Modify the Data Hold/;
    Expected results:
        1. User can select any value in the drop-down list;
        2. User can select any value in the drop-down list;
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
        super(Test200SmartFullIdevice040, self).prepare()

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
        super(Test200SmartFullIdevice040, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Modify the Update Time;')
        self.logger.info('2. Modify the Data Hold/;')

        self.logger.info('Expected results:')
        self.logger.info('1. User can select any value in the drop-down list;')
        self.logger.info('2. User can select any value in the drop-down list;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice040, self).cleanup()
