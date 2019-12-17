#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice005(CaseMW):
    """Compile failed
    No.: test_200smart_full_idevice_005
    Preconditions:
        1. Open Micro/WIN V2.5;
    Step actions:
        1. Create a project with incorrect program, open PN Wizard;
    Expected results:
        1. Open failed, has prompt message about compile error;
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
        super(Test200SmartFullIdevice005, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice005, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Create a project with incorrect program, open PN Wizard;')

        self.logger.info('Expected results:')
        self.logger.info('1. Open failed, has prompt message about compile error;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice005, self).cleanup()
