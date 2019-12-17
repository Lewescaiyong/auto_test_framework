# !/usr/bin/python3
# coding: utf-8

import os
import threading

from lib.tools.public.information import Information
from lib.base.framework.smart200_base import Smart200Base


class RunCMD(Smart200Base):
    """Run windows cmd.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-19
    """

    lock = threading.Lock()

    def __init__(self):
        super(RunCMD, self).__init__()
        self.information = Information()

    def run_admin(self, cmd, mode=1):
        """Run windows cmd as administrator.
        Args:
            cmd        type(str)        the command need to be executed.
            mode       type(int)        run type: (0: hide the cmd window, 1: display the cmd window).
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-17
        """

        with self.lock:
            self.update_vbs_admin(mode)
            self.update_bat(cmd)
            self.cmd()

    def run_normal(self, cmd):
        """run windows cmd normally.
        Args:
            cmd        type(str)        the command need to be executed.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-17
        """

        with self.lock:
            self.update_vbs_normal()
            self.update_bat(cmd)
            self.cmd()

    def update_vbs_admin(self, mode=1):
        """run windows cmd.
        Args:
            mode        type(int)        run type: (0: normal, 1: admin).
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-17
        """

        vbs_cmd = r"""
cwd = CreateObject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
path = cwd & "\cmd.bat"

Set shell = CreateObject("Shell.Application")
shell.ShellExecute path,"","","runas",%s

WScript.Quit
""" % mode

        local_path = self.information.get_framework_local_path()
        vbs_file = os.path.join(local_path, 'lib', 'tools', 'run_cmd', 'shell.vbs')
        with open(vbs_file, 'w') as f:
            f.write(vbs_cmd)

    def update_vbs_normal(self):
        """run windows cmd.
        Args:
            mode        type(int)        run type: (0: normal, 1: admin).
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-17
        """

        vbs_cmd = r"""
cwd = CreateObject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
path = cwd & "\cmd.bat"

Set shell = CreateObject("WScript.Shell")
shell.run "cmd /c" & path

WScript.Quit
"""

        local_path = self.information.get_framework_local_path()
        vbs_file = os.path.join(local_path, 'lib', 'tools', 'run_cmd', 'shell.vbs')
        with open(vbs_file, 'w') as f:
            f.write(vbs_cmd)

    def update_bat(self, cmd):
        """run windows cmd.
        Args:
            cmd        type(str)        the command need to be executed.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-17
        """

        local_path = self.information.get_framework_local_path()
        bat_file = os.path.join(local_path, 'lib', 'tools', 'run_cmd', 'cmd.bat')
        with open(bat_file, 'w') as f:
            f.write(cmd + '\n')
            f.write('exit' + '\n')

    def cmd(self):
        """run windows cmd.
        Args:
            file_name        type(str)        the file to be executed.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-17
        """

        local_path = self.information.get_framework_local_path()
        vbs_file = os.path.join(local_path, 'lib', 'tools', 'run_cmd', 'shell.vbs')
        os.system(vbs_file)
