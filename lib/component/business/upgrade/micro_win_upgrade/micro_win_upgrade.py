#!/usr/bin/env python

import os
import re
import time
import winreg
from xml.etree.ElementTree import ParseError

from lib.tools.xml.xml_parser import XMLParser
from lib.component.business.upgrade.upgrade_base import UpgradeBase


class MicroWINUpgrade(UpgradeBase):
    """MicroWIN upgrade class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-22
    """

    def __init__(self, own_software, params=None):
        super(MicroWINUpgrade, self).__init__(own_software, params)

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
            'sftp_path': '/package/MW',
            'filter_pattern': 'MW_SMART',
            'version_pattern': '[VR]\\d+\\.\\d+\\.\\d+\\.\\d+_\\d+\\.\\d+\\.\\d+\\.\\d+',
            'zip_path': {'R': 'Setup/R/setup.exe', 'V': 'Setup/V/setup.exe'},
            'local_path': r'C:\Package\MW'
        }

        return config

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        config = {'upgrade_type': 'R'}

        return config

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

        if is_task_server:
            self.update_upgrade_result(need_restart='no')

    def _upgrade(self, upgrade_file, is_task_server=True):
        """Upgrade MicroWIN
        Args:
            upgrade_file        type(str)         the abspath of upgrade file
            is_task_server      type(bool)        is the task server calling
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """
        if is_task_server:
            self.update_upgrade_result()
        self.uninstall(upgrade_file)
        self.install(upgrade_file)

    def update_upgrade_result(self, need_restart='yes'):
        """Update upgrade result
        Args:
            need_restart        type(str)         is need to restart client device
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        self.xml_options.update_upgrade_result(need_restart=need_restart)
        self.wait_download_upgrade_result()

    def wait_download_upgrade_result(self):
        """Wait for Server download upgrade result
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        files_path = self.information.get_agent_files_path()
        file_name = os.path.join(files_path, 'upgrade_result', 'upgrade_result_record.xml')

        while True:
            time.sleep(5)
            try:
                info = XMLParser(file_name).xml_parser()
            except ParseError:
                continue
            else:
                need_restart = info['UpgradeResult']['MicroWIN']['NeedRestart']
                if need_restart == '':
                    return

    def find_upgrade_file(self):
        """Find the setup.exe file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        zip_path = self.upgrade_config['zip_path'][self.params['upgrade_type']]
        setup_file = os.path.join(self.unzip_path, zip_path)

        return setup_file

    def uninstall(self, setup_file):
        """Uninstall the existing MicroWIN.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        if not self.check_if_installed():
            self.logger.info('MicroWIN was not installed, not need to uninstall.')
            return

        self.logger.info('Kill process pycharm64.exe')
        self.common.kill_process('pycharm64.exe')

        gui_path = self.information.get_micro_win_gui_path()
        uninstall_file = os.path.join(gui_path, 'uninstall.iss')
        log_file = os.path.join(gui_path, 'uninstall.log')
        cmd = '%s /S /f1"%s" -f2"%s"' % (setup_file, uninstall_file, log_file)
        self.run_cmd.run_admin(cmd)
        self.wait_setup_complete()

    def install(self, setup_file):
        """Install MicroWIN.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        gui_path = self.information.get_micro_win_gui_path()
        install_file = os.path.join(gui_path, 'install_not_restart.iss')
        log_file = os.path.join(gui_path, 'install.log')
        cmd = '%s /S /f1"%s" -f2"%s"' % (setup_file, install_file, log_file)
        self.run_cmd.run_admin(cmd)
        self.wait_setup_complete()
        self.reach_device.restart_local_device()

    def check_if_installed(self):
        """Check whether MicroWIN is installed locally.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        if self.information.check_windows_if_64():
            key = 'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{' \
                  '6BA8BB2D-F711-43F9-A5D1-F2182C26BB6D}'
        else:
            key = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{' \
                  '6BA8BB2D-F711-43F9-A5D1-F2182C26BB6D}'

        try:
            explorer = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
            winreg.QueryValueEx(explorer, 'InstallLocation')
        except (FileNotFoundError, OSError):
            result = False
            self.logger.info('MicroWIN was not installed.')
        else:
            result = True
            self.logger.info('MicroWIN has installed.')

        return result

    def wait_setup_complete(self):
        """Wait for the process setup.exe run to end.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-19
        """
        is_print = False
        time.sleep(10)

        while True:
            if not self.checker.process_is_running('setup.exe', False):
                self.logger.debug('The process [setup.exe] run finished.')
                break
            if not is_print:
                self.logger.debug('The process [setup.exe] is running.')
                is_print = True
            time.sleep(1)

    def compare_version(self, upgrade_file):
        """Compare the upgrade file version with the software current version information.
        Args:
            upgrade_file        type(str)         the abspath of upgrade file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-24
        """

        version_pattern = self.upgrade_config['version_pattern']
        searcher = re.search(version_pattern, upgrade_file, re.I)
        file_version = searcher.group()
        file_version = self.process_upgrade_version(file_version)
        self.logger.info('Target version: %s, current version: %s.' % (file_version, self.own_software.version))
        if file_version == self.own_software.version:
            return True

        return False

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

        file_version = self.params['upgrade_type'] + file_version[1:]

        return file_version
