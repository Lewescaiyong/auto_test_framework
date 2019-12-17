#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice049(CaseMW):
    """Startup time--i-device with L-L device
    No.: test_200smart_full_idevice_049
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Set startup mode to "RUN";
        3. Plc role is "Controller & I-Device" add transfer area, add an io device;
    Step actions:
        1. Set startup time to 0, generate and download, power cycle the CPU;
        2. Set startup time to 10000, generate and download, power cycle the CPU;
        3. Set startup time to 60000, generate and download, power cycle the CPU;
        4. Set startup time to 0,  generate and download, power cycle the CPU;
    Expected results:
        1. Startup time takes effect;
        2. Startup time takes effect;
        3. Startup time takes effect;
        4. Generate failed, has reasonable prompt message;
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
        super(Test200SmartFullIdevice049, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Set startup mode to "RUN";')
        self.logger.info('3. Plc role is "Controller & I-Device" add transfer area, add an io device;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice049, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Set startup time to 0, generate and download, power cycle the CPU;')
        self.logger.info('2. Set startup time to 10000, generate and download, power cycle the CPU;')
        self.logger.info('3. Set startup time to 60000, generate and download, power cycle the CPU;')
        self.logger.info('4. Set startup time to 0,  generate and download, power cycle the CPU;')

        self.logger.info('Expected results:')
        self.logger.info('1. Startup time takes effect;')
        self.logger.info('2. Startup time takes effect;')
        self.logger.info('3. Startup time takes effect;')
        self.logger.info('4. Generate failed, has reasonable prompt message;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice049, self).cleanup()
