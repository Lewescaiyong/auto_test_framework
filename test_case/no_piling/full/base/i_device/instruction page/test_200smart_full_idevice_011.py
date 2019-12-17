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
        1. Select "Fixed IP address and name", input valid ip and name, add some transfer areas, generate, View the
        "Communication" in system block;
        2. Modify the ip and name in system block;
        3. In PN Wizard, select "Obtain IP address by other services", generate;
    Expected results:
        1. In system block, "IP address data is fixed..." is checked and grey, ip and name is same with PN Wizard;
        2. In PN Wizard, the ip and name is also modifyed;
        3. In system block, the  "IP address data is fixed..." is unchecked and not grey, ip and name are grey.
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
        super(Test200SmartFullIdevice011, self).prepare()

        self.logger.info('Preconditions:')
        self.logger.info('1. Open Micro/WIN V2.5;  ')
        self.logger.info('2. Connect to a plc with V2.5 FW;')
        self.logger.info('3. select plc role as "I-Device";')
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
        super(Test200SmartFullIdevice011, self).process()

        self.logger.info('Step actions:')
        self.logger.info('1. Select "Fixed IP address and name", input valid ip and name, add some transfer areas, '
                         'generate, View the "Communication" in system block;')
        # config a i-device
        params = {'role': 'i-device', 'areas_info': [{'io_type': 'input', 'address': 1152},
                                                     {'io_type': 'output', 'address': 1152}]}
        wizard_pn = self.PROJECT.find('wizard_pn')
        wizard_pn.config_i_device(params)
        ip_01 = wizard_pn.params['ip']
        station_name_01 = wizard_pn.params['station_name']
        sdb_data_01 = wizard_pn.own_system_block.config_data

        self.logger.info('2. Modify the ip and name in system block;')
        ip_info = self.PLC['1'].ip.split('.')
        ip_info[-1] = str(int(ip_info[-1]) + 1)
        wizard_pn.own_system_block.set_communication({'fixed_ip': True, 'ip': '.'.join(ip_info)})
        ip_02 = wizard_pn.own_system_block.params['ip']
        station_name_02 = wizard_pn.own_system_block.params['station_name']
        wizard_data = wizard_pn.config_data

        self.logger.info('3. In PN Wizard, select "Obtain IP address by other services", generate;')
        params = {'role': 'i-device', 'fixed_ip': False}
        wizard_pn.config_i_device(params)
        sdb_data_02 = wizard_pn.own_system_block.config_data

        self.logger.info('Expected results:')
        self.logger.info('1. In system block, "IP address data is fixed..." is checked and grey, '
                         'ip and name is same with PN Wizard;')
        if sdb_data_01['fixed_ip'] != 1 or sdb_data_01['ip'] != ip_01 or \
                self.compare.compare_c_str(sdb_data_01['station_name'], station_name_01):
            raise CheckException('1. In system block, "IP address data is not fixed, or ip is not same with PN Wizard,'
                                 'or name is not same with PN Wizard;')

        self.logger.info('2. In PN Wizard, the ip and name is also modifyed;')
        if wizard_data['ip'] != ip_02 or self.compare.compare_c_str(wizard_data['station_name'], station_name_02):
            raise CheckException('2. In PN Wizard, the ip and name is not modified;')

        self.logger.info('3. In system block, the  "IP address data is fixed..." is unchecked and not grey, '
                         'ip and name are grey.')
        if sdb_data_02['fixed_ip'] != 0 or sdb_data_02['ip'] != '192.168.2.1' or \
                self.compare.compare_c_str(sdb_data_02['station_name'], ''):
            raise CheckException('3. In system block, the  "IP address data is not fixed;')

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-11-18 create
        """
        super(Test200SmartFullIdevice011, self).cleanup()
