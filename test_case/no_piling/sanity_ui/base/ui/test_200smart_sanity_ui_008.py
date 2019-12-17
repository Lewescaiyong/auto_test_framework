#!/usr/bin/env python

from lib.tools.sanity_comm.utils import *
from lib.tools.sanity_comm.file_helper import open_file
from lib.exceptions.check_exception import CheckException
from lib.base.script.gui_test.case_mw_gui import CaseMWGUI


class Test200SmartSanityUi008(CaseMWGUI):
    """Compare
    No.: test_200smart_sanity_ui_008
    Preconditions:
        1. Open Micro/WIN;  
        2. Create a new project with DB,OB,SDB;
        3. Set up connection with PLC;
    Step actions:
        1. Compare project with cpu;
        3. Download all, then compare project to cpu;
    Expected results:
        1. compare successful, the result is different, and information is correct;
        2.  compare successful, and the result is passed.
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
        super(Test200SmartSanityUi008, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN;  ')
        self.logger.info('2. Create a new project with DB,OB,SDB;')
        self.logger.info('3. Set up connection with PLC;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi008, self).process()
        typ = self.plc_info['CPUType']
        ip = self.plc_info['PLCIp']

        self.logger.info('Step actions:')

        self.logger.info('Expected results:')

        open_file(PROJECT_PATH + 'test.smart')
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

        # open another file
        success = open_file(PROJECT_PATH+'PWM.smart')
        if not success:
            raise CheckException('open new file failed')
        self.logger.info('opened new file')

        # ---------------------- connect to PLC ------------------------------
        success = get_connect_with_plc(which=ip)
        if not success:
            raise CheckException('connect to PLC failed')
        self.logger.info('connected to PLC device.')

        # ---------------------- compare different program with PLC ----------
        success = exec_cmd(PLC_COMPARE)
        if not success:
            raise CheckException('send compare cmd failed')
        self.logger.info('compare different program with in PLC.')
        # start to compare with CPU
        compare_win = wait_window_exists(Title.COMPARE)
        compare_btn = compare_win.child_window(class_name="Button", ctrl_index=0)
        click_btn(compare_btn)
        time.sleep(3)
        # get comparing result
        pb_txt = compare_win.child_window(class_name=Title.COMB, ctrl_index=0).selected_text()
        db_txt = compare_win.child_window(class_name=Title.COMB, ctrl_index=1).selected_text()
        # sb_txt = compare_win.child_window(class_name=Title.COMB, ctrl_index=2).selected_text()
        assert pb_txt.endswith('different') or pb_txt.endswith('不同')
        assert db_txt.endswith('different') or db_txt.endswith('不同')
        # assert sb_txt.endswith('different')
        close_dialog_with_button(compare_win, Button.CLOSE, btn_index=1)
        self.logger.info('2. the compare results are different.')

        # open the same file
        success = open_file(PROJECT_PATH+'test.smart')
        assert success
        self.logger.info('opened test.smart file.')

        # ---------------------- connect to PLC ------------------------------
        success = get_connect_with_plc(which=ip)
        if not success:
            raise CheckException('connect to PLC failed')
        self.logger.info('connected to PLC device.')

        # ---------------------- compare the same program with PLC -----------
        success = exec_cmd(PLC_COMPARE)
        if not success:
            raise CheckException('send compare cmd failed')
        self.logger.info('compare the same program with in PLC.')
        # start to compare with CPU
        compare_win = wait_window_exists(Title.COMPARE)
        compare_btn = compare_win.child_window(class_name='Button', ctrl_index=0)
        click_btn(compare_btn)
        time.sleep(3)
        # get comparing result
        pb_txt = compare_win.child_window(class_name=Title.COMB, ctrl_index=0).selected_text()
        db_txt = compare_win.child_window(class_name=Title.COMB, ctrl_index=1).selected_text()
        # sb_txt = compare_win.child_window(class_name=Title.COMB, ctrl_index=2).selected_text()
        assert pb_txt == 'Passed' or pb_txt == '已通过'
        assert db_txt == 'Passed' or db_txt == '已通过'
        # assert sb_txt == 'Passed'
        close_dialog_with_button(compare_win, Button.CLOSE, btn_index=1)
        self.logger.info('3. the compare results are the same.')

        # ---------------------- STOP connected PLC -----------------------------
        success = set_plc_stop()
        if not success:
            raise CheckException('set PLC stop failed')
        self.logger.info('PLC is in `STOP` mode.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Wang, Xing Yu
        IsInterface: False
        ChangeInfo: Wang, Xing Yu 2019-10-30 create
        """
        super(Test200SmartSanityUi008, self).cleanup()
