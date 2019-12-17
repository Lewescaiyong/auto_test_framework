#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import datetime
from xml.etree.ElementTree import ParseError

from lib.tools.xml.xml_parser import XMLParser
from lib.agent.device.device_base import DeviceBase
from lib.exceptions.check_exception import CheckException


class IPCDeviceBase(DeviceBase):
    """IPC device base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
    """

    @property
    def conn_info(self):
        """Host class
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        conn_info = {
            'ip': self.device_info['ipc_ip'],
            'user': self.device_info['user_name'],
            'password': self.device_info['password'],
            'port': self.device_info['port']
        }

        return conn_info

    @property
    def sftp_info(self):
        """Host class
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-15
        """

        sftp_info = dict()
        sftp_info['ip'] = self.device_info['ipc_ip']
        sftp_info['user'] = self.device_info['sftp_user']
        sftp_info['password'] = self.device_info['sftp_password']
        sftp_info['sftp_path'] = self.device_info['sftp_path']

        return sftp_info

    def sftp_download(self, sftp_path, local_path, search_str, local_filename=''):
        """Download file from IPC
        Args:
            sftp_path       type(str)        the path where the download file in sftp server
            local_path      type(str)        the path in local after download
            search_str      type(str)        the filename keyword of download file
            local_filename  type(bool)       file name on local path after download
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-16
        """

        sftp = self.create_sftp_client()
        sftp.download_file(sftp_path, local_path, search_str, local_filename)
        sftp.close()

    def sftp_upload(self, sftp_path, local_path, search_str, sftp_filename='', is_clear=False):
        """Upload file to IPC.
        Args:
            sftp_path       type(str)        the path in sftp server after upload
            local_path      type(str)        the path where the upload file in local
            search_str      type(str)        the filename keyword of upload file
            sftp_filename   type(bool)       file name on sftp path after upload
            is_clear        type(bool)       whether to clear it before upload
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-16
        """

        sftp = self.create_sftp_client()
        sftp.upload_file(sftp_path, local_path, search_str, sftp_filename, is_clear)
        sftp.close()

    def upload_test_bed_file(self, file_path, file_name):
        """Upload the test_bed.xml file to IPC device
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-16
        """

        self.logger.info('Upload test_bed.xml to ipc: %s.' % self.conn_info['ip'])
        # copy file to ipc device
        remote_path = self.sftp_info['sftp_path'] + '/lib/config'
        self.sftp_upload(remote_path, file_path, file_name, sftp_filename='test_bed.xml')
        # remove test_bed.xml of current task
        self.logger.info('Delete test_bed file[%s] of [ipc: %s] which on server device.' % (
            file_name, self.conn_info['ip']))
        os.remove(os.path.join(file_path, file_name))

    def start_task(self):
        """Start task on IPC device
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-16
        """

        # record task start time
        self.task_start_time = datetime.datetime.now()

        # update framework code on ipc
        self.logger.info('Update framework code on ipc: [%s].' % self.conn_info['ip'])
        self.run(cmd='git pull', directory=self.device_info['framework_path'])

        # upgrade interface api on ipc
        self.logger.info('Upgrade interface api on ipc: [%s].' % self.conn_info['ip'])
        directory = os.path.join(
            self.device_info['framework_path'], 'test_case', 'no_piling', 'common', 'base', 'upgrade')
        result = self.run(cmd='python zest_200smart_common_upgrade_001.py', directory=directory, timeout=120)
        if not self.parser.parse_upgrade_result(result['stdout']):
            self.logger.info('Upgrade interface api failed')
            if self.task_type not in ('upgrade_micro_win',):
                raise CheckException('Upgrade interface api failed.')

        # start task on ipc
        self.logger.info('Start task on ipc: [%s].' % self.conn_info['ip'])
        self.upload_need_start()
        # directory = os.path.join(self.device_info['framework_path'], 'lib')
        # self.run(cmd='python automation_script.py', directory=directory, timeout=20)

    def wait_upgrade_complete(self):
        """Wait for IPC software upgrade to completion
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        # whether restart is required to ipc device
        need_restart = self.is_need_to_restart()
        # update upgrade_result_record.xml file
        self.update_upgrade_result()
        if not need_restart:
            self.logger.info('Not need to restart IPC device: %s.' % self.conn_info['ip'])
            time.sleep(60)
            return
        # wait for ipc device restart
        self.wait_restart_complete()

    def is_need_to_restart(self):
        """Whether restart is required to ipc after software upgrade
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        files_path = self.information.get_agent_files_path()
        file_name = os.path.join(files_path, 'upgrade_result', 'upgrade_result_record.xml')

        while True:
            time.sleep(5)
            try:
                self.download_upgrade_result()
                info = XMLParser(file_name).xml_parser()
            except ParseError:
                continue
            else:
                need_restart = info['UpgradeResult']['MicroWIN']['NeedRestart']
                if need_restart:
                    self.logger.info('Got field [NeedRestart: %s] from IPC device: %s.' % (
                        need_restart, self.conn_info['ip']))
                    return need_restart.lower() == 'yes'

    def download_upgrade_result(self):
        """Download upgrade_result_record.xml file from IPC
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        self.logger.info('Download upgrade_result_record.xml from ipc: %s.' % self.conn_info['ip'])
        sftp_path = self.sftp_info['sftp_path'] + '/lib/agent/files/upgrade_result'
        local_path = os.path.join(self.information.get_agent_files_path(), 'upgrade_result')
        search_str = 'upgrade_result_record'
        self.sftp_download(sftp_path, local_path, search_str)

    def update_upgrade_result(self):
        """Upload download_result_record.xml file to IPC
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        self.logger.info('Upload upgrade_result_record.xml to ipc: %s.' % self.conn_info['ip'])
        # update upgrade_result_record.xml file
        self.xml_options.update_upgrade_result(result='', need_restart='')
        # upload upgrade_result_record.xml file to ipc device
        remote_path = self.sftp_info['sftp_path'] + '/lib/agent/files/upgrade_result'
        local_path = os.path.join(self.information.get_agent_files_path(), 'upgrade_result')
        search_str = 'upgrade_result_record'
        self.sftp_upload(remote_path, local_path, search_str)

    def upload_need_start(self):
        """Upload need_start.xml file to IPC
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-07
        """

        self.logger.info('Upload need_start.xml to ipc: %s.' % self.conn_info['ip'])
        # update download_result_record.xml
        self.xml_options.update_need_start(need_start='yes')
        # copy file to ipc device
        remote_path = self.sftp_info['sftp_path'] + '/lib/agent/files/server_client'
        local_path = os.path.join(self.information.get_agent_files_path(), 'server_client')
        search_str = 'need_start'
        self.sftp_upload(remote_path, local_path, search_str)

    def wait_restart_complete(self):
        """Wait for IPC restart to completion
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        # wait for shutdown
        self.host.wait_restart_complete()
