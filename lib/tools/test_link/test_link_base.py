#!/usr/bin/env python

import testlink

from lib.tools.tools_base import ToolsBase


class TestLinkBase(ToolsBase):
    """Test link options base class.
    Args:
        url           type(str)            the URL address of test link server for automation
        key           type(str)            the key of test link user for automation
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-12 create
    """

    def __init__(self, url, key):
        super(TestLinkBase, self).__init__()
        self.url = url
        self.key = key
        self.client = None

    def login(self):
        """Login.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-12 create
        """

        if not self.client:
            self.client = testlink.TestlinkAPIClient(self.url, self.key)

    def close(self):
        """Close connection.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        self.client = None

    def reconnect(self):
        """Login again.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        self.close()
        self.login()

    def get_plan(self, project_name, plan_name):
        """Get plan.
        Args:
            project_name        type(str)            the name of the project on the test link
            plan_name           type(str)            the name of the plan on the test link
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        plan = self.client.getTestPlanByName(project_name, plan_name)[0]

        return plan

    def get_plan_id(self, project_name, plan_name):
        """Get plan id.
        Args:
            project_name        type(str)            the name of the project on the test link
            plan_name           type(str)            the name of the plan on the test link
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        plan = self.get_plan(project_name, plan_name)
        plan_id = plan['id']

        return plan_id

    def get_build(self, plan_id, build_name):
        """Get build.
        Args:
            plan_id             type(str)            the id of the plan on the test link
            build_name          type(str)            the name of the build on the test link
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        builds = self.client.getBuildsForTestPlan(plan_id)
        for i in builds:
            if i['name'] == build_name:
                build = i
                break
        else:
            build = None

        return build

    def get_build_id(self, plan_id, build_name):
        """Get build id.
        Args:
            plan_id             type(str)            the id of the plan on the test link
            build_name          type(str)            the name of the build on the test link
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        build = self.get_build(plan_id, build_name)
        build_id = build['id']

        return build_id

    def get_case(self, case_name, project_name):
        """Get test case.
        Args:
            case_name           type(str)            the name of the test case on the test link
            project_name        type(str)            the name of the project on the test link
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        response = self.client.getTestCaseIDByName(case_name, testprojectname=project_name)
        case_id = response[0]['id']
        case = self.client.getTestCase(testcaseid=case_id)[0]

        return case

    def get_case_external_id(self, case_name, project_name):
        """Get the external id of the test case.
        Args:
            case_name           type(str)            the name of the test case on the test link
            project_name        type(str)            the name of the project on the test link
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        case = self.get_case(case_name, project_name)
        external_id = case['full_tc_external_id']

        return external_id

    def create_build(self, plan_id, build_name, build_description='', release_date=''):
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

        if not build_description:
            build_description = 'This is a test build.'
        if not release_date:
            release_date = self.converter.convert_time_to_str(pattern='%Y-%m-%d')

        self.logger.info('Create build: %s.' % build_name)
        new_build = self.client.createBuild(
            plan_id, build_name, build_description, releasedate=release_date)[0]

        return new_build

    def back_fill_single(self, plan_id, result, external_id, build_id):
        """Back fill single test case result.
        Args:
            plan_id             type(str)            the id of the plan on the test link
            result              type(str)            test case executed result
            external_id         type(str)            the external id of the test case on the test link
            build_id            type(str)            the id of the build on the test link
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-13 create
        """

        response = self.client.reportTCResult(
            None, plan_id, None, result, "", guess=True, testcaseexternalid=external_id,
            buildid=build_id, platformname="0")

        return response
