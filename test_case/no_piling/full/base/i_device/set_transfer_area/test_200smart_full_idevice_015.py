#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice015(CaseMW):
    """Transfer area name
    No.: test_200smart_full_idevice_015
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. In PN wizard, select plc role is "I-Device", click "Next" and add one transfer area;
    Step actions:
        1. Add the second transfer area name, name is same with the first one;
        2. Modify the first transfer area name with chinese characters;
        3. Modify the first transfer area name to empty;
        4. Modify the first transfer area name more than 64 characters;
        5. Put the mouse on the first name;
        6. Modify the second transfer area name same with the step 5.
    Expected results:
        1. The name is automatically followed by a suffix of 01;
        2. Modify successful;
        3. Modify failed, name is restored automatically;
        4. The name automatically retains the first 64 characters;
        5. The tooltip display the name correctly;
        6. There is a prompt message "name should be unique!"
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
        super(Test200SmartFullIdevice015, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. In PN wizard, select plc role is "I-Device", click "Next" and add one transfer area;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice015, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Add the second transfer area name, name is same with the first one;')
        self.logger.info('2. Modify the first transfer area name with chinese characters;')
        self.logger.info('3. Modify the first transfer area name to empty;')
        self.logger.info('4. Modify the first transfer area name more than 64 characters;')
        self.logger.info('5. Put the mouse on the first name;')
        self.logger.info('6. Modify the second transfer area name same with the step 5.')

        self.logger.info('Expected results:')
        self.logger.info('1. The name is automatically followed by a suffix of 01;')
        self.logger.info('2. Modify successful;')
        self.logger.info('3. Modify failed, name is restored automatically;')
        self.logger.info('4. The name automatically retains the first 64 characters;')
        self.logger.info('5. The tooltip display the name correctly;')
        self.logger.info('6. There is a prompt message "name should be unique!"')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice015, self).cleanup()
