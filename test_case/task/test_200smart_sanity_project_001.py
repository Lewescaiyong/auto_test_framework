#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityProject001(CaseMW):
    """New file
    No.: test_200smart_sanity_project_001
    Preconditions:
        1. Open Micro/WIN;
    Step actions:
        1. Create a new file;
    Expected results:
        1. Create successful;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-09-20 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityProject001, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityProject001, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Create a new file;')
        time_str = self.converter.convert_time_to_str()
        self.prj_file = 'new_%s.smart' % time_str
        self.PROJECT.project_new('self.prj_file')
        result = self.PROJECT.project_save_as(self.prj_file)

        self.logger.info('Expected results:')
        self.logger.info('1. Create successful;')
        if not result:
            raise CheckException('1. Create failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(Test200SmartSanityProject001, self).cleanup()
        self.file_options.remove_file_dir(self.prj_file, is_project=True)
