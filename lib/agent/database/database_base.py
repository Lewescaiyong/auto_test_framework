#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.command.host.mysql_host import MySQLHost
from lib.base.framework.has_interface.has_interface import HasInterface


class DatabaseBase(HasInterface):
    """Database base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
    """

    def __init__(self):
        super(DatabaseBase, self).__init__()
        self.host = None
        self.tables = dict()
        self.register_tables()
        self.create_host()

    def run(self, cmd, option, table_name):
        """Execute cmd.
        Args:
            cmd         type(str)          commands to execute
            option      type(str)          enumerate(query, insert, update, delete)
            table_name  type(str)          the name of the table
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        cmd_info = {'cmd': cmd, 'option': option, 'table_name': table_name, 'database': self.name}
        result = self.host.run(cmd_info)

        return result

    @property
    def name(self):
        """Database name
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return 'database_base'

    @property
    def conn_info(self):
        """Connection information
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return dict()

    @property
    def protocol(self):
        """Database name
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return 'mysql'

    def register_tables(self):
        """Create
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        tables = self.table_config
        self.tables = {i: tables[i](self) for i in tables}

    @property
    def table_config(self):
        """Table config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return dict()

    def create_host(self):
        """Create connection pool.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        params = {
            'protocol': self.protocol,
            'database': self.name,
            'conn_info': self.conn_info
        }

        self.host = self.host_class(params)

    @property
    def host_class(self):
        """Host class
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return MySQLHost

    def find(self, table_name):
        """Get registered business by business type
        Args:
            table_name        type(str)          the name of the table
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        table = self.tables.get(table_name)

        return table
