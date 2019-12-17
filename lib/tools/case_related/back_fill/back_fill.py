#!/usr/bin/env python

from lib.tools.tools_base import ToolsBase
from lib.tools.case_related.back_fill.my_test_link import MyTestLink
from lib.tools.case_related.back_fill.report_parser import ReportParser


class BackFill(ToolsBase):
    """Back fill test result.
    Args:
        task_type           type(str)            task type: sanity, full
        mw_version          type(str)            Micro/WIN interface version information
        cpu_version         type(str)            PLC information
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-13 create
    """

    def __init__(self, task_type, build_description=''):
        super(BackFill, self).__init__()
        self.task_type = task_type
        self.build_description = build_description
        self.test_link = MyTestLink(self.task_type)
        self.parser = ReportParser()

    def back_fill(self):
        """Back fill all test cases results.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        # login
        self.test_link.login()
        # create test build
        if isinstance(self.build_description, dict):
            build_description = ''
            for k, v in self.build_description.items():
                build_description += '%s: %s; ' % (k, v)
        elif isinstance(self.build_description, list):
            build_description = '|'.join(self.build_description)
        else:
            build_description = str(self.build_description)
        build = self.test_link.create_build(build_description=build_description)
        # get test report information
        cases_info = self.parser.report_parser()['cases_info']
        # back fill
        for k, v in cases_info.items():
            result = 'p' if v['result'].lower().startswith('p') else 'f'
            self.test_link.back_fill_single(k, result, build['id'])
        # logout
        self.test_link.close()
