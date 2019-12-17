#!/usr/bin/env python

from lib.component.business.project.pou.pou_page.pou_base import POUBase


class POUInt(POUBase):
    """The INT POU page class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-21
    """

    def __init__(self, project, params=None):
        super(POUInt, self).__init__(project, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        public = super(POUInt, self).properties_config
        local = {'pou_type': 'POU_INT'}
        config = {**public, **local}

        return config
