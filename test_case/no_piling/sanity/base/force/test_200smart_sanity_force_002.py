#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityForce002(CaseMW):
    """Force new value in STOP mode
    No.: test_200smart_sanity_force_002
    Preconditions:
        1. Open Micro/WIN;  
        2. Set up connection with PLC;
    Step actions:
        1. Make the PLC in stop Mode, Force a new value to QB0;
        2. Enable the "Force in STOP" in Debug, then  force a new value to output.
        3. Unforce the forced new value;
    Expected results:
        1. Force failed, and bring up a popup window with "Requested operation is not possible.
           You must enable Write-Forcing of Outputs in STOP mode";
        2. Force successful;
        3. Unforce successful;
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
        super(Test200SmartSanityForce002, self).prepare()

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
        super(Test200SmartSanityForce002, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Make the PLC in stop Mode, Force a new value to QB0;')
        self.PLC['1'].set_plc_mode(0)

        self.logger.info('2. Enable the "Force in STOP" in Debug, then  force a new value to output.')
        memory_options = self.PLC['1'].find('memory_options')
        memory_options.force('q', 'byte', 0, value=self.force_value)
        self.common.sleep(1)
        qb0_after_force = memory_options.read_memory_data('q')

        self.logger.info('3. Unforce the forced new value;')
        result = memory_options.unforce_all()
        self.common.sleep(1)
        qb0_after_unforce = memory_options.read_memory_data('q')

        self.logger.info('Expected results:')
        self.logger.info('force_value: %s, qb0_after_force: %s, qb0_after_unforce: %s.' % (
            self.force_value, qb0_after_force, qb0_after_unforce))
        self.logger.info('1. Force failed, and bring up a popup window with "Requested operation is not possible. '
                         'You must enable Write-Forcing of Outputs in STOP mode";')

        self.logger.info('2. Force successful;')
        if qb0_after_force != self.force_value:
            self.logger.info('Force value: %s, memory value: %s.' % (self.force_value, qb0_after_force))
            raise CheckException('Force failed, the value of QB0 is not same with the forced new value;')

        self.logger.info('3. Unforce successful;')
        if result['code'] != 0:
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

        self.PLC['1'].plc_clear('all')
        super(Test200SmartSanityForce002, self).cleanup()
