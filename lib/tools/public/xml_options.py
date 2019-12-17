#!/usr/bin/env python

import os
import re
import datetime
from copy import deepcopy

from lib.tools.public.information import Information
from lib.tools.xml.xml_generator import XMLGenerator
from lib.base.framework.smart200_base import Smart200Base


class XMLOptions(Smart200Base):
    """XML file options.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-17
    """

    def __init__(self):
        super(XMLOptions, self).__init__()
        self.information = Information()

    @property
    def download_result_fields(self):
        """Configuration of fields in download_result_record.xml file
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-17
        """

        content = {
            'DownloadResult': {
                'MicroWIN': {'HasDownload': ''}
            }
        }

        return content

    @property
    def upgrade_result_fields(self):
        """Configuration of fields in upgrade_result_record.xml file
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-17
        """

        content = {
            'UpgradeResult': {
                'MicroWIN': {'Result': '', 'NeedRestart': ''}
            }
        }

        return content

    @property
    def normal_task_fields(self):
        """Configuration of fields in normal task file
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-17
        """

        content = {
            'Task': {
                'Info': {'TestType': '', 'TaskType': '', 'PLCNumber': '', 'ReportFile': '', 'Features': '',
                         'PLCVersion': '', 'MicroWINVersion': ''}
            }
        }

        return content

    @property
    def test_bed_fields(self):
        """Configuration of fields in test_bed.xml file
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-17
        """

        content = {
            'TestBed': {
                'GlobalConfig': {'TestType': str() or dict() or list(), 'TaskType': str() or dict() or list(),
                                 'ReportFile': str() or dict() or list()},
                'MicroWIN': {'Version': '', 'Features': ''},
                'PLCs': {'PLC': str() or dict() or list()},
            }
        }

        return content

    @property
    def need_start_fields(self):
        """Configuration of fields in need_start.xml file
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-07
        """

        content = {
            'NeedStart': {
                'Info': {'NeedStart': ''}
            }
        }

        return content

    @staticmethod
    def xml_generator(info, file_name):
        """Generator xml file
        Args:
            file_name           type(str)            the name of xml file for generator
            info                type(dict)           the contents of write to xml file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        generator = XMLGenerator(file_name)
        generator.xml_generator(info)

    def update_upgrade_result(self, software='MicroWIN', result='successfully', need_restart='yes'):
        """Update upgrade result in upgrade_result_record.xml file
        Args:
            software          type(str)          software name: MicroWIN
            result            type(str)          upgrade result: successfully, failed
            need_restart      type(str)          whether need to restart the computer
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        content = deepcopy(self.upgrade_result_fields)
        content['UpgradeResult'][software]['Result'] = result
        content['UpgradeResult'][software]['NeedRestart'] = need_restart

        files_path = self.information.get_agent_files_path()
        file_name = os.path.join(files_path, 'upgrade_result', 'upgrade_result_record.xml')
        self.xml_generator(content, file_name)

    def update_download_result(self, software='MicroWIN', has_download='yes'):
        """Update upgrade result in download_result_record.xml file
        Args:
            software          type(str)          software name: MicroWIN
            has_download      type(str)          whether has download
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        content = deepcopy(self.download_result_fields)
        content['DownloadResult'][software]['HasDownload'] = has_download

        files_path = self.information.get_agent_files_path()
        file_name = os.path.join(files_path, 'upgrade_result', 'download_result_record.xml')
        self.xml_generator(content, file_name)

    def generator_normal_task(self, parameters):
        """Generated the task file of the normal task.
        Args:
            parameters         type(dict)       task parameters
            --------------------------------------------------
            parameters details
            test_type          type(str)        Test type, enumerate: (no_piling, mw_piling, plc_piling).
            task_type          type(str)        CI task type, enumerate: (sanity, sanity_ui, full).
            plc_number         type(int)        the number of plc need to be tested.
            report_file        type(int)        the report file name of this task.
            features           type(str)        the name of the features.
            plc_version        type(int)        the version of plc to test.
            micro_win_version  type(int)        the version of micro win to test.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        content = deepcopy(self.normal_task_fields)
        content['Task']['Info']['TestType'] = parameters['test_type']
        content['Task']['Info']['TaskType'] = parameters['task_type']
        content['Task']['Info']['Features'] = parameters['features']
        content['Task']['Info']['PLCNumber'] = parameters['plc_number']
        content['Task']['Info']['ReportFile'] = parameters['report_file']
        content['Task']['Info']['PLCVersion'] = parameters['plc_version']
        content['Task']['Info']['MicroWINVersion'] = parameters['micro_win_version']

        cur_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = '%s%s.xml' % (parameters['task_type'], cur_time)
        files_path = self.information.get_agent_files_path()
        abspath = os.path.join(files_path, 'task_file', file_name)
        self.xml_generator(content, abspath)
        self.logger.info('Generator task file: %s' % abspath)

    def generator_test_bed(self, ipc_ip, plc_ip, device_info, field_config, task_info):
        """Generated test_bed.xml file.
        Args:
            plc_ip             type(list)       the ip of plc need to be tested.
            ipc_ip             type(str)        the ip of ipc need to be tested.
            device_info        type(dict)       the information detail of ipc/plc need to be tested.
            task_info          type(dict)       task information
            ------------------------------------------------------------------------------------------
            task_info details
            test_type          type(str)        Test type, enumerate: (no_piling, mw_piling, plc_piling).
            task_type          type(str)        CI task type, enumerate: (sanity, smoke, full).
            features           type(str)        the name of the features.
            plc_version        type(int)        the version of plc to test.
            micro_win_version  type(int)        the version of micro win to test.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        content = deepcopy(self.test_bed_fields)
        content['TestBed']['GlobalConfig']['TestType'] = task_info['TestType']
        content['TestBed']['GlobalConfig']['TaskType'] = task_info['TaskType']
        content['TestBed']['GlobalConfig']['ReportFile'] = task_info['ReportFile']
        content['TestBed']['MicroWIN']['Version'] = task_info['MicroWINVersion']
        content['TestBed']['MicroWIN']['Features'] = task_info['Features']

        if not plc_ip:
            content['TestBed'].pop('PLCs')

        for i, v in enumerate(plc_ip):
            plc_info = {'id': str(i + 1), 'PLCInfo': {'Version': task_info['PLCVersion']}}
            for key, value in device_info['plc_info'][v].items():
                plc_info['PLCInfo'][field_config.get(key, key)] = value
            if not content['TestBed']['PLCs']['PLC']:
                content['TestBed']['PLCs']['PLC'] = plc_info
            else:
                if isinstance(content['TestBed']['PLCs']['PLC'], dict):
                    content['TestBed']['PLCs']['PLC'] = [content['TestBed']['PLCs']['PLC']]
                content['TestBed']['PLCs']['PLC'].append(plc_info)

        # merge testbed.xml file path
        file_name = 'test_bed_%s.xml' % re.sub('\\.', '', ipc_ip)
        file_path = os.path.join(self.information.get_agent_files_path(), 'test_bed_file')
        abspath = os.path.join(file_path, file_name)
        self.xml_generator(content, abspath)
        self.logger.debug('Generator test_bed.xml for [ipc: %s].' % ipc_ip)

        return file_path, file_name

    def update_need_start(self, need_start='yes'):
        """Update need_start filed in need_start.xml file
        Args:
            need_start      type(str)          whether need to start task
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-07
        """

        content = deepcopy(self.need_start_fields)
        content['NeedStart']['Info']['NeedStart'] = need_start

        files_path = self.information.get_agent_files_path()
        file_name = os.path.join(files_path, 'server_client', 'need_start.xml')
        self.xml_generator(content, file_name)
