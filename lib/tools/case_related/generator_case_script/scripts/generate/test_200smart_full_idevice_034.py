#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice034(CaseMW):
    """Compatibility
    No.: test_200smart_full_idevice_034
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Open 2.4 project with PN configuration;
    Step actions:
        1. Open 2.4 project with PN, and modify some config, generate;
        2. Download the configuration;
    Expected results:
        1. Generate successful;
        2. Download configuration successful;
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
        super(Test200SmartFullIdevice034, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Open 2.4 project with PN configuration;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice034, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Open 2.4 project with PN, and modify some config, generate;')
        self.logger.info('2. Download the configuration;')

        self.logger.info('Expected results:')
        self.logger.info('1. Generate successful;')
        self.logger.info('2. Download configuration successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice034, self).cleanup()
