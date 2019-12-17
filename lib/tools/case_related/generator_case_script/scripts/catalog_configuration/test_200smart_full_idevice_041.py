#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice041(CaseMW):
    """Parameter
    No.: test_200smart_full_idevice_041
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Plc role is "Controller", add a catalog device in device table, add an input submodule, go to next page;
    Step actions:
        1. View the "Parameter assignment of PROFINET interface by higher-level controller";
        2. Check the option;
    Expected results:
        1. The option is unchecked by default, and the "Port1" can not be configured, the "Port1" and "Interface" in module page is grey;
        2. The "Port1" can be configured, the "Port1" and "Interface" in module page is black;
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
        super(Test200SmartFullIdevice041, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Plc role is "Controller", add a catalog device in device table, add an input submodule, go to next page;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice041, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. View the "Parameter assignment of PROFINET interface by higher-level controller";')
        self.logger.info('2. Check the option;')

        self.logger.info('Expected results:')
        self.logger.info('1. The option is unchecked by default, and the "Port1" can not be configured, the "Port1" and "Interface" in module page is grey;')
        self.logger.info('2. The "Port1" can be configured, the "Port1" and "Interface" in module page is black;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice041, self).cleanup()
