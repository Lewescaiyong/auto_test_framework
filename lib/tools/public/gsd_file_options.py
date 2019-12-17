#!/usr/bin/env python

import os
import re

from lib.tools.public.my_zip import MyZip
from lib.tools.public.file_options import FileOptions


class GSDFileOptions(FileOptions):
    """GSD file options.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-13
    """

    def __init__(self):
        super(GSDFileOptions, self).__init__()
        self.zip_file = None
        self.my_zip = MyZip()

    @property
    def gsd_file_path(self):
        """GSD files path of MicroWIN software
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-28 create
        """

        file_path = r'C:\Users\Public\Documents\Siemens\STEP 7-MicroWIN SMART\GSDML'

        return file_path

    def copy_gsd_file(self, files):
        """Copy the gsd file to self.gsd_file_path
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-28 create
        """

        # backup files
        self.gsd_file_backup()

        # add InstallLog.dat file
        files = list(files)
        files.insert(0, 'InstallLog.dat')
        # copy files to target directory
        for gsd_file in files:
            if not re.search(':', gsd_file):
                source_path = self.information.get_resource_path()
                gsd_file = os.path.join(source_path, 'gsd', gsd_file)
            self.copy_file(gsd_file, self.gsd_file_path)

    def gsd_file_backup(self):
        """Backup gsd files in self.gsd_file_path
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-29 create
        """

        self.zip_file = self.my_zip.zip_file(self.gsd_file_path)
        self.remove_file_dir(self.gsd_file_path, is_dir=True)
        self.create_dir(self.gsd_file_path)

    def gsd_file_reduction(self):
        """Reduction gsd files in self.gsd_file_path
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-28 create
        """

        self.remove_file_dir(self.gsd_file_path, is_dir=True)
        self.my_zip.unzip_file(self.zip_file, add_dir=True)
        self.remove_file_dir(self.zip_file)
