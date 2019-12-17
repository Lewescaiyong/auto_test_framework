#!/usr/bin/env python

from lib.base.script.case_base import CaseBase


class Test200SmartCommonInformation001(CaseBase):
    """Print version information of software
    No.: test_200smart_common_information_001
    Preconditions:
        1. Get version information
    Step actions:
        1. Print Micro/WIN version;
        2. Print CPU version;
    Expected results:
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-11-13 create
    """

    info = None

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-13 create
        """
        super(Test200SmartCommonInformation001, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Get version information ')
        self.info = self.information.get_version_information(self.resource)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-13 create
        """
        super(Test200SmartCommonInformation001, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Print Micro/WIN version;')
        mw_version = self.info['mw_version']
        self.logger.info('Micro/WIN version: %s' % mw_version)

        self.logger.info('2. Print CPU version;')
        cpu_version = self.info['cpu_version']
        self.logger.info('CPU version: %s' % cpu_version)

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-13 create
        """
        super(Test200SmartCommonInformation001, self).cleanup()
