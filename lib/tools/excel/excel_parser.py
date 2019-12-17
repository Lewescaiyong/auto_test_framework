#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

from lib.tools.tools_base import ToolsBase


class ExcelParser(ToolsBase):
    """parse excel file to dict.
    Args:
        file_name           ype(str)            the absolute_path of xml file
        title_line          type(int)           the line id of title
        value_line          type(int)           the line id of first value line
        sheet_index         type(int)           the index id of sheet to parse
        sheet_name          type(str)           the name of sheet to parse
    Example:
        parser = ExcelParser(file_name=r'C:\file.xls')
        result = parser.excel_parser()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """
    
    def __init__(self, file_name, title_line=0, value_line=1, sheet_index=0, sheet_name=None):
        super(ExcelParser, self).__init__()
        self.file_name = file_name
        self.title_line = title_line
        self.value_line = value_line
        self.sheet_index = sheet_index
        self.sheet_name = sheet_name
        self.workbook = None
        self.sheet = None
        self.get_sheet()
    
    def excel_parser(self):
        """parse excel file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        result = dict()

        # get all merged cells
        merges = self.sheet.merged_cells
        merges = [(range(*i[:2]), range(*i[2:])) for i in merges]
        # get titles field
        titles = list()
        if self.title_line is not None:
            titles = self.sheet.row_values(self.title_line)
        # get values field
        rows, cols = self.sheet.nrows, self.sheet.ncols
        values = list()
        for i in range(self.value_line, rows):
            value = list()
            for j in range(cols):
                for k in merges:
                    if i in k[0] and j in k[1]:
                        cell = self.sheet.cell(k[0][0], k[1][0])
                        break
                else:
                    cell = self.sheet.cell(i, j)
                value.append(self.get_cell_value(cell))
            values.append(value)

        if titles:
            result['titles'] = titles
            # match the title to the value of each row
            result['values'] = [{titles[i]: value[i] for i in range(len(value))} for value in values]
        else:
            result['values'] = values

        return result
    
    def get_sheet(self):
        """get the sheet object which need to be parsed.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        self.workbook = xlrd.open_workbook(filename=self.file_name)
        if self.sheet_name:
            self.sheet = self.workbook.sheet_by_name(self.sheet_name)
        else:
            self.sheet = self.workbook.sheet_by_index(self.sheet_index)

    def get_cell_value(self, cell):
        """get the value of cell.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        if cell.ctype == 3:
            value = xlrd.xldate_as_datetime(cell.value, self.workbook.datemode).strftime('%Y/%m/%d')
        else:
            value = cell.value

        if isinstance(value, float):
            value = int(value)
        elif isinstance(value, str):
            value = value.strip()

        return value
