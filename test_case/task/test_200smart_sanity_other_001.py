#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityOther001(CaseMW):
    """Project protection
    No.: test_200smart_sanity_other_001
    Preconditions:
        1. Open Micro/WIN as administrator;  
        1. Create a new file and save successful;
    Step actions:
        1. Click "File" -> "Project", select "Password-protect this project", and input the password and click "OK";
        2. Reopen the project;
    Expected results:
        1. Set protection successful;
        2. Need input the password to reopen and edit the project;
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
        super(Test200SmartSanityOther001, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN as administrator;  ')
        self.logger.info('1. Create a new file and save successful;')
        self.prj_file = 'project_password.smart'
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
        super(Test200SmartSanityOther001, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Click "File" -> "Project", select "Password-protect this project", and input the '
                         'password and click "OK";')
        result = self.PROJECT.project_set_protection(self.password)
        self.save_as_file = self.prj_file.replace('.', '_%s.' % self.password)
        self.PROJECT.project_save_as(self.save_as_file)

        self.logger.info('2. Reopen the project;')
        self.PROJECT.project_close()
        try:
            self.PROJECT.project_open(self.save_as_file, '')
        except CheckException:
            result1 = False
        else:
            result1 = True
            self.PROJECT.project_close()
        result2 = self.PROJECT.project_open(self.save_as_file)

        self.logger.info('Expected results:')
        self.logger.info('1. Set protection successful;')
        if result['code'] != 0:
            raise CheckException('1. Set protection failed.')

        self.logger.info('2. Need input the password to reopen and edit the project;')
        if result1:
            raise CheckException(
                '2. After set password, not need to input the password to reopen and edit the project;')
        if result2['code'] != 0:
            raise CheckException('2. After input the password, reopen the project failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityOther001, self).cleanup()
        self.file_options.remove_file_dir(self.save_as_file, is_project=True)
