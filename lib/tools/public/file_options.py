#!/usr/bin/env python

import os
import shutil
import traceback

from lib.tools.public.information import Information
from lib.base.framework.smart200_base import Smart200Base


class FileOptions(Smart200Base):
    """File options.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-29
    """

    def __init__(self):
        super(FileOptions, self).__init__()
        self.information = Information()

    @staticmethod
    def file_is_exist(file_path):
        """Check the file whether exist.
        Args:
            file_path        type(str)        the path of the file to be checked.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-17
        """

        if os.path.exists(file_path):
            return True

        return False

    def remove_file_dir(self, file_path, is_project=False, is_awl=False, is_data_log=False, is_dir=False):
        """Remove the file or dir.
        Args:
            file_path        type(str)        the path of the file/dir to be removed.
            is_project       type(bool)       is it a project file?
            is_awl           type(bool)       is it a awl file?
            is_data_log      type(bool)       is it a data_log.csv file?
            is_dir           type(bool)       is it a directory?
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-17
        """
        # Automatically go to the smart200 framework /lib/resource/project directory to find the project file
        if is_project:
            resource_path = self.information.get_resource_path()
            file_path = os.path.join(resource_path, 'project', file_path)
        # Automatically go to the smart200 framework /lib/resource/awl directory to find the awl file
        elif is_awl:
            resource_path = self.information.get_resource_path()
            file_path = os.path.join(resource_path, 'awl', file_path)
        # Automatically go to the smart200 framework /lib/resource/data_log directory to find the csv file
        elif is_data_log:
            resource_path = self.information.get_resource_path()
            file_path = os.path.join(resource_path, 'data_log', file_path)

        if not self.file_is_exist(file_path):
            self.logger.info('The file to be deleted was not found: %s.' % file_path)
            return

        # Remove the file or dir
        result = False
        if os.path.isfile(file_path):
            os.remove(file_path)
            self.logger.info('File deleted successfully: "%s".' % file_path)
            result = True
        elif is_dir:
            for i in range(2):
                try:
                    shutil.rmtree(file_path)
                except OSError:
                    self.logger.warning(traceback.format_exc())
                    continue
                else:
                    result = True
                    self.logger.info('Directory deleted successfully: "%s".' % file_path)
                    break

        return result

    def change_file_name(self, file_path, old_name, new_name=''):
        """Change file name
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        if not new_name:
            new_name = 'backup_' + old_name
        old_name = os.path.join(file_path, old_name)
        new_name = os.path.join(file_path, new_name)
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            self.logger.info('Change filename: %s -> %s.' % (old_name, new_name))

    def copy_file(self, source_file, target_path):
        """Copy source_file into the target_path.
        Args:
            source_file       type(str)        the absolute path of file which needs to be copied.
            target_path       type(str)        target path.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        file_name = os.path.basename(source_file)

        # remove old source_file in target_path
        if os.path.exists(os.path.join(target_path, file_name)):
            os.remove(os.path.join(target_path, file_name))

        # copy file to target_path
        shutil.copy(source_file, target_path)
        self.logger.info('Copy file: %s to : %s.' % (file_name, target_path))

    @staticmethod
    def copy_dir(source_dir, target_dir):
        """Copy source_file into the target_path.
        Args:
            source_dir        type(str)        the absolute path of directory which needs to be copied.
            target_dir        type(str)        the absolute path of directory after copied.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        # remove old target_dir
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)

        # copy source_dir to target_dir
        shutil.copytree(source_dir, target_dir)

    def create_dir(self, dir_name):
        """Create directory.
        Args:
            dir_name        type(str)        the absolute path of directory which needs to be created.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        if not self.file_is_exist(dir_name):
            os.makedirs(dir_name)
            self.logger.info('Create directory: %s.' % dir_name)
