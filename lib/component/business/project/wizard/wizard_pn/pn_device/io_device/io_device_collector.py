#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.wizard.wizard_pn.pn_device.io_device.by_gsd.gsd_i_device import GSDIDevice
from lib.component.business.project.wizard.wizard_pn.pn_device.io_device.by_catalog.catalog_i_device import \
    CatalogIDevice


class IODeviceCollector(BusinessBase):
    """POU collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-20
    """

    def __init__(self, own_software, params=None):
        super(IODeviceCollector, self).__init__(own_software, params)

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

        config = {'gsd_i_device': GSDIDevice, 'catalog_i_device': CatalogIDevice}

        return config
