#!/usr/bin/env python


def convert_to_c_str(self, data):
    """Convert python object to c_type str
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    def func(_data):
        c_str = self.str_list.AddTail(str(_data))
        result = self.str_list.GetAt(c_str)

        return result

    return self.convert(data, func)


def convert_to_c_int_s(self, data):
    """Convert python object to c_type LongS
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-28
    """

    def func(_data):
        number = self.interface.create_puint(_data)
        result = self.interface.get_puintValueS(number)

        return result

    return self.convert(data, func)


def convert_to_c_str_array(self, data):
    """Convert python object to c_type CStringArray
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    def func(_data):
        array = self.interface.CStringArray()

        return array

    return self.convert(data, func)


def convert_to_int_pointer(self, data):
    """Convert python object to c_type int pointer
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    return self.convert(data, self.interface.create_pint)


def convert_to_word_pointer(self, data):
    """Convert python object to c_type word pointer
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    return self.convert(data, self.interface.create_pWORD)


def convert_to_bool_pointer(self, data):
    """Convert python object to c_type bool pointer
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    return self.convert(data, self.interface.create_pBOOL)


def convert_to_byte_pointer(self, data):
    """Convert python object to c_type byte pointer
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
        data_type      type(int)                                   1-byte, 2-word, 3-dword
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """
    config = {
        'eCOMMCOMPASS_MEM_TYPE_BYTE': 1,
        'eCOMMCOMPASS_MEM_TYPE_WORD': 2,
        'eCOMMCOMPASS_MEM_TYPE_DWORD': 3,
        1: 1,
        2: 2,
        3: 3
              }

    def func(_data):
        data_type = config.get(_data['data_type'])
        result = self.interface.create_pByte(_data['data'], data_type)

        return result

    return self.convert(data, func)


def convert_to_struct_arg(self, data):
    """Convert python object to c_type struct_arg
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    def func(_data):
        result = getattr(self.interface, _data)

        return result

    return self.convert(data, func)


def convert_to_hwnd(self, data):
    """Convert python object to c_type HWND
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    def func(_data):
        hwnd = self.interface.get_defaultHWND()

        return hwnd

    return self.convert(data, func)


def convert_to_mw_id(self, data):
    """Convert python object to c_type MW_ID
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    def func(_data):
        if not _data:
            result = self.interface.MW_ID()
        else:
            e_type = self.convert_data_type(_data.get('e_type', 'POU_MAIN'), 'struct_arg')
            mw_protection = self.convert_data_type('USER_NO_PROTECTION', 'struct_arg')
            result = self.interface.MW_ID(e_type, 0, mw_protection)

        return result

    return self.convert(data, func)


def convert_to_cell_location(self, data):
    """Convert python object to c_type cell_location
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    def func(_data):
        row = self.convert_data_type(_data['row_id'], 'p_int')
        col = self.convert_data_type(_data['col_id'], 'p_int')
        result = self.interface.GRID_CELL_LOCATION(row, col)

        return result

    return self.convert(data, func)


def convert_to_operand_location(self, data):
    """Convert python object to c_type operand_location
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    def func(_data):
        row = self.convert_data_type(_data['row_id'], 'p_int')
        col = self.convert_data_type(_data['col_id'], 'p_int')
        location = self.convert_data_type(_data['location'], 'p_int')
        result = self.interface.GRID_OPERAND_LOCATION(row, col, location)

        return result

    return self.convert(data, func)


def convert_to_rectangle(self, data):
    """Convert python object to c_type GRID_RECTANGLE
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    def func(_data):
        result = self.interface.GRID_RECTANGLE()

        return result

    return self.convert(data, func)


def convert_to_plc_info(self, data):
    """Convert python object to c_type plc information
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    def func(_data):
        info_data = self.interface.EX_PLCInformationData()

        return info_data

    return self.convert(data, func)


def convert_to_compare_options(self, data):
    """Convert python object to c_type COMPARE_DLG_OPTIONS
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-09
    """

    def func(_data):
        compare_options = self.interface.COMPARE_DLG_OPTIONS()
        network_info = self.convert_data_type(_data, 'network_info')
        for k, v in (('cNetInfo', network_info), ('ProgramCodeBlock', 1), ('DataBlock', 1),
                     ('SystemDataBlock', 1), ('Recipes', 1), ('DataLogs', 1),):
            setattr(compare_options, k, v)

        return compare_options

    return self.convert(data, func)


def convert_to_compare_results(self, data):
    """Convert python object to c_type COMPARE_RESULTS
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-09
    """

    def func(_data):
        compare_results = self.interface.COMPARE_RESULTS()

        return compare_results

    return self.convert(data, func)


def convert_to_network_info(self, data):
    """Convert python object to c_type MWNetworkInfo
    Args:
        data           type(dict)           network info.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-09
    """

    def func(_data):
        ip = self.convert_data_type(_data['ip'], 'c_str')
        mask = self.ip_to_long(_data.get('mask', '255.255.255.0'))
        network_info = self.interface.MWNetworkInfo()
        network_info.SetNetworkType(2)
        network_info.SetIPAddress(ip)
        network_info.SetSubnet(mask)
        network_info.SetGateway(0)

        return network_info

    return self.convert(data, func)


def convert_to_data_log_upload_options(self, data):
    """Convert python object to c_type DATA LOG UPLOAD OPTIONS
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-09
    """

    def func(_data):
        options = self.interface.DATALOG_UPLOAD_OPTIONS()

        return options

    return self.convert(data, func)


def convert_to_memory_info(self, data):
    """Convert python object to c_type sCOMM COMPASS MEM STRUCT
    Args:
        data           type(dict)           memory address information.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-09
    """

    def func(_data):
        mem_address = self.interface.sCOMMCOMPASS_ADDRESS()
        for k, v in (('m_dwMemoryArea', self.convert_data_type(_data['memory_area'], 'struct_arg')),
                     ('m_eMemMode', self.interface.eCOMMCOMPASS_DIRECT_ADDRESS),
                     ('m_eMemType', self.convert_data_type(_data['address_type'], 'struct_arg')),
                     ('m_nByteOffset', self.convert_data_type(_data['start_address'], 'p_int'))):
            setattr(mem_address, k, v)

        mem_struct = self.interface.sCOMMCOMPASS_MEM_STRUCT()
        for k, v in (('m_sAddress', mem_address), ('m_nNumberOfAddr', 1),
                     ('m_nDataLength', self.convert_data_type(_data['address_length'], 'p_int'))):
            setattr(mem_struct, k, v)
        if _data.get('address_value'):
            params = {'data': _data['address_value'], 'data_type': _data['address_type']}
            setattr(mem_struct, 'm_pData', self.convert_data_type(params, 'byte_pointer'))

        return mem_struct

    return self.convert(data, func)


def convert_to_wizard_pn_data(self, data):
    """Convert python object to c_type EX_PNWizardData
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-23
    """

    def func(_data):
        if _data:
            pn_data = _data['obj']
            m_smart200 = pn_data.m_Smart200PLCPDEV
            # change role information
            if _data.get('role'):
                m_smart200.SetPLCRole(self.convert_data_type(_data['role'], 'p_int'))
            # change communication information
            if _data.get('communication'):
                communication = _data['communication']
                m_smart200.SetSendClock(self.convert_data_type(communication['send_clock'], 'p_float'))
                m_smart200.SetStartUpTime(self.convert_data_type(communication['startup_time'], 'p_int'))
        else:
            pn_data = self.interface.EX_PNWizardData()

        return pn_data

    return self.convert(data, func)


def convert_to_sdb_data(self, data):
    """Convert python object to c_type SDBData
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-23
    """

    def func(_data):
        if _data:
            sdb_data = _data['obj']
            cpu = sdb_data.m_cpu
            startup = sdb_data.m_common.m_startup
            ethernet = sdb_data.m_common.m_ethernet
            # change module information
            if _data.get('cpu'):
                if _data['cpu'].get('cpu_type'):
                    cpu.SetDeviceType(self.convert_data_type(_data['cpu']['cpu_type'], 'c_str'))
                if _data['cpu'].get('cpu_version'):
                    cpu.SetDeviceVersion(self.convert_data_type(_data['cpu']['cpu_version'], 'c_type'))
            # change communication information
            if _data.get('fixed_ip', None) is not None:
                ethernet.SetStoreInProject(self.convert_data_type(_data['fixed_ip'], 'p_int'))
                if _data.get('ip'):
                    ethernet.SetIP(self.ip_to_long(_data['ip']))
                if _data.get('subnet_mask'):
                    ethernet.SetSubnetMask(self.ip_to_long(_data['subnet_mask']))
                if _data.get('default_gateway'):
                    ethernet.SetDefaultGateway(self.ip_to_long(_data['default_gateway']))
                if _data.get('station_name'):
                    ethernet.SetStationName(self.convert_data_type(_data['station_name'], 'c_str'))
            # change startup information
            if _data.get('cpu_mode'):
                startup.SetCPUMode(self.convert_data_type(_data['cpu_mode'], 'struct_arg'))
        else:
            # init SDBData
            sdb_data = self.interface.SDBData()

        return sdb_data

    return self.convert(data, func)


def convert_to_clock_struct(self, data):
    """Convert python object to c_type TIME_DATE_STRUCT
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-24
    """

    def set_date(obj, time_str):
        time_info = [int(i) for i in time_str.split('_')]
        obj.year = int(str(time_info[0])[2:])
        for i, v in enumerate(('month', 'date', 'hour', 'minutes', 'seconds')):
            setattr(obj, v, time_info[i + 1])

    def func(_data):
        if _data == 1:
            date = self.interface.TIME_DATE_STRUCT()
            time_str = self.convert_time_to_str(pattern='%Y_%m_%d_%H_%M_%S')
            set_date(date, time_str)
        elif _data == 2:
            date = self.interface.TIME_DATE_STRUCT()
            time_str = '2000_01_01_00_00_00'
            set_date(date, time_str)
        else:
            date = self.interface.TIME_DATE_STRUCT()

        return date

    return self.convert(data, func)


def convert_to_compass_element(self, data):
    """Convert python object to c_type COMPASS_ELEMENT
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-04
    """

    def func(_data):
        element = self.interface.COMPASS_ELEMENT()

        return element

    return self.convert(data, func)


def convert_to_c_type(self, data):
    """Convert c_type to c_type
    Args:
        data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-09
    """

    return self.convert(data, lambda x: x)
