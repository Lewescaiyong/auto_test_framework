#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from lib.tools.tools_base import ToolsBase
from lib.tools.excel.excel_parser import ExcelParser


class EnvironmentParser(ToolsBase):
    """parse environment_info.xlsx file to dict.
    Args:
    Example:
        parser = EnvironmentParser()
        result = parser.environment_parser()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """

    def __init__(self):
        super(EnvironmentParser, self).__init__()
        self.file_name = ''

    def environment_parser(self):
        """parse excel file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """
        result = dict()
        self.file_name = os.path.join(self.information.get_framework_local_path(), 'lib', 'agent', 'files',
                                      'device_file', 'environment_info.xlsx')
        for sheet in ['IPC', 'PLC']:
            result[sheet] = self.parse(sheet)

        return result

    def parse(self, sheet_name, title_line=0, value_line=1):
        """parse sheet information.
        Args:
            title_line          type(int)           the line id of title
            value_line          type(int)           the line id of first value line
            sheet_name          type(str)           the name of sheet to parse
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        parser = ExcelParser(self.file_name, title_line, value_line, sheet_name=sheet_name)
        result = parser.excel_parser()

        return result


if __name__ == '__main__':
    import pprint

    env_parser = EnvironmentParser()
    pprint.pprint(env_parser.environment_parser())
