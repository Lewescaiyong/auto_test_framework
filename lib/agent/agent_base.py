#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.agent.database.smart200_database import Smart200Database
from lib.base.framework.has_interface.has_interface import HasInterface


class AgentBase(HasInterface):
    """Agent's base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-15
    """

    def __init__(self):
        super(AgentBase, self).__init__()
        self.database = Smart200Database()
        self.tables = self.database.tables
