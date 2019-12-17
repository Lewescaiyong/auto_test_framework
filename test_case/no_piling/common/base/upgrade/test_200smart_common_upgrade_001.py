#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartCommonUpgrade001(CaseMW):
    """New file
    No.: test_200smart_common_upgrade_001
    Preconditions:
        1. Open Micro/WIN;
    Step actions:
        1. Upgrade Firmware;
    Expected results:
        1. Upgrade successful;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-09-24 create
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
        super(Test200SmartCommonUpgrade001, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartCommonUpgrade001, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Upgrade Firmware;')
        update_result = dict()
        for k, v in self.PLC.items():
            update_result[k] = v.upgrade()

        self.logger.info('Expected results:')
        self.logger.info('1. Upgrade successful;')
        for k, v in update_result.items():
            if not v:
                raise CheckException('1. Upgrade failed: %s.' % update_result)

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartCommonUpgrade001, self).cleanup()
