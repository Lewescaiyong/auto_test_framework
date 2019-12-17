#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice045(CaseMW):
    """I-Device with 8 L-L devices
    No.: test_200smart_full_idevice_045
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "Controller & I-Device";
    Step actions:
        1. Config IP and station name, add transfer area, add 8 L-L devices, generate and download to CPU;
        2. New a project, upload all from CPU;
    Expected results:
        1. Download successful;
        2. Upload successful, the configuration is corret;
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
        super(Test200SmartFullIdevice045, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Plc role is "Controller & I-Device";')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice045, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Config IP and station name, add transfer area, add 8 L-L devices, generate and download to CPU;')
        self.logger.info('2. New a project, upload all from CPU;')

        self.logger.info('Expected results:')
        self.logger.info('1. Download successful;')
        self.logger.info('2. Upload successful, the configuration is corret;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice045, self).cleanup()
