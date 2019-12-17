#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice024(CaseMW):
    """IP Setting
    No.: test_200smart_full_idevice_024
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Import two gsdml files, fixed and dcp;
        3. In PN wizard, config plc as controller and add the two devices;
    Step actions:
        1. View the "IP Setting" and "IP Address" of the fixed device in device table;
        2. View the "IP Setting" and "IP Address" of the dcp device in device table;
        3. Add a catalog device, View the "IP Setting" and "IP Address" of the dcp device in device table;
    Expected results:
        1. The "IP Setting" of fixed device is "Fixed" and cannot be modifyed, the "IP Address" is grey and cannot be edited.
        2. The "IP Setting" of dcp device is "Set by user" and can be modifyed, the "IP Address" can be edited.
        3. The "IP Setting" of catalog device is "Set by user" and can be modifyed, the "IP Address" can be edited.
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
        super(Test200SmartFullIdevice024, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Import two gsdml files, fixed and dcp;')
        self.logger.info('3. In PN wizard, config plc as controller and add the two devices;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice024, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. View the "IP Setting" and "IP Address" of the fixed device in device table;')
        self.logger.info('2. View the "IP Setting" and "IP Address" of the dcp device in device table;')
        self.logger.info('3. Add a catalog device, View the "IP Setting" and "IP Address" of the dcp device in device table;')

        self.logger.info('Expected results:')
        self.logger.info('1. The "IP Setting" of fixed device is "Fixed" and cannot be modifyed, the "IP Address" is grey and cannot be edited.')
        self.logger.info('2. The "IP Setting" of dcp device is "Set by user" and can be modifyed, the "IP Address" can be edited.')
        self.logger.info('3. The "IP Setting" of catalog device is "Set by user" and can be modifyed, the "IP Address" can be edited.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice024, self).cleanup()
