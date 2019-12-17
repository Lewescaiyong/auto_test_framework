#!/usr/bin/env python

import re
import os

from lib.tools.public.information import Information
from lib.base.framework.smart200_base import Smart200Base


class Parser(Smart200Base):
    """Parser class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    def __init__(self):
        super(Parser, self).__init__()
        self.information = Information()

    @staticmethod
    def split(info, pattern='\x0a?\x0d|\x0a'):
        """Split by line
        Args:
            info        type(str)        information that needs to be split.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        result = re.split(pattern, info)
        result = [i.strip() for i in result]

        return result

    def parse_data_log(self, log_file='', log_path='', is_desc=False):
        """Parse data log
        Args:
            log_file         type(str)        data log file name.
            log_path         type(str)        data log file path.
            is_desc          type(bool)       whether the number recorded is decreasing
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-09
        """

        def get_the_user_defined(a_line):
            # get the user defined filed
            elements = a_line.strip().split(',')[2:-1]
            # remove the blank space
            elements = [element.strip() for element in elements]
            elements = [int(element) if element.isdigit() else element for element in elements]

            return elements

        def check(current, previous):
            # check if the number changes in the two lines of information are normal
            check_result = True
            current_number = get_the_user_defined(current)
            previous_number = get_the_user_defined(previous)
            for index, value in enumerate(current_number):
                if is_desc:
                    if value != previous_number[index] + 1 and not (previous_number[index] == 0 and value == 65535):
                        check_result = False
                        break
                else:
                    if value != previous_number[index] - 1 and not (previous_number[index] == 0 and value == 65535):
                        check_result = False
                        break

            return check_result

        result = {'check_result': True, 'abnormal_lines': list(), 'abnormal_number': 0, 'data_log_file': ''}

        # search below /lib/resource/data_log by default
        if not log_path:
            local_path = self.information.get_resource_path()
            log_path = os.path.join(local_path, 'data_log')

        # automatically find the name of the data log file
        if not log_file:
            for i in os.listdir(log_path):
                if re.search('Data Log.+\\.csv', i):
                    log_file = i
                    break

        # get the abspath of the data log file
        log_file = os.path.join(log_path, log_file)

        if os.path.isdir(log_file) or (not os.path.exists(log_file)):
            result['check_result'] = False
            self.logger.info('Data log file not found.')
            return result

        result['data_log_file'] = log_file
        with open(log_file) as f:
            previous_line = None
            for line in f:
                # skip the title line
                if re.search('Date,Time,|Missing resource', line):
                    continue

                # skip the first recorded line
                if not previous_line:
                    previous_line = line
                    continue

                if not check(line, previous_line):
                    result['check_result'] = False
                    result['abnormal_number'] += 1
                    result['abnormal_lines'].append([line, previous_line])

                previous_line = line

        return result

    @staticmethod
    def parse_upgrade_result(info):
        """Parse upgrade result
        Args:
            info         type(str)        log information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-06 create
        """

        result = False

        searcher = re.search('Upgrade result: True', info, re.I)
        if searcher:
            result = True

        return result
