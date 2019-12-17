#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from lib.tools.public.finder import Finder
from lib.tools.sftp.sftp_client import SFTPClient
from lib.tools.public.information import Information
from lib.base.framework.smart200_base import Smart200Base


class TaskServerDevice(Smart200Base):
    """Task server device class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-21
    """

    def __init__(self):
        super(TaskServerDevice, self).__init__()
        self.finder = Finder()
        self.information = Information()

    @property
    def sftp_info(self):
        """SFTP server connection information
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-21
        """

        return {'ip': '192.168.10.5', 'user': 'admin', 'password': '123456', 'port': 22}

    @property
    def report_path(self):
        """SFTP server report file path
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-21
        """

        return '/Project/smart200/lib/agent/files/report'

    def create_sftp_client(self):
        """create sftp client
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-21
        """

        sftp = SFTPClient(self.sftp_info)
        sftp.login()

        return sftp

    def upload_report(self, local_filename, sftp_filename):
        """Upload the test report file to task server device
        Args:
            local_filename      type(bool)       file name on local device
            sftp_filename       type(bool)       file name on sftp device after upload
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-21
        """

        local_path = self.information.get_framework_local_path()
        local_path = os.path.join(local_path, 'report')

        # download package
        sftp = self.create_sftp_client()
        sftp.upload_file(self.report_path, local_path, local_filename, sftp_filename)
        sftp.close()
