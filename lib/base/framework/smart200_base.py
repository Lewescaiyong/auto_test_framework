#!/usr/bin/env python

from lib.log.log import Log


class Smart200Base(object):
    """Parent class of smart200 automation framework.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-06
    """

    def __init__(self):
        self.logger = Log
