#!/usr/bin/env python

import re

from lib.tools.html.html_parser import HTMLParser


class ReportParser(HTMLParser):
    """Parse the test report.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-04
    """

    def __init__(self):
        super(ReportParser, self).__init__()
        self.html_file = self.find_latest_report()

    def find_latest_report(self):
        """Find the latest test report file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-04
        """

        latest_report = self.finder.find_latest_report()

        return latest_report

    def report_parser(self):
        """Parse report file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-04 create
        """

        result = dict()
        info = self.html_parser()['html']['html']['body']
        result['summary_info'] = self.process_summary_info(info)
        result['cases_info'] = self.process_cases_info(info)

        return result

    @staticmethod
    def process_summary_info(info):
        """Parse summary information.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-05 create
        """

        result = dict()
        for i in info['span']:
            for k, v in i.items():
                value, title = v.split(' ', 1)
                result[title.replace(' ', '_')] = int(value)

        return result

    def process_cases_info(self, info):
        """Parse cases information.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-05 create
        """

        result = dict()
        cases_info = info['table'][1]['tbody']
        if not isinstance(cases_info, list):
            cases_info = [cases_info]
        for i in cases_info:
            case_info = self.process_case_info(i)
            result[case_info['case_id']] = case_info

        return result

    @staticmethod
    def process_case_info(info):
        """Parse case information.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-05 create
        """

        result = {'log_info': info['text']}
        titles = ['result', 'case_id', 'duration', 'start_time']
        for i, v in enumerate(info['tr'][0]['td']):
            result[titles[i]] = v['text']
        if re.search('.*/(.+)\\.py', result['case_id']):
            result['case_id'] = re.search('.*/(.+)\\.py', result['case_id']).group(1)

        return result


if __name__ == '__main__':
    parser = ReportParser()
    parsed_info = parser.report_parser()
    print(parsed_info)
