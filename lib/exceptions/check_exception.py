#!/usr/bin/env python

from lib.exceptions.automation_exception import AutomationException


class CheckException(AutomationException):
    """The exception class for check.
    Args:
    Example:
        raise CheckException('error info')
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-19
    """
