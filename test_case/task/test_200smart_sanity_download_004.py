#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityDownload004(CaseMW):
    """Download All
    No.: test_200smart_sanity_download_004
    Preconditions:
        1. Open Micro/WINr;  
        2. Set up connection with PLC;
        3. Create a project which has OB,DB,SDB;
    Step actions:
        1. Download All to PCL;
    Expected results:
        4. Download All successful;
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
        super(Test200SmartSanityDownload004, self).prepare()

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
        super(Test200SmartSanityDownload004, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Download All to PCL;')
        self.PROJECT.project_download()
        result = self.MicroWIN.compare_with_plc()

        self.logger.info('Expected results:')
        self.logger.info('4. Download All successful;')
        if not (result['sdb'] and result['ob'] and result['db']):
            self.logger.info('Download result: %s' % result)
            raise CheckException('1. Download All failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityDownload004, self).cleanup()
