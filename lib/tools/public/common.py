#!/usr/bin/env python

import os
import re
import sys
import time
import socket
import random
import datetime
from types import MethodType

from importlib import import_module
from lib.tools.public.checker import Checker
from lib.tools.public.information import Information
from lib.base.framework.smart200_base import Smart200Base
from lib.exceptions.connecton_exception import ConnectionException


class Common(Smart200Base):
    """Common function.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-22
    """

    def __init__(self):
        super(Common, self).__init__()
        self.checker = Checker()
        self.information = Information()

    @staticmethod
    def sleep(seconds=1):
        """Sleep some time
        Args:
            seconds         type(int)         sleep time
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        time.sleep(seconds)

    @staticmethod
    def create_socket(ip, port):
        """Create a socket object.
        Args:
            ip                  type(str)           ip address
            port                type(str)           port number
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        reason = "No suitable address family"
        address_info = socket.getaddrinfo(
            ip, port, socket.AF_UNSPEC, socket.SOCK_STREAM
        )
        for family, sock_type, proto, canon_name, sock_address in address_info:
            if sock_type == socket.SOCK_STREAM:
                sock = socket.socket(family, socket.SOCK_STREAM)
                try:
                    sock.connect((ip, port))
                except socket.error as e:
                    reason = str(e)
                else:
                    break
        else:
            raise ConnectionException(
                "Unable to connect to {}: {}".format(ip, reason)
            )

        return sock

    @staticmethod
    def get_random_element(scope=255):
        """Get the random element
        Args:
            scope         type(int, list)         the scope of random
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        if isinstance(scope, int):
            scope = range(1, scope)

        result = random.choice(scope)

        return result

    @staticmethod
    def exit(code=0):
        """Exit
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-07
        """

        sys.exit(code)

    def kill_process(self, name):
        """Kill process
        Args:
            name_re           type(str)           the name of the process
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-08
        """

        while self.checker.process_is_running(name):
            os.system('taskkill /F /IM %s' % name)
            self.sleep(1)

    @staticmethod
    def register_functions(obj, modules):
        """Register functions.
        Args:
            obj                type(object)                  the object used to register functions
            modules            type(list, tuple)             modules information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        for i in modules:
            module = import_module(i)
            for j in module.__dict__:
                if re.search('^__.+__$', j):
                    continue
                func = getattr(module, j)
                if 'function' in str(func) and (func.__code__.co_varnames[0] == 'self'):
                    setattr(obj, j, MethodType(func, obj))
                else:
                    setattr(obj, j, func)

    def wait_task_complete_server(self, report_file):
        """Wait for task completion on server device
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        local_path = self.information.get_framework_local_path()
        report_path = os.path.join(local_path, 'lib', 'agent', 'files', 'report')
        self.logger.info('Wait for task completion...')
        while True:
            time.sleep(40)
            self.logger.info('Check test report....')
            files = os.listdir(report_path)
            if report_file in files:
                self.logger.info('The test report[%s] has been generated.' % report_file)
                self.logger.info('End of CI task execution!')
                break
            self.logger.info('The test report has not been generated, please wait...')

    def wait_report_generate_client(self, start_time):
        """Wait for test report file generated on client device
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-08
        """

        self.logger.info('Wait for test report file generated...')
        local_path = self.information.get_framework_local_path()
        while True:
            files = os.listdir(os.path.join(local_path, 'report'))
            for i in files[::-1]:
                searcher = re.search(r'\d+-\d+-\d+\s+\d+-\d+-\d+', i)
                if not searcher:
                    continue
                time_str = searcher.group()
                file_time = datetime.datetime.strptime(time_str, '%Y-%m-%d %H-%M-%S')
                if file_time > start_time:
                    self.logger.info('Find test report file: %s.' % i)
                    return i
            else:
                self.sleep(5)
