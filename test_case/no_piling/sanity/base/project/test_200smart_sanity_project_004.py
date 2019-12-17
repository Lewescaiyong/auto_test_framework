#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityProject004(CaseMW):
    """Open a existed file
    No.: test_200smart_sanity_project_004
    Preconditions:
        1. Open Micro/WIN;  
        2. There is an existed file;
    Step actions:
        1. Open an existed file;
    Expected results:
        1. Open successful;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-09-20 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityProject004, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. There is an existed file;')
        self.prj_file = 'counter_ctu.smart'

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityProject004, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Open an existed file;')
        result1 = self.PROJECT.project_open(self.prj_file)

        self.logger.info('Expected results:')
        self.logger.info('1. Open successful;')
        if result1['code'] != 0:
            raise CheckException('1. Open failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityProject004, self).cleanup()
