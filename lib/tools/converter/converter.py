#!/usr/bin/env python

import os
import sys
import socket
import struct
import datetime

try:
    import lib.wrapper.integration_mw.source.MicroWinExecInterface as Interface
except ImportError:
    Interface = None
from lib.log.log import Log
from lib.log.txt_to_html import TxtToHtml
from lib.tools.public.common import Common
from lib.tools.public.information import Information
from lib.base.framework.smart200_base import Smart200Base


class Converter(Smart200Base):
    """Converter.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-29
    """

    def __init__(self):
        super(Converter, self).__init__()
        self.common = Common()
        self.interface = Interface
        self.information = Information()
        self.str_list = self.interface.CStringList() if self.interface else None
        self.register_functions()

    @property
    def register_config(self):
        """Register configuration.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        modules = ['lib.tools.converter.functions.destroy',
                   'lib.tools.converter.functions.get_value',
                   'lib.tools.converter.functions.to_c_type',
                   'lib.tools.converter.functions.to_p_type']

        return modules

    def register_functions(self):
        """Register functions.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-29
        """

        modules = self.register_config
        self.common.register_functions(self, modules)

    @property
    def data_type_config(self):
        """[smart200 wrapper data type -- C++ interface data type] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        config = {
            'c_str': 'CString',
            'c_int_s': 'LongS',
            'c_str_array': 'CStringArray',
            'int_pointer': '',
            'word_pointer': ('LPWORD', 'HMWPROJ*', 'WORD&'),
            'bool_pointer': '',
            'byte_pointer': 'byte *',
            'struct_arg': ('BLOCK_TYPES', 'PROGRAMMING_EDITOR'),
            'hwnd': 'HWND',
            'rectangle': 'GRID_RECTANGLE',
            'mw_id': 'MW_ID',
            'cell_location': 'GRID_CELL_LOCATION',
            'operand_location': 'GRID_OPERAND_LOCATION',
            'plc_info': 'EX_PLCInformationData',
            'compare_options': 'COMPARE_DLG_OPTIONS',
            'compare_results': 'COMPARE_RESULTS',
            'network_info': 'MWNetworkInfo',
            'data_log_upload_options': 'DATALOG_UPLOAD_OPTIONS',
            'memory_info': 'sCOMMCOMPASS_MEM_STRUCT',
            'wizard_pn_data': 'EX_PNWizardData',
            'sdb_data': 'SDBData',
            'clock_struct': 'TIME_DATE_STRUCT',
            'compass_element': 'COMPASS_ELEMENT',
            'p_int': ('WORD', 'DWORD', 'HMWPROJ'),
            'p_float': 'float',
            'p_bool': 'bool',
            'p_str': ('LPCTSTR', 'LPTSTR')
        }

        return config

    @property
    def data_type_convert_config(self):
        """[data type -- convert function] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        config = {
            'c_str': getattr(self, 'convert_to_c_str'),
            'c_int_s': getattr(self, 'convert_to_c_int_s'),
            'c_str_array': getattr(self, 'convert_to_c_str_array'),
            'int_pointer': getattr(self, 'convert_to_int_pointer'),
            'word_pointer': getattr(self, 'convert_to_word_pointer'),
            'bool_pointer': getattr(self, 'convert_to_bool_pointer'),
            'byte_pointer': getattr(self, 'convert_to_byte_pointer'),
            'struct_arg': getattr(self, 'convert_to_struct_arg'),
            'hwnd': getattr(self, 'convert_to_hwnd'),
            'rectangle': getattr(self, 'convert_to_rectangle'),
            'mw_id': getattr(self, 'convert_to_mw_id'),
            'cell_location': getattr(self, 'convert_to_cell_location'),
            'operand_location': getattr(self, 'convert_to_operand_location'),
            'plc_info': getattr(self, 'convert_to_plc_info'),
            'compare_options': getattr(self, 'convert_to_compare_options'),
            'compare_results': getattr(self, 'convert_to_compare_results'),
            'network_info': getattr(self, 'convert_to_network_info'),
            'data_log_upload_options': getattr(self, 'convert_to_data_log_upload_options'),
            'memory_info': getattr(self, 'convert_to_memory_info'),
            'wizard_pn_data': getattr(self, 'convert_to_wizard_pn_data'),
            'sdb_data': getattr(self, 'convert_to_sdb_data'),
            'clock_struct': getattr(self, 'convert_to_clock_struct'),
            'compass_element': getattr(self, 'convert_to_compass_element'),
            'p_int': getattr(self, 'convert_to_p_int'),
            'p_float': getattr(self, 'convert_to_p_float'),
            'p_str': getattr(self, 'convert_to_p_str'),
            'p_type': getattr(self, 'convert_to_p_type'),
            'p_bool': getattr(self, 'convert_to_p_bool'),
            'c_type': getattr(self, 'convert_to_c_type')
        }

        return config

    def convert_data_type(self, data, to_type):
        """Convert python object to c_type
        Args:
            data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
            to_type        type(str)                                   type to be converted
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-09
        """

        data = self.data_type_convert_config.get(to_type)(data)

        return data

    @staticmethod
    def convert(data, func):
        """Convert python object to c_type str
        Args:
            data           type(int, str, tuple, list, dict)           Python data that needs to be converted.
            func           type(function)                              the method converting data types
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-09
        """

        result = func(data)

        return result

    @staticmethod
    def ip_to_long(ip):
        """Converts a str type IP address to decimal number
        Args:
        Example:
            self.converter.ip_to_long('255.255.255.0')
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        long = struct.unpack('!I', socket.inet_aton(ip))

        return long[0]

    @staticmethod
    def long_to_ip(number):
        """Converts a decimal number to str type IP address
        Args:
        Example:
            self.converter.long_to_ip(4294967040)
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        ip = socket.inet_ntoa((struct.pack('!I', number)))

        return ip

    def get_data_from_std(self, obj, c_type='c_str'):
        """Get data from stdout
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-18
        """

        # redirect the standard output stream
        old_file = sys.stdout
        resource_path = self.information.get_resource_path()
        new_file = os.path.join(resource_path, 'txt', 'get_data_from_std.txt')
        f = open(new_file, 'w')
        sys.stdout = f

        if c_type == 'c_str':
            print('test')
            self.interface.print_CString(obj)

        sys.stdout = old_file
        f.close()

        with open(new_file) as f:
            data = f.read()

        return data

    @staticmethod
    def convert_time_to_str(datetime_obj=None, pattern='%Y%m%d_%H%M%S'):
        """Converts a datetime object to str
        Args:
            datetime_obj          type(datetime)          datetime object
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-27
        """

        if datetime_obj is None:
            datetime_obj = datetime.datetime.now()

        time_str = datetime_obj.strftime(pattern)

        return time_str

    @staticmethod
    def convert_to_int(number, number_type):
        """Converts a number to int
        Args:
            number          type(int, hex, bin)          the number to be converted
            number_type     type(int)                    enum: 2, 10, 16
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        result = int(str(number), number_type)

        return result

    def convert_to_hex(self, number, number_type, remove_0x=True):
        """Converts a number to hex
        Args:
            number          type(int, hex, bin)          the number to be converted
            number_type     type(int)                    enum: 2, 10, 16
            remove_0x       type(bool)                   whether to remove start str: "0x"
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        result = self.convert_to_int(number, number_type)
        result = hex(result)
        if remove_0x:
            result = result[2:]

        return result

    def convert_to_bin(self, number, number_type, length=32, remove_0b=True):
        """Converts a number to bin
        Args:
            number          type(int, hex, bin)          the number to be converted
            number_type     type(int)                    enum: 2, 10, 16
            length          type(int)                    length of str after converted to bin
            remove_0b       type(bool)                   whether to remove start str: "0b"
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        result = self.convert_to_int(number, number_type)
        result = bin(result)
        if remove_0b:
            result = result[2:]
            result = self.convert_to_special_length_str(result, length)

        return result

    @staticmethod
    def convert_to_special_length_str(data, length, fill='0', fill_type='left'):
        """Converts a number to be a special length str
        Args:
            data            type(int, str)          the data to be converted
            length          type(int)               the length of str after converted
            fill            type(str)               str used to be filled
            fill_type       type(str)               fill type: left, right
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        data = str(data).strip()

        if fill_type == 'left':
            data = data.rjust(length, fill)
        else:
            data = data.ljust(length, fill)

        return data

    def change_byte(self, number, number_type, length=8, bit=0, value=0):
        """Change
        Args:
            number          type(int, hex, bin)     the number to be converted
            number_type     type(int)               enum: 2, 10, 16
            length          type(int)               the length of bin(${data})
            bit             type(str)               range(${length})
            value           type(str)               the value of the ${bit}
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        number = self.convert_to_bin(number, number_type, length)
        number = list(number)
        number.reverse()
        number[bit] = value
        number.reverse()

        return ''.join(number)

    @staticmethod
    def convert_log_to_html(log_files=(), is_del=True,
                            ignore=('agent_server.txt', 'initialize.txt', 'agent_client.txt')):
        """Convert TXT log file to HTML file
        Args:
            log_files      type(tuple)           files to be converted to html.
            is_del         type(bool)            whether to delete the txt file after converted
            ignore         type(tuple)           files to ignore.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        converter = TxtToHtml(log_path=Log.log_path, log_files=log_files, is_del=is_del, ignore=ignore)
        converter.txt_to_html()

    def convert_log_to_html_not_del(self, ignore=('agent_server.txt', 'initialize.txt', 'agent_client.txt')):
        """Not delete the txt file after converting to HTML file
        Args:
            ignore         type(tuple)           files to ignore.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        log_file = self.information.get_current_thread_log_file()
        self.convert_log_to_html(log_files=(log_file,), is_del=False, ignore=ignore)
