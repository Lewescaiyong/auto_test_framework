#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.base.framework.has_interface.has_interface import HasInterface


class TableBase(HasInterface):
    """Table's base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-11
    """

    def __init__(self, own_database):
        super(TableBase, self).__init__()
        self.own_database = own_database

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

        return 'table_base'

    def run(self, cmd, option):
        """Execute cmd.
        Args:
            cmd         type(str)          commands to execute
            option      type(str)          enumerate(query, insert, update, delete)
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        result = self.own_database.run(cmd, option, self.name)

        return result
