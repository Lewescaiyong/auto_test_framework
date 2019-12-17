#!/usr/bin/env python

from bs4.element import Tag
from bs4 import BeautifulSoup

from lib.tools.tools_base import ToolsBase


class HTMLParser(ToolsBase):
    """Parse the test report.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-04
    """

    def __init__(self, html_file=''):
        super(HTMLParser, self).__init__()
        self.html_file = html_file
        self.soup = None

    def html_parser(self):
        """Parse html file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-04 create
        """

        with open(self.html_file) as f:
            self.soup = BeautifulSoup(f.read(), 'html.parser')
        result = {self.soup.contents[0]: self._parser(self.soup)}

        return result

    def _parser(self, node):
        """parse html node.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-04 create
        """

        result = {'text': getattr(node, 'text')} if getattr(node, 'text') else dict()
        for i in node.contents:
            if isinstance(i, Tag):
                child_info = self._parser(i)
                if not child_info:
                    continue
                if i.name in result:
                    if isinstance(result[i.name], dict):
                        result[i.name] = [result[i.name]]
                    result[i.name].append(child_info)
                else:
                    result[i.name] = child_info

        return result


if __name__ == '__main__':
    parser = HTMLParser()
    print(parser.html_parser())
