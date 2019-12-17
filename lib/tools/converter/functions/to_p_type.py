#!/usr/bin/env python


def convert_to_p_int(self, data):
    """Convert python object to p_type int
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    return self.convert(data, int)


def convert_to_p_float(self, data):
    """Convert python object to p_type float
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-26
    """

    return self.convert(data, float)


def convert_to_p_str(self, data):
    """Convert python object to p_type str
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    return self.convert(data, str)


def convert_to_p_bool(self, data):
    """Convert python object to p_type bool
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    return self.convert(data, bool)


def convert_to_p_type(self, data):
    """Convert python object to p_type
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    return self.convert(data, lambda x: x)
