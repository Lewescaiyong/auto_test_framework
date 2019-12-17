#!/usr/bin/env python

from lib.exceptions.automation_exception import AutomationException


class NotFoundException(AutomationException):
    """The exception class for find.
    Args:
    Example:
        raise NotFoundException('error info')
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-19
    """
