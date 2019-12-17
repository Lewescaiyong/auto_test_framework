#!/usr/bin/env python

import os
import re

from lib.component.business.business_base import BusinessBase


class UpgradeBase(BusinessBase):
    """Upgrade base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-22
    """

    unzip_path = ''

    def __init__(self, own_software, params=None):
        super(UpgradeBase, self).__init__(own_software, params)

    def upgrade(self, upgrade_file='', is_task_server=True):
        """Upgrade software
        Args:
            upgrade_file        type(str)         the abspath of upgrade file
            is_task_server      type(bool)        is the task server calling
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        if not self.check_is_need_upgrade(upgrade_file):
            self.when_not_upgrade(is_task_server)
            self.logger.info('Not need to upgrade')
            return True

        if not upgrade_file:
            if not self.__class__.unzip_path:
                # download update package
                package_file = self.download_upgrade_package()
                # unzip the package
                unzip_path, dir_name = self.my_zip.unzip_file(package_file)
                self.__class__.unzip_path = os.path.join(unzip_path, dir_name)
            upgrade_file = self.find_upgrade_file()

        self.logger.info('Upgrade file: %s.' % upgrade_file)
        self._upgrade(upgrade_file, is_task_server)
        result = self.compare_version(upgrade_file)

        return result

    def when_not_upgrade(self, is_task_server=True):
        """Execute some steps if not need to upgrade
        Args:
            is_task_server      type(bool)        is the task server calling
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

    def _upgrade(self, upgrade_file, is_task_server=True):
        """Upgrade software
        Args:
            upgrade_file        type(str)         the abspath of upgrade file
            is_task_server      type(bool)        is the task server calling
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

    def download_upgrade_package(self):
        """Download the upgrade package from sftp server
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        # delete old update file
        upgrade_config = self.upgrade_config
        self.file_options.remove_file_dir(upgrade_config['local_path'], is_dir=True)
        # download package
        package_file = self.package_device.download_upgrade_package(upgrade_config, self.own_software.upgrade_version)

        return package_file

    def check_is_need_upgrade(self, upgrade_file=''):
        """Check whether need to upgrade.
        Args:
            upgrade_file        type(str)         the abspath of upgrade file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """
        if not upgrade_file:
            upgrade_file = self.query_upgrade_package()

        result = not self.compare_version(upgrade_file)

        return result

    def query_upgrade_package(self):
        """Query the upgrade package from sftp server
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        # find upgrade package
        upgrade_config = self.upgrade_config
        find_file = self.package_device.query_upgrade_package(upgrade_config, self.own_software.upgrade_version)

        return find_file

    def get_upgrade_version(self):
        """Get upgrade version.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13
        """

        upgrade_file = self.query_upgrade_package()
        version_pattern = self.upgrade_config['version_pattern']
        searcher = re.search(version_pattern, upgrade_file, re.I)
        file_version = searcher.group()
        file_version = self.process_upgrade_version(file_version)

        return file_version

    def process_upgrade_version(self, file_version):
        """Process the version information for the upgrade file before making the comparison.
        Args:
            file_version        type(str)         the version of the upgrade file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        return file_version

    def compare_version(self, upgrade_file):
        """Compare the upgrade file version with the software current version information.
        Args:
            upgrade_file        type(str)         the abspath of upgrade file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        version_pattern = self.upgrade_config['version_pattern']
        searcher = re.search(version_pattern, upgrade_file, re.I)
        file_version = searcher.group()
        if not self.compare.compare_c_str(file_version, self.own_software.version):
            return True

        return False

    def find_upgrade_file(self):
        """Find the upgrade file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

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

        config = dict()

        return config
