#!/usr/bin/env python

import os
import zipfile

from lib.base.framework.smart200_base import Smart200Base


class MyZip(Smart200Base):
    """cleanup class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    def unzip_file(self, zip_file, unzip_path='', add_dir=False):
        """unzip the file.
        Args:
            zip_file        type(str)        the abspath of the file to be unzipped.
            unzip_path      type(str)        unzipped path
            add_dir         type(bool)       whether to add a layer of directory when unzip the file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-23
        """

        self.logger.debug('Start unzipping the file: %s.' % zip_file)
        dir_name = os.path.basename(zip_file).rsplit('.', 1)[0]
        if not unzip_path:
            if add_dir:
                unzip_path = zip_file.rsplit('.', 1)[0]
            else:
                unzip_path = os.path.dirname(zip_file)

        # starting unzip the file
        with zipfile.ZipFile(zip_file, 'r') as f:
            for i in f.namelist():
                f.extract(i, unzip_path)
        self.logger.debug('Unzip completed, unzip path: %s.' % unzip_path)

        return unzip_path, dir_name

    def zip_file(self, file_path, zip_path='', zip_file_name=''):
        """zip the files.
        Args:
            file_path       type(str)        the path of the file to be zipped.
            zip_path        type(str)        zipped path
            zip_file_name   type(str)        the name of the zipped file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-23
        """

        self.logger.debug('Start zipping the file: %s.' % file_path)
        if not zip_path:
            zip_path = os.path.dirname(file_path)
        if not zip_file_name:
            zip_file_name = '%s.zip' % os.path.basename(file_path).rsplit('.', 1)[0]
        zip_file = os.path.join(zip_path, zip_file_name)

        # starting zip the files
        zip_obj = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
        if os.path.isfile(file_path):
            zip_obj.write(file_path, os.path.basename(file_path))
        else:
            for path, dirs, files in os.walk(file_path):
                # get rid of the root path
                current_path = path.replace(file_path, '')
                for i in files:
                    zip_obj.write(os.path.join(path, i), os.path.join(current_path, i))
        zip_obj.close()
        self.logger.debug('Zip completed, zip file: %s.' % zip_file)

        return zip_file
