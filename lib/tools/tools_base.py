#!/usr/bin/env python

from lib.tools.public.common import Common
from lib.tools.public.parser import Parser
from lib.tools.public.finder import Finder
from lib.tools.run_cmd.run_cmd import RunCMD
from lib.tools.converter.converter import Converter
from lib.tools.public.information import Information
from lib.base.framework.smart200_base import Smart200Base


class ToolsBase(Smart200Base):
    """parent class of tools.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """

    def __init__(self):
        super(ToolsBase, self).__init__()
        self.common = Common()
        self.parser = Parser()
        self.finder = Finder()
        self.run_cmd = RunCMD()
        self.converter = Converter()
        self.information = Information()
