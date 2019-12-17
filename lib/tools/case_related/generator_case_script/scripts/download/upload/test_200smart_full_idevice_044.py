#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice044(CaseMW):
    """I-Device  fix
    No.: test_200smart_full_idevice_044
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "I-Device";
    Step actions:
        1. Check "Paraneter assignment..." and config fixed IP and station name, add transfer area,generate and download to CPU;
        2. New a project, upload all from CPU;
        3. Uncheck "Paraneter assignment...", generate and download to CPU;
        4. New a project, upload all from CPU;
    Expected results:
        1. Download successful;
        2. Upload successful, the configuration is corret;
        3. Download successful;
        4. Upload successful, the configuration is corret;
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
        super(Test200SmartFullIdevice044, self).prepare()

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
        super(Test200SmartFullIdevice044, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Check "Paraneter assignment..." and config fixed IP and station name, add transfer area,generate and download to CPU;')
        self.logger.info('2. New a project, upload all from CPU;')
        self.logger.info('3. Uncheck "Paraneter assignment...", generate and download to CPU;')
        self.logger.info('4. New a project, upload all from CPU;')

        self.logger.info('Expected results:')
        self.logger.info('1. Download successful;')
        self.logger.info('2. Upload successful, the configuration is corret;')
        self.logger.info('3. Download successful;')
        self.logger.info('4. Upload successful, the configuration is corret;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice044, self).cleanup()
