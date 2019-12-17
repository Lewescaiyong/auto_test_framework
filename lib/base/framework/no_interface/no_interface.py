#!/usr/bin/env python

from lib.tools.public.my_zip import MyZip
from lib.tools.public.common import Common
from lib.tools.public.parser import Parser
from lib.tools.public.finder import Finder
from lib.tools.public.checker import Checker
from lib.tools.run_cmd.run_cmd import RunCMD
from lib.tools.public.error_code import ErrorCode
from lib.tools.public.xml_options import XMLOptions
from lib.tools.public.information import Information
from lib.tools.public.reach_device import ReachDevice
from lib.tools.public.file_options import FileOptions
from lib.base.framework.smart200_base import Smart200Base
from lib.tools.public.gsd_file_options import GSDFileOptions
from lib.tools.public.task_server_device import TaskServerDevice
from lib.tools.public.package_server_device import PackageServerDevice


class NoInterface(Smart200Base):
    """Parent class of smart200 automation framework.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    def __init__(self):
        super(NoInterface, self).__init__()
        self.my_zip = MyZip()
        self.common = Common()
        self.parser = Parser()
        self.finder = Finder()
        self.run_cmd = RunCMD()
        self.checker = Checker()
        self.error_code = ErrorCode()
        self.xml_options = XMLOptions()
        self.information = Information()
        self.file_options = FileOptions()
        self.reach_device = ReachDevice()
        self.task_device = TaskServerDevice()
        self.gsd_file_options = GSDFileOptions()
        self.package_device = PackageServerDevice()
