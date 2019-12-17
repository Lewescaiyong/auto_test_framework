#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.pou_page.pou_sbr.pou_sbr import POUSbr
from lib.component.business.project.pou.pou_page.pou_int.pou_int import POUInt
from lib.component.business.project.pou.pou_page.pou_main.pou_main import POUMain


class POUCollector(BusinessBase):
    """POU collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-20
    """

    def __init__(self, own_software, params=None):
        super(POUCollector, self).__init__(own_software, params)

    @property
    def business_config(self):
        """Config the businesses type that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        business = ('pou_main', 'pou_sbr', 'pou_int')

        return business

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        config = {'pou_main': POUMain, 'pou_sbr': POUSbr, 'pou_int': POUInt}

        return config
