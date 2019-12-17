#!/usr/bin/env python
import os
import time
from shutil import rmtree

from lib.tools.sanity_comm.utils import PROJECT_PATH
from lib.exceptions.check_exception import CheckException
from lib.base.script.gui_test.case_mw_gui import CaseMWGUI
from lib.tools.sanity_comm.file_helper import close_file, open_file, new_file, save_as_file


class Test200SmartSanityUi001(CaseMWGUI):
    """Project
    No.: test_200smart_sanity_ui_001
    Preconditions:
        1. Open Micro/WIN;
    Step actions:
        1. New a project;
        2. Save the project;
        3. Open an existed project;
        4. Save as the project;
        5. Close the project;
    Expected results:
        1. Create successful;
        2. Save successful;
        3. Open successful;
        4. Save successful;
        5. Close successful;
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
        super(Test200SmartSanityUi001, self).prepare()
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
        super(Test200SmartSanityUi001, self).process()

        self.logger.info('Step actions:')
        self.logger.info('Expected results:')

        self.logger.info('1. New a project;')
        success = new_file()

        self.logger.info('1. Create successful;')
        if not success:
            raise CheckException('create new project failed;')

        self.logger.info('2. Save the project;')
        new_name = time.strftime('%Y-%m-%d@%H-%M-%S', time.localtime()) + '.smart'
        success = save_as_file(PROJECT_PATH+new_name)

        self.logger.info('2. Save successful;')
        if not success:
            raise CheckException('save project failed;')
        self.tmp['file'].append(PROJECT_PATH + new_name)

        self.logger.info('3. Open an existed project;')
        success = open_file()

        self.logger.info('3. Open successful;')
        if not success:
            raise CheckException('open project failed;')

        self.logger.info('4. Save as the project;')
        success = save_as_file('', False)

        self.logger.info('4. Save successful;')
        if not success:
            raise CheckException('save as project failed;')

        self.logger.info('5. Close the project;')
        success = close_file()

        self.logger.info('5. Close successful;')
        if not success:
            raise CheckException('close project failed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        # close Micro/WIN
        super(Test200SmartSanityUi001, self).cleanup()
        for f in self.tmp['file']:
            os.remove(f)
        for d in self.tmp['dir']:
            rmtree(d)
