#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice026(CaseMW):
    """Screen resolution and size
    No.: test_200smart_full_idevice_026
    Preconditions:
        1. Screen resolution is the max, the magnification is 200%;
        2. Open Micro/WIN, config plc as controller&I-Device;
    Step actions:
        1. View the pn wizard pages;
        2. In controller page, add a catalog device, add the ip address;
    Expected results:
        1. The pages display normally;
        2. Add successful;
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
        super(Test200SmartFullIdevice026, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Screen resolution is the max, the magnification is 200%;')
        self.logger.info('2. Open Micro/WIN, config plc as controller&I-Device;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice026, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. View the pn wizard pages;')
        self.logger.info('2. In controller page, add a catalog device, add the ip address;')

        self.logger.info('Expected results:')
        self.logger.info('1. The pages display normally;')
        self.logger.info('2. Add successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice026, self).cleanup()
