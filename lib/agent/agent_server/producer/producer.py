#!/usr/bin/env python

import os
from xml.etree.ElementTree import ParseError

from lib.agent.agent_base import AgentBase
from lib.threads.threads import Threads
from lib.tools.xml.xml_parser import XMLParser


class Producer(AgentBase):
    """Task producer.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
    """

    def __init__(self, task_queue):
        super(Producer, self).__init__()
        self.task_queue = task_queue

    def run(self):
        """Produce task
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        th = Threads(target=self.task_parse)
        th.setDaemon(True)
        th.start()

    def task_parse(self):
        """parse task from task file
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        while True:
            local_path = self.information.get_framework_local_path()
            task_path = os.path.join(local_path, 'lib', 'agent', 'files', 'task_file')
            task_files = os.listdir(task_path)
            for task_file in task_files:
                if '.xml' not in task_file:
                    continue
                try:
                    parser_info = XMLParser(os.path.join(task_path, task_file)).xml_parser()
                except ParseError:
                    continue
                task_info = parser_info['Task']['Info']
                self.logger.info('****task_producer****\n receive task: %s' % task_info)
                self.task_queue.put(task_info)
                self.tables['task_records'].generate_task_record(task_info)
                os.remove(os.path.join(task_path, task_file))
