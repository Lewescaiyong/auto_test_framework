#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.database.table.smart200_table.smart200_table_base import Smart200TableBase


class PlcDevicesTable(Smart200TableBase):
    """Table plc_devices in smart200 database .
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-11
    """

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

        return 'plc_devices'

    def get_free_plc(self, number=1):
        """Get the specified number of plc devices.
        Args:
            number         type(int)          number of the plc device
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        result = self.get_free_device(number)

        return result

    def query_free_device(self):
        """Query plc devices in free state.
        Args:
            cmd         type(str)          commands for querying data
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        result = dict()
        cmd = 'select * from plc_devices where status="free";'
        data = self.run(cmd, 'query')
        for i in data:
            plc_info = {'plc_ip': i[1], 'cpu_type': i[2]}
            result[plc_info['plc_ip']] = plc_info

        return result

    def update_plc_status(self, update_info):
        """Update the plc device status.
        Args:
            update_info        type(dict, list)        plc info
            ------------------------------------------------------------------------------
            update_info detail:
            plc_ip             type(str)               the plc ip address used to perform the task
            ipc_ip             type(str)               the ip address of the ipc device
            executing_task     type(str)               the name of the task being performed
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        if not isinstance(update_info, list):
            update_info = [update_info]

        for i in update_info:
            if not i.get('executing_task'):
                plc_ip = i['plc_ip']
                command = "update plc_devices set status='free', ipc_ip='', executing_task='' where plc_ip='%s';" \
                          % plc_ip
            else:
                plc_ip = i['plc_ip']
                ipc_ip = i['ipc_ip']
                executing_task = i['executing_task']
                command = "update plc_devices set status='using', ipc_ip='%s', executing_task='%s', " \
                          "last_task_time=NOW() where plc_ip='%s';" % (ipc_ip, executing_task, plc_ip)
            self.run(command, 'update')
