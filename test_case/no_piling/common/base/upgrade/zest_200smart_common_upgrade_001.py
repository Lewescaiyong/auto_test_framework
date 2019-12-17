#!/usr/bin/env python

import os
import re
import sys
import traceback
import threading

from lib.log.log import Log
from lib.tools.public.my_zip import MyZip
from lib.tools.public.finder import Finder
from lib.tools.xml.xml_parser import XMLParser
from lib.tools.sftp.sftp_client import SFTPClient
from lib.tools.public.information import Information
from lib.tools.public.file_options import FileOptions
from lib.exceptions.check_exception import CheckException


class Zest200SmartCommonUpgrade001(object):
    """New file
    No.: zest_200smart_common_upgrade_001
    Preconditions:
    Step actions:
        1. Upgrade MicroWin auto test api;
    Expected results:
        1. Upgrade successful;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-11-05 create
    """

    unzip_path = ''
    logger = Log
    case_id = ''
    __upgrade_version = ''
    converter = None
    finder = Finder()
    information = Information()
    file_options = FileOptions()
    upgrade_type = 'R'

    def setup_class(self):
        """Initialize test resource
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """

        # Get the case id of the current test case
        full_path = sys.modules[self.__module__].__file__
        self.case_id = os.path.basename(full_path).split('.')[0]
        # set logger object of current thread
        threading.currentThread().logger = Log(self.case_id, date_type=1)

    def test_process(self):
        """Executive process control
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """

        try:
            self.logger.info('Start executing the test case: [%s]' % self.case_id)
            self.prepare()
            self.process()
        except Exception:
            self.logger.error(traceback.format_exc())
            raise
        finally:
            try:
                self.cleanup()
            except Exception:
                self.logger.error(traceback.format_exc())
                raise
            self.logger.info('Test case: [%s] is completed' % self.case_id)

    def teardown_class(self):
        """Clean up the environment after script execution
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """

        from lib.tools.converter.converter import Converter

        self.converter = Converter()
        self.converter.convert_log_to_html()

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-05 create
        """
        self.logger.info('Preconditions:')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-05 create
        """

        self.logger.info('Step actions:')
        self.logger.info('1. Upgrade MicroWin auto test api;')
        # result = self.upgrade(r'C:\Package\MW_SMART_R02.05.00.00_09.35.00.01\Test\AutoTest')
        result = self.upgrade()

        self.logger.info('Expected results:')
        self.logger.info('1. Upgrade successful;')
        self.logger.info('Upgrade result: %s.' % result)
        if not result:
            raise CheckException('1. Upgrade failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-05 create
        """

    @property
    def version(self):
        """The information of micro win interface.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-05 create
        """

        version_pattern = self.upgrade_config['version_pattern']
        version = self.information.get_micro_win_interface_version(version_pattern)

        return version

    @property
    def upgrade_version(self):
        """The information of firmware.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-05 create
        """

        if not self.__upgrade_version:
            local_path = self.information.get_framework_local_path()
            test_bed = os.path.join(local_path, 'lib', 'config', 'test_bed.xml')
            test_bed_info = XMLParser(test_bed).xml_parser()['TestBed']
            self.__upgrade_version = test_bed_info['MicroWIN'].get('Version', '')

        return self.__upgrade_version

    @property
    def sftp_info(self):
        """SFTP server connection information
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        return {'ip': '192.168.10.5', 'user': 'admin', 'password': '123456', 'port': 22}

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
            'zip_path': 'Test/AutoTest',
            'local_path': r'C:\Package\MW_API'
        }

        return config

    def upgrade(self, upgrade_file=''):
        """Upgrade software
        Args:
            upgrade_file        type(str)         the abspath of upgrade file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        if not self.check_is_need_upgrade(upgrade_file):
            self.logger.info('Not need to upgrade')
            return True

        if not upgrade_file:
            if not self.__class__.unzip_path:
                # download update package
                package_file = self.download_update_package()
                # unzip the package
                unzip_path, dir_name = MyZip().unzip_file(package_file)
                self.__class__.unzip_path = os.path.join(unzip_path, dir_name)
            upgrade_file = self.find_upgrade_file()

        self._upgrade(upgrade_file)
        result = self.compare_version(upgrade_file)

        return result

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
        """Query the update package from sftp server
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        sftp = SFTPClient(self.sftp_info)
        sftp.login()

        # find update package
        update_config = self.upgrade_config
        sftp_path = update_config['sftp_path']
        filter_pattern = update_config['filter_pattern']
        version_pattern = update_config['version_pattern']
        files = sftp.query_files(sftp_path)
        sftp.close()
        find_file = self.finder.find_by_version(files, self.upgrade_version, version_pattern,
                                                filter_pattern)

        return find_file

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
        self.logger.info('Target version: %s, current version: %s.' % (file_version, self.version))
        if file_version == self.version:
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

        file_version = self.upgrade_type + file_version[1:]

        return file_version

    def download_update_package(self):
        """Download the update package from sftp server
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """
        sftp = SFTPClient(self.sftp_info)
        sftp.login()

        # delete old update file
        update_config = self.upgrade_config
        self.file_options.remove_file_dir(update_config['local_path'], is_dir=True)

        # find update package
        sftp_path = update_config['sftp_path']
        filter_pattern = update_config['filter_pattern']
        version_pattern = update_config['version_pattern']
        files = sftp.query_files(sftp_path)
        find_file = self.finder.find_by_version(files, self.upgrade_version, version_pattern,
                                                filter_pattern)
        # download package
        sftp.download_file(sftp_path, update_config['local_path'], find_file)
        package_file = os.path.join(update_config['local_path'], find_file)
        sftp.close()

        return package_file

    def find_upgrade_file(self):
        """Find the setup.exe file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        zip_path = self.upgrade_config['zip_path']
        setup_file = os.path.join(self.unzip_path, zip_path)

        return setup_file

    def _upgrade(self, upgrade_dir):
        """Upgrade MicroWIN api
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-05
        """

        self.copy_new_api(upgrade_dir)

    def copy_new_api(self, upgrade_dir):
        """Copy the new MicroWIN api file
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-05
        """

        source_path = self.information.get_micro_win_interface_path()
        self.logger.info('Copy new api file to source path: %s.' % source_path)
        self.file_options.copy_dir(upgrade_dir, source_path)


if __name__ == '__main__':
    case = Zest200SmartCommonUpgrade001()
    try:
        case.setup_class()
        case.test_process()
    except Exception:
        case.teardown_class()
        raise
    else:
        case.teardown_class()
