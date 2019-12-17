#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice023(CaseMW):
    """Device name
    No.: test_200smart_full_idevice_023
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "Controller", click "Next";
        3. Two devices have been added;
    Step actions:
        1. Modify device name to 63 characters with lower case letters, digits, "-" and ".";
        2. Modify device name to 64 characters;
        3. Modify device name with capital letters;
        4. Modify device name with Chinese characters;
        5. Modify device name to "device192.168.0.2";
        6. Modify device name begin with port-123 or port-123-45678;
        7. Modify device name begin with  "-" or ".".
        8. Modify device name end with  "-" or ".".
    Expected results:
        1. Modify successful;
        2. Modify failed with reasonable prompt;
        3. Modify failed with reasonable prompt;
        4. Modify successful;
        5. Modify failed with reasonable prompt;
        6. Modify failed with reasonable prompt;
        7. Modify failed with reasonable prompt;
        8. Modify failed with reasonable prompt;
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
        super(Test200SmartFullIdevice023, self).prepare()

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
        super(Test200SmartFullIdevice023, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Modify device name to 63 characters with lower case letters, digits, "-" and ".";')
        self.logger.info('2. Modify device name to 64 characters;')
        self.logger.info('3. Modify device name with capital letters;')
        self.logger.info('4. Modify device name with Chinese characters;')
        self.logger.info('5. Modify device name to "device192.168.0.2";')
        self.logger.info('6. Modify device name begin with port-123 or port-123-45678;')
        self.logger.info('7. Modify device name begin with  "-" or ".".')
        self.logger.info('8. Modify device name end with  "-" or ".".')

        self.logger.info('Expected results:')
        self.logger.info('1. Modify successful;')
        self.logger.info('2. Modify failed with reasonable prompt;')
        self.logger.info('3. Modify failed with reasonable prompt;')
        self.logger.info('4. Modify successful;')
        self.logger.info('5. Modify failed with reasonable prompt;')
        self.logger.info('6. Modify failed with reasonable prompt;')
        self.logger.info('7. Modify failed with reasonable prompt;')
        self.logger.info('8. Modify failed with reasonable prompt;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice023, self).cleanup()
