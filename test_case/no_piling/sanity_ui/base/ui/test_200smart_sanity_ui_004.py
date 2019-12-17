#!/usr/bin/env python

from lib.tools.sanity_comm.utils import *
from lib.tools.sanity_comm.file_helper import open_file
from lib.exceptions.check_exception import CheckException
from lib.base.script.gui_test.case_mw_gui import CaseMWGUI


class Test200SmartSanityUi004(CaseMWGUI):
    """Download/Upload
    No.: test_200smart_sanity_ui_004
    Preconditions:
        1. Open Micro/WIN as administrator;  
        2. Set up connection with PLC;
        3. Create a new project with DB,OB,SDB;
    Step actions:
        1. Download  all to the PLC;
        2. Make the PLC in run Mode,view the status of PLC and program;
        3. Upload all to a new project;
        4. Make the PLC in stop Mode, view the event log in PLC Information;
    Expected results:
        1. Download successful;
        2. PLC in run mode, and the program run normally;
        3. Upload  successful;
        4. The event log record correctly;
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
        super(Test200SmartSanityUi004, self).prepare()
        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN as administrator;  ')
        self.logger.info('2. Set up connection with PLC;')
        self.logger.info('3. Create a new project with DB,OB,SDB;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi004, self).process()
        typ = self.plc_info['CPUType']
        ip = self.plc_info['PLCIp']

        self.logger.info('Step actions:')

        self.logger.info('Expected results:')

        open_file(PROJECT_PATH+'MOV.smart')

        # if PLC type is not the same with project system type, to change type for download
        # just uncomment line bellow
        set_system_block_type(typ)

        # ---------------------- connect to PLC ---------------------------------
        success = get_connect_with_plc(which=ip)
        if not success:
            raise CheckException('connect to PLC failed')
        self.logger.info('connected to PLC device.')

        # ---------------------- STOP connected PLC -----------------------------
        success = set_plc_stop()
        if not success:
            raise CheckException('set PLC stop failed')
        self.logger.info('PLC is in `STOP` mode.')

        # ---------------------- download all to PLC ----------------------------
        self.logger.info('1. Download  all to the PLC;')
        success = download_to_plc(PLC_DOWNLOAD_ALL)
        self.logger.info('1. Download successful;')
        if not success:
            raise CheckException('download failed')

        # ---------------------- RUN connected PLC ------------------------------
        self.logger.info('2. Make the PLC in run Mode,view the status of PLC and program;')
        success = set_plc_run()
        self.logger.info('2. PLC in run mode, and the program run normally;')
        if not success:
            raise CheckException('set PLC run failed')

        # ---------------------- upload all from PLC ---------------------
        self.logger.info('3. Upload all to a new project;')
        success = upload_from_plc(PLC_UPLOAD_ALL)
        self.logger.info('3. Upload  successful;')
        if not success:
            raise CheckException('upload all from PLC failed')

        # ---------------------- STOP connected PLC -----------------------------
        self.logger.info('4. Make the PLC in stop Mode, view the event log in PLC Information;')
        success = set_plc_stop()
        if not success:
            raise CheckException('set PLC stop failed')
        self.logger.info('PLC is in `STOP` mode.')

        success = exec_cmd(PLC_INFO)
        if not success:
            raise CheckException('check PLC info failed')
        self.logger.info('open PLC information window.')

        # get PLC information window ready
        plc_win = wait_window_exists(Title.PLC)

        # get tree view control, and choose `Event Log` option
        tree_view = plc_win.child_window(class_name=Title.PLC_Tree)
        tree_view.set_focus()
        time.sleep(0.5)
        tree_view.select((1,))

        # look at the event log of the grid table
        grid = plc_win.child_window(class_name=Title.GIRD)
        grid.set_focus()

        time.sleep(3)

        close_dialog_with_button(plc_win, Button.CLOSE, btn_index=1)
        self.logger.info('4. The event log record correctly;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi004, self).cleanup()
