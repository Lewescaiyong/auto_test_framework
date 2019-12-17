#!/usr/bin/env python

from lib.tools.public.compare import Compare
from lib.tools.converter.converter import Converter
from lib.base.framework.no_interface.no_interface import NoInterface


class HasInterface(NoInterface):
    """Parent class of smart200 automation framework.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    def __init__(self):
        super(HasInterface, self).__init__()
        self.compare = Compare()
        self.converter = Converter()
