#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice025(CaseMW):
    """Catalog tree
    No.: test_200smart_full_idevice_025
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Import one gsdml file;
        3. In PN wizard, config plc as controller and add the device;
    Step actions:
        1. View the imported device in Catalog tree;
        2. View the catalog devices in Catalog tree;
    Expected results:
        1. The device display correctly under Catalog->PROFINET-IO, select the device with mouse, the information is display correctly.
        2. The devices display correctly under Catalog->PLC S7-200 SMART, select one device with mouse, the information is display correctly.
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
        super(Test200SmartFullIdevice025, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Import one gsdml file;')
        self.logger.info('3. In PN wizard, config plc as controller and add the device;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice025, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. View the imported device in Catalog tree;')
        self.logger.info('2. View the catalog devices in Catalog tree;')

        self.logger.info('Expected results:')
        self.logger.info('1. The device display correctly under Catalog->PROFINET-IO, select the device with mouse, the information is display correctly.')
        self.logger.info('2. The devices display correctly under Catalog->PLC S7-200 SMART, select one device with mouse, the information is display correctly.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice025, self).cleanup()
