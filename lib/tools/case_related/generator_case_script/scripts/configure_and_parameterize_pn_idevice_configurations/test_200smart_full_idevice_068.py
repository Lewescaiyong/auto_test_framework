#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice068(CaseMW):
    """Controller + 8 io-device
    No.: test_200smart_full_idevice_068
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "Controller";
    Step actions:
        1. Add 8 io-device, generate and download;
        2. View the device status and module status in plc information;
        3. Power cycle the PLC, then view the configuration;
    Expected results:
        1. Download successful;
        2. The status in plc information is correct;
        3. The configuration not lost after power cycle;
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
        super(Test200SmartFullIdevice068, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Plc role is "Controller";')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice068, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add 8 io-device, generate and download;')
        self.logger.info('2. View the device status and module status in plc information;')
        self.logger.info('3. Power cycle the PLC, then view the configuration;')

        self.logger.info('Expected results:')
        self.logger.info('1. Download successful;')
        self.logger.info('2. The status in plc information is correct;')
        self.logger.info('3. The configuration not lost after power cycle;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice068, self).cleanup()
