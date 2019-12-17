#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityProject007(CaseMW):
    """Import
    No.: test_200smart_sanity_project_007
    Preconditions:
        1. Open Micro/WIN;  
        2. Open an existed file;
        3. Export the file;
    Step actions:
        1. New a file, and then import the file in step2;
    Expected results:
        1. Import successful;
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
        super(Test200SmartSanityProject007, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. Open an existed file;')
        self.PROJECT.project_open('export_awl.smart')

        self.logger.info('3. Export the file;')
        date_str = self.converter.convert_time_to_str()
        self.export_file = '%s.awl' % date_str
        self.PROJECT.project_export(export_name=self.export_file)
        self.import_file = self.export_file

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject007, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. New a file, and then import the file in step2;')
        result1 = self.PROJECT.project_import(import_name=self.import_file)

        self.logger.info('Expected results:')
        self.logger.info('1. Import successful;')
        if result1['code'] != 0:
            raise CheckException('1. Import failed.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject007, self).cleanup()

        # delete the awl file generated during the test
        self.file_options.remove_file_dir(self.export_file, is_awl=True)
