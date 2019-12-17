#!/usr/bin/env python

import os
import re
import time

from lib.tools.run_cmd.run_cmd import RunCMD
from lib.base.framework.smart200_base import Smart200Base


class ReachDevice(Smart200Base):
    """Determine device network status.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-11
    """

    def __init__(self):
        super(ReachDevice, self).__init__()
        self.run_cmd = RunCMD()

    def wait_for_power_off(self, ip, times=1, timeout=1200):
        """wait for ipc device power off
        Args:
            ip         type(dict)          IP address of IPC device
            times      type(int)           number of consecutive unPings
            timeout    type(int)           max waiting time
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        end_time = time.time() + timeout
        number = 0
        while time.time() < end_time:
            if not self.is_reachable(ip, False):
                number += 1
            if number >= times:
                self.logger.debug('Wait for device power off successfully, ip: %s.' % ip)
                return True

        self.logger.debug('Wait for device power off failed, ip: %s.' % ip)
        return False

    def wait_for_power_on(self, ip, times=2, timeout=1200):
        """wait for ipc device power off
        Args:
            ip         type(dict)          IP address of IPC device
            times      type(int)           number of consecutive Pings
            timeout    type(int)           max waiting time
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        end_time = time.time() + timeout
        number = 0
        while time.time() < end_time:
            if self.is_reachable(ip):
                number += 1
            if number >= times:
                self.logger.debug('Wait for device power on successfully, ip: %s.' % ip)
                return True

        self.logger.debug('Wait for device power on failed, ip: %s.' % ip)
        return False

    def is_reachable(self, ip, is_power_on=True):
        """determine if ip is ping
        Args:
            ip                type(dict)          IP address of IPC device
            is_power_on       type(true)          is wait for device power on
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        file_obj = os.popen('ping -n 1 %s' % ip)
        data = file_obj.read()
        if re.search('无法访问|unreachable', data, re.I):
            if not is_power_on:
                self.logger.debug(data)
            return False

        if is_power_on:
            self.logger.debug(data)

        return True

    def restart_local_device(self, wait_time=60):
        """wait for ipc device power off
        Args:
            wait_time    type(int)           wait time before shutdown
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        self.run_cmd.run_admin('shutdown /r /t %s' % wait_time)
