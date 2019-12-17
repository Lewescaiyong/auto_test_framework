#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import Document

from lib.base.framework.smart200_base import Smart200Base


class XMLGenerator(Smart200Base):
    """Generator xml file.
    Args:
        file_name           type(str)            the name of xml file for generator
    Example:
        ger = XMLGenerator(file_name=r'C:\file.xml')
        result = ger.generator_xml()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-26
    """

    def __init__(self, file_name):
        super(XMLGenerator, self).__init__()
        self.file_name = file_name

    def xml_generator(self, info):
        """generator xml file.
        Args:
            info      type(dict)        the contents of write to xml file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """
        # create document
        doc = Document()
        # write into each child node
        self.append_child(doc, info, doc)
        # save as xml file
        with open(self.file_name, "wb") as f:
            f.write(doc.toprettyxml(encoding="utf-8"))

    def append_child(self, doc, info, father):
        """append child node.
        Args:
            doc       type(Document)        document object
            info      type(dict)            the contents of write to node
            father    type(element)         father node
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        for k, v in info.items():
            if isinstance(v, dict):
                v = [v]
            if isinstance(v, list):
                for value in v:
                    element = doc.createElement(k)
                    self.append_child(doc, value, element)
                    father.appendChild(element)
            elif k == "text":
                text_node = doc.createTextNode(v)
                father.appendChild(text_node)
            else:
                father.setAttribute(k, v)
