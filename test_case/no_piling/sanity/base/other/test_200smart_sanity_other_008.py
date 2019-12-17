#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityOther008(CaseMW):
    """Event log
    No.: test_200smart_sanity_other_008
    Preconditions:
        1. Open Micro/WIN as administrator;  
        2. Set up connection with PLC;
        3. Create a new project with program;
    Step actions:
        1. Download all to the PLC;
        2. Make the PLC in run Mode, View the status of PLC and program;
        3. Make the PLC in stop Mode, view the event log in PLC Information;
    Expected results:
        1. Download successful;
        2. PLC in run mode, and the program run normally;
        3. The event log record correctly;
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
        super(Test200SmartSanityOther008, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN as administrator;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.logger.info('3. Create a new project with program;')
        self.PROJECT.project_open('ob_db_sdb_02.smart')

    def process(self):
        """execute the test     steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityOther008, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Download all to the PLC;')
        result1 = self.PROJECT.project_download()

        self.logger.info('2. Make the PLC in run Mode, View the status of PLC and program;')
        self.PLC['1'].set_plc_mode(1)
        result2 = self.PLC['1'].get_plc_mode()
        self.common.sleep(5)

        self.logger.info('3. Make the PLC in stop Mode, view the event log in PLC Information;')
        self.PLC['1'].set_plc_mode(0)
        plc_info = self.PLC['1'].plc_info
        run_status = self.PLC['1'].get_program_run_status()

        self.logger.info('Expected results:')
        self.logger.info('1. Download successful;')
        if result1['code'] != 0:
            raise CheckException('1. Download failed;')

        self.logger.info('2. PLC in run mode, and the program run normally;')
        if result2 != 1:
            raise CheckException('2. PLC is not in run mode;')
        if not run_status:
            raise CheckException('the program run not normally;')

        self.logger.info('3. The event log record correctly;')
        if plc_info['event_logs'][0]['type_code'] != 3 or plc_info['event_logs'][1]['type_code'] != 2:
            raise CheckException('3. The event log record error;')

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
        super(Test200SmartSanityOther008, self).cleanup()
