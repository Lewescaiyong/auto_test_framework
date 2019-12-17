#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice018(CaseMW):
    """Length
    No.: test_200smart_full_idevice_018
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "I-Device", click "Next" and add one transfer area, address is 1152;
    Step actions:
        1. Modify the length less than 128 bytes for input and output;
        2. Modify the length is 128bytes for input and output;
        3. Modify the length over 128 bytes for input and output;
    Expected results:
        1. Modify successful;
        2. Modify successful;
        3. Modify failed, the address has red under line, When the mouse is over the address,
           there are reasonable prompts;
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
        super(Test200SmartFullIdevice018, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. In PN wizard, select plc role is "I-Device", click "Next" '
                         'and add one transfer area, address is 1152;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice018, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Modify the length less than 128 bytes for input and output;')
        self.logger.info('2. Modify the length is 128bytes for input and output;')
        self.logger.info('3. Modify the length over 128 bytes for input and output;')

        self.logger.info('Expected results:')
        self.logger.info('1. Modify successful;')
        self.logger.info('2. Modify successful;')
        self.logger.info('3. Modify failed, the address has red under line, When the mouse is over the address, '
                         'there are reasonable prompts;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice018, self).cleanup()
