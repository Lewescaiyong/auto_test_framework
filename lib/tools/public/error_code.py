#!/usr/bin/env python

from lib.base.framework.smart200_base import Smart200Base


class ErrorCode(Smart200Base):
    """Error code summary.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-13
    """

    @property
    def error_code_config(self):
        """[Error code --> reasonable prompt] config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-13
        """

        config = {
            -1610610847: 'State name conversion error.'
        }

        return config
