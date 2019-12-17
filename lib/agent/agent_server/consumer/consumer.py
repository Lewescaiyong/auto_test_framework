#!/usr/bin/env python

import datetime
import threading

from lib.log.log import Log
from lib.agent.agent_base import AgentBase
from lib.threads.threads import Threads
from lib.agent.task.task_normal import TaskNormal
from lib.agent.task.task_upgrade_micro_win import TaskUpgradeMicroWIN


class Consumer(AgentBase):
    """Task consumer.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
    """

    def __init__(self, task_queue):
        super(Consumer, self).__init__()
        self.task_queue = task_queue

    def run(self):
        """Consume task
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        th = Threads(target=self.task_create)
        th.setDaemon(True)
        th.start()

    def task_create(self):
        """continue to create task
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        while True:
            task_info = self.task_queue.get()
            self.tables['task_records'].update_task_record(task_info)
            self.logger.info('****task_consumer****\n start processing task: %s' % task_info)
            th = Threads(target=self.task_manager, args=(task_info,))
            th.setDaemon(True)
            th.start()

    def task_manager(self, task_info):
        """manage task
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        # set logger object for current thread
        date = datetime.datetime.now().strftime("%H%M%S")
        threading.currentThread().logger = Log('task_%s_%s' % (task_info['TaskType'], date), date_type=1)

        # create task
        if task_info['TaskType'] in ('sanity_ui',):
            task = TaskUpgradeMicroWIN(task_info)
        else:
            task = TaskNormal(task_info)

        # execute task
        task.execute()
        self.tables['task_records'].update_task_record(task_info, True)
        self.converter.convert_log_to_html(log_files=(self.information.get_current_thread_log_file(),))
