#!/usr/bin/env python

import os
import sys
import traceback
import threading

from lib.log.log import Log
from lib.tools.public.my_zip import MyZip
from lib.tools.public.common import Common
from lib.tools.public.parser import Parser
from lib.resource.resource import Resource
from lib.tools.public.compare import Compare
from lib.tools.public.checker import Checker
from lib.tools.run_cmd.run_cmd import RunCMD
from lib.tools.converter.converter import Converter
from lib.tools.public.information import Information
from lib.tools.public.reach_device import ReachDevice
from lib.tools.public.file_options import FileOptions
from lib.tools.public.gsd_file_options import GSDFileOptions


class CaseBase(object):
    """Test case top-level parent class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    is_init = False
    lock = threading.Lock()
    logger = Log
    my_zip = MyZip()
    common = Common()
    parser = Parser()
    run_cmd = RunCMD()
    compare = Compare()
    checker = Checker()
    resource = Resource()
    converter = Converter()
    information = Information()
    reach_device = ReachDevice()
    file_options = FileOptions()
    gsd_file_options = GSDFileOptions()
    case_id = 'test case base'

    def setup_class(self):
        """Initialize test resource
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """

        # remove redundant test report files
        with self.lock:
            if not CaseBase.is_init:
                self.remove_report_file()
                CaseBase.is_init = True
        # Get the case id of the current test case
        full_path = sys.modules[self.__module__].__file__
        self.case_id = os.path.basename(full_path).split('.')[0]
        # set logger object of current thread
        threading.currentThread().logger = Log(self.case_id, date_type=2, is_task=True)

    def test_process(self):
        """Executive process control
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """

        try:
            self.logger.info('Start executing the test case: [%s]' % self.case_id)
            self.prepare()
            self.process()
        except Exception:
            self.logger.error(traceback.format_exc())
            raise
        finally:
            try:
                self.cleanup()
            except Exception:
                self.logger.error(traceback.format_exc())
                raise
            self.logger.info('Test case: [%s] is completed' % self.case_id)

    def teardown_class(self):
        """Clean up the environment after script execution
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """

        self.converter.convert_log_to_html()

    def prepare(self):
        """The preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """
        self.logger.info('\n%sIn prepare...' % (' ' * 33))

    def process(self):
        """Execute the test steps
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """
        self.logger.info('\n%sIn process...' % (' ' * 33))

    def cleanup(self):
        """Clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """
        self.logger.info('\n%sIn cleanup...' % (' ' * 33))

    @classmethod
    def remove_report_file(cls, save_number=5):
        """Remove redundant test report files.
        Args:
            save_times       type(int)        number of retained logs
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        local_path = cls.information.get_framework_local_path()
        report_path = os.path.join(local_path, 'report')
        file_list = os.listdir(report_path)
        rm_list = file_list[1:-save_number]
        list(map(lambda report_file: os.remove(os.path.join(report_path, report_file)), rm_list))
