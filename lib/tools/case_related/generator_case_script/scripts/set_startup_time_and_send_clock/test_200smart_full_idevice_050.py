#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice050(CaseMW):
    """Sendclock
    No.: test_200smart_full_idevice_050
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "I-Device";
    Step actions:
        1. In PN Wizard, view the value of sendclock;
        2. Modify sendclock;
    Expected results:
        1. The default sendclock is 1.000ms;
        2. The sendclock can not be modified;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-12-13 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice050, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Plc role is "I-Device";')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice050, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. In PN Wizard, view the value of sendclock;')
        self.logger.info('2. Modify sendclock;')

        self.logger.info('Expected results:')
        self.logger.info('1. The default sendclock is 1.000ms;')
        self.logger.info('2. The sendclock can not be modified;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice050, self).cleanup()
