#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityOther005(CaseMW):
    """Compare
    No.: test_200smart_sanity_other_005
    Preconditions:
        1. Open Micro/WIN;  
        2. Set up connection with PLC;
        3. Create a file;
    Step actions:
        1. add OB, config some sdb, config DB;
        2. Compare project to cpu;
        3. Download all, then compare project to cpu;
    Expected results:
        1. compare successful, the result is different, and information is correct;
        2.  compare successful, and the result is passed.
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
        super(Test200SmartSanityOther005, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.logger.info('3. Create a file;')
        self.MicroWIN.test_prepare('ob_db_sdb_01.smart')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityOther005, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. add OB, config some sdb, config DB;')
        self.PROJECT.project_open('ob_db_sdb_02.smart')

        self.logger.info('2. Compare project to cpu;')
        result1 = self.MicroWIN.compare_with_plc()

        self.logger.info('3. Download all, then compare project to cpu;')
        self.PROJECT.project_download()
        result2 = self.MicroWIN.compare_with_plc()

        self.logger.info('Expected results:')
        self.logger.info('1. compare successful, the result is different, and information is correct;')
        if result1['sdb'] or result1['ob'] or result1['db']:
            self.logger.info('1. Compare result: %s' % result1)
            raise CheckException('1. Compare failed;')

        self.logger.info('2.  compare successful, and the result is passed.')
        if not (result2['sdb'] and result2['ob'] and result2['db']):
            self.logger.info('2. Compare result: %s' % result2)
            raise CheckException('2. Compare failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityOther005, self).cleanup()
