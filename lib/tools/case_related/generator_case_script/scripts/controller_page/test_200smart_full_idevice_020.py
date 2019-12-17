#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice020(CaseMW):
    """Default configuration
    No.: test_200smart_full_idevice_020
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "Controller", click "Next";
    Step actions:
        1. View controller configurations;
        2. Click "Previous", change ip or station name, then click "Next" to controller page;
    Expected results:
        1. Ip and station name show correctly in the network topology, there is a  "Catalog" tree with correct module in the right.
        2. Ip and station name show correctly in the network topology.
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-12-13 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice020, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. In PN wizard, select plc role is "Controller", click "Next";')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice020, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. View controller configurations;')
        self.logger.info('2. Click "Previous", change ip or station name, then click "Next" to controller page;')

        self.logger.info('Expected results:')
        self.logger.info('1. Ip and station name show correctly in the network topology, there is a  "Catalog" tree with correct module in the right.')
        self.logger.info('2. Ip and station name show correctly in the network topology.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice020, self).cleanup()
