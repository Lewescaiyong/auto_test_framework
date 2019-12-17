#!/usr/bin/env python

import time
import threading
from queue import Queue

from lib.log.log import Log
from lib.agent.agent_base import AgentBase
from lib.threads.threads import Threads
from lib.agent.agent_server.producer.producer import Producer
from lib.agent.agent_server.consumer.consumer import Consumer


class AgentServer(AgentBase):
    """The main program of agent server.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """

    def __init__(self):
        super(AgentServer, self).__init__()
        threading.currentThread().logger = Log('agent_server', date_type=1)
        self.task_queue = Queue()
        self.producer = Producer(self.task_queue)
        self.consumer = Consumer(self.task_queue)

    def run(self):
        """Start program
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        self.logger.info('*' * 80)
        self.logger.info('Agent server is running, start processing task...\n')
        # start a thread to update log file
        self.reset_log_file()
        # start a thread to parse task info
        self.producer.run()
        # start a thread to create and execute task
        self.consumer.run()
        # show status of task
        self.show_status()

    def reset_log_file(self):
        """The current process is taking longer to execute and needs to reset log files
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """
        th = Threads(target=self._reset_log_file)
        th.setDaemon(True)
        th.start()

    def _reset_log_file(self):
        """The current process is taking longer to execute and needs to reset log files
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        while True:
            time.sleep(3600)
            self.logger.reset_log_file()

    def show_status(self):
        """Show status of server
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        while True:
            self.logger.info('-' * 50)
            task_info = self.tables['task_records'].query_executing_tasks()

            self.logger.info('There are %s tasks in execution.' % len(task_info))
            for i in task_info:
                self.logger.info('task information: %s.' % str(i))

            self.converter.convert_log_to_html_not_del()
            time.sleep(30)


if __name__ == '__main__':
    AgentServer().run()
