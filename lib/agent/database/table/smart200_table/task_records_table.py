#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.database.table.smart200_table.smart200_table_base import Smart200TableBase


class TaskRecordsTable(Smart200TableBase):
    """Table task_records in smart200 database .
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-11
    """

    @property
    def name(self):
        """Database name
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return 'task_records'

    def generate_task_record(self, task_info):
        """Generate task record.
        Args:
            task_info         type(dict)          task info
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        test_type = task_info['TestType']
        task_type = task_info['TaskType']
        report_file = task_info['ReportFile']

        cmd = "insert into task_records (test_type, task_type, status, report_file, generated_time) values " \
              "('%s', '%s', '%s', '%s', %s);" % (test_type, task_type, 'generated', report_file, 'now()')

        self.run(cmd, 'insert')

    def update_task_record(self, task_info, is_complete=False):
        """Update task record.
        Args:
            task_info         type(dict)          task info
            is_complete       type(bool)          is it the end of the task
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        task_type = task_info['TaskType']
        report_file = task_info['ReportFile']

        if is_complete:
            cmd = "update task_records set status='completed', completion_time=now() where report_file='%s'" \
                  % report_file
        else:
            cmd = "update task_records set status='executing', executed_time=now() where task_type='%s' and " \
                  "report_file='%s'" % (task_type, report_file)

        self.run(cmd, 'update')

    def query_executing_tasks(self):
        """Query executing tasks.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        cmd = "select * from task_records where status != 'completed';"

        result = self.run(cmd, 'query')

        return result
