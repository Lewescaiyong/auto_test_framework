#!/usr/bin/env python

import re
import os

from lib.tools.public.information import Information
from lib.base.framework.smart200_base import Smart200Base
from lib.exceptions.not_found_exception import NotFoundException


class Finder(Smart200Base):
    """Finder class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    def __init__(self):
        super(Finder, self).__init__()
        self.information = Information()

    @staticmethod
    def find(file_path, pattern=r'^test_.*\.py$'):
        """Identifies files in the specified directory.
        Args:
            file_path        type(str)        the path of files needs to be Identifies.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        # record the absolute path to the identified file
        absolute_path = list()
        # record the file_name to the identified file
        file_name = list()

        if not file_path:
            return absolute_path, file_name

        for path, dirs, files in os.walk(file_path):
            for i in files:
                if re.search(pattern, i):
                    file_name.append(i)
                    absolute_path.append(os.path.join(path, i))

        return absolute_path, file_name

    @staticmethod
    def find_by_version(files, version='', version_pattern='', filter_pattern='', is_zip=True):
        """Find the specified version file or latest file.
        Args:
            files                 type(list, tuple)        files name list
            version               type(str)                software version
            version_pattern       type(str)                software version pattern
            filter_pattern        type(str)                filter pattern
            is_zip                type(bool)               is a zip file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-16
        """

        # record the [file <--> version] information
        file_version = dict()

        for i in files:
            if is_zip and '.zip' not in i:
                continue
            if not re.search(filter_pattern, i):
                continue
            searcher = re.search(version_pattern, i)
            if searcher:
                file_version[i] = searcher.group()

        # choice by version
        if not version:
            versions = list(file_version.values())
            versions.sort()
            version = versions[-1]
        for k, v in file_version.items():
            if re.search(version, v):
                return k

        raise NotFoundException('Not package was found.')

    def find_latest_report(self):
        """Find the latest test report file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-24
        """

        local_path = self.information.get_framework_local_path()
        report_path = os.path.join(local_path, 'report')
        files, name = self.find(report_path, '\\d+-\\d+')
        files.sort()
        latest_report = files[-1]

        return latest_report
