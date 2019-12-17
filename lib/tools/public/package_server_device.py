#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from lib.tools.public.task_server_device import TaskServerDevice


class PackageServerDevice(TaskServerDevice):
    """Package server device class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-21
    """

    def query_upgrade_package(self, upgrade_config, upgrade_version):
        """Query the upgrade package from sftp server
        Args:
            upgrade_config         type(dict)             [package type -- package path on sftp server] config dict.
            upgrade_version        type(str)              upgrade version of the specified in test_bed.xml
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-21
        """

        sftp = self.create_sftp_client()

        # find update package
        sftp_path = upgrade_config['sftp_path']
        filter_pattern = upgrade_config['filter_pattern']
        version_pattern = upgrade_config['version_pattern']
        files = sftp.query_files(sftp_path)
        sftp.close()
        find_file = self.finder.find_by_version(files, upgrade_version, version_pattern,
                                                filter_pattern)

        return find_file

    def download_upgrade_package(self, upgrade_config, upgrade_version):
        """Download the upgrade package from sftp server
        Args:
            upgrade_config         type(dict)             [package type -- package path on sftp server] config dict.
            upgrade_version        type(str)              upgrade version of the specified in test_bed.xml
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-21
        """

        # query the upgrade package
        find_file = self.query_upgrade_package(upgrade_config, upgrade_version)
        # download package
        sftp = self.create_sftp_client()
        sftp.download_file(upgrade_config['sftp_path'], upgrade_config['local_path'], find_file)
        package_file = os.path.join(upgrade_config['local_path'], find_file)
        sftp.close()

        return package_file
