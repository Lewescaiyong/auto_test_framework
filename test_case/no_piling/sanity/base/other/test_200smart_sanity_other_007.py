#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityOther007(CaseMW):
    """Set clock
    No.: test_200smart_sanity_other_007
    Preconditions:
        1. Open Micro/WIN as administrator;  
        2. Set up connection with PLC;
    Step actions:
        1. Reaed PC and Set;
        2. Run a program and Stop;
        3. View the envet log;
        4. Power cycle the CPU, and view the clock;
    Expected results:
        1. Set successful;
        2. Operate successful;
        3. The latest logs record with the setted clock;
        4. The clock revert to default;
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
        super(Test200SmartSanityOther007, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN as administrator;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.MicroWIN.test_prepare('ob_db_sdb_01.smart', False)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityOther007, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Reaed PC and Set;')
        self.PLC['1'].plc_clock = 1
        clock = self.PLC['1'].plc_clock
        now = self.converter.convert_time_to_str(pattern='%Y%m%d')

        self.logger.info('2. Run a program and Stop;')
        self.PLC['1'].set_plc_mode(1)
        result1 = self.PLC['1'].get_plc_mode()
        self.common.sleep(5)
        self.PLC['1'].set_plc_mode(0)
        result2 = self.PLC['1'].get_plc_mode()

        self.logger.info('3. View the envet log;')
        # set clock does not record event log
        self.logger.info('4. Power cycle the CPU, and view the clock;')
        self.PLC['1'].plc_power_cycle()
        result3 = self.PLC['1'].check_clock()

        self.logger.info('Expected results:')
        self.logger.info('1. Set successful;')
        month = self.converter.convert_to_special_length_str(str(clock['month']), 2)
        day = self.converter.convert_to_special_length_str(str(clock['day']), 2)
        if (str(clock['year']) + month + day) != now[2:]:
            self.logger.info('PLC clock: %s, PC clock: %s.' % (str(clock), now))
            raise CheckException('1. Set failed;')

        self.logger.info('2. Operate successful;')
        if result1 != 1 or result2 != 0:
            raise CheckException('2. Operate failed;')

        self.logger.info('3. The latest logs record with the setted clock;')
        self.logger.info('4. The clock not revert to default;')
        if not result3:
            raise CheckException('4. The clock revert to default;')

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
        super(Test200SmartSanityOther007, self).cleanup()
