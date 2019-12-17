#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice046(CaseMW):
    """Download with different configuration
    No.: test_200smart_full_idevice_046
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc configed as I-Device with fixed IP and station name, download;
    Step actions:
        1. Modify the station name, generate and download;
        2. Modify the IP, generate and download;
        3. Modify the IP and subnet mask, generate and download;
        4. Modify the IP, subnetmask and station name, generate and download;
    Expected results:
        1. Download successful, the modifications take effect;
        2. Download successful, the modifications take effect;
        3. Download successful, the modifications take effect;
        4. Download successful, the modifications take effect;
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
        super(Test200SmartFullIdevice046, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Plc configed as I-Device with fixed IP and station name, download;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice046, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Modify the station name, generate and download;')
        self.logger.info('2. Modify the IP, generate and download;')
        self.logger.info('3. Modify the IP and subnet mask, generate and download;')
        self.logger.info('4. Modify the IP, subnetmask and station name, generate and download;')

        self.logger.info('Expected results:')
        self.logger.info('1. Download successful, the modifications take effect;')
        self.logger.info('2. Download successful, the modifications take effect;')
        self.logger.info('3. Download successful, the modifications take effect;')
        self.logger.info('4. Download successful, the modifications take effect;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice046, self).cleanup()
