#!/usr/bin/env python

import os
import re
import shutil

from lib.tools.tools_base import ToolsBase


class CopyCaseToTask(ToolsBase):
    """Copy the cases that need to be executed into the directory: smart200\test_case\task.
    Args:
        task_type        type(str)        CI task type, enumerate: (smoke, full).
        version          type(str)        version of software
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    def __init__(self, bed_info):
        super(CopyCaseToTask, self).__init__()
        self.bed_info = bed_info
        self.test_type = self.bed_info['GlobalConfig']['TestType']
        self.task_type = self.bed_info['GlobalConfig']['TaskType']
        self.version = self.bed_info['MicroWIN'].get('Version', '')
        self.features = self.bed_info['MicroWIN'].get('Features', '')

    def copy_case(self):
        """Copy the case of path smoke/full into the directory: smart200\test_case\task.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        local_path = self.information.get_framework_local_path()
        target_path = os.path.join(local_path, 'test_case', 'task')
        # find test cases scripts
        need_copy = self.find_case()
        # copy case script into task path
        self.copy(need_copy, target_path)

    def find_case(self):
        """Find all case that need to be copied.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        need_copy = list()
        if self.test_type == 'no_piling':
            need_copy = self.find_case_no_piling()

        return need_copy

    def find_case_no_piling(self):
        """Find all case that need to be copied.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        # find task case
        features = None
        files_name = None
        local_path = self.information.get_framework_local_path()
        if self.task_type == 'sanity':
            task_path = os.path.join(local_path, 'test_case', 'no_piling', 'sanity')
        elif self.task_type == 'sanity_ui':
            task_path = os.path.join(local_path, 'test_case', 'no_piling', 'sanity_ui')
        elif self.task_type == 'upgrade_micro_win':
            task_path = os.path.join(local_path, 'test_case', 'no_piling', 'common')
            files_name = ['test_200smart_common_upgrade_002.py']
        else:
            task_path = os.path.join(local_path, 'test_case', 'no_piling', 'full')
        need_copy = self._find_case(task_path, features, files_name)

        # find common case
        files_name = None
        task_path = os.path.join(local_path, 'test_case', 'no_piling', 'common')
        features = 'information'
        common_cases = self._find_case(task_path, features, files_name)

        return need_copy + common_cases

    def _find_case(self, task_path, features=None, files_name=None):
        """Find all case that need to be copied.
        Args:
            task_path         type(str)                the path of the task.
            features_name     type(str)                the name of the features.
            files_name        type(list, tuple)        the name of the script files.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        if not features:
            features = self.features
        if not files_name:
            files_name = ['']

        if features:
            # find test cases by features
            need_copy = self.find_case_by_features(task_path, features)
        else:
            # find test cases by task
            need_copy = self.find_case_by_task(task_path)

        # filter by file_name
        need_copy = [i for i in need_copy for file_name in files_name if file_name in i]

        return need_copy

    def find_case_by_task(self, task_path):
        """Find all case that need to be copied from task directory.
        Args:
            task_path        type(str)        the path of the task.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        base_case_path = os.path.join(task_path, 'base')
        version_case_path = os.path.join(task_path, 'version', self.version) if self.version else ''

        # identifies all cases in the base_case_path
        b_ibs, b_name = self.finder.find(base_case_path)
        # identifies all cases in the version_case_path
        v_ibs, v_name = self.finder.find(version_case_path)
        need_copy = [i for i in b_ibs if not (v_name and re.search('|'.join(v_name), i))]
        need_copy.extend(v_ibs)

        return need_copy

    def find_case_by_features(self, task_path, features):
        """Find all case that need to be copied from feature directory.
        Args:
            task_path        type(str)            the path of the task.
            features         type(str)            the name of the features.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        need_copy = list()
        features = [i.strip() for i in features.split(',')]
        for feature_name in features:
            need_copy += self.find_case_by_feature(task_path, feature_name)

        return need_copy

    def find_case_by_feature(self, task_path, feature_name):
        """Find all case that need to be copied from feature directory.
        Args:
            task_path        type(str)        the path of the task.
            feature_name     type(str)        the name of the feature.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        base_case_path = os.path.join(task_path, 'base', feature_name)
        version_case_path = os.path.join(task_path, 'version', self.version, feature_name) if self.version else ''

        # identifies all cases in the base_case_path
        b_ibs, b_name = self.finder.find(base_case_path)
        # identifies all cases in the version_case_path
        v_ibs, v_name = self.finder.find(version_case_path)
        need_copy = [i for i in b_ibs if not (v_name and re.search('|'.join(v_name), i))]
        need_copy.extend(v_ibs)

        return need_copy

    @staticmethod
    def copy(case_files, target_path):
        """Copy the case into the directory.
        Args:
            case_files       type(str)        the absolute path of cases needs to be copied.
            target_path      type(str)        the path to execute the test case.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        # clear task_path
        if os.path.exists(target_path):
            shutil.rmtree(target_path)
        os.makedirs(target_path)

        # copy file to directory
        list(map(lambda x: shutil.copy(x, target_path), case_files))
