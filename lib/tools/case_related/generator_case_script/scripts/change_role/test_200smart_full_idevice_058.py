#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice058(CaseMW):
    """From controller to I-device with L-L IO
    No.: test_200smart_full_idevice_058
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Config plc as a controller in PN Wizard, generate and download;
    Step actions:
        1. In PN Wizard, add role "I-Device", add transfer area, Generate and Downlaod;
    Expected results:
        1.Generate and download successful;
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
        super(Test200SmartFullIdevice058, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Config plc as a controller in PN Wizard, generate and download;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice058, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. In PN Wizard, add role "I-Device", add transfer area, Generate and Downlaod;')

        self.logger.info('Expected results:')
        self.logger.info('1.Generate and download successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice058, self).cleanup()
