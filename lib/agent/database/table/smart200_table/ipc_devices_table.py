#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.database.table.smart200_table.smart200_table_base import Smart200TableBase


class IpcDevicesTable(Smart200TableBase):
    """Table ipc_devices in smart200 database .
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-10
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

        return 'ipc_devices'

    def get_free_ipc(self, number=1):
        """Get the specified number of ipc devices.
        Args:
            number         type(int)          number of the ipc device
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        result = self.get_free_device(number)

        return result

    def query_free_device(self):
        """Query ipc devices in free state.
        Args:
            cmd         type(str)          commands for querying data
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        result = dict()
        cmd = 'select * from ipc_devices where status="free";'
        data = self.run(cmd, 'query')
        for i in data:
            ipc_info = {'ipc_ip': i[1], 'user_name': i[2], 'password': i[3], 'port': i[4], 'framework_path': i[5],
                        'sftp_user': i[9], 'sftp_password': i[10], 'sftp_path': i[11]}
            result[ipc_info['ipc_ip']] = ipc_info

        return result

    def update_ipc_status(self, update_info):
        """Update the ipc device status.
        Args:
            update_info        type(dict, list)        ipc info
            ------------------------------------------------------------------------------
            update_info detail:
            ipc_ip             type(str)               the ip address of the ipc device
            plc_ip             type(str)               the plc ip address used to perform the task
            executing_task     type(str)               the name of the task being performed
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-10
        """

        if not isinstance(update_info, list):
            update_info = [update_info]

        for i in update_info:
            if not i.get('executing_task'):
                ipc_ip = i['ipc_ip']
                command = "update ipc_devices set status='free', plc_ip='', executing_task='' where ipc_ip='%s';" \
                          % ipc_ip
            else:
                ipc_ip = i['ipc_ip']
                plc_ip = i['plc_ip']
                executing_task = i['executing_task']
                command = "update ipc_devices set status='using', plc_ip='%s', executing_task='%s', " \
                          "last_task_time=NOW() where ipc_ip='%s';" % (plc_ip, executing_task, ipc_ip)
            self.run(command, 'update')
