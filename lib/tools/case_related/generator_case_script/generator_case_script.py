#!/usr/bin/env python

import os
import re
import datetime

from lib.tools.tools_base import ToolsBase
from lib.tools.excel.manual_case_parser import ManualCaseParser
from lib.tools.generator_by_template.generator_by_template import GeneratorByTemplate


class GeneratorCaseScript(ToolsBase):
    """Analyze the test case information in the excel file and generate the test case script automatically.
    Args:
        case_file           type(str)          the abspath of test case excel file
        template            type(str)          the path of test case script template file
    Example:
        generator = GeneratorCaseScript(excel_file=r'C:\test_case.xls')
        generator.generator_case_script()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-18
    """

    def __init__(self, author, case_file, template='case_template.txt', title_line=1, value_line=2, sheet_index=0,
                 sheet_name=None):
        super(GeneratorCaseScript, self).__init__()
        self.author = author
        self.case_file = case_file
        self.template = template
        self.title_line = title_line
        self.value_line = value_line
        self.sheet_index = sheet_index
        self.sheet_name = sheet_name
        self.script_path = ''

    def generator_case_script(self):
        """Generate the test case script.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        # dynamic calculation script_path path
        local_path = self.information.get_framework_local_path()
        self.script_path = os.path.join(local_path, 'lib', 'tools', 'case_related', 'generator_case_script', 'scripts')
        if not re.search(':', self.template):
            self.template = os.path.join(
                local_path, 'lib', 'tools', 'case_related', 'generator_case_script', self.template)

        parser = ManualCaseParser(self.case_file, title_line=self.title_line, value_line=self.value_line,
                                  sheet_index=self.sheet_index, sheet_name=self.sheet_name)
        data = parser.manual_case_parser()
        for case in data:
            self.generator(case)

    def generator(self, case_info):
        """Generate the test case script.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        file_path = os.path.join(self.script_path, *case_info['Module'])
        file_abspath = os.path.join(file_path, '%s.py' % case_info['No.'])

        params = dict()
        params['date'] = datetime.datetime.now().strftime('%Y-%m-%d')
        params['Author'] = self.author
        params['case_info'] = case_info

        gen = GeneratorByTemplate(template=self.template, file_abspath=file_abspath)
        gen.generator(params)


if __name__ == '__main__':
    generator = GeneratorCaseScript(author='Cai, Yong', case_file=r'D:\Full_testcases.xlsx', sheet_index=3)
    generator.generator_case_script()
