#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityProject005(CaseMW):
    """Close a file
    No.: test_200smart_sanity_project_005
    Preconditions:
        1. Open Micro/WIN;
        2. Open an existed file;
    Step actions:
        1.  Close the file;
    Expected results:
        1. Close successful;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-09-21 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject005, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. Open an existed file;')
        self.PROJECT.project_open('counter_ctu.smart')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject005, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1.  Close the file;')
        result1 = self.PROJECT.project_close()

        self.logger.info('Expected results:')
        self.logger.info('1. Close successful;')
        if result1['code'] != 0:
            raise CheckException('1. Close failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject005, self).cleanup()
