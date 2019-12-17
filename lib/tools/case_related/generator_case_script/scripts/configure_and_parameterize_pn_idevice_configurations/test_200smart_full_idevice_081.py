#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice081(CaseMW):
    """Controller + i-device(with low level system:1 i-device)
    No.: test_200smart_full_idevice_081
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Connect Micro/WIN to PLC;
        3. Select plc role is "idevice" in PN wizard;
    Step actions:
        1. Config ip and name, add transfer area, export gsdml file, generate and download for 8 plc;
        2. The second PLC,  import the gsdml file in step 1, Select plc role is "controller & idevice" in PN wizard, config ip and name, add transfer area, export gsdml file,  add the plc in step 1, then generate and download;
        3. View configuration in plc information, then power cycle the PLC, and view the config;
        4. The third PLC, import gsdml file in step2,  select role is controller,add idevices in step2, generate and download;
        5. View configuration in controller plc information and cyclic data between cpus;
        6. Power cycle the second idevice, view the configuration, view the connection with high level controller and low level system;
    Expected results:
        1. Export successful, generate and download ok;
        2. Generate and download ok;
        3. The configuration is corret before and after power cycle;
        4. Generate and download ok;
        5. The configuration is corret, cyclic data is correct between cpus;
        6. The configuration is corret, connect to high-level controller success, connect to low-level system success;
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
        super(Test200SmartFullIdevice081, self).prepare()

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
        super(Test200SmartFullIdevice081, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Config ip and name, add transfer area, export gsdml file, generate and download for 8 plc;')
        self.logger.info('2. The second PLC,  import the gsdml file in step 1, Select plc role is "controller & idevice" in PN wizard, config ip and name, add transfer area, export gsdml file,  add the plc in step 1, then generate and download;')
        self.logger.info('3. View configuration in plc information, then power cycle the PLC, and view the config;')
        self.logger.info('4. The third PLC, import gsdml file in step2,  select role is controller,add idevices in step2, generate and download;')
        self.logger.info('5. View configuration in controller plc information and cyclic data between cpus;')
        self.logger.info('6. Power cycle the second idevice, view the configuration, view the connection with high level controller and low level system;')

        self.logger.info('Expected results:')
        self.logger.info('1. Export successful, generate and download ok;')
        self.logger.info('2. Generate and download ok;')
        self.logger.info('3. The configuration is corret before and after power cycle;')
        self.logger.info('4. Generate and download ok;')
        self.logger.info('5. The configuration is corret, cyclic data is correct between cpus;')
        self.logger.info('6. The configuration is corret, connect to high-level controller success, connect to low-level system success;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice081, self).cleanup()
