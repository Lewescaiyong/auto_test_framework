#!/usr/bin/env python

import os
import codecs
from mako.template import Template

from lib.tools.tools_base import ToolsBase


class GeneratorByTemplate(ToolsBase):
    """Analyze the test case information in the excel file and generate the test case script automatically.
    Args:
        template            type(str)           the abspath of the template file
        file_abspath        type(str)           the abspath of generated file
    Example:
        generator = GeneratorByTemplate(../template.txt, ../file_name)
        generator.generator()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-18
    """

    def __init__(self, template, file_abspath):
        super(GeneratorByTemplate, self).__init__()
        self.template = template
        self.file_abspath = file_abspath

    def generator(self, params=None):
        """Generate the test case script.
        Args:
            params         type(dict)         the parameters used to generate file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        if params is None:
            return

        file_path = os.path.dirname(self.file_abspath)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        output = codecs.open(filename=self.file_abspath, mode="w", encoding="UTF-8")
        my_template = Template(filename=self.template, output_encoding="UTF-8", input_encoding="UTF-8")
        output.write(my_template.render(**params).decode("UTF-8"))
        output.close()
