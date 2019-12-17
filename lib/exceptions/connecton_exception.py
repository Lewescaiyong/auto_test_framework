#!/usr/bin/env python

from lib.exceptions.automation_exception import AutomationException


class ConnectionException(AutomationException):
    """The exception class for connection.
    Args:
    Example:
        raise ConnectionException('error info')
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-23
    """
