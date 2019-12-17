#!/usr/bin/env python

import time
import threading

from lib.agent.agent_base import AgentBase
from lib.agent.device.ipc_device.ipc_device_base import IPCDeviceBase


class TaskBase(AgentBase):
    """parent class for Task.
    Args:
        task_info        type(dict)       task information
        --------------------------------------------------------
        task_info details:
        TaskType         type(str)        CI task type, enumerate: (smoke, full).
        PLCNumber        type(int)        the number of plc need to be tested.
        ReportFile       type(int)        the report file name of this task.
        PLCVersion       type(int)        the version of plc to test.
        MicroWINVersion  type(int)        the version of micro win to test.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """

    lock = threading.Lock()

    def __init__(self, task_info):
        super(TaskBase, self).__init__()
        self.ipc_device = None
        self.is_print = False
        self.ipc_ip = ''
        self.plc_ip = list()
        self.device_info = dict()
        self.test_bed_path = ''
        self.test_bed_file = ''
        self.ipc_number = 1
        self.task_info = task_info

    def execute(self):
        """Execute task on IPC device
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        self.logger.info('task type: %s, report_file: %s.' % (self.task_info['TaskType'], self.task_info['ReportFile']))
        # get test device info
        self.get_test_device_info()
        # create ipc device
        self.create_ipc_device(self.device_info['ipc_info'][self.ipc_ip])
        # execute prepare steps
        self.prepare_steps()
        # generator test_bed.xml file for ipc device
        self.generator_test_bed_file()
        # copy the file to IPC device
        self.ipc_device.upload_test_bed_file(self.test_bed_path, self.test_bed_file)
        # start task on IPC device
        self.ipc_device.start_task()
        # wait for all IPC task completion
        self.common.wait_task_complete_server(self.task_info['ReportFile'])
        # release ipc/plc
        self.set_device_status(True)

    def get_test_device_info(self):
        """Get device information based on task information
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        while True:
            time.sleep(1)
            with self.lock:
                self.reset()
                # get test ipc device information
                if not self.get_ipc_device():
                    continue
                # get test ipc device information
                if not self.get_plc_device():
                    continue
                # set device status
                self.set_device_status()
            break

    def get_ipc_device(self):
        """Get ipc device
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        table = self.tables['ipc_devices']
        ipc_info = table.get_free_ipc(self.ipc_number)

        if not ipc_info:
            if not self.is_print:
                self.logger.info('Get free ipc device failed, please wait...')
                self.is_print = True
            return False

        self.device_info['ipc_info'] = ipc_info
        self.ipc_ip = list(ipc_info.keys())[0]
        self.logger.info('Get free ipc device successfully.')

        return True

    def get_plc_device(self):
        """Get plc device
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        table = self.tables['plc_devices']
        plc_info = table.get_free_plc(self.task_info['PLCNumber'])

        if not plc_info:
            if not self.is_print:
                self.logger.info('Get enough free plc device failed, please wait...')
                self.is_print = True
            return False

        self.device_info['plc_info'] = plc_info
        self.plc_ip = list(plc_info.keys())
        self.logger.info('Get enough free plc device successfully.')

        return True

    def reset(self):
        """Reset device information of the task
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        self.device_info = dict()

    def set_device_status(self, used_complete=False):
        """Set device status in database smart200
        Args:
            used_complete        type(bool)         whether the use is complete and then release the device
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        # set ipc device status
        ipc_table = self.tables['ipc_devices']
        self.logger.info('Set ipc[%s] status in smart200 database.' % self.ipc_ip)
        if used_complete:
            update_info = {'ipc_ip': self.ipc_ip}
        else:
            update_info = {
                'ipc_ip': self.ipc_ip,
                'plc_ip': '|'.join(self.plc_ip),
                'executing_task': self.task_info['TaskType']
            }
        ipc_table.update_ipc_status(update_info)

        # set plc device status
        plc_table = self.tables['plc_devices']
        self.logger.info('Set plc[%s] status in smart200 database.' % '|'.join(self.plc_ip))
        if used_complete:
            update_info = [{'plc_ip': i} for i in self.plc_ip]
        else:
            update_info = [{'plc_ip': i, 'ipc_ip': self.ipc_ip, 'executing_task': self.task_info['TaskType']}
                           for i in self.plc_ip]
        plc_table.update_plc_status(update_info)

    def prepare_steps(self):
        """The preparation steps
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-18
        """

    def generator_test_bed_file(self, plc_ip=None, task_info=None):
        """generator testbed.xml file
        Args:
            task_type          type(str)        CI task type, enumerate: (sanity, smoke, full).
            plc_ip             type(list)       the ip of plc need to be tested.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-19
        """

        if plc_ip is None:
            plc_ip = self.plc_ip

        if task_info is None:
            task_info = self.task_info

        self.test_bed_path, self.test_bed_file = self.xml_options.generator_test_bed(
            self.ipc_ip, plc_ip, self.device_info, self.database.field_config, task_info)

    def create_ipc_device(self, device_info):
        """create ipc device
        Args:
            device_info        type(dict)         ipc device's connection information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-16
        """

        self.ipc_device = IPCDeviceBase(device_info, self.task_info['TaskType'])
