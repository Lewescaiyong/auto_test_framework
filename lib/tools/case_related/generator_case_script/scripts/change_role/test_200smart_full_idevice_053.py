#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice053(CaseMW):
    """From none to I-device without L-L IO
    No.: test_200smart_full_idevice_053
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. New project and download;
    Step actions:
        1. Config plc as an idevice without L-L device  in PN Wizard, generate and download;
    Expected results:
        1. Generate and download successful;
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
        super(Test200SmartFullIdevice053, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. New project and download;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice053, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Config plc as an idevice without L-L device  in PN Wizard, generate and download;')

        self.logger.info('Expected results:')
        self.logger.info('1. Generate and download successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice053, self).cleanup()
