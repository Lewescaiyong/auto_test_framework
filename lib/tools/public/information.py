#!/usr/bin/env python

import os
import re
import sys
import winreg
import threading

from lib.base.framework.smart200_base import Smart200Base


class Information(Smart200Base):
    """Return public information of smart200 project.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    @staticmethod
    def get_current_thread_log_file():
        """Get log file of current thread
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        log_file = ''
        logger = getattr(threading.currentThread(), 'logger', None)
        if logger:
            log_file = '%s.txt' % logger.name

        return log_file

    @staticmethod
    def get_framework_local_path():
        """Get local path of smart200 project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        local_path = ''
        for i in sys.path:
            if re.search('.*smart200$', i):
                local_path = re.search('.*smart200$', i).group()
                break

        return local_path

    def get_resource_path(self):
        """Get resource path of smart200 project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-09
        """

        local_path = self.get_framework_local_path()
        source_path = os.path.join(local_path, 'lib', 'resource')

        return source_path

    def get_agent_files_path(self):
        """Get agent-files path of smart200 project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-09
        """

        local_path = self.get_framework_local_path()
        files_path = os.path.join(local_path, 'lib', 'agent', 'files')

        return files_path

    def get_micro_win_gui_path(self):
        """Get tools->micro_win_gui path of smart200 project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-09
        """

        local_path = self.get_framework_local_path()
        gui_path = os.path.join(local_path, 'lib', 'tools', 'gui', 'micro_win_upgrade')

        return gui_path

    def get_micro_win_interface_version(self, version_pattern=''):
        """Get the version information of the Micro/WIN interface
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13
        """

        if not version_pattern:
            version_pattern = '[VR]\\d+\\.\\d+\\.\\d+\\.\\d+_\\d+\\.\\d+\\.\\d+\\.\\d+'
        source_path = self.get_micro_win_interface_path()
        try:
            with open(os.path.join(source_path, 'mwversion.h')) as f:
                data = f.read()
        except FileNotFoundError:
            version = ''
        else:
            searcher = re.search(version_pattern, data, re.I)
            version = searcher.group()

        return version

    def get_micro_win_interface_path(self):
        """Get wrapper->interface_mw->source path of smart200 project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-09
        """

        local_path = self.get_framework_local_path()
        source_path = os.path.join(local_path, 'lib', 'wrapper', 'integration_mw', 'source')

        return source_path

    @staticmethod
    def get_version_information(resource):
        """Get Micro/WIN and CPU version information.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        # get Micro/WIN version information
        updater = resource.micro_win.find('upgrade')
        mw_version = updater.get_upgrade_version()

        # get cpu version information
        updater = resource.plc['1'].find('upgrade')
        cpu_version = updater.get_upgrade_version()

        return {'mw_version': mw_version, 'cpu_version': cpu_version}

    def get_micro_win_install_location(self):
        """Get the install location of the MicroWIN.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-19
        """

        if self.check_windows_if_64():
            key = 'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{' \
                  '6BA8BB2D-F711-43F9-A5D1-F2182C26BB6D}'
        else:
            key = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{' \
                  '6BA8BB2D-F711-43F9-A5D1-F2182C26BB6D}'

        try:
            explorer = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
            location = winreg.QueryValueEx(explorer, 'InstallLocation')[0]
        except (FileNotFoundError, OSError):
            location = ''
            self.logger.info('Get MicroWIN install location failed.')
        else:
            self.logger.info('Get MicroWIN install location successfully, location: "%s".' % location)

        return location

    @staticmethod
    def check_windows_if_64():
        """Check whether windows system is x64.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-19
        """

        result = 'PROGRAMFILES(X86)' in os.environ

        return result
