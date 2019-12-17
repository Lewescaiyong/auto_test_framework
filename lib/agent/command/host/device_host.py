#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.command.host.host_base import HostBase


class DeviceHost(HostBase):
    """Device Host class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
    """

    def wait_restart_complete(self):
        """Wait for IPC restart to completion
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

        # wait for power off
        self.reach_device.wait_for_power_off(self.params['conn_info']['ip'])
        # wait for power on
        self.reach_device.wait_for_power_on(self.params['conn_info']['ip'])
        # reconnect
        self.conn_pool.reset()
