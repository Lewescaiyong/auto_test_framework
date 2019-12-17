#!/usr/bin/env python

from lib.agent.task.task_generator.task_generator_base import TaskGeneratorBase


class NormalTaskGenerator(TaskGeneratorBase):
    """Receive jenkins data and generate normal task file.
    Args:
    Example:
        C:\\Users>python normal_task_generator.py -t smoke -p 2
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-19
    """


if __name__ == '__main__':
    NormalTaskGenerator().run()
