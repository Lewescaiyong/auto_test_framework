#!/usr/bin/env python

import os

from lib.tools.xml.xml_parser import XMLParser
from lib.component.software.plc.plc_base import PLCBase
from lib.base.framework.has_interface.has_interface import HasInterface
from lib.component.software.micro_win.micro_win_base import MicroWINBase


class Resource(HasInterface):
    """The class of test resource consolidation.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    def __init__(self):
        super(Resource, self).__init__()
        self.micro_win = None
        self.plc = dict()
        self.test_bed_info = dict()
        self.initialize()

    def initialize(self):
        """Initialize test resource.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """
        # parse test_bed.xml
        self.parse_test_bed()

        # create Micro/WIN
        if 'MicroWIN' in self.test_bed_info:
            self.create_mw(self.test_bed_info['MicroWIN'])

        # create PLC
        if 'PLCs' in self.test_bed_info:
            self.create_plc(self.test_bed_info['PLCs'])

    def parse_test_bed(self):
        """parse test_bed.xml file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        local_path = self.information.get_framework_local_path()
        test_bed = os.path.join(local_path, 'lib', 'config', 'test_bed.xml')
        self.test_bed_info = XMLParser(test_bed).xml_parser()['TestBed']

    def create_mw(self, info):
        """initialize micro/win object.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        micro_win = MicroWINBase(info)
        self.micro_win = micro_win

    def create_plc(self, info):
        """initialize plc object.
        Args:
            info          type(dict)           plc info
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        plc_info = info['PLC']
        if isinstance(plc_info, dict):
            plc_info = [plc_info]
        for i in plc_info:
            plc = self.create_single_plc(i)
            self.plc[plc.id] = plc

    def create_single_plc(self, info):
        """initialize plc object.
        Args:
            info          type(dict)           single plc info
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        plc = PLCBase(info, self.micro_win)

        return plc


if __name__ == '__main__':
    resource = Resource()
    resource.initialize()
    print(1)
