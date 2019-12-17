#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice021(CaseMW):
    """Add device
    No.: test_200smart_full_idevice_021
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "Controller", click "Next";
        3. Import a gsdml file of io device;
    Step actions:
        1. Add device by catalog;
        2. Add device by imported gsdml file;
        3. Add device by "Add" button;
        4. Add device by Tab key;
        5. Add device by draging from tree;
        6. Add 8 devices;
        7. Add 9th device;
    Expected results:
        1. Add successful, display correctly in network tree and network topology;
        2. Add successful, display correctly in network tree and network topology;
        3. Add successful, display correctly in network tree and network topology;
        4. Add successful, display correctly in network tree and network topology;
        5. Add successful, display correctly in network tree and network topology;
        6. Add successful, display correctly in network tree and network topology;
        7. Add failed, has resonable prompt message;
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
        super(Test200SmartFullIdevice021, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. In PN wizard, select plc role is "Controller", click "Next";')
        self.logger.info('3. Import a gsdml file of io device;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice021, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add device by catalog;')
        self.logger.info('2. Add device by imported gsdml file;')
        self.logger.info('3. Add device by "Add" button;')
        self.logger.info('4. Add device by Tab key;')
        self.logger.info('5. Add device by draging from tree;')
        self.logger.info('6. Add 8 devices;')
        self.logger.info('7. Add 9th device;')

        self.logger.info('Expected results:')
        self.logger.info('1. Add successful, display correctly in network tree and network topology;')
        self.logger.info('2. Add successful, display correctly in network tree and network topology;')
        self.logger.info('3. Add successful, display correctly in network tree and network topology;')
        self.logger.info('4. Add successful, display correctly in network tree and network topology;')
        self.logger.info('5. Add successful, display correctly in network tree and network topology;')
        self.logger.info('6. Add successful, display correctly in network tree and network topology;')
        self.logger.info('7. Add failed, has resonable prompt message;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice021, self).cleanup()
