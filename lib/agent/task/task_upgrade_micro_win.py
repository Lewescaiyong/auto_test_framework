#!/usr/bin/env python

import copy

from lib.agent.task.task_base import TaskBase


class TaskUpgradeMicroWIN(TaskBase):
    """Parent class for Task.
    Args:
        task_info        type(dict)       task information
        --------------------------------------------------------
        task_info details:
        TaskType         type(str)        CI task type, enumerate: (smoke, full).
        PLCNumber        type(int)        the number of plc need to be tested.
        ReportFile       type(int)        the report file name of this task.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """

    def __init__(self, task_info):
        super(TaskUpgradeMicroWIN, self).__init__(task_info)

    def prepare_steps(self):
        """The preparation steps
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        # upgrade micro win
        self.upgrade_micro_win()

    def upgrade_micro_win(self):
        """The preparation steps
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        # generate test_bed.xml file
        task_info = copy.deepcopy(self.task_info)
        task_info['TaskType'] = 'upgrade_micro_win'
        task_info['ReportFile'] = ''
        self.generator_test_bed_file(plc_ip=tuple(), task_info=task_info)
        # copy the file to IPC device
        self.ipc_device.upload_test_bed_file(self.test_bed_path, self.test_bed_file)
        # start task on IPC device
        self.ipc_device.start_task()
        # wait for all IPC task completion
        self.ipc_device.wait_upgrade_complete()


if __name__ == '__main__':
    info = {'TaskType': 'sanity', 'PLCNumber': '1', 'ReportFile': 'test_report.html'}
    task = TaskUpgradeMicroWIN(info)
    task.execute()
