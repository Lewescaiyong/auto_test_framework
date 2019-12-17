#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice036(CaseMW):
    """Modify device info
    No.: test_200smart_full_idevice_036
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Select plc role is "Controller" in PN wizard;
        3. Add a catalog device;
    Step actions:
        1. Modify "Device name" with valid name;
        2. Modify the IP Setting to "Fixed";
    Expected results:
        1. Modify successful;
        2. Modify successful;
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
        super(Test200SmartFullIdevice036, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Select plc role is "Controller" in PN wizard;')
        self.logger.info('3. Add a catalog device;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice036, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Modify "Device name" with valid name;')
        self.logger.info('2. Modify the IP Setting to "Fixed";')

        self.logger.info('Expected results:')
        self.logger.info('1. Modify successful;')
        self.logger.info('2. Modify successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice036, self).cleanup()
