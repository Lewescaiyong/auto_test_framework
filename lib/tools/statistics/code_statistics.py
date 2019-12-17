#!/usr/bin/env python

import os

from lib.tools.tools_base import ToolsBase


class CodeStatistics(ToolsBase):
    """code statistics.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-26
    """

    def total_lines_statistics(self, statistics_case=False):
        """Remove the file or dir.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-26
        """

        total = 0

        local_path = self.information.get_framework_local_path()
        if not statistics_case:
            statistics_path = os.path.join(local_path, 'lib')
        else:
            statistics_path = local_path

        # find all .py files
        absolute_path, file_name = self.find(statistics_path, '\\.py$')
        # statistics total lines
        for i in absolute_path:
            with open(i, encoding='utf-8') as f:
                data = f.readlines()
                total += len(data)

        return total


if __name__ == '__main__':
    statistics = CodeStatistics()
    print(statistics.total_lines_statistics())

