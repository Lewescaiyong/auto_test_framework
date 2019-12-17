#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityDownload003(CaseMW):
    """Download SDB
    No.: test_200smart_sanity_download_003
    Preconditions:
        1. Open Micro/WINr;  
        2. Set up connection with PLC;
        3. Create a project which has OB,DB,SDB;
    Step actions:
        1. Download SDB to PCL;
    Expected results:
        3. Download SDB successful;
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
        super(Test200SmartSanityDownload003, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WINr;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.logger.info('3. Create a project which has OB,DB,SDB;')
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
        super(Test200SmartSanityDownload003, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Download SDB to PCL;')
        self.PROJECT.project_download('sdb')
        result = self.MicroWIN.compare_with_plc()

        self.logger.info('Expected results:')
        self.logger.info('3. Download SDB successful;')
        if not (result['sdb'] and (not result['ob']) and (not result['db'])):
            self.logger.info('Download result: %s' % result)
            raise CheckException('1. Download SDB failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityDownload003, self).cleanup()
