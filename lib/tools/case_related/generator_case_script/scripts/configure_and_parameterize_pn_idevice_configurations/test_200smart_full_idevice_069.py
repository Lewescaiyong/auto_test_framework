#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice069(CaseMW):
    """Controller + i-device(fixed ip)
    No.: test_200smart_full_idevice_069
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "I-Device";
    Step actions:
        1. Config fixed ip and name, add transfer area, export gsdml file,  then generate and download;
        2. View status in plc information, then power cycle the PLC, and view the config;
        3. Another PLC, import gsdml file in step1, select role is controller, add idevice in step1, generate and download;
        4. View configuration in controller plc information and cyclic data between the two cpu;
        5. Power cycle the idevice, view the configuration and the connection with controller;
    Expected results:
        1. Export successful, generate and download ok;
        2. The configuration is corret before and after power cycle;
        3. Generate and download ok;
        4. The configuration is corret, cyclic data is correct between controller and idevice.
        5. The configuration is corret, connect to high-level controller success.
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
        super(Test200SmartFullIdevice069, self).prepare()

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
        super(Test200SmartFullIdevice069, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Config fixed ip and name, add transfer area, export gsdml file,  then generate and download;')
        self.logger.info('2. View status in plc information, then power cycle the PLC, and view the config;')
        self.logger.info('3. Another PLC, import gsdml file in step1, select role is controller, add idevice in step1, generate and download;')
        self.logger.info('4. View configuration in controller plc information and cyclic data between the two cpu;')
        self.logger.info('5. Power cycle the idevice, view the configuration and the connection with controller;')

        self.logger.info('Expected results:')
        self.logger.info('1. Export successful, generate and download ok;')
        self.logger.info('2. The configuration is corret before and after power cycle;')
        self.logger.info('3. Generate and download ok;')
        self.logger.info('4. The configuration is corret, cyclic data is correct between controller and idevice.')
        self.logger.info('5. The configuration is corret, connect to high-level controller success.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice069, self).cleanup()
