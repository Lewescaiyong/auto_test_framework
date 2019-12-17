#!/usr/bin/env python
import os
import time
from shutil import rmtree

from lib.exceptions.check_exception import CheckException
from lib.base.script.gui_test.case_mw_gui import CaseMWGUI
from lib.tools.sanity_comm.utils import SOURCE_PATH, FILE_PREVIOUS, exec_cmd
from lib.tools.sanity_comm.file_helper import import_pou, open_file, new_file, export_pou


class Test200SmartSanityUi002(CaseMWGUI):
    """Import/Export
    No.: test_200smart_sanity_ui_002
    Preconditions:
        1. Open Micro/WIN;
    Step actions:
        1. Click "File" -> "Open" to open an existed file;
        2. Click "File" -> "Export" to export the file;
        3. New a file, and then import the file in step2;
        4. New a file, and then Click "File" -> "Previous";
    Expected results:
        1. open successful;
        2. export successful, there is a xx.awl file in exported location;
        3. Import successful;
        4. There is a file name of step1, select it and open successful;
    Priority: H
    Author: Wang, Xing Yu
    ChangeInfo: Wang, Xing Yu 2019-10-30 create
    """
    tmp = ''

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi002, self).prepare()
        self.tmp = {
            'file': [],
            'dir': []
        }
        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi002, self).process()

        self.logger.info('Step actions:')
        self.logger.info('Expected results:')

        self.logger.info('1. Click "File" -> "Open" to open an existed file;')
        success = open_file()

        self.logger.info('1. open successful;')
        if not success:
            raise CheckException('open file failed')

        self.logger.info('2. Click "File" -> "Export" to export the file;')
        pou_name = time.strftime('%Y-%m-%d@%H-%M-%S', time.localtime()) + '.awl'
        success = export_pou(SOURCE_PATH+pou_name)

        self.logger.info('2. export successful, there is a xx.awl file in exported location;')
        if not success:
            raise CheckException('export POU file failed')
        self.tmp['file'].append(SOURCE_PATH+pou_name)

        self.logger.info('3. New a file, and then import the file in step2;')
        success = new_file()

        self.logger.info('3. Import successful;')
        if not success:
            raise CheckException('new project failed')

        success = import_pou(SOURCE_PATH+pou_name)
        if not success:
            raise CheckException('import pou file failed')

        self.logger.info('4. New a file, and then Click "File" -> "Previous";')
        success = new_file()

        self.logger.info('4. There is a file name of step1, select it and open successful;')
        if not success:
            raise CheckException('new project failed')

        success = exec_cmd(FILE_PREVIOUS)
        if not success:
            raise CheckException('change to previous file failed')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi002, self).cleanup()
        for f in self.tmp['file']:
            os.remove(f)
        for d in self.tmp['dir']:
            rmtree(d)
