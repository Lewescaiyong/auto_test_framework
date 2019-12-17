#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice035(CaseMW):
    """Add catalog device
    No.: test_200smart_full_idevice_035
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Select plc role is "Controller" in PN wizard;
    Step actions:
        1. Add a catalog device by Add button;
        2. Add a catalog device by draging from tree;
        3. Add 8 catalog devices;
        4. Delete all devices, add 8 all types of catalog devices;
        5. Add 9th catalog devices;
        6. Delete a catalog device and add an ET200-SP device;
    Expected results:
        1. Add suucessful;
        2. Add suucessful;
        3. Add suucessful;
        4. Delete and add successful;
        5. Add failed, has resonable prompt message;
        6. Delete and add successful;
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
        super(Test200SmartFullIdevice035, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Select plc role is "Controller" in PN wizard;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice035, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add a catalog device by Add button;')
        self.logger.info('2. Add a catalog device by draging from tree;')
        self.logger.info('3. Add 8 catalog devices;')
        self.logger.info('4. Delete all devices, add 8 all types of catalog devices;')
        self.logger.info('5. Add 9th catalog devices;')
        self.logger.info('6. Delete a catalog device and add an ET200-SP device;')

        self.logger.info('Expected results:')
        self.logger.info('1. Add suucessful;')
        self.logger.info('2. Add suucessful;')
        self.logger.info('3. Add suucessful;')
        self.logger.info('4. Delete and add successful;')
        self.logger.info('5. Add failed, has resonable prompt message;')
        self.logger.info('6. Delete and add successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice035, self).cleanup()
