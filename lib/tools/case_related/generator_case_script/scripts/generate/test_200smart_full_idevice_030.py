#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice030(CaseMW):
    """I-Device-abnormal
    No.: test_200smart_full_idevice_030
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Select plc role is "I-Device" in PN wizard;
    Step actions:
        1. Startup time>60000ms;
        2. Fix ip, ip is empty/invalid;
        3. Fix ip, station name is empty/invalid;
        4. Fix ip, subnet mask/gateway  is invalid;
        5. No transfer area;
        6. Transfer area name empty/invalid/unique;
        7. Transfer area type invalid;
        8. Transfer area Address smaller than 1152/larger than 1279;
        9. Transfer area length larger than 128 bytes/invalid;
    Expected results:
        1. Generate failed and has reasonable prompt;
        2. Generate failed and has reasonable prompt;
        3. Generate failed and has reasonable prompt;
        4. Generate failed and has reasonable prompt;
        5. Generate failed and has reasonable prompt;
        6. Generate failed and has reasonable prompt;
        7. Generate failed and has reasonable prompt;
        8. Generate failed and has reasonable prompt;
        9. Generate failed and has reasonable prompt;
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
        super(Test200SmartFullIdevice030, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Select plc role is "I-Device" in PN wizard;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice030, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Startup time>60000ms;')
        self.logger.info('2. Fix ip, ip is empty/invalid;')
        self.logger.info('3. Fix ip, station name is empty/invalid;')
        self.logger.info('4. Fix ip, subnet mask/gateway  is invalid;')
        self.logger.info('5. No transfer area;')
        self.logger.info('6. Transfer area name empty/invalid/unique;')
        self.logger.info('7. Transfer area type invalid;')
        self.logger.info('8. Transfer area Address smaller than 1152/larger than 1279;')
        self.logger.info('9. Transfer area length larger than 128 bytes/invalid;')

        self.logger.info('Expected results:')
        self.logger.info('1. Generate failed and has reasonable prompt;')
        self.logger.info('2. Generate failed and has reasonable prompt;')
        self.logger.info('3. Generate failed and has reasonable prompt;')
        self.logger.info('4. Generate failed and has reasonable prompt;')
        self.logger.info('5. Generate failed and has reasonable prompt;')
        self.logger.info('6. Generate failed and has reasonable prompt;')
        self.logger.info('7. Generate failed and has reasonable prompt;')
        self.logger.info('8. Generate failed and has reasonable prompt;')
        self.logger.info('9. Generate failed and has reasonable prompt;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice030, self).cleanup()
