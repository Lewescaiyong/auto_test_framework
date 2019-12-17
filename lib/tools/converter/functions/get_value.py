#!/usr/bin/env python


def get_special_type_value(self, obj, c_type):
    """get the value from special c_type object
    Args:
        obj        type(word_pointer,)        C++ interface return value.
        c_type     type(str)                  the type of object
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    value = obj
    if c_type == 'int_pointer':
        value = self.interface.get_pintValue(obj)
    elif c_type == 'word_pointer':
        value = self.interface.get_pWORDValue(obj)
    elif c_type == 'bool_pointer':
        value = self.interface.get_pBOOLValue(obj)
    elif c_type == 'compare_results':
        value = self.get_special_type_value_from_compare_results(obj)
    elif c_type == 'plc_info':
        value = self.get_special_type_value_from_plc_info(obj)
    elif c_type == 'memory_info':
        value = self.get_special_type_value_from_memory_info(obj)
    elif c_type == 'clock_struct':
        value = self.get_special_type_value_from_clock_struct(obj)
    elif c_type == 'sdb_data':
        value = self.get_special_type_value_from_sdb_data(obj)
    elif c_type == 'compass_element':
        value = self.get_special_type_value_from_compass_element(obj)
    elif c_type == 'wizard_pn_data':
        value = self.get_special_type_value_from_wizard_pn_data(obj)

    return value


def get_special_type_value_from_compare_results(obj):
    """get the value from special c_type object
    Args:
        obj        type(word_pointer,)        C++ interface return value.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-14
    """

    value = dict()
    field_info = (('ob', 'cObResults'), ('db', 'cDbResults'), ('sdb', 'cSdbResults'))
    for k, v in field_info:
        result = getattr(obj, v)
        value[k] = result

    return value


def get_special_type_value_from_plc_info(obj):
    """get the value from special c_type object
    Args:
        obj        type(word_pointer,)        C++ interface return value.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    value = dict()
    field_info = (
        ('version', 'GetFirmwareRevision', (0,)),
        ('event_count', 'GetEventCount', tuple()),
        ('alarm_count', 'GetAlarmCount', tuple())
    )
    for k, v, p in field_info:
        c_str = getattr(obj, v)(*p)
        value[k] = c_str
    # get all event log
    value['event_logs'] = list()
    for i in range(value['event_count']):
        event_type_code = getattr(obj, 'GetEventTypeCode')(i)
        event_error_code = getattr(obj, 'GetEventErrorCode')(i)
        event_datetime = getattr(obj, 'GetEventDateTime')(i)
        event_log = {'type_code': event_type_code, 'error_code': event_error_code, 'datetime': event_datetime}
        value['event_logs'].append(event_log)

    return value


def get_special_type_value_from_memory_info(self, obj):
    """get the value from special c_type object
    Args:
        obj        type(word_pointer,)        C++ interface return value.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    value = None
    address_type = obj.m_sAddress.m_eMemType
    if address_type == self.convert_data_type('eCOMMCOMPASS_MEM_TYPE_BYTE', 'struct_arg'):
        value = self.interface.get_pByteBYTE(obj.m_pData)
    elif address_type == self.convert_data_type('eCOMMCOMPASS_MEM_TYPE_WORD', 'struct_arg'):
        value = self.interface.get_pByteWord(obj.m_pData)
    elif address_type == self.convert_data_type('eCOMMCOMPASS_MEM_TYPE_DWORD', 'struct_arg'):
        value = self.interface.get_pByteDWORD(obj.m_pData)

    return value


def get_special_type_value_from_clock_struct(obj):
    """get the value from special c_type object
    Args:
        obj        type(word_pointer,)        C++ interface return value.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    result = {
        'year': obj.year,
        'month': obj.month,
        'day': obj.date,
        'hour': obj.hour,
        'minutes': obj.minutes,
        'seconds': obj.seconds,
        'spare': obj.spare,
        'weekDay': obj.weekDay,
    }

    return result


def get_special_type_value_from_sdb_data(self, obj):
    """get the value from special c_type object
    Args:
        obj        type(word_pointer,)        C++ interface return value.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    result = {
        'password_level': obj.m_common.m_password.GetPasswordLevel(),
        'back_ground_time': obj.m_common.m_backgroundTime.GetBackgroundTime(),
        'retentive_ranges': obj.m_common.m_retentiveRanges.GetNumberOfElements(0),
        'cpu_mode': obj.m_common.m_startup.GetCPUMode(),
        'fixed_ip': obj.m_common.m_ethernet.IsStoreInProject(),
        'ip': self.long_to_ip(obj.m_common.m_ethernet.GetIP()),
        'station_name': obj.m_common.m_ethernet.GetStationName(),
        'versions': self.convert_data_type(0, 'c_str_array'),
        'obj': obj
    }
    obj.m_cpu.GetModuleVersions(result['versions'])

    return result


def get_special_type_value_from_compass_element(obj):
    """get the value from special c_type object
    Args:
        obj        type(word_pointer,)        C++ interface return value.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-04
    """

    result = {
        'cpu_type': obj.m_ModuleData.m_Device,
        'cpu_version': obj.m_ModuleData.m_Version
    }

    return result


def get_special_type_value_from_wizard_pn_data(self, obj):
    """get the value from special c_type object
    Args:
        obj        type(word_pointer,)        C++ interface return value.
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    m_smart200 = obj.m_Smart200PLCPDEV
    result = {
        'is_enabled': obj.IsEnabled(),
        'role': m_smart200.GetPLCRole(),
        'ip': self.long_to_ip(m_smart200.GetIPAddr()),
        'sub_net_mask': self.long_to_ip(m_smart200.GetSubNetMask()),
        'gate_way': self.long_to_ip(m_smart200.GetGateWay()),
        'station_name': m_smart200.GetStationName(),
        'send_clock': m_smart200.GetSendClock(),
        'startup_time': m_smart200.GetStartUpTime(),
        'obj': obj
    }

    return result
