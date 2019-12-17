#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase


class TableNormal(BusinessBase):
    """Table1, Table2, Table3....
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-25
    """

    def __init__(self, own_software, params=None):
        super(TableNormal, self).__init__(own_software, params)
