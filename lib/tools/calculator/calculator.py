#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from lib.tools.tools_base import ToolsBase


class Calculator(ToolsBase):
    """Calculator tool.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2020-02-10 create
    """

    def __init__(self):
        super(Calculator, self).__init__()
        self.symbol = '+'
        self.pattern_01 = r'\((.*)\)'
        self.pattern_02 = r'\d+(?:\.\d+)?'

    @staticmethod
    def add(a, b):
        """Sum of a and b.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2020-02-10 create
        """

        return str(a + b)

    @staticmethod
    def sub(a, b):
        """Subtraction of a and b.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2020-02-10 create
        """

        return str(a - b)

    @staticmethod
    def mul(a, b):
        """Multiplication of a and b.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2020-02-10 create
        """

        return str(a * b)

    @staticmethod
    def div(a, b):
        """Division of a and b.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2020-02-10 create
        """

        return str(a / b)

    @staticmethod
    def get_number(a_str):
        """Get number from a_str.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2020-02-10 create
        """

        if '.' in a_str:
            return float(a_str)
        else:
            return int(a_str)

    def calculate(self, a_str):
        """Calculate a str.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2020-02-10 create
        """

        a_str = re.sub(r'\s', '', a_str)

        if a_str.startswith('-'):
            a_str = '0' + a_str

        while re.search(self.pattern_01, a_str):
            # replace the outermost parentheses
            a = re.search(self.pattern_01, a_str).group(1)
            a_str = re.sub(self.pattern_01, str(self.calculate(a)), a_str, 1)

        while re.search(r'[\*/]', a_str):
            if re.search(r'[\*/]', a_str).group() == '*':
                pattern = r'(%s)\*(%s)' % (self.pattern_02, self.pattern_02)
                a = re.search(pattern, a_str).group(1)
                b = re.search(pattern, a_str).group(2)
                a_str = re.sub(pattern, self.mul(self.get_number(a), self.get_number(b)), a_str, 1)
            else:
                pattern = r'(%s)/(%s)' % (self.pattern_02, self.pattern_02)
                a = re.search(pattern, a_str).group(1)
                b = re.search(pattern, a_str).group(2)
                a_str = re.sub(pattern, self.div(self.get_number(a), self.get_number(b)), a_str, 1)

        a_str = self.process(a_str)
        while re.search(r'[\+-]', a_str):
            if re.search(r'[\+-]', a_str).group() == '+':
                pattern = r'(%s)\+(%s)' % (self.pattern_02, self.pattern_02)
                a = re.search(pattern, a_str).group(1)
                b = re.search(pattern, a_str).group(2)
                a_str = re.sub(pattern, self.add(self.get_number(a), self.get_number(b)), a_str, 1)
            else:
                pattern = r'(%s)-(%s)' % (self.pattern_02, self.pattern_02)
                a = re.search(pattern, a_str).group(1)
                b = re.search(pattern, a_str).group(2)
                a_str = re.sub(pattern, self.sub(self.get_number(a), self.get_number(b)), a_str, 1)

        result = self.get_number(a_str) if self.symbol == '+' else -self.get_number(a_str)

        return result

    def process(self, a_str):
        """Process special symbol.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2020-02-10 create
        """

        subs = re.findall('-\d', a_str)
        a_str = re.sub('-\d', '', a_str) + ''.join(subs)
        if re.search('^0?-', a_str):
            a_str = re.sub('-', '+', a_str)
            self.symbol = '-'
        else:
            self.symbol = '+'
        a_str = a_str[1:] if a_str.startswith('+') else a_str

        return a_str


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.calculate('(-1 - 2) * 3 -4 * 0'))
