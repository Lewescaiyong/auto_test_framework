#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import queue
import threading

from lib.agent.command.command_base import CommandBase
from lib.agent.command.connection.telnet_connection import TelnetConnection


class ConnectionPoolBase(CommandBase):
    """Connection pool base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
    """

    def __init__(self, params):
        super(ConnectionPoolBase, self).__init__()
        self.conn_pool = dict()
        self.conn_info = params
        self.max_connections = params.get('max_connections', 1)

    def run(self, cmd_info):
        """Execute cmd interface.
        Args:
            cmd_info            type(dict)          command info
            ---------------------------------------------------------
            cmd_info details
            cmd                 type(str)           commands to execute
            directory           type(str)           the path of the commands executed
            timeout             type(str)           the time of timeout
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        conn_info = self.conn_info
        conn = self.get_connection(conn_info)
        conn.check_is_active()
        try:
            result = conn.cmd(cmd_info)
        finally:
            self.release_connection(conn, conn_info)

        return result

    def get_connection(self, conn_info):
        """Get connection object.
        Args:
            conn_info        type(dict)         connection information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """
        user_name = conn_info['user']
        if user_name not in self.conn_pool:
            self.create_connection(conn_info)

        while True:
            try:
                conn = self.conn_pool[user_name].get(timeout=5)
                self.logger.debug('Require the connection of user: %s, thread_id: %s.' % (
                    user_name, threading.currentThread().ident))
            except queue.Empty:
                self.logger.debug('The connection of user %s is in use, please wait...' % user_name)
                time.sleep(5)
                continue
            else:
                return conn

    def release_connection(self, conn, conn_info):
        """Release connection object.
        Args:
            conn                type(object)        network connection object
            conn_info           type(dict)         connection information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        user_name = conn_info['user']

        if user_name in self.conn_pool:
            self.conn_pool[user_name].put(conn)
            self.logger.debug('Release the connection of user: %s, thread_id: %s.' % (
                user_name, threading.currentThread().ident))

    def create_connection(self, conn_info):
        """Get connection object.
        Args:
            conn_info        type(dict)         connection information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        user_name = conn_info['user']
        que = queue.Queue()
        for i in range(self.max_connections):
            conn = TelnetConnection(conn_info)
            que.put(conn)

        self.conn_pool[user_name] = que

    def reset(self):
        """reset connections.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        self.conn_pool = dict()
        self.send_first_cmd()

    def send_first_cmd(self):
        """reset connections.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        self.run(({'command': ''}))
