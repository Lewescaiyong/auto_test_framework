#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.agent_base import AgentBase
from lib.tools.sftp.sftp_client import SFTPClient
from lib.agent.command.host.device_host import DeviceHost


class DeviceBase(AgentBase):
    """Device base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
    """

    def __init__(self, device_info, task_type):
        super(DeviceBase, self).__init__()
        self.device_info = device_info
        self.task_type = task_type
        self.host = None
        self.create_host()
        self.task_start_time = None

    def run(self, cmd, directory='', timeout=60):
        """Execute cmd.
        Args:
            cmd         type(str)          commands to execute
            directory   type(str)          the path of the commands executed
            timeout     type(str)          the time of timeout
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        cmd_info = {'command': cmd, 'directory': directory, 'timeout': timeout}
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
    def protocol(self):
        """Database name
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return 'telnet'

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
            'conn_info': self.conn_info
        }

        self.host = self.host_class(params)

    def create_sftp_client(self):
        """create sftp client
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-16
        """

        sftp = SFTPClient(self.sftp_info)
        sftp.login()

        return sftp

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

        return DeviceHost

    @property
    def conn_info(self):
        """Host class
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return self.device_info

    @property
    def sftp_info(self):
        """Host class
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return dict()
