#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice016(CaseMW):
    """Type
    No.: test_200smart_full_idevice_016
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "I-Device", click "Next" and add one transfer area;
    Step actions:
        1. Add second trasnfer area and set the length to 128 bytes;
        2. Add third transfer area, and change the type to "Output";
        3. Change the third transfer area to "Input";
    Expected results:
        1. Add successful, the address and length  has red under line;
        2. Add succssful, change successful;
        3. Change successful, Micro/win is normal, not crash;
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
        super(Test200SmartFullIdevice016, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. In PN wizard, select plc role is "I-Device", click "Next" and add one transfer area;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice016, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add second trasnfer area and set the length to 128 bytes;')
        self.logger.info('2. Add third transfer area, and change the type to "Output";')
        self.logger.info('3. Change the third transfer area to "Input";')

        self.logger.info('Expected results:')
        self.logger.info('1. Add successful, the address and length  has red under line;')
        self.logger.info('2. Add succssful, change successful;')
        self.logger.info('3. Change successful, Micro/win is normal, not crash;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice016, self).cleanup()
