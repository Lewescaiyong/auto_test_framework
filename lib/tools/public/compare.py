#!/usr/bin/env python

from lib.tools.tools_base import ToolsBase


class Compare(ToolsBase):
    """Compare class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-27
    """

    def compare_c_str(self, str_1, str_2, length=None):
        """Compare if two c_str are equal
        Args:
            str1          type(c_str, p_str)          a string used for comparision
            str2          type(c_str, p_str)          a string used for comparision
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """
        if isinstance(str_1, str):
            str_1 = self.converter.convert_data_type(str_1, 'c_str')
        if isinstance(str_2, str):
            str_2 = self.converter.convert_data_type(str_2, 'c_str')

        if length is None:
            result = self.converter.interface.compare_CString1(str_1, str_2)
        else:
            result = self.converter.interface.compare_CString4(str_1, str_2, length)

        return result
