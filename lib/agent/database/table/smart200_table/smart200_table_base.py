#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.database.table.table_base import TableBase


class Smart200TableBase(TableBase):
    """Database Smart200 table's base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
    """

    def get_free_device(self, number=1):
        """Query ipc device in free state.
        Args:
            number         type(int)          number of the ipc device
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        result = dict()
        number = int(number)

        all_free = self.query_free_device()
        if len(all_free) < number:
            return result

        for index, value in enumerate(all_free.keys()):
            if index < number:
                result[value] = all_free[value]
            else:
                break

        return result

    def query_free_device(self):
        """Query ipc device in free state.
        Args:
            cmd         type(str)          commands for querying data
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        return dict()
