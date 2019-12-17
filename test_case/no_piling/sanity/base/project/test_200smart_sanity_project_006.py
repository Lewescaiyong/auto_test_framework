#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartSanityProject006(CaseMW):
    """Export
    No.: test_200smart_sanity_project_006
    Preconditions:
        1. Open Micro/WIN;  
        2. Open an existed file;
    Step actions:
        1. Export the file;
    Expected results:
        1. Export successful, there is a xx.awl file in exported location;
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
        super(Test200SmartSanityProject006, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. Open an existed file;')
        self.PROJECT.project_open('export_awl.smart')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject006, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Export the file;')
        date_str = self.converter.convert_time_to_str()
        self.export_file = '%s.awl' % date_str
        result1 = self.PROJECT.project_export(export_name=self.export_file)

        self.logger.info('Expected results:')
        self.logger.info('1. Export successful, there is a xx.awl file in exported location;')
        if not result1:
            raise CheckException('1. Export failed, there is not a %s file in exported location;' % self.export_file)

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(Test200SmartSanityProject006, self).cleanup()

        # delete the awl file generated during the test
        self.file_options.remove_file_dir(self.export_file, is_awl=True)
