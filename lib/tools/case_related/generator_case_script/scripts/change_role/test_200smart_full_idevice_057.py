#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice057(CaseMW):
    """From controller to I-device without L-L IO
    No.: test_200smart_full_idevice_057
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Config plc as a controller in PN Wizard, generate and download;
    Step actions:
        1. In PN Wizard,  uncheck "Controller" in PLC Role;
        2. Select yes, Check "I-Device" in PLC Role, add transfer area, Generate and Downlaod;
    Expected results:
        1. Prompt user the existing PROFINET configuration will be lost, continue or not;
        2. Generate and download successful;
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
        super(Test200SmartFullIdevice057, self).prepare()

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
        super(Test200SmartFullIdevice057, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. In PN Wizard,  uncheck "Controller" in PLC Role;')
        self.logger.info('2. Select yes, Check "I-Device" in PLC Role, add transfer area, Generate and Downlaod;')

        self.logger.info('Expected results:')
        self.logger.info('1. Prompt user the existing PROFINET configuration will be lost, continue or not;')
        self.logger.info('2. Generate and download successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice057, self).cleanup()
