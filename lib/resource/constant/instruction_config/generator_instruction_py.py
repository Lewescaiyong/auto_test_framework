#!/usr/bin/env python

import os

from lib.tools.tools_base import ToolsBase


class GeneratorInstructionPy(ToolsBase):
    """Generator the file: instruction_id.py.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-26
    """

    def __init__(self):
        super(GeneratorInstructionPy, self).__init__()
        self.path = ''
        self.instruction_txt = 'instruction_config.txt'
        self.instruction_py = 'instruction_config_new.py'

    def get_path(self):
        """Get the current path.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-26
        """

        if not self.path:
            local_path = self.information.get_framework_local_path()
            self.path = os.path.join(local_path, 'lib', 'resource', 'constant', 'instruction_config')

        return self.path

    def get_instruction_txt_data(self):
        """Get the data of the instruction.txt file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-26
        """

        instruction_txt = os.path.join(self.get_path(), self.instruction_txt)
        with open(instruction_txt) as f:
            data = f.readlines()

        return data

    def generator_instruction_py(self):
        """Get the data of the instruction.txt file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-26
        """

        data = self.get_instruction_txt_data()
        instruction_py = os.path.join(self.get_path(), self.instruction_py)
        with open(instruction_py, 'w') as f:
            f.write('#!/usr/bin/env python' + '\n\n\n')
            for line in data:
                name = line.split('=')[0].strip()
                new_line = "%s = {'id': '%s', 'values': dict()}" % (name, name)
                f.write(new_line + '\n')


if __name__ == '__main__':
    generator = GeneratorInstructionPy()
    generator.generator_instruction_py()
