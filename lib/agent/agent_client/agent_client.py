#!/usr/bin/env python

import os
import time
import threading
from xml.etree.ElementTree import ParseError

from lib.log.log import Log
from lib.threads.threads import Threads
from lib.tools.xml.xml_parser import XMLParser
from lib.base.framework.no_interface.no_interface import NoInterface


class AgentClient(NoInterface):
    """The main program of agent client.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-07
    """

    def __init__(self):
        super(AgentClient, self).__init__()
        threading.currentThread().logger = Log('agent_client', date_type=1)

    def run(self):
        """Start program
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-07
        """

        self.logger.info('*' * 80)
        self.logger.info('Agent client start running...\n')
        # start a thread to update log file
        self.reset_log_file()
        # monitor task start
        self.start_task()

    def reset_log_file(self):
        """The current process is taking longer to execute and needs to reset log files
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-07
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
        ChangeInfo: cai, yong 2019-11-07
        """

        while True:
            time.sleep(3600)
            self.logger.reset_log_file()

    def start_task(self):
        """Start task
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-07
        """

        while True:
            self.logger.info('*' * 80)
            self.logger.info('Wait for starting CI task...')
            self.is_need_start()
            local_path = self.information.get_framework_local_path()
            file_path = os.path.join(local_path, 'lib', 'automation_script.py')
            self.logger.info('Starting task.')
            os.system('python %s' % file_path)

    def is_need_start(self):
        """Is need to start task
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-07
        """

        files_path = self.information.get_agent_files_path()
        file_name = os.path.join(files_path, 'server_client', 'need_start.xml')

        while True:
            time.sleep(5)
            try:
                info = XMLParser(file_name).xml_parser()
            except (ParseError, FileNotFoundError):
                continue
            else:
                need_start = info['NeedStart']['Info']['NeedStart']
                if need_start.lower() == 'yes':
                    self.xml_options.update_need_start(need_start='no')
                    return True


if __name__ == '__main__':
    AgentClient().run()
