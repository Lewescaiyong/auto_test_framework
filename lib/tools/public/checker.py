#!/usr/bin/env python

import win32com.client

from lib.base.framework.smart200_base import Smart200Base


class Checker(Smart200Base):
    """check class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    def process_is_running(self, name, print_log=True):
        """Check the process whether is running.
        Args:
            name            type(str)        the name of the process.
            print_log       type(bool)       whether to echo log
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-19
        """

        wmi = win32com.client.GetObject('winmgmts:')
        total_name = [i.Name for i in wmi.InstancesOf('win32_process')]
        if name in total_name:
            if print_log:
                self.logger.debug('The process [%s] is running.' % name)
            result = True
        else:
            if print_log:
                self.logger.debug('The process [%s] is not running.' % name)
            result = False

        return result
