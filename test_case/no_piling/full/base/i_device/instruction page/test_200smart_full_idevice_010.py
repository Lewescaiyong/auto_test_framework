#!/usr/bin/env python

from lib.exceptions.check_exception import CheckException
from lib.base.script.integration_test.case_mw import CaseMW


class Test200SmartFullIdevice010(CaseMW):
    """Commnication
    No.: test_200smart_full_idevice_010
    Preconditions:
        1. Open Micro/WIN V2.5;  
        2. Connect to a plc with V2.5 FW;
    Step actions:
        1. Open PN wizard, select plc role as "Control";
    Expected results:
        1. The default value of "Send Clock" and "Start Up time" is 1.000 and 10000, the "Send Clock" cannot be
        changed, the "Start Up time" can be changed;
    Priority: H
    Author: Cai, Yong
    ChangeInfo: Cai, Yong 2019-11-18 create
    """

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice010, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;  ')
        self.logger.info('2. Connect to a plc with V2.5 FW;')
        # new a project
        time_str = self.converter.convert_time_to_str()
        self.prj_file = 'new_%s.smart' % time_str
        self.PROJECT.project_new(self.prj_file)

    def process(self):
        """execute the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice010, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Open PN wizard, select plc role as "Control";')
        # define the target startup_time
        startup_time = 15000
        # config a controller, add io device by catalog
        controller_params = {'role': 'controller', 'startup_time': startup_time}
        io_device_params = {'add_type': 'by_catalog', 'io_device_type': 'i-device',
                            'cpu_type': self.PLC['2'].cpu_type,
                            'fixed_ip': True,
                            'device_ip': self.PLC['2'].ip,
                            'station_name': 'idevice%s' % self.PLC['2'].ip.split('.')[-1],
                            'areas_info': [{'io_type': 'output', 'address': 128},
                                           {'io_type': 'input', 'address': 128}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        wizard_pn.config_controller(controller_params, io_device_params)
        config_data = wizard_pn.config_data

        self.logger.info('Expected results:')
        self.logger.info('1. The default value of "Send Clock" and "Start Up time" is 1.000 and 10000, the '
                         '"Send Clock" cannot be changed, the "Start Up time" can be changed;')
        if config_data['startup_time'] != startup_time:
            raise CheckException('The "Start Up time" can not be changed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice010, self).cleanup()
