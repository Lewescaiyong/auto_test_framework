#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice011(CaseMW):
    """Consistency
    No.: test_200smart_full_idevice_011
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Connect to a plc with V2.5 FW;
        3. select plc role as "I-Device";
    Step actions:
        1. Select "Fixed IP address and name", input valid ip and name, add some transfer areas, generate, View the "Communication" in system block;
        2. Modify the ip and name in system block;
        3. In PN Wizard, select "Obtain IP address by other services", generate;
    Expected results:
        1. In system block, "IP address data is fixed..." is checked and grey, ip and name is same with PN Wizard;
        2. In PN Wizard, the ip and name is also modifyed;
        3. In system block, the  "IP address data is fixed..." is unchecked and not grey, ip and name are grey.
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
        super(Test200SmartFullIdevice011, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Connect to a plc with V2.5 FW;')
        self.logger.info('3. select plc role as "I-Device";')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice011, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Select "Fixed IP address and name", input valid ip and name, add some transfer areas, generate, View the "Communication" in system block;')
        self.logger.info('2. Modify the ip and name in system block;')
        self.logger.info('3. In PN Wizard, select "Obtain IP address by other services", generate;')

        self.logger.info('Expected results:')
        self.logger.info('1. In system block, "IP address data is fixed..." is checked and grey, ip and name is same with PN Wizard;')
        self.logger.info('2. In PN Wizard, the ip and name is also modifyed;')
        self.logger.info('3. In system block, the  "IP address data is fixed..." is unchecked and not grey, ip and name are grey.')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice011, self).cleanup()
