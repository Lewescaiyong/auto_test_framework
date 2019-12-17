#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import paramiko

from lib.tools.public.common import Common
from lib.tools.public.finder import Finder
from lib.base.framework.smart200_base import Smart200Base


class SFTPClient(Smart200Base):
    """sftp client.
    Args:
        connect_info        type(dict)         connection information
        --------------------------------------------------
        connect_info details
        ip                  type(str)           ip address
        user                type(str)           username
        password            type(str)           password
        port                type(str)           port number
    Example:
        connect_info = {'ip': '127.127.0.1', 'user': 'admin', 'password': '123456', 'port': 22}
        sftp = SFTPClient(connect_info)
        sftp.login()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """

    def __init__(self, connect_info):
        super(SFTPClient, self).__init__()
        self.common = Common()
        self.finder = Finder()
        self.ip = connect_info['ip']
        self.user = connect_info['user']
        self.password = str(connect_info['password'])
        self.port = connect_info.get('port', 22)
        self.trans = None
        self.sftp = None
        self.sep = '\n'

    def login(self):
        """login remote sftp server.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        if not self.trans:
            self.trans = self.create_client()
        # open channel
        self.sftp = paramiko.SFTPClient.from_transport(self.trans)
        self.logger.debug('Login sftp server[%s, %s] successfully' % (self.ip, self.port))

    def create_client(self):
        """create a connection client to the remote device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        sock = self.common.create_socket(self.ip, self.port)
        trans = paramiko.Transport(sock)
        trans.connect(username=self.user, password=self.password)

        return trans

    def close(self):
        """logout remote sftp server.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        if self.sftp:
            if self.trans:
                self.trans.close()
            self.sftp.close()

        self.trans = None
        self.sftp = None

    def reconnect(self):
        """login remote sftp server again.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        self.close()
        self.login()

    def download_file(self, sftp_path, local_path, search_str, local_filename=''):
        """download file from remote sftp server.
        Args:
            sftp_path       type(str)        the path where the download file in sftp server
            local_path      type(str)        the path in local after download
            search_str      type(str)        the filename keyword of download file
            local_filename  type(bool)       file name on local path after download
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        # query all files in directory sftp_path
        files = self.query_files(sftp_path)
        # switch to the path: sftp_path
        self.change_dir(sftp_path)
        if not os.path.exists(local_path):
            os.makedirs(local_path)
        for i in files:
            if re.search(search_str, i):
                local_file = os.path.join(local_path, local_filename or i)
                self.sftp.get(i, local_file)
                self.logger.debug('Download file successfully: %s' % local_file)

    def upload_file(self, sftp_path, local_path, search_str, sftp_filename='', is_clear=False):
        """upload file to remote sftp server.
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
        ChangeInfo: cai, yong 2019-08-26
        """

        # query all files in directory sftp_path
        if os.path.isfile(local_path):
            local_path = os.path.dirname(local_path)
        absolute_path, file_name = self.finder.find(local_path, pattern=search_str)
        # clear sftp path
        if is_clear:
            self.clear_dir(sftp_path)
        # switch to the path: sftp_path
        self.change_dir(sftp_path, is_create=True)
        for index, value in enumerate(absolute_path):
            if re.search(search_str, value):
                remote_file = sftp_filename or file_name[index]
                self.sftp.put(value, remote_file)
                self.logger.debug('Upload file successfully: %s' % os.path.join(sftp_path, remote_file))

    def query_files(self, sftp_path):
        """query all files in directory "sftp_path".
        Args:
            sftp_path       type(str)        the path where the download file in sftp server
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        # switch to the root path
        self.change_dir('/')
        # query all files in directory sftp_path
        files = self.sftp.listdir(sftp_path)

        return files

    def change_dir(self, sftp_path, is_create=False):
        """change dir.
        Args:
            sftp_path       type(str)        the path in sftp server need to switch
            is_create       type(bool)       whether to create it if the sftp_path does not exist
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        for i in range(2):
            try:
                self.sftp.chdir(sftp_path)
            except FileNotFoundError:
                if is_create:
                    self.create_dir(sftp_path)
                else:
                    break
            else:
                break

    def create_dir(self, sftp_path):
        """change dir.
        Args:
            sftp_path       type(str)        the path in sftp server need to create
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        self.sftp.mkdir(sftp_path)
        self.logger.debug('Create path in sftp server: %s' % sftp_path)

    def clear_dir(self, sftp_path):
        """clear dir.
        Args:
            sftp_path       type(str)        the path in sftp server need to clear
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        files = self.query_files(sftp_path)

        for i in files:
            file_path = os.path.join(sftp_path, i)
            if self.is_dir(file_path):
                self.clear_dir(file_path)

        self.sftp.rmdir(sftp_path)

    def is_dir(self, sftp_path):
        """check if the sftp_path is a dir .
        Args:
            sftp_path       type(str)        the path in sftp server
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        try:
            self.sftp.remove(sftp_path)
            result = False
        except IOError:
            result = True

        return result
