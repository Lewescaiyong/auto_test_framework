#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice004(CaseMW):
    """Compile pass
    No.: test_200smart_full_idevice_004
    Preconditions:
        1. Open Micro/WIN V2.5;
    Step actions:
        1. Create a project with correct program, open PN Wizard;
    Expected results:
        1. Open successful;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-11-18 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice004, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice004, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Create a project with correct program, open PN Wizard;')
        time_str = self.converter.convert_time_to_str()
        self.prj_file = 'new_%s.smart' % time_str
        self.PROJECT.project_new('self.prj_file')

        # get is support
        wizard_pn = self.PROJECT.find('wizard_pn')
        is_support = wizard_pn.is_support

        self.logger.info('Expected results:')
        self.logger.info('1. Open successful;')
        if not is_support:
            raise CheckException('2. Open failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice004, self).cleanup()
