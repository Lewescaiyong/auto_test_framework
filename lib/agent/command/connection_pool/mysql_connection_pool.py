#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import queue
import threading

from lib.log.log import Log
from lib.agent.command.connection.mysql_connection import MySQLConnection
from lib.tools.single_instance.single_instance import SingleInstance


class MySQLConnectionPool(metaclass=SingleInstance):
    """MySQL Connection pool.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-12
    """

    def __init__(self):
        super(MySQLConnectionPool, self).__init__()
        self.logger = Log
        self.conn_pool = dict()
        self.conn_info = dict()

    def run(self, cmd_info):
        """Execute cmd interface.
        Args:
            cmd_info            type(dict)          command info
            ---------------------------------------------------------
            cmd_info details
            database            type(str)           tha name of the database to be connected
            table_name          type(str)           tha name of the table to be optioned
            cmd                 type(str)           commands to execute
            option              type(str)           enumerate(query, insert, update, delete)
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        database = cmd_info['database']
        table_name = cmd_info['table_name']
        conn = self.get_connection(database, table_name)
        conn.check_is_active()
        try:
            result = getattr(conn, cmd_info['option'])(cmd_info['cmd'])
        finally:
            self.release_connection(database, table_name, conn)

        return result

    def get_connection(self, database, table_name):
        """Get connection object.
        Args:
            database            type(str)           tha name of the database to be connected
            table_name          type(str)           tha name of the table to be optioned
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """
        if database not in self.conn_pool or table_name not in self.conn_pool[database]:
            self.create_connection(database, table_name)

        while True:
            try:
                conn = self.conn_pool[database][table_name].get(timeout=5)
                self.logger.debug('Require the connection of table %s, thread_id: %s.' % (
                    table_name, threading.currentThread().ident))
            except queue.Empty:
                self.logger.debug('The connection of table %s is in use, please wait...' % table_name)
                time.sleep(5)
                continue
            else:
                return conn

    def release_connection(self, database, table_name, conn):
        """Release connection object.
        Args:
            database            type(str)           tha name of the database to be connected
            table_name          type(str)           tha name of the table to be optioned
            conn                type(object)        network connection object
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        if database in self.conn_pool and table_name in self.conn_pool[database]:
            self.conn_pool[database][table_name].put(conn)
            self.logger.debug('Release the connection of [database: %s, table %s], thread_id: %s.' % (
                database, table_name, threading.currentThread().ident))

    def create_connection(self, database, table_name):
        """Get connection object.
        Args:
            database            type(str)           tha name of the database to be connected
            table_name          type(str)           tha name of the table to be optioned
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        que = queue.Queue()
        conn_info = self.conn_info[database]
        if database not in self.conn_pool:
            self.conn_pool[database] = dict() 
        
        for i in range(conn_info.get('max_connections', 1)):
            conn = MySQLConnection(conn_info)
            que.put(conn)

        self.conn_pool[database][table_name] = que
