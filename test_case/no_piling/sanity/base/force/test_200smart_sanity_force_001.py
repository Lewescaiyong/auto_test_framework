#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityForce001(CaseMW):
    """Force and unforce new value
    No.: test_200smart_sanity_force_001
    Preconditions:
        1. Open Micro/WIN;  
        2. Set up connection with PLC;
    Step actions:
        1. Make the PLC in run Mode, open status chart, Force  a new value to QB0;
        2. Unforce the forced new value;
    Expected results:
        1. Force successful, the value of QB0 is same with the forced new value;
        2. Unforce successful;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-09-20 create
    """

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
        super(Test200SmartSanityForce001, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.MicroWIN.test_prepare('force_qb0.smart', False)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityForce001, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Make the PLC in run Mode, open status chart, Force  a new value to QB0;')
        self.PLC['1'].set_plc_mode(1)
        self.common.sleep(5)
        memory_options = self.PLC['1'].find('memory_options')
        memory_options.force('q', 'byte', 0, value=self.force_value)
        self.common.sleep(5)
        qb0_after_force = memory_options.read_memory_data('q')

        self.logger.info('2. Unforce the forced new value;')
        memory_options.unforce_all()
        self.common.sleep(5)
        qb0_after_unforce = memory_options.read_memory_data('q')

        self.logger.info('Expected results:')
        self.logger.info('force_value: %s, qb0_after_force: %s, qb0_after_unforce: %s.' % (
            self.force_value, qb0_after_force, qb0_after_unforce))
        self.logger.info('1. Force successful, the value of QB0 is same with the forced new value;')
        if qb0_after_force != self.force_value:
            raise CheckException('Force failed, the value of QB0 is not same with the forced new value;')

        self.logger.info('2. Unforce successful;')
        if qb0_after_unforce == self.force_value:
            raise CheckException('UnForce failed;')

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
        super(Test200SmartSanityForce001, self).cleanup()
