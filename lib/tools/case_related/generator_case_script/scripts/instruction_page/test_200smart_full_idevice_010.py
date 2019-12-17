#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice010(CaseMW):
    """Commnication
    No.: test_200smart_full_idevice_010
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Connect to a plc with V2.5 FW;
    Step actions:
        1. Open PN wizard, select plc role as "Control";
    Expected results:
        1. The default value of "Send Clock" and "Start Up time" is 1.000 and 10000, the "Send Clock" cannot be changed, the "Start Up time" can be changed;
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
        super(Test200SmartFullIdevice010, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Connect to a plc with V2.5 FW;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice010, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Open PN wizard, select plc role as "Control";')

        self.logger.info('Expected results:')
        self.logger.info('1. The default value of "Send Clock" and "Start Up time" is 1.000 and 10000, the "Send Clock" cannot be changed, the "Start Up time" can be changed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice010, self).cleanup()
