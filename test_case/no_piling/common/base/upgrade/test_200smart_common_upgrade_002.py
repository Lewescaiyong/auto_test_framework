#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartCommonUpgrade002(CaseMW):
    """New file
    No.: test_200smart_common_upgrade_002
    Preconditions:
    Step actions:
        1. Upgrade MicroWin;
    Expected results:
        1. Upgrade successful;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-10-17 create
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
        super(CaseMW, self).prepare()

        self.logger.info('Preconditions:')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartCommonUpgrade002, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Upgrade MicroWin;')
        result = self.MicroWIN.upgrade(is_task_server=True)

        self.logger.info('Expected results:')
        self.logger.info('1. Upgrade successful;')
        if not result:
            raise CheckException('1. Upgrade failed: %s.' % result)

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
