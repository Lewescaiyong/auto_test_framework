#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.command.command_base import CommandBase
from lib.agent.command.connection_pool.mysql_connection_pool import MySQLConnectionPool
from lib.agent.command.connection_pool.device_connection_pool import DeviceConnectionPool


class HostBase(CommandBase):
    """Command's base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-11
    """

    def __init__(self, params):
        super(HostBase, self).__init__()
        self.params = params
        self.conn_pool = None
        self.create_connection_pool()

    def run(self, cmd_info):
        """Execute cmd.
        Args:
            cmd_info         type(dict)          commands information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        result = self.conn_pool.run(cmd_info)

        return result

    def create_connection_pool(self):
        """Create connection pool.
        Args:
            params              type(dict)          connection information
            ---------------------------------------------------------
            params details
            protocol            type(str)           network connection protocol
            conn_info           type(str)           connection information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        pool = None

        protocol = self.params['protocol']
        if protocol == 'mysql':
            pool = MySQLConnectionPool()
            database = self.params['database']
            pool.conn_info[database] = self.params['conn_info']
        elif protocol == 'telnet':
            pool = DeviceConnectionPool(self.params['conn_info'])

        self.conn_pool = pool
