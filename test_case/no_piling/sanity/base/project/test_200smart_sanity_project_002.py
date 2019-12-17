#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityProject002(CaseMW):
    """Save file
    No.: test_200smart_sanity_project_002
    Preconditions:
        1. Open Micro/WIN;
        2. Create a new file;
    Step actions:
        1. Save the new file;
        2. Modify some configuration in this project;
        3.Save modified project;
    Expected results:
        1. Save successful;
        2. Modify successful;
        3. Save successful;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-09-21 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject002, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. Create a new file;')
        time_str = self.converter.convert_time_to_str()
        self.prj_file = 'new_%s.smart' % time_str
        self.PROJECT.project_new('self.prj_file')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject002, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Save the new file;')
        result1 = self.PROJECT.project_save_as(self.prj_file)

        self.logger.info('2. Modify some configuration in this project;')
        system_block = self.PROJECT.find('system_block')
        result2 = system_block.set_startup({'cpu_mode': 'run'})
        self.logger.info('3.Save modified project;')
        result3 = self.PROJECT.project_save()

        self.logger.info('Expected results:')
        self.logger.info('1. Save successful;')
        if not result1:
            raise CheckException('1. Save failed;')

        self.logger.info('2. Modify successful;')
        if result2['code'] != 0:
            raise CheckException('2. Modify failed;')

        self.logger.info('3. Save successful;')
        if result3['code'] != 0:
            raise CheckException('3. Save failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject002, self).cleanup()
        self.file_options.remove_file_dir(self.prj_file, is_project=True)
