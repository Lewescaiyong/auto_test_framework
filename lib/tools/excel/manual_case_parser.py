#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from lib.tools.excel.excel_parser import ExcelParser


class ManualCaseParser(ExcelParser):
    """parse test case excel file to dict.
    Args:
        file_name           ype(str)            the absolute_path of xml file
        title_line          type(int)           the line id of title
        value_line          type(int)           the line id of first value line
        sheet_index         type(int)           the index id of sheet to parse
        sheet_name          type(str)           the name of sheet to parse
    Example:
        parser = ManualCaseParser('D:\\Sanity_TestCases.xls', title_line=1, value_line=2)
        result = parser.manual_case_parser()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-18
    """

    def __init__(self, file_name, title_line=0, value_line=1, sheet_index=0, sheet_name=None, for_test_link=False):
        super(ManualCaseParser, self).__init__(file_name, title_line, value_line, sheet_index, sheet_name)
        self.for_test_link = for_test_link

    def manual_case_parser(self):
        """parse case excel file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """
        data = self.excel_parser()
        result = self.process_module_field(data)
        self.add_class_name_field(result)
        self.process_multi_step_field(result)

        return result

    def process_module_field(self, data):
        """Process the "Module" filed.
        Args:
            data          type(dict)           case excel file parse dict
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """

        result = list()

        case_info = data['values']
        # add Module filed
        for i, v in enumerate(case_info):
            if not v['Module']:
                v['Module'] = case_info[i - 1]['Module']
            else:
                module = tuple(self.parser.split(v['Module'].lower(), '\\.'))
                v['Module'] = tuple((re.sub('\\s+', '_', i) for i in module))

        # brush out the test case that need to generate the script
        for i, v in enumerate(case_info):
            if not v['Step actions']:
                continue
            if (v['Execution'].lower() in ('m',)) or (v['Auto status'].lower() in ('y',)):
                if not self.for_test_link:
                    continue
            result.append(v)

        return result

    @staticmethod
    def add_class_name_field(data):
        """Add the "ClassName" filed.
        Args:
            data          type(dict)           case excel file parse dict
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """

        for case in data:
            case_id = case['No.']
            filed_list = case_id.split('_')
            filed_list = list(map(lambda x: x.title(), filed_list))
            case['ClassName'] = ''.join(filed_list)

    def process_multi_step_field(self, data):
        """Process the multi_step filed: "Expected results"/"Step actions"/"Preconditions".
        Args:
            data          type(dict)           case excel file parse dict
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """

        for i in data:
            i['Step actions'] = self.multi_step_field(i['Step actions'])
            i['Expected results'] = self.multi_step_field(i['Expected results'])
            i['Preconditions'] = self.multi_step_field(i['Preconditions'])

    def multi_step_field(self, info):
        """Process the multi_step filed.
        Args:
            info          type(str)           the str info of multi_step filed
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """

        result = list()

        for i, v in enumerate(self.parser.split(info)):
            if re.search(r'^\d+', v):
                result.append(v)
            else:
                result[-1] += ' %s' % v

        return result


if __name__ == '__main__':
    import pprint

    env_parser = ManualCaseParser(r'D:\Full_testcases.xlsx', sheet_index=4, title_line=1, value_line=2)
    pprint.pprint(env_parser.manual_case_parser())
