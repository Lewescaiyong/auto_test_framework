#!/usr/bin/env python

from lib.component.software.software_base import SoftwareBase
from lib.exceptions.automation_exception import AutomationException
from lib.component.business.upgrade.plc_upgrade.plc_upgrade import PLCUpgrade
from lib.component.business.memory_options.memory_options import MemoryOptions


class PLCBase(SoftwareBase):
    """Micro/WIN parent class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    def __init__(self, params, own_micro_win=None):
        super(PLCBase, self).__init__(params)
        self.own_micro_win = own_micro_win
        self.id = params['id']
        self.ip = params['PLCInfo']['PLCIp']
        self.cpu_type = params['PLCInfo']['CPUType']

    @property
    def plc_info(self):
        """The information of firmware.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-24
        """

        plc_info = self.dispatch('get_plc_info')['rcInfo']

        return plc_info

    @property
    def plc_clock(self):
        """The clock of PLC device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-24
        """

        info = self.dispatch('plc_get_clock')['pTimeDate']

        return info

    @plc_clock.setter
    def plc_clock(self, set_type=1):
        """The clock of PLC device.
        Args:
            set_type           type(int)           1: now, 2: 2010-01-01 00:00:00
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-24
        """

        self.dispatch('plc_set_clock', {'pTimeDate': set_type})

    @property
    def version(self):
        """The information of firmware.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-24
        """

        version = self.plc_info['version']

        return version

    @property
    def business_config(self):
        """Config the businesses type that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        business = ('upgrade', 'memory_options')

        return business

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        config = {'memory_options': MemoryOptions, 'upgrade': PLCUpgrade}

        return config

    @property
    def log_str(self):
        """Define the log str for invoking interface
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        return 'Current connected PLC: %s' % self.ip

    def dispatch(self, wrapper, params=None):
        """Channel to invoke the interface
        Args:
            wrapper        type(str)                            the function name of wrapper
            params         type(str)                            The parameters used to invoke the interface
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        if self.own_micro_win:
            dispatcher = self.own_micro_win
            self.own_micro_win.set_connect_plc(self, False)
        else:
            dispatcher = self

        result = dispatcher.dispatch(wrapper, params)

        return result

    def create_session(self, plc=None):
        """create connection with plc
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """
        self.own_micro_win.create_session(self)

    def set_plc_mode(self, mode=0):
        """set PLC mode
        Args:
            mode           type(int)                            PLC mode: {0: stop, 1: run}
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        current_mode = self.get_plc_mode()
        if current_mode != mode:
            self.dispatch('set_plc_mode', {'Mode': mode})

    def get_plc_mode(self):
        """get PLC mode
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """
        mode = 0

        for i in range(2):
            try:
                result = self.dispatch('get_plc_mode')
                mode = result['pMode']
            except AutomationException:
                continue
            else:
                break

        return mode

    def plc_clear(self, clear_type='all'):
        """Clear project on plc
        Args:
            clear_type          type(str)         upload type: ob, db, sdb, all, invalid
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-11
        """

        clear_type = self.block_type_config[clear_type]
        result = self.dispatch('plc_clear', {'eBlockType': clear_type})
        self.common.sleep(1)

        return result

    def plc_power_cycle(self):
        """Power cycle
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-28
        """

        self.set_plc_mode(0)
        result = self.own_software.dispatch('plc_power_up_reset')

        return result

    def get_program_run_status(self):
        """Get the program running status on plc
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-29
        """

        result = True
        memory_options = self.find('memory_options')

        # check SM4.3[non-fatal error]
        value = memory_options.read_memory_data('sm', start_address=4, need_type=2)[4]
        if int(value) != 0:
            self.logger.debug('There are some errors in the progress of running the program.')
            result = False

        return result

    def check_after_clear(self, check_iq=False):
        """Check project and PLC after reset PLC
        Args:
            check_iq           type(bool)            whether to check memory_area: I, Q
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-21
        """

        result = True

        # check OB DB SDB
        status = self.check_project_after_clear()
        if not status:
            result = False
        # check information
        status = self.check_information_after_clear()
        if not status:
            result = False

        # check memory
        status = self.check_memory_after_clear(check_iq)
        if not status:
            result = False

        return result

    def check_project_after_clear(self):
        """Check the project on PLC after reset PLC
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-23
        """

        # check SDB
        project = self.own_micro_win.find('project')
        result = project.check_after_clear()

        return result

    def check_information_after_clear(self):
        """Check the PLC information after reset
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-23
        """

        result = True
        data = self.plc_info

        # check event log
        if data['event_count'] != 0:
            self.logger.info('After reset factory, event log count is %s not 0.' % data['event_count'])
            result = False
        # check alarm
        if data['alarm_count'] != 0:
            self.logger.info('After reset factory, alarm count is %s not 0.' % data['alarm_count'])
            result = False
        # check the mode of PLC
        mode = self.get_plc_mode()
        if int(mode) != 0:
            self.logger.info('After reset factory, the mode of PLC is [%s] not 0.' % mode)
            result = False
        # check the clock of PLC
        status = self.check_clock()
        if not status:
            result = False

        return result

    def check_clock(self):
        """Check the clock of the PLC
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-23
        """

        result = True
        clock = self.plc_clock
        self.logger.debug('PLC clock: %s.' % str(clock))
        if clock['year'] == 0:
            self.logger.info('After reset factory, the clock of PLC is 2000-01-01.' % clock)
            result = False

        return result

    def check_memory_after_clear(self, check_iq=False):
        """Check the PLC memory after reset
        Args:
            check_iq           type(bool)            whether to check memory_area: I, Q
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-04
        """

        result = True
        memory_options = self.find('memory_options')

        # check force
        value = memory_options.read_memory_data('sm', start_address=4, need_type=2)[0]
        if int(value) != 0:
            self.logger.info('After reset factory, the value of force tag is [%s] not 0.' % value)
            result = False
        # check RTC_Lost
        value = memory_options.read_memory_data('sm', start_address=0, need_type=2)[0]
        if int(value) != 0:
            self.logger.info('After reset factory, the value of RTC_Lost is [%s] not 0.' % value)
            result = False
        # check IO_Error
        value = memory_options.read_memory_data('sm', start_address=5, need_type=2)[-1]
        if int(value) != 0:
            self.logger.info('After reset factory, the value of IO_Error is [%s] not 0.' % value)
            result = False
        # check Data_Log
        for i in range(4):
            start_address = 480 + i
            value = memory_options.read_memory_data('sm', start_address=start_address)
            if value != 255:
                self.logger.info('After reset factory, the value of Data_Log %s is [%s] not 0xFF.' % (i, value))
                result = False

        if check_iq:
            # check memory_area: I
            value = memory_options.read_memory_data('i', address_type='dword', number=288)
            if value != 0:
                self.logger.info('After reset factory, the value of memory_area: I is [%s] not 0.' % value)
                result = False
            # check memory_area: Q
            value = memory_options.read_memory_data('q', address_type='dword', number=288)
            if value != 0:
                self.logger.info('After reset factory, the value of memory_area: Q is [%s] not 0.' % value)
                result = False

        return result
