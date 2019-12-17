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
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice005, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Create a project with incorrect program, open PN Wizard;')
        time_str = self.converter.convert_time_to_str()
        self.prj_file = 'new_%s.smart' % time_str
        self.PROJECT.project_new('self.prj_file')
        self.PROJECT.project_add_instruction(pou_type='pou_main', network_id=0, row_id=0, col_id=0,
                                             instruction_type='normally_open', instruction_values=('Always_On',))

        # get is support
        wizard_pn = self.PROJECT.find('wizard_pn')
        is_support = wizard_pn.is_support

        self.logger.info('Expected results:')
        self.logger.info('1. Open failed, has prompt message about compile error;')
        if is_support:
            raise CheckException('2. Open successfully;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice005, self).cleanup()
