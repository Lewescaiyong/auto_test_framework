#!/usr/bin/env python

from lib.tools.sanity_comm.utils import *
from lib.tools.sanity_comm.file_helper import open_file
from lib.exceptions.check_exception import CheckException
from lib.base.script.gui_test.case_mw_gui import CaseMWGUI


class Test200SmartSanityUi007(CaseMWGUI):
    """Force/Unforce
    No.: test_200smart_sanity_ui_007
    Preconditions:
        1. Open Micro/WIN as administrator;  
        2. Set up connection with PLC;
    Step actions:
        1. Create a MOV project with Q output, Download all to the PLC;
        2. Make the PLC in run Mode, open status chart in Debug, Force  a new value to output, View the status of PLC and program;
        3. Unforce the forced new value;
    Expected results:
        1. Download successful;
        2. PLC in run mode, the output value is same with the forced new value;
        3. Unforce successful, the output is the normal output of the program;
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
        super(Test200SmartSanityUi007, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN as administrator;  ')
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
        super(Test200SmartSanityUi007, self).process()
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
        self.logger.info('1. Create a MOV project with Q output, Download all to the PLC;')
        success = download_to_plc(PLC_DOWNLOAD_ALL)
        self.logger.info('1. Download successful;')
        if not success:
            raise CheckException('download failed')

        # ---------------------- RUN connected PLC ------------------------------
        self.logger.info('2. Make the PLC in run Mode, open status chart in Debug, Force  a new value to output, View the status of PLC and program;')
        success = set_plc_run()
        self.logger.info('2. PLC in run mode')
        if not success:
            raise CheckException('set PLC run failed')

        self.logger.info('open status chart.')
        success = exec_cmd(STATUS_CHART)
        if not success:
            raise CheckException('set PLC run failed')

        status_chart = self.smart_app.SmartApp[Title.STATUS_CHART]
        try:
            grid = status_chart.child_window(class_name=Title.GIRD)
            grid.set_focus()
        except Exception:
            status_chart = self.smart_app.SmartApp[Title.STATUS_CHART_ZH]
            grid = status_chart.child_window(class_name=Title.GIRD)
            grid.set_focus()

        # input addr and value in grid cell
        set_grid_text(1, 1, 'Q0.7', grid)
        time.sleep(1)
        set_grid_text(1, 4, '1', grid)

        # force input value to PLC
        success = exec_cmd(DEBUG_FORCE)
        if not success:
            raise CheckException('Force value failed')
        self.logger.info('3. Force  a new value to output, View the status of PLC and program;')

        time.sleep(3)

        # unforce input value to PLC
        success = exec_cmd(DEBUG_UNFORCE)
        if not success:
            raise CheckException('Unforce the forced new value failed')
        self.logger.info('4. Unforce the forced new value;')

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
        super(Test200SmartSanityUi007, self).cleanup()
