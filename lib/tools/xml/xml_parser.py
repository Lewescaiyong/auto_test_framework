#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
try:
    import xml.etree.ElementTree as XMLTree
except ImportError:
    import xml.etree.cElementTree as XMLTree

from lib.base.framework.smart200_base import Smart200Base


class XMLParser(Smart200Base):
    """parse xml file to dict.
    Args:
        file_name           ype(str)            the absolute_path of xml file
    Example:
        parser = XMLParser(file_name=r'C:\file.xml')
        result = parser.xml_parser()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """

    def __init__(self, file_name):
        super(XMLParser, self).__init__()
        self.file_name = file_name

    def xml_parser(self):
        """parse xml file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        root = XMLTree.parse(self.file_name).getroot()

        return {re.sub('{http.+}', '', root.tag): self._parser(root)}

    def _parser(self, node):
        """parse xml node.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        result = dict()
        if node.items():
            result.update(dict(node.items()))
        if node.text and node.text.strip():
            result['text'] = node.text.strip()
        for i in node:
            child_tag = re.sub('{http.+}', '', i.tag)
            child_info = self._parser(i)
            if not child_info:
                continue
            if child_tag in result:
                if isinstance(result[child_tag], dict):
                    result[child_tag] = [result[child_tag]]
                result[child_tag].append(child_info)
            else:
                result[child_tag] = child_info

        return result


if __name__ == '__main__':
    parser = XMLParser(r'D:\Project\smart200\lib\agent\files\test_bed_file\test_bed_19216810120.xml')
    print(parser.xml_parser())
