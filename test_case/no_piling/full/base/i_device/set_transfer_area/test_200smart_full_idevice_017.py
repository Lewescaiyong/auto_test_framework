#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice017(CaseMW):
    """Address
    No.: test_200smart_full_idevice_017
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "I-Device", click "Next" and add one transfer area;
    Step actions:
        1. Modify the address is 1152 for input and output;
        2. Modify the address is 1151 for input and output;
        3. Modify the address is 1279 for input and output;
        4. Modify the address is 1280 for input and output;
        5. Modify the address is VB1152  for input and output;
    Expected results:
        1. Modify successful;
        2. Modify failed, the address has red under line, When the mouse is over the address, there are reasonable prompts;
        3. Modify successful;
        4. Modify failed, the address has red under line, When the mouse is over the address, there are reasonable prompts;
        5. Modify failed, the address will be  restored to I/Q automatically;
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
        super(Test200SmartFullIdevice017, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. In PN wizard, select plc role is "I-Device", click "Next" and add one transfer area;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice017, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Modify the address is 1152 for input and output;')
        self.logger.info('2. Modify the address is 1151 for input and output;')
        self.logger.info('3. Modify the address is 1279 for input and output;')
        self.logger.info('4. Modify the address is 1280 for input and output;')
        self.logger.info('5. Modify the address is VB1152  for input and output;')

        self.logger.info('Expected results:')
        self.logger.info('1. Modify successful;')
        self.logger.info('2. Modify failed, the address has red under line, When the mouse is over the address, there are reasonable prompts;')
        self.logger.info('3. Modify successful;')
        self.logger.info('4. Modify failed, the address has red under line, When the mouse is over the address, there are reasonable prompts;')
        self.logger.info('5. Modify failed, the address will be  restored to I/Q automatically;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice017, self).cleanup()
