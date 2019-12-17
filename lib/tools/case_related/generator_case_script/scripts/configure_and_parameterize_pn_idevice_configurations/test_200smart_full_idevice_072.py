#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice072(CaseMW):
    """Controller + i-device(DCP)
                     + io-device
    No.: test_200smart_full_idevice_072
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Connect Micro/WIN to PLC;
        3. Select plc role is "idevice" in PN wizard;
    Step actions:
        1.  Select obtain IP by other services, add transfer area, export gsdml file,  then generate and download;
        2. View configuration in plc information, then power cycle the PLC, and view the config;
        3. Another PLC, import gsdml file in step1,  select role is controller,add idevice in step1 and an io-device, generate and download;
        4. View configuration in controller plc information and cyclic data between controller and idevice/io-device;
    Expected results:
        1. Export successful, generate and download ok;
        2. The configuration is corret before and after power cycle;
        3. Generate and download ok;
        4. The configuration is corret, cyclic data is correct between controller and idevice/io-device.
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
        super(Test200SmartFullIdevice072, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Connect Micro/WIN to PLC;')
        self.logger.info('3. Select plc role is "idevice" in PN wizard;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice072, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1.  Select obtain IP by other services, add transfer area, export gsdml file,  then generate and download;')
        self.logger.info('2. View configuration in plc information, then power cycle the PLC, and view the config;')
        self.logger.info('3. Another PLC, import gsdml file in step1,  select role is controller,add idevice in step1 and an io-device, generate and download;')
        self.logger.info('4. View configuration in controller plc information and cyclic data between controller and idevice/io-device;')

        self.logger.info('Expected results:')
        self.logger.info('1. Export successful, generate and download ok;')
        self.logger.info('2. The configuration is corret before and after power cycle;')
        self.logger.info('3. Generate and download ok;')
        self.logger.info('4. The configuration is corret, cyclic data is correct between controller and idevice/io-device.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice072, self).cleanup()
