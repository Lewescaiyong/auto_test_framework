#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt
from xlwt.Style import XFStyle

from lib.tools.tools_base import ToolsBase


class ExcelGenerator(ToolsBase):
    """change excel file contents.
    Args:
        file_name           type(str)            the absolute_path of xml file、
        title_line          type(int)           the line id of title
        value_line          type(int)           the line id of first value line
        sheet_info          type(dict)           one or more sheet info
        ----------------------------------------------
        sheet_info detail:
        key            type(str)            the name of sheet
        value          type(dict)           information of write to sheet(named key)
    Example:
        ger = ExcelGenerator(file_name, sheet_info)
        ger.excel_generator()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """
    width_config = dict()

    def __init__(self, file_name, title_line=0, value_line=1, sheet_info=None):
        super(ExcelGenerator, self).__init__()
        self.file_name = file_name
        self.title_line = title_line
        self.value_line = value_line
        self.sheet_info = sheet_info

        self.workbook = None
        self.sheet = None

    def excel_generator(self):
        """generator excel file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        self.workbook = xlwt.Workbook(encoding='utf-8')
        for key, value in self.sheet_info.items():
            self.add_sheet(key, value)

        self.workbook.save(self.file_name)

    def add_sheet(self, sheet_name, sheet_info):
        """add a sheet.
        Args:
            sheet_name           type(str)             the name of new sheet
            sheet_info           type(dict)            contents needs to be writen to sheet
            -------------------------------------------------------------------------
            sheet_info details:
            titles         type(list)            the title field of the excel file
            values         type(list)            the value field of the excel file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """
        self.sheet = self.workbook.add_sheet(sheet_name)

        # process title line
        titles = sheet_info.get('titles', list())
        self.write_title_line(titles)

        # process value line
        values = sheet_info.get('values', list())
        self.write_value_line(values)

        # set col width and row height
        self.set_title_line_width_height(titles)

    def write_title_line(self, titles, style=None):
        """write the title line to the excel.
        Args:
            titles         type(list)            the title field of the excel file
            style          type(XFStyle)         style object
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        if not titles:
            self.value_line = 0
            return
        if not style:
            style = self.get_default_style()
            pattern = self.set_pattern()
            font = self.set_font()
            alignment = self.set_alignment(xlwt.Alignment.HORZ_CENTER, xlwt.Alignment.VERT_CENTER)
            style.pattern = pattern
            style.font = font
            style.alignment = alignment

        for col, value in enumerate(titles):
            self.write(self.title_line, col, value, style)

    def write_value_line(self, values, style=None):
        """write the value line to the excel.
        Args:
            values         type(list)            the value field of the excel file
            style          type(XFStyle)         style object
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        if not values:
            return
        if not style:
            style = self.get_default_style()
            alignment = self.set_alignment()
            font = self.set_font(height=20 * 11)
            style.alignment = alignment
            style.font = font

        for row, value in enumerate(values):
            if isinstance(value, dict):
                value = value.values()
            for col, v in enumerate(value):
                self.write(self.value_line + row, col, v, style)

    def write(self, row, col, value, style=None):
        """write content to cell.
        Args:
            row         type(int)            the row id of cell
            col         type(int)            the col id of cell
            value       type(int)            cell value
            style       type(XFStyle)        style object
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        if not style:
            style = self.get_default_style()

        self.sheet.write(row, col, value, style)

    @staticmethod
    def get_default_style():
        """get the default style.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        style = XFStyle()

        return style

    @staticmethod
    def set_pattern(color=3):
        """set the fore color of cell.
        Args:
            color           type(int)            the fore color of cell
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = color

        return pattern

    @staticmethod
    def set_font(name="Arial", height=20 * 14):
        """set the font of cell.
        Args:
            name            type(int)            the name of font
            height          type(int)            the height of font
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        font = xlwt.Font()
        font.name = name
        font.height = height

        return font

    @staticmethod
    def set_alignment(horz=None, vert=None):
        """set the alignment of cell.
        Args:
            horz         type(int)          the position of the cell value
            vert         type(int)          the position of the cell value
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """
        if horz is None:
            horz = xlwt.Alignment.HORZ_LEFT
        if vert is None:
            vert = xlwt.Alignment.VERT_TOP

        alignment = xlwt.Alignment()
        alignment.horz = horz
        alignment.vert = vert

        return alignment

    def set_title_line_width_height(self, titles):
        """set title line col width and row height.
        Args:
            titles         type(list)            the title field of the excel file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        self.set_width_height(row_id=self.title_line, height=700)
        for i, v in enumerate(titles):
            width = self.width_config.get(v, 256 * 18)
            self.set_width_height(col_id=i, width=width)

    def set_width_height(self, col_id=None, width=None, row_id=None, height=None):
        """set col width and row height.
        Args:
            col_id         type(int)          the col id of set width
            width          type(int)          the width of set col
            row_id         type(int)          the row id of set height
            height         type(int)          the height of set row
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """
        if col_id is not None and width:
            self.sheet.col(col_id).width = width

        if row_id is not None and height:
            self.sheet.row(row_id).height_mismatch = True
            self.sheet.row(row_id).height = height
