#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityOther002(CaseMW):
    """POU protection
    No.: test_200smart_sanity_other_002
    Preconditions:
        1. Open Micro/WIN as administrator;  
        1. Create a new file and save successful;
    Step actions:
        1. Click "File" -> "POU", select "Password-protect this block", and input the password and click "OK";
        2. Click "File" -> "POU", select "Permanently remove password", input password and click "Authorize";
    Expected results:
        1. Set protection successful, and the MAIN pou is locked, can't view and edit;
        2. Remove successful, the MAIN pou restore,can view and edit.
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-09-20 create
    """

    password = '123456'

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityOther002, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN as administrator;  ')
        self.logger.info('1. Create a new file and save successful;')
        self.prj_file = 'pou_password.smart'
        self.PROJECT.project_open(self.prj_file)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityOther002, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Click "File" -> "POU", select "Password-protect this block", and input the password and '
                         'click "OK";')
        pou_collector = self.PROJECT.find('pou_collector')
        pou_main = pou_collector.find('pou_main')
        result1 = pou_main.pou_set_protection(self.password)
        self.save_as_file = self.prj_file.replace('.', '_%s.' % self.password)
        self.PROJECT.project_save_as(self.save_as_file)
        self.PROJECT.project_close()
        self.PROJECT.project_open(self.save_as_file)
        result2 = pou_main.pou_is_protected()

        self.logger.info('2. Click "File" -> "POU", select "Permanently remove password", input password and click '
                         '"Authorize";')
        result3 = pou_main.pou_authorize(self.password, is_clear=True)
        result4 = pou_main.pou_is_protected()

        self.logger.info('Expected results:')
        self.logger.info('1. Set protection successful, and the MAIN pou is locked, can not view and edit;')
        if result1['code'] != 0 or result2 != 2:
            raise CheckException('1. Set protection failed.')

        self.logger.info('2. Remove successful, the MAIN pou restore,can view and edit.')
        if result3['code'] != 0 or result4 != 0:
            raise CheckException('2. Remove failed.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityOther002, self).cleanup()
        self.file_options.remove_file_dir(self.save_as_file, is_project=True)
