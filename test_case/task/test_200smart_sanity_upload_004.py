#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityUpload004(CaseMW):
    """Upload All
    No.: test_200smart_sanity_upload_004
    Preconditions:
        1. Open Micro/WINr;  
        2. Set up connection with PLC;
        3. Download a project which has OB,DB,SDB;
    Step actions:
        1. Upload All to a new project;
        2. Compare;
    Expected results:
        1. Upload All successful;
        2. All are same;
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
        super(Test200SmartSanityUpload004, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WINr;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.logger.info('3. Download a project which has OB,DB,SDB;')
        self.MicroWIN.test_prepare('ob_db_sdb_01.smart')
        self.PROJECT.project_open('ob_db_sdb_02.smart')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityUpload004, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Upload All to a new project;')
        result1 = self.PROJECT.project_upload()

        self.logger.info('2. Compare;')
        result2 = self.MicroWIN.compare_with_plc()

        self.logger.info('Expected results:')
        self.logger.info('1. Upload All successful;')
        if result1['code'] != 0:
            raise CheckException('1. Upload ALL failed;')

        self.logger.info('2. All are same;')
        if not (result2['sdb'] and result2['ob'] and result2['db']):
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
        super(Test200SmartSanityUpload004, self).cleanup()
