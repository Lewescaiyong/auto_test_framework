#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice009(CaseMW):
    """Controller&I-Device
    No.: test_200smart_full_idevice_009
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Connect to a plc with V2.5 FW;
    Step actions:
        1. Open PN wizard, select plc role as "Controller&I-Device";
    Expected results:
        1. "Paraneter assignment..." is grey and unchecked, Only "Fixed IP address and name" checked and displayed under "Ethernet Port"; a controller page and an idevice pageunder PROFINET network;
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
        super(Test200SmartFullIdevice009, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Connect to a plc with V2.5 FW;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice009, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Open PN wizard, select plc role as "Controller&I-Device";')

        self.logger.info('Expected results:')
        self.logger.info('1. "Paraneter assignment..." is grey and unchecked, Only "Fixed IP address and name" checked and displayed under "Ethernet Port"; a controller page and an idevice pageunder PROFINET network;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice009, self).cleanup()
