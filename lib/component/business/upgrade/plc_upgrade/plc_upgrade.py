#!/usr/bin/env python

import re
import os

from lib.exceptions.not_found_exception import NotFoundException
from lib.component.business.upgrade.upgrade_base import UpgradeBase


class PLCUpgrade(UpgradeBase):
    """PLC upgrade class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-22
    """

    def __init__(self, own_software, params=None):
        super(PLCUpgrade, self).__init__(own_software, params)

    @property
    def upgrade_config(self):
        """Upgrade config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        config = {
            'sftp_path': '/package/FW',
            'filter_pattern': 'SMARTCPU',
            'version_pattern': '[VR]\\d+\\.\\d+\\.\\d+_\\d+\\.\\d+\\.\\d+\\.\\d+',
            'zip_path': r'bin_fw/sdcard_fwupdate/FWUPDATE.S7S',
            'local_path': r'C:\Package\FW'
        }

        return config

    def _upgrade(self, upgrade_file, is_task_server=True):
        """Upgrade firmware by upd file
        Args:
            upgrade_file        type(str)         the abspath of upgrade file
            is_task_server      type(bool)        is the task server calling
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        self.own_software.dispatch('upgrade_fw', {'strFilePath': upgrade_file})
        self.own_software.plc_power_cycle()

    def find_upgrade_file(self):
        """Find the upd file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        zip_path = self.upgrade_config['zip_path']
        upd_file_path = os.path.join(self.unzip_path, zip_path)
        files = os.listdir(upd_file_path)
        for i in files:
            if re.search(self.own_software.cpu_type, i, re.I):
                upd_file = os.path.join(upd_file_path, i)
                break
        else:
            self.logger.debug('UPD files: %s.' % files)
            self.logger.debug('CPU type: %s.' % self.own_software.cpu_type)
            raise NotFoundException('The plc update file not found.')

        return upd_file
