#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityProject003(CaseMW):
    """Save as
    No.: test_200smart_sanity_project_003
    Preconditions:
        1. Open Micro/WIN;  
        2. Open an existed file;
    Step actions:
        1. Use "Save as" to save  project;
    Expected results:
        1. Save as successful;
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
        super(Test200SmartSanityProject003, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. Open an existed file;')
        self.PROJECT.project_open('always_outputQ00.smart')
        self.save_as_file = 'always_outputQ00_save_as.smart'

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject003, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Use "Save as" to save  project;')
        result1 = self.PROJECT.project_save_as(self.save_as_file)

        self.logger.info('Expected results:')
        self.logger.info('1. Save as successful;')
        if not result1:
            raise CheckException('2. Save as failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject003, self).cleanup()

        # delete the project file generated during the test
        self.file_options.remove_file_dir(self.save_as_file, is_project=True)
