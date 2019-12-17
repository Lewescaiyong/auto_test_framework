#!/usr/bin/env python

import time

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityUpload005(CaseMW):
    """Upload datalogs
    No.: test_200smart_sanity_upload_005
    Preconditions:
        1. Open Micro/WINr;  
        2. Set up connection with PLC;
    Step actions:
        1.  Generate subroutine with data logs wizard, the max number of records is 100;
        2. Create a new project with program that write data logs with the frequency of 1 times  1s;
        3. Download all to the PLC;
        4.Make the PLC in run Mode lasts 60s ,View the status of PLC and program;
        5.Upload the Data Logs;
    Expected results:
        1. Generate successful;
        2.Create successful;
        3.Download successful;
        4. PLC in run mode, and the program run normally;
        5. Upload Successful, the file of data logs record correctly;
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
        super(Test200SmartSanityUpload005, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WINr;  ')
        self.logger.info('2. Set up connection with PLC;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityUpload005, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1.  Generate subroutine with data logs wizard, the max number of records is 100;')
        self.logger.info('2. Create a new project with program that write data logs with the frequency of 1 times  1s;')
        self.PROJECT.project_open('data_log100ms100inc.smart')

        self.logger.info('3. Download all to the PLC;')
        result1 = self.PROJECT.project_download()

        self.logger.info('4.Make the PLC in run Mode lasts 60s ,View the status of PLC and program;')
        self.PLC['1'].set_plc_mode(1)
        time.sleep(60)
        plc_mode = self.PLC['1'].get_plc_mode()

        self.logger.info('5.Upload the Data Logs;')
        self.PROJECT.project_upload_data_log()
        result2 = self.parser.parse_data_log()
        self.data_log_file = result2['data_log_file']

        self.logger.info('Expected results:')
        self.logger.info('1. Generate successful;')
        self.logger.info('2.Create successful;')
        self.logger.info('3.Download successful;')
        if result1['code'] != 0:
            raise CheckException('3.Download failed;')

        self.logger.info('4. PLC in run mode, and the program run normally;')
        if plc_mode != 1:
            raise CheckException('4. PLC not in run mode')

        self.logger.info('5. Upload Successful, the file of data logs record correctly;')
        if not result2['check_result']:
            self.logger.info('Data log file check result: %s' % result2)
            raise CheckException('the file of data logs record incorrectly;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """

        self.PLC['1'].set_plc_mode(0)
        super(Test200SmartSanityUpload005, self).cleanup()
        self.file_options.remove_file_dir(self.data_log_file, is_data_log=True)
