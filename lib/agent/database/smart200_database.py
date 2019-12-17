#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.database.database_base import DatabaseBase
from lib.agent.database.table.smart200_table.ipc_devices_table import IpcDevicesTable
from lib.agent.database.table.smart200_table.plc_devices_table import PlcDevicesTable
from lib.agent.database.table.smart200_table.task_records_table import TaskRecordsTable


class Smart200Database(DatabaseBase):
    """Database smart200 class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
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

        return 'smart200'

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

        return {'ip': '192.168.10.5', 'user': 'root', 'password': '123456', 'database': 'smart200'}

    @property
    def table_config(self):
        """Table config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """

        config = {
            'ipc_devices': IpcDevicesTable,
            'plc_devices': PlcDevicesTable,
            'task_records': TaskRecordsTable
        }

        return config

    @property
    def field_config(self):
        """[Table fields <--> xml fields] config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-17
        """

        config = {'ipc_ip': 'IPCIp', 'user_name': 'UserName', 'password': 'Password', 'port': 'Port',
                  'framework_path': 'FrameworkPath', 'status': 'Status', 'executing_task': 'ExecutingTask',
                  'plc_ip': 'PLCIp', 'sftp_user': 'SftpUser', 'sftp_password': 'SftpPassword',
                  'cpu_type': 'CPUType'}

        return config
