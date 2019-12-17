#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json
import shutil

from lib.log.log import Log


class TxtToHtml(object):
    """Convert TXT log file to HTML file.
    Args:
        log_path         type(str)        directory of TXT log file.
        log_files        type(tuple)      files to be converted to html.
        is_del           type(bool)       whether to delete the txt file after converted
        ignore           type(tuple)      files to ignore.
        template_file    type(str)        template of HTML file.
    Example:
        converter = TxtToHtml(log_path='D:\\Project\\smart200\\lib\\log\\logs\2019_08_20_10_35_10')
        converter.txt_to_html()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    def __init__(self, log_path, log_files=(), is_del=True,
                 ignore=('agent_server.txt', 'initialize.txt', 'agent_client.txt'), template_file=''):
        super(TxtToHtml, self).__init__()
        self.local_path = ''
        self.log_path = log_path
        self.log_files = log_files
        self.is_del = is_del
        self.ignore = ignore
        self.template_file = template_file
        self.init_config()

    def txt_to_html(self):
        """Convert TXT log file to HTML file.
        Args:
            ignore         type(tuple)           files to ignore.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """
        self.copy_static_file()
        txt_files = self.log_files or self.get_txt_files()
        for i in txt_files:
            if i in self.ignore and i not in self.log_files:
                continue
            data = self.parse_txt_file(i)
            self.convert_to_html(i, data)

    def copy_static_file(self):
        """Copy the static file to the log folder.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        for i in os.listdir(self.log_path):
            if os.path.isdir(os.path.join(self.log_path, i)) and i == 'static':
                return

        src = os.path.join(self.local_path, 'static')
        dst = os.path.join(self.log_path, 'static')
        shutil.copytree(src, dst)

    def get_txt_files(self):
        """Get txt files.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        files = [i for i in os.listdir(self.log_path) if i.endswith('txt')]

        return files

    def parse_txt_file(self, txt_file):
        """Parse txt log file.
        Args:
            txt_file         type(str)           abspath of the txt file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        log_data = list()
        execute_result = 'Pass'
        with open(os.path.join(self.log_path, txt_file), encoding='utf-8') as f:
            for line in f:
                if re.search(r'-ERROR]:\s', line):
                    execute_result = 'Failed'
                searcher = re.search(r'\[(\d+-\d+-\d+ \d+:\d+:\d+,\d+)-(\d+)-(\w+)]:\s*(.*)', line)
                if searcher:
                    data = {
                        'Date': searcher.group(1),
                        'ThreadId': searcher.group(2),
                        'Level': searcher.group(3),
                        'Detail': [searcher.group(4)],
                    }
                    log_data.append(data)
                else:
                    log_data[-1]['Detail'].append(line)

        # merge the log contents into strings
        for i in log_data:
            # handing exception characters
            for index, line in enumerate(i['Detail']):
                for m, n in (('<', '('), ('>', ')')):
                    line = re.sub(m, n, line)
                i['Detail'][index] = line
            i['Detail'] = '<br>'.join(i['Detail'])

        return {'log_data': log_data, 'execute_result': execute_result}

    def convert_to_html(self, txt_file, data):
        """convert to html file.
        Args:
            txt_file         type(str)           name of the txt file
            data             type(dict)          txt file parse result
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        output_file = os.path.join(self.log_path, '%s.html' % txt_file.split('.txt')[0])
        with open(self.template_file) as f:
            template = f.read()
        with open(output_file, 'w') as f:
            new_html = template.replace('{log_data}', json.dumps(data['log_data']))
            new_html = new_html.replace('{execute_result}', data['execute_result'])
            f.write(new_html)

        if self.is_del:
            Log.release_log_file()
            os.remove(os.path.join(self.log_path, txt_file))

    def init_config(self):
        """initialize config.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """
        self.local_path = os.path.dirname(__file__)
        if not self.template_file:
            self.template_file = os.path.join(self.local_path, 'template.html')


if __name__ == '__main__':
    converter = TxtToHtml(log_path=r'D:\Project\smart200\lib\log\logs\2019_08_21_16_23_08')
    converter.txt_to_html()
