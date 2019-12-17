#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

from lib.agent.command.connection.connection_base import ConnectionBase


class MySQLConnection(ConnectionBase):
    """MySQL connection class.
    Args:
        connect_info        type(dict)         connection information
        --------------------------------------------------
        connect_info details
        ip                  type(str)           ip address
        user                type(str)           username
        password            type(str)           password
        port                type(str)           port number
    Example:
        connect_info = {'ip': '127.127.0.1', 'user': 'admin', 'password': '123456'}
        conn = MySQLConnection(connect_info)
        conn.login()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-10
    """

    def __init__(self, connect_info):
        super(MySQLConnection, self).__init__()
        self.ip = connect_info['ip']
        self.user = connect_info['user']
        self.password = connect_info['password']
        self.port = connect_info.get('port', 3306)
        self.database = connect_info['database']
        self.charset = connect_info.get('charset', 'utf8')
        self.conn = None
        self.cursor = None

    def login(self):
        """Login.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """
        self.conn = pymysql.connect(host=self.ip, user=self.user, password=self.password, port=self.port,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()
        self.use_database()

    def close(self):
        """Logout.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        if self.conn:
            if self.cursor:
                self.cursor.close()
            self.conn.close()

        self.cursor = None
        self.conn = None

    def reconnect(self):
        """Login again.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        self.close()
        self.login()

    def is_active(self):
        """Get connection status.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        try:
            self.query('show databases;')
        except (pymysql.MySQLError, AttributeError):
            return False

        return True

    def use_database(self):
        """Use database.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        cmd = 'use %s;' % self.database
        self.execute(cmd)

    def query(self, cmd):
        """Query the data from the database.
        Args:
            cmd         type(str)          commands for querying data
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        self.execute(cmd)
        data = self.cursor.fetchall()
        self.logger.debug('Receive: \n %s' % str(data))

        return data

    def insert(self, cmd):
        """Insert the data into the database.
        Args:
            cmd         type(str)          commands for inserting data
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        self.execute(cmd)
        self.conn.commit()

    def update(self, cmd):
        """update the data in the database.
        Args:
            cmd         type(str)          commands for updating data
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        self.execute(cmd)
        self.conn.commit()

    def delete(self, cmd):
        """delete the data in the database.
        Args:
            cmd         type(str)          commands for deleting data
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        self.execute(cmd)
        self.conn.commit()

    def execute(self, cmd):
        """Executing the command in the database.
        Args:
            cmd         type(str)          commands to execute
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        self.logger.debug('execute cmd: [%s].' % cmd)
        for i in range(3):
            try:
                self.cursor.execute(cmd)
            except pymysql.MySQLError:
                self.reconnect()
            else:
                break
