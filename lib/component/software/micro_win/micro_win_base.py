#!/usr/bin/env python

import winreg

from lib.component.business.project.project import Project
from lib.component.software.software_base import SoftwareBase
from lib.component.business.upgrade.micro_win_upgrade.micro_win_upgrade import MicroWINUpgrade


class MicroWINBase(SoftwareBase):
    """Micro/WIN parent class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    def __init__(self, params):
        super(MicroWINBase, self).__init__(params)
        self.conn_ip = ''
        self.conn_plc = None
        self.is_env_init = False
        self.project = self.find('project')

    @property
    def version(self):
        """The information of firmware.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-24
        """
        if self.information.check_windows_if_64():
            key = 'SOFTWARE\\Wow6432Node\\Siemens\\AUTSW\\MicroWIN SMART'
        else:
            key = 'SOFTWARE\\Siemens\\AUTSW\\MicroWIN SMART'

        try:
            explorer = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
            version = winreg.QueryValueEx(explorer, 'Release')[0]
        except (FileNotFoundError, OSError):
            version = ''

        return version

    def test_env_init(self):
        """Initialize the test environment.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        if not self.is_env_init:
            self.dispatch('test_env_init')
            self.dispatch('load_instruction_libs')
            self.is_env_init = True

    def create_session(self, plc=None):
        """create connection with plc
        Args:
            plc            type(lib.component.plc.plc.PLC)      PLC to be connected to Micro/WIN.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """
        plc = plc or self.conn_plc
        if self.conn_ip == plc.ip:
            self.logger.debug('The current connection is already with plc[%s]' % plc.ip)
            return

        self.test_env_init()
        params = {'ipAddress': plc.ip}
        self.dispatch('create_session', params)
        self.set_connect_plc(plc)

    def set_connect_plc(self, plc=None, record_ip=True):
        """Set connection info of plc
        Args:
            plc            type(lib.component.plc.plc.PLC)      PLC to be connected to Micro/WIN.
            record_ip      type(bool)                           whether to record plc ip.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """
        if not plc:
            self.conn_ip = ''
        else:
            self.conn_plc = plc
            if record_ip:
                self.conn_ip = plc.ip

    @property
    def register_views(self):
        """The wrapper views needs to register
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        views = {
            'IntegrationMW': 'lib.wrapper.integration_mw.integration_mw'
        }

        return views

    @property
    def business_config(self):
        """Config the businesses type that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        business = ('project', 'upgrade')

        return business

    @property
    def log_str(self):
        """Define the log str for invoking interface
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        return 'Current connected PLC: %s' % self.conn_ip

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        config = {'project': Project, 'upgrade': MicroWINUpgrade}

        return config

    def compare_with_plc(self, plc=None):
        """Compare the project between MicroWin and PLC device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-09
        """

        result = dict()

        plc = plc or self.conn_plc
        params = {'rOptions': {'ip': plc.ip, 'cpu_type': plc.cpu_type}}
        info = self.dispatch('compare_with_plc', params)
        for k, v in info['pResults'].items():
            result[k] = not v.GetSize()

        return result

    def test_prepare(self, prj_name='a_new_project.smart', is_close=True, is_download=True, plc=None):
        """Prepare to test the download or upload functionality
        Args:
            prj_name          type(str)         the name of the project file to reset the plc project
            is_close          type(bool)        whether to close the project after download
            is_download       type(str)         whether download to PLC device
            plc               type(bool)        the PLC device which to be reset project, default current connect plc
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-09
        """

        if plc:
            plc.create_session()

        self.project.project_close()
        self.project.project_open(prj_name)

        if is_download:
            self.project.project_download()

        if is_close:
            self.project.project_close()
