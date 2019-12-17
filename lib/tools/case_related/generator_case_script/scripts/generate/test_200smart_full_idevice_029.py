#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice029(CaseMW):
    """I-Device-normal
    No.: test_200smart_full_idevice_029
    Preconditions:
        1. Open Micro/WIN V2.5;
        2. Select plc role is "I-Device" in PN wizard;
    Step actions:
        1. Check "Parameter assignment...", generate and download;
        2. Uncheck "Parameter assignment...", generate and download;
        3. Fix ip, generate and download;
        4. Obtain ip by other device, generate and download;
        5. 8 transfer areas, generate and download;
        6. Transfer area name contains chinese characters;
    Expected results:
        1. Generate successful, download configuration successful;
        2. Generate successful, download configuration successful;
        3. Generate successful, download configuration successful;
        4. Generate successful, download configuration successful;
        5. Generate successful, download configuration successful;
        6. Generate successful, download configuration successful;
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
        super(Test200SmartFullIdevice029, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;')
        self.logger.info('2. Select plc role is "I-Device" in PN wizard;')

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice029, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Check "Parameter assignment...", generate and download;')
        self.logger.info('2. Uncheck "Parameter assignment...", generate and download;')
        self.logger.info('3. Fix ip, generate and download;')
        self.logger.info('4. Obtain ip by other device, generate and download;')
        self.logger.info('5. 8 transfer areas, generate and download;')
        self.logger.info('6. Transfer area name contains chinese characters;')

        self.logger.info('Expected results:')
        self.logger.info('1. Generate successful, download configuration successful;')
        self.logger.info('2. Generate successful, download configuration successful;')
        self.logger.info('3. Generate successful, download configuration successful;')
        self.logger.info('4. Generate successful, download configuration successful;')
        self.logger.info('5. Generate successful, download configuration successful;')
        self.logger.info('6. Generate successful, download configuration successful;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-13 create
        """
        super(Test200SmartFullIdevice029, self).cleanup()
