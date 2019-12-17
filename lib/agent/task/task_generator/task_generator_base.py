#!/usr/bin/env python

import datetime
import argparse
import threading
from argparse import RawDescriptionHelpFormatter

from lib.log.log import Log
from lib.exceptions.check_exception import CheckException
from lib.base.framework.has_interface.has_interface import HasInterface


class TaskGeneratorBase(HasInterface):
    """Receive jenkins data and generator task file.
    Args:
        task_type        type(str)        CI task type, enumerate: (sanity, sanity_ui, full).
        ipc_number       type(int)        the number of ipc need to be tested.
        plc_number       type(int)        the number of plc need to be tested.
        version          type(str)        the version of software
    Example:
        C:\\Users>python generator_task_file.py -t smoke -p 2
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-19
    """

    def __init__(self):
        super(TaskGeneratorBase, self).__init__()
        self.parameters = dict()
        self.init_logger()

    def run(self):
        """receive task information
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        self.logger.info('-' * 80)
        self.logger.info('Receiving task information...')
        self.logger.info('Parsing command-line parameters...')
        self.process_cmd_args()
        self.logger.info(r'Task parameters: %s' % self.parameters)
        self.xml_options.generator_normal_task(self.parameters)
        self.common.wait_task_complete_server(self.parameters['report_file'])
        self.converter.convert_log_to_html(log_files=(self.information.get_current_thread_log_file(),))

    @staticmethod
    def init_logger():
        """Parse task args
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        date = datetime.datetime.now().strftime("%H%M%S")
        threading.currentThread().logger = Log('generator_task_%s' % date, date_type=1)

    def process_cmd_args(self):
        """Process cmd args
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        msg = """
        *************************************************************

        *               S7-200 SMART Integration test               *

        *************************************************************
        smart200 is an automation framework for S7-200 SMART business
        testing, based on python. 
        """
        parser = argparse.ArgumentParser(description=msg, formatter_class=RawDescriptionHelpFormatter)
        self.parser_cmd_args(parser)

    def parser_cmd_args(self, parser):
        """Parse all cmd args
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        parser.add_argument("-te", "--test_type", dest="test_type",
                            help="Test type, enumerate: (no_piling, mw_piling, plc_piling).", default='no_piling')
        parser.add_argument("-ta", "--task_type", dest="task_type",
                            help="CI task type, enumerate: (sanity, sanity_ui, full).", required=True)
        parser.add_argument("-f", "--features", dest="features",
                            help="Features, enumerate: (project, download, upload...).", default='')
        parser.add_argument("-r", "--report_file", dest="report_file", help="report file name.", required=True)
        parser.add_argument("-p", "--plc_number", dest="plc_number", help="PLC number.", default=1)
        parser.add_argument("-pv", "--plc_version", dest="plc_version", help="PLC version to test.", default='')
        parser.add_argument("-mv", "--micro_win_version", dest="micro_win_version", help="MicroWIN version to test.",
                            default='')

        # parse all cmd args
        args = parser.parse_args()
        self.check_cmd_args(args)
        self.parameters['test_type'] = args.test_type
        self.parameters['task_type'] = args.task_type.lower()
        self.parameters['features'] = args.features
        self.parameters['report_file'] = args.report_file
        self.parameters['plc_number'] = str(args.plc_number)
        self.parameters['plc_version'] = args.plc_version
        self.parameters['micro_win_version'] = args.micro_win_version

    @staticmethod
    def check_cmd_args(args):
        """Automation task start file.
        Args:
            args        type(Namespace)        all cmd args.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        if args.task_type.lower() not in ('sanity', 'sanity_ui', 'full'):
            raise CheckException("The parameter task_type can only be smoke/full, please check!")
