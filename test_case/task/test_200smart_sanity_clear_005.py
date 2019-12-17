#!/usr/bin/env python

import time

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityClear005(CaseMW):
    """Reset to factory defaults
    No.: test_200smart_sanity_clear_005
    Preconditions:
        1. Open Micro/WINr;  
        2. Set up connection with PLC;
        3. Download a project which has OB,DB,SDB;
    Step actions:
        1. Select Reset to factory defaults in clear popup;
        2. Compare; ;
    Expected results:
        1. Clear successful, all blocks is cleared, all user memory is reset to initial powerup state,
           all special memory is reset to initial values, ip and station name and day clock is not cleared;
        2. The OB, DB, SDB is different;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-09-20 create
    """

    memory_options = None
    force_value = CaseMW.common.get_random_element()

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityClear005, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WINr;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.logger.info('3. Download a project which has OB,DB,SDB;')
        self.MicroWIN.test_prepare('reset_factory_01.smart', False)
        # set cpu mode to run
        self.PLC['1'].set_plc_mode(1)
        self.memory_options = self.PLC['1'].find('memory_options')
        # force some value
        self.memory_options.force('v', 'byte', 0, value=self.force_value)
        time.sleep(5)
        self.PLC['1'].set_plc_mode(0)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityClear005, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Select Reset to factory defaults in clear popup;')
        result1 = self.PLC['1'].check_after_clear()
        vb0_after_force = self.memory_options.read_memory_data('v')
        self.logger.info('Before reset factory, check result: %s, VB0: %s.' % (result1, vb0_after_force))
        result2 = self.PLC['1'].plc_clear('all')

        self.logger.info('2. Compare; ;')
        result3 = self.MicroWIN.compare_with_plc()
        result4 = self.PLC['1'].check_after_clear()
        vb0_after_clear = self.memory_options.read_memory_data('v')

        self.logger.info('Expected results:')
        self.logger.info('1. Clear successful, all blocks is cleared, all user memory is reset to initial powerup '
                         'state, all special memory is reset to initial values, ip and station name and day clock '
                         'is not cleared; ')
        if result2['code'] != 0:
            raise CheckException('1. Clear ALL failed;')

        self.logger.info('2. The OB, DB, SDB is different;')
        if result3['ob'] or result3['db'] or result3['sdb']:
            self.logger.info('Compare result: %s' % result3)
            raise CheckException('Compare failed;')
        if (not result4) or vb0_after_clear != 0:
            raise CheckException('After reset factory, PLC check does not pass.')

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
        self.PLC['1'].plc_clear('all')
        super(Test200SmartSanityClear005, self).cleanup()
