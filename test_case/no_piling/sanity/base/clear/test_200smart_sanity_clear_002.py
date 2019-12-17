#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityClear002(CaseMW):
    """Clear DB
    No.: test_200smart_sanity_clear_002
    Preconditions:
        1. Open Micro/WINr;  
        2. Set up connection with PLC;
        3. Download a project which has OB,DB,SDB;
    Step actions:
        1. Clear data block;
        2. Compare;
    Expected results:
        1. Clear successful;
        2. The DB is different;
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
        super(Test200SmartSanityClear002, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WINr;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.logger.info('3. Download a project which has OB,DB,SDB;')
        self.MicroWIN.test_prepare('ob_db_sdb_02.smart', False)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityClear002, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Clear data block;')
        result1 = self.PLC['1'].plc_clear('db')

        self.logger.info('2. Compare;')
        result2 = self.MicroWIN.compare_with_plc()

        self.logger.info('Expected results:')
        self.logger.info('1. Clear successful;')
        if result1['code'] != 0:
            raise CheckException('1. Clear DB failed;')

        self.logger.info('2. The DB is different;')
        if not ((not result2['db']) and result2['ob'] and result2['sdb']):
            self.logger.info('Compare result: %s' % result2)
            raise CheckException('Compare failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityClear002, self).cleanup()
