#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase


class IOSymbols(BusinessBase):
    """I/O Symbols table class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-25
    """

    def __init__(self, own_software, params=None):
        super(IOSymbols, self).__init__(own_software, params)
