#!/usr/bin/env python

import os
import datetime
import threading

from lib.log.log import Log
from lib.resource.resource import Resource
# from lib.tools.case_related.back_fill.back_fill import BackFill
from lib.tools.case_related.copy_case_to_task import CopyCaseToTask
from lib.base.framework.has_interface.has_interface import HasInterface
from test_case.no_piling.common.base.upgrade.test_200smart_common_upgrade_001 import Test200SmartCommonUpgrade001


class AutomationScript(HasInterface):
    """Automation task start file.
    Args:
    Example:
        python automation_script.py
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-19
    """

    def __init__(self):
        super(AutomationScript, self).__init__()
        self.init_logger()
        self.mw_version = ''
        self.cpu_version = ''
        self.resource = Resource()
        self.task_start_time = None
        self.get_version_information()
        self.task_type = self.resource.test_bed_info['GlobalConfig']['TaskType']

    def run(self):
        """Start to perform
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        self.logger.info('-' * 80)
        self.logger.info('Start executing CI task...')
        self.logger.info(r'Copy the cases that need to be executed into the directory: smart200\test_case\task')
        copier = CopyCaseToTask(self.resource.test_bed_info)
        copier.copy_case()
        self.logger.info(r'Start executing the test case script...')
        self.execute_test_case()
        self.init_logger()
        report_file = self.common.wait_report_generate_client(self.task_start_time)
        self.logger.info('Kill process pytest.exe')
        self.common.kill_process('pytest.exe')
        self.logger.info(r'Start back filling test case execution results...')
        # description_info = {'mw_version': self.mw_version, 'cpu_version': self.cpu_version}
        # back_fill = BackFill(self.task_type, description_info)
        # back_fill.back_fill()
        if self.task_type != 'upgrade_micro_win' and self.resource.test_bed_info['GlobalConfig']['ReportFile']:
            self.logger.info(r'Upload report file to server device.')
            self.task_device.upload_report(report_file, self.resource.test_bed_info['GlobalConfig']['ReportFile'])
        self.logger.info(r'CI task execution is completed.')
        self.converter.convert_log_to_html(log_files=('initialize.txt',))

    @staticmethod
    def init_logger():
        """Initialize logger object for current thread
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        threading.currentThread().logger = Log('initialize', date_type=1)

    def get_version_information(self):
        """Get Micro/WIN and CPU version information.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        info = self.information.get_version_information(self.resource)
        self.mw_version = info['mw_version']
        self.cpu_version = info['cpu_version']

    def execute_test_case(self):
        """Executing the test case script.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        # upgrade firmware
        # self.upgrade_firmware()

        # record task start time
        self.task_start_time = datetime.datetime.now()

        # executing the test case script
        local_path = self.information.get_framework_local_path()
        test_case_path = os.path.join(local_path, 'test_case', 'task')
        cmd = r'pytest %s' % test_case_path
        self.run_cmd.run_admin(cmd, mode=1)

    def upgrade_firmware(self):
        """Upgrade firmware.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        if self.task_type != 'upgrade_micro_win':
            case = Test200SmartCommonUpgrade001()
            case.setup_class()
            case.test_process()
            case.teardown_class()


if __name__ == '__main__':
    AutomationScript().run()
