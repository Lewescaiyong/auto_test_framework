#!/usr/bin/env python

from lib.base.framework.smart200_base import Smart200Base


class ConnectionBase(Smart200Base):
    """The base class for connection class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-23
    """

    def check_is_active(self):
        """Get connection object.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-12
        """
        if not self.is_active():
            self.reconnect()

    def reconnect(self):
        """login remote device again.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

    def is_active(self):
        """get connection status.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        return True
