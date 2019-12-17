#!/usr/bin/env python

from lib.agent.task.task_base import TaskBase


class TaskNormal(TaskBase):
    """Normal Task class.
    Args:
        task_info        type(dict)       task information
        --------------------------------------------------------
        task_info details:
        TaskType         type(str)        CI task type, enumerate: (smoke, full).
        PLCNumber        type(int)        the number of plc need to be tested.
        ReportFile       type(int)        the report file name of this task.
        PLCVersion       type(int)        the version of plc to test.
        MicroWINVersion  type(int)        the version of micro win to test.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """


if __name__ == '__main__':
    info = {'TaskType': 'smoke', 'PLCNumber': '1', 'ReportFile': 'test_report.html'}
    task = TaskNormal(info)
    task.execute()
