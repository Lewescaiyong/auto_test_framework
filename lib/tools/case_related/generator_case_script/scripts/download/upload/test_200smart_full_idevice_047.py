#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice047(CaseMW):
    """Download to different CPU
    No.: test_200smart_full_idevice_047
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "I-Device";
    Step actions:
        1. Config IP and station name, add transfer area, generate and download to a CPU which has different type with configed in PN Wizard;
        2. Modify the CPU module in system block same as connected CPU, re-generate and download;
    Expected results:
        1. Download failed, has reasonable prompt message;
        2. Download successful;
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
        super(Test200SmartFullIdevice047, self).prepare()

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
        super(Test200SmartFullIdevice047, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Config IP and station name, add transfer area, generate and download to a CPU which has different type with configed in PN Wizard;')
        self.logger.info('2. Modify the CPU module in system block same as connected CPU, re-generate and download;')

        self.logger.info('Expected results:')
        self.logger.info('1. Download failed, has reasonable prompt message;')
        self.logger.info('2. Download successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice047, self).cleanup()
