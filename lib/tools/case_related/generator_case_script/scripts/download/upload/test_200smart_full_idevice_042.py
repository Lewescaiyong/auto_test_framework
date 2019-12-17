#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice042(CaseMW):
    """Empty project
    No.: test_200smart_full_idevice_042
    Preconditions:
        1. Open Micro/WIN V2.5;
    Step actions:
        1. Download empty project to CPU;
        2. Upload all from CPU;
    Expected results:
        1. Download successful;
        2. Upload successful;
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
        super(Test200SmartFullIdevice042, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice042, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Download empty project to CPU;')
        self.logger.info('2. Upload all from CPU;')

        self.logger.info('Expected results:')
        self.logger.info('1. Download successful;')
        self.logger.info('2. Upload successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice042, self).cleanup()
