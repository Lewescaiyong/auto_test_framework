#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.gui_test.case_mw_gui import CaseMWGUI
from lib.tools.sanity_comm.file_helper import add_gsd_file, delete_gsd_file


class Test200SmartSanityUi003(CaseMWGUI):
    """Gsdml
    No.: test_200smart_sanity_ui_003
    Preconditions:
        1. Open Micro/WIN;  
        2. Set up connection with PLC;
    Step actions:
        1. Click "File" -> "GSDML Management", then click "Browse" to add a  GSDML file;
        2. Select a GSDML file, and click "Delete" to delete the gsd file;
    Expected results:
        1. add successful;
        2. delete successful;
    Priority: H
    Author: Wang, Xing Yu
    ChangeInfo: Wang, Xing Yu 2019-10-30 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi003, self).prepare()
        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. Set up connection with PLC;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi003, self).process()

        self.logger.info('Step actions:')
        self.logger.info('Expected results:')

        self.logger.info('1. Click "File" -> "GSDML Management", then click "Browse" to add a  GSDML file;')
        success = add_gsd_file()

        self.logger.info('1. add successful;')
        if not success:
            raise CheckException('add GSDML file failed')

        self.logger.info('2. Select a GSDML file, and click "Delete" to delete the gsd file;')
        success = delete_gsd_file()

        self.logger.info('2. delete successful;')
        if not success:
            raise CheckException('delete GSDML file failed')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi003, self).cleanup()
