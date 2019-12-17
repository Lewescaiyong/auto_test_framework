#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityOther006(CaseMW):
    """Warm start
    No.: test_200smart_sanity_other_006
    Preconditions:
        1. Open Micro/WIN as administrator;  
        2. Set up connection with PLC;
        3. Create a new project with program  and Download all to the PLC;
        4. Make the PLC in run Mode;
    Step actions:
        1. Warm start the CPU;
        2. Modify the cpu startup mode to run in system block and download all to the PLC, then Warm start the CPU;
    Expected results:
        1. Warm start successful;
        2. Warm start successful, the PLC run successful;
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
        super(Test200SmartSanityOther006, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN as administrator;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.logger.info('3. Create a new project with program  and Download all to the PLC;')
        self.MicroWIN.test_prepare('ob_db_sdb_02.smart', False)

        self.logger.info('4. Make the PLC in run Mode;')
        self.PLC['1'].set_plc_mode(1)
        self.common.sleep(3)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityOther006, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Warm start the CPU;')
        result1 = self.PLC['1'].plc_power_cycle()
        mode_1 = self.PLC['1'].get_plc_mode()

        self.logger.info('2. Modify the cpu startup mode to run in system block and download all to the PLC, '
                         'then Warm start the CPU;')
        self.MicroWIN.test_prepare('ob_db_sdb_03.smart', False)
        result2 = self.PLC['1'].plc_power_cycle()
        mode_2 = self.PLC['1'].get_plc_mode()

        self.logger.info('Expected results:')
        self.logger.info('1. Warm start successful;')
        if result1['code'] != 0 or mode_1 != 0:
            raise CheckException('1. Warm start failed;')

        self.logger.info('2. Warm start successful, the PLC run successful;')
        if result2['code'] != 0 or mode_2 != 1:
            raise CheckException('2. Warm start failed or the PLC run failed;')

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
        super(Test200SmartSanityOther006, self).cleanup()
