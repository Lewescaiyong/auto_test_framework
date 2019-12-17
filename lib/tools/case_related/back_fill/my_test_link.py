#!/usr/bin/env python

import testlink
import traceback

from lib.tools.test_link.test_link_base import TestLinkBase


class MyTestLink(TestLinkBase):
    """Test link tool for smart200 project.
    Args:
        plan_name           type(str)            the name of the plan on the test link
        project_name        type(str)            the name of the project on the test link
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-13 create
    """

    def __init__(self, plan_name, project_name='smart200_integration'):
        super(MyTestLink, self).__init__(**self.connection_info)
        self.plan_name = plan_name
        self.project_name = project_name

    @property
    def connection_info(self):
        """URL information.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        url = 'http://intranet.cnctu04401.siemens.com:90/testlink1.9/lib/api/xmlrpc/v1/xmlrpc.php'
        key = '1d84e55169665a59857863edfb3cadf2'

        return {'url': url, 'key': key}

    def create_build(self, plan_id='', build_name='', build_description='', release_date=''):
        """Create test build.
        Args:
            plan_id             type(str)            the id of the plan on the test link
            build_name          type(str)            the name of the build on the test link
            build_description   type(str)            build description
            release_date        type(str)            release date: 2019-11-13
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        if not plan_id:
            plan_id = self.get_plan_id(self.project_name, self.plan_name)
        if not build_name:
            date_str = self.converter.convert_time_to_str()
            build_name = '%s_build_%s' % (self.plan_name, date_str)

        new_build = TestLinkBase.create_build(self, plan_id, build_name, build_description, release_date)

        return new_build

    def back_fill_single(self, case_name, result, build_id, plan_id=''):
        """Back fill single test case result.
        Args:
            case_name           type(str)            the name of the test case on the test link
            result              type(str)            test case executed result
            build_id            type(str)            the id of the build on the test link
            plan_id             type(str)            the id of the plan on the test link
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        try:
            external_id = self.get_case_external_id(case_name, self.project_name)
            if not plan_id:
                plan_id = self.get_plan_id(self.project_name, self.plan_name)
            # back fill
            self.logger.info('Backfill executed result, case name: %s, result: %s.' % (case_name, result))
            response = TestLinkBase.back_fill_single(
                self, plan_id, result, external_id, build_id)
        except testlink.testlinkerrors.TestLinkError:
            response = None
            self.logger.warning(traceback.format_exc())

        return response
