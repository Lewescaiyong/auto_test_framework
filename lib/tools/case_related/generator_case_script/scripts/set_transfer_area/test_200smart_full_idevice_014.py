#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice014(CaseMW):
    """Move
    No.: test_200smart_full_idevice_014
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "I-Device", click "Next" and add some transfer areas;
    Step actions:
        1. Move up or move down transfer area
    Expected results:
        1. Move success but subslot can not be moved
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
        super(Test200SmartFullIdevice014, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. In PN wizard, select plc role is "I-Device", click "Next" and add some transfer areas;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice014, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Move up or move down transfer area')

        self.logger.info('Expected results:')
        self.logger.info('1. Move success but subslot can not be moved')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice014, self).cleanup()
