#!/usr/bin/env python

from lib.resource.resource import Resource
from lib.base.script.case_base import CaseBase


class CaseMW(CaseBase):
    """ The parent class of micro win interface test.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    # test object
    PLC = None
    PROJECT = None
    MicroWIN = None

    # variable
    prj_file = ''
    save_as_file = ''
    export_file = ''
    import_file = ''
    create_file = ''
    data_log_file = ''

    def setup_class(self):
        """Initialize test resource
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-03
        """
        CaseBase.setup_class(self)

        # get test resource
        self.MicroWIN = self.resource.micro_win
        self.PLC = self.resource.plc

        # get project business object
        self.PROJECT = self.MicroWIN.find('project')

    def prepare(self):
        """The preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-20 create
        """
        super(CaseMW, self).prepare()

        # create session with the first plc configured
        if self.PLC:
            self.PLC['1'].create_session()

    def cleanup(self):
        """Clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-09-21 create
        """
        super(CaseMW, self).cleanup()

        # reset test resource
        self.reset_test_resource()

    def reset_test_resource(self):
        """Reset test resource
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-12-10 create
        """

        # close the opened project
        self.PROJECT.project_close()
        # reset test resource
        CaseBase.resource = Resource()
        self.MicroWIN = self.resource.micro_win
        self.PLC = self.resource.plc
        self.PROJECT = self.MicroWIN.find('project')
