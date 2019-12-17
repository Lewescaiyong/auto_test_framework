#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice019(CaseMW):
    """Comment
    No.: test_200smart_full_idevice_019
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "I-Device", click "Next" and add one transfer area;
    Step actions:
        1. Add comment with 256 characters;
        2. Add comment more than 256 characters;
        3. Add comment with Chinese characters;
    Expected results:
        1. Add successful;
        2. Add successful, the comment automatically retains the first 256 characters;
        3. Add successful;
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
        super(Test200SmartFullIdevice019, self).prepare()

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
        super(Test200SmartFullIdevice019, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add comment with 256 characters;')
        self.logger.info('2. Add comment more than 256 characters;')
        self.logger.info('3. Add comment with Chinese characters;')

        self.logger.info('Expected results:')
        self.logger.info('1. Add successful;')
        self.logger.info('2. Add successful, the comment automatically retains the first 256 characters;')
        self.logger.info('3. Add successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice019, self).cleanup()
