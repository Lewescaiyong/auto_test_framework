#!/usr/bin/env python

from lib.tools.sanity_comm.utils import *
from lib.exceptions.check_exception import CheckException
from lib.base.script.gui_test.case_mw_gui import CaseMWGUI
from lib.tools.sanity_comm.file_helper import open_file, new_file


class Test200SmartSanityUi005(CaseMWGUI):
    """Clear all
    No.: test_200smart_sanity_ui_005
    Preconditions:
        1. Open Micro/WIN as administrator;  
        2. Set up connection with PLC;
        3. Create a new project with DB,OB,SDB;
    Step actions:
        1. Download all to the PLC;
        2. Clear all(PLC-Modify-Clear);
        3. Upload all to a new project; ;
    Expected results:
        1. Download successful;
        2. Clear successful;
        3. Upload successful, all blocks is cleared in the project, ip and station name and day clock is not cleared;
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
        super(Test200SmartSanityUi005, self).prepare()

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
        super(Test200SmartSanityUi005, self).process()
        typ = self.plc_info['CPUType']
        ip = self.plc_info['PLCIp']

        self.logger.info('Step actions:')

        self.logger.info('Expected results:')

        open_file(PROJECT_PATH + 'MOV.smart')
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
        self.logger.info('Make the PLC in run Mode,view the status of PLC and program;')
        success = set_plc_run()
        self.logger.info('PLC in run mode, and the program run normally;')
        if not success:
            raise CheckException('set PLC run failed')

        # ---------------------- STOP connected PLC -----------------------------
        success = set_plc_stop()
        if not success:
            raise CheckException('set PLC stop failed')
        self.logger.info('PLC is in `STOP` mode.')

        # ---------------------- Clear all -------------------------------------
        self.logger.info('2. Clear all(PLC-Modify-Clear);')
        success = exec_cmd(CLEAR_ALL)
        # clear system block window operation
        handle_popup_dialog(Title.WIN_SMART, Button.NO, btn_index=0)

        clear_win = wait_window_exists(Title.CLEAR)

        # choose 'Close dialog on success' option
        set_check_box(clear_win, OPT_CLOSE, index=5)

        # click `Clear` button to close the window
        close_dialog_with_button(clear_win, Button.CLEAR, btn_index=7)

        self.logger.info('2. Clear successful;')
        if not success:
            raise CheckException('clear all failed')

        success = new_file()
        if not success:
            raise CheckException('create new file failed')

        # ---------------------- connect to PLC ---------------------------------
        success = get_connect_with_plc(which=ip)
        if not success:
            raise CheckException('connect to PLC failed')
        self.logger.info('connected to PLC device.')

        # ---------------------- upload all from PLC ---------------------
        self.logger.info('3. Upload all to a new project;')
        success = upload_from_plc(PLC_UPLOAD_ALL)
        self.logger.info('3. Upload  successful;')
        if not success:
            raise CheckException('upload all from PLC failed')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi005, self).cleanup()
