#!/usr/bin/env python

import os

from lib.tools.tools_base import ToolsBase
from lib.tools.xml.xml_generator import XMLGenerator
from lib.tools.excel.manual_case_parser import ManualCaseParser


class ConvertToXML(ToolsBase):
    """Copy the cases that need to be executed into the directory: smart200\test_case\task.
    Args:
        file_name           type(str)           the absolute_path of xml file
        suite_name          type(str)           the name of the suite on test link
        title_line          type(int)           the line id of title
        value_line          type(int)           the line id of first value line
        sheet_index         type(int)           the index id of sheet to parse
        sheet_name          type(str)           the name of sheet to parse
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    def __init__(self, case_file, suite_name, title_line=1, value_line=2, sheet_index=0, sheet_name=None,
                 add_base_suite=True):
        super(ConvertToXML, self).__init__()
        self.case_file = case_file
        self.suite_name = suite_name
        self.title_line = title_line
        self.value_line = value_line
        self.sheet_index = sheet_index
        self.sheet_name = sheet_name
        self.add_base_suite = add_base_suite

    @property
    def priority(self):
        """Priority config.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-14 create
        """

        config = {
            'h': '3',
            'm': '2',
            'l': '1'
        }

        return config

    @property
    def execution_type(self):
        """Execution type config.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-14 create
        """

        config = {
            'a': '2',
            'm': '1'
        }

        return config

    def convert_to_xml(self):
        """Convert to xml file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        # dynamic calculation xml_file path
        local_path = self.information.get_framework_local_path()
        xml_path = os.path.join(local_path, 'lib', 'tools', 'case_related', 'convert_to_xml', 'xml_file')
        data = self.get_xml_data()
        self.convert(data, os.path.join(xml_path, '%s.xml' % self.suite_name))

    def get_xml_data(self):
        """Process cases data for test link import.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        # get cases data
        data = self.get_cases_data()
        # convert to xml data
        result = self.get_xml_template()
        if self.add_base_suite:
            result['testsuite']['testsuite']['testsuite'] = self._get_xml_data(data)
        else:
            result['testsuite']['testsuite'] = self._get_xml_data(data)

        return result

    def get_cases_data(self):
        """Get cases data for test link import.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-14
        """

        result = dict()
        # get cases data
        parser = ManualCaseParser(self.case_file, title_line=self.title_line, value_line=self.value_line,
                                  sheet_index=self.sheet_index, sheet_name=self.sheet_name, for_test_link=True)
        data = parser.manual_case_parser()
        for case in data:
            current = None
            feature = None
            for index, feature in enumerate(case['Module']):
                current = result
                for i in case['Module'][:index]:
                    current = current[i]
                if feature not in current:
                    current[feature] = dict()
            if 'cases' not in current[feature]:
                current[feature]['cases'] = list()
            current[feature]['cases'].append(case)

        return result

    def _get_xml_data(self, data):
        """Process cases data for test link import.
        Args:
            data           type(dict)           test cases information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        result = None

        for k, v in data.items():
            parent_suite = dict()
            parent_suite['name'] = k
            parent_suite['details'] = {'text': '<p>This is a test suite for %s feature.</p>' % k}
            for key, value in v.items():
                if key == 'cases':
                    # process all test cases
                    for case in value:
                        execution_type = self.execution_type.get(case['Execution'].lower(), '1')
                        case_info = {
                            'name': case['No.'],
                            'summary': {'text': '<p>%s</p>' % case['Description']},
                            'preconditions': {'text': '<p>%s</p>' % '<br />\n'.join(case['Preconditions'])},
                            'execution_type': {'text': execution_type},
                            'importance': {'text': '%s' % self.priority.get(case['Priority'].lower(), '3')},
                            'status': {'text': '7'},
                            'is_open': {'text': '1'},
                            'active': {'text': '1'},
                            'steps': dict(),
                        }
                        # process all test steps of current test case
                        if len(case['Step actions']) != len(case['Expected results']):
                            self.logger.debug('Case name: %s' % case['No.'])
                            self.logger.debug('Step actions: %s' % case['Step actions'])
                            self.logger.debug('Expected results: %s' % case['Expected results'])
                        for index, step in enumerate(case['Step actions']):
                            step_info = {
                                'step_number': {'text': step[0] if step[0].isdigit() else '1'},
                                'actions': {'text': '<p>%s</p>' % step[2:].strip() if step[0].isdigit() else step},
                                'expectedresults': {'text': '<p>%s</p>' % case['Expected results'][index][2:].strip() if
                                                    step[0].isdigit() else case['Expected results'][index]},
                                'execution_type': {'text': execution_type}
                            }
                            if 'step' in case_info['steps']:
                                if isinstance(case_info['steps']['step'], dict):
                                    case_info['steps']['step'] = [case_info['steps']['step']]
                                case_info['steps']['step'].append(step_info)
                            else:
                                case_info['steps']['step'] = step_info

                        if 'testcase' in parent_suite:
                            if isinstance(parent_suite['testcase'], dict):
                                parent_suite['testcase'] = [parent_suite['testcase']]
                            parent_suite['testcase'].append(case_info)
                        else:
                            parent_suite['testcase'] = case_info
                else:
                    child_suit = self._get_xml_data(value)
                    if 'testsuite' in parent_suite:
                        if isinstance(parent_suite['testsuite'], dict):
                            parent_suite['testsuite'] = [parent_suite['testsuite']]
                        parent_suite['testsuite'].append(child_suit)
                    else:
                        parent_suite['testsuite'] = child_suit
            if result:
                if isinstance(result, dict):
                    result = [result]
                result.append(parent_suite)
            else:
                result = parent_suite

        return result

    def get_xml_template(self):
        """Get xml template.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-18 create
        """

        if self.add_base_suite:
            template = {
                'testsuite': {
                    'name': self.suite_name,
                    'details': {'text': '<p>This is a test suite for %s test.</p>' % self.suite_name},
                    'testsuite': {
                        'name': 'base',
                        'details': {'text': '<p>This is a test suite for storing basic test cases.</p>'},
                        'testsuite': dict() or list()
                    }
                }
            }
        else:
            template = {
                'testsuite': {
                    'name': self.suite_name,
                    'details': {'text': '<p>This is a test suite for %s test.</p>' % self.suite_name},
                    'testsuite': dict() or list()
                }
            }

        return template

    @staticmethod
    def convert(info, file_name):
        """Generate the test case script.
        Args:
            info              type(dict)         xml file data
            file_name         type(str)          the name of xml file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        generator = XMLGenerator(file_name)
        generator.xml_generator(info)


if __name__ == '__main__':
    converter = ConvertToXML(case_file=r'D:\Sanity.xlsx', suite_name='sanity', sheet_index=2)
    converter.convert_to_xml()
