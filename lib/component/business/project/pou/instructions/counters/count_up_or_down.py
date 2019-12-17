#!/usr/bin/env python

from lib.component.business.project.pou.instructions.counters.counters_base import CountersBase


class CountUpOrDown(CountersBase):
    """The "Count Up Or Down" instruction.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-06
    """

    def __init__(self, own_software, params=None):
        super(CountUpOrDown, self).__init__(own_software, params)

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-06
        """

        public = super(CountUpOrDown, self).properties_config
        local = {'id': 312, 'locations': [{'row_add': 3, 'col_add': 0, 'id': 0}, {'row_add': 0, 'col_add': 1, 'id': 0}]}
        config = {**public, **local}

        return config
