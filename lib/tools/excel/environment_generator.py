#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.tools.excel.excel_generator import ExcelGenerator


class EnvironmentGenerator(ExcelGenerator):
    """Generator environment_info.xlsx file.
    Args:
    Example:
        ger = EnvironmentGenerator("environment_info.xlsx", sheet_info)
        ger.excel_generator()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """

    width_config = {
        'IpcIP': 256 * 18,
        'UserName': 256 * 18,
        'Password': 256 * 18,
        'Port': 256 * 10,
        'FrameworkPath': 256 * 30,
        'PackagePath': 256 * 30,
        'Status': 256 * 10,
        'ExecutingTask': 256 * 18,
        'PlcIP': 256 * 18,
    }
