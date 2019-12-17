#!/usr/bin/env python

import time

from lib.component.business.business_base import BusinessBase


class MemoryOptions(BusinessBase):
    """Force business class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-22
    """

    @property
    def convert_type_config(self):
        """Convert type config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        config = {
            2: lambda x, y: x,
            10: self.converter.convert_to_int,
            16: self.converter.convert_to_hex,
        }

        return config

    @property
    def memory_area_config(self):
        """Memory area type config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        config = {
            'i': 'eCOMMCOMPASS_MEM_AREA_I',
            'q': 'eCOMMCOMPASS_MEM_AREA_Q',
            'v': 'eCOMMCOMPASS_MEM_AREA_V',
            'm': 'eCOMMCOMPASS_MEM_AREA_M',
            't': 'eCOMMCOMPASS_MEM_AREA_T',
            'c': 'eCOMMCOMPASS_MEM_AREA_C',
            'hc': 'eCOMMCOMPASS_MEM_AREA_HC',
            'sm': 'eCOMMCOMPASS_MEM_AREA_SM'
        }

        return config

    @property
    def address_type_config(self):
        """Address type config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        config = {
            'byte': {'type': 'eCOMMCOMPASS_MEM_TYPE_BYTE', 'length': 1},
            'word': {'type': 'eCOMMCOMPASS_MEM_TYPE_WORD', 'length': 2},
            'dword': {'type': 'eCOMMCOMPASS_MEM_TYPE_DWORD', 'length': 4}
        }

        return config

    def read_memory_data(self, memory_area, address_type='byte', start_address=0, number=1, need_type=10):
        """Read memory data of PLC.
        Args:
            memory_area           type(str)            memory area type: i, q, v, m, t, c, hc, sm
            address_type          type(str)            address type: byte, word, dword
            start_address         type(int)            start address
            number                type(str)            the number of ${address_type} need to be queried
            need_type             type(int)            the result type of return
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        values = list()
        for i in range(number):
            value = self._read_memory_data(memory_area, address_type, start_address)
            # byte[high>low], word[low>high]
            values.append(value)
            start_address += self.address_type_config[address_type]['length']
            time.sleep(1)

        result = self.convert_type_config[need_type](''.join(values), 2)

        return result

    def _read_memory_data(self, memory_area, address_type, start_address=0):
        """Read a DWORD memory data of PLC.
        Args:
            memory_area           type(str)            memory area type: i, q, v, m, t, c, hc, sm
            address_type          type(str)            address type: byte, word, dword
            start_address         type(int)            start address
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        network_info = {'ip': self.own_software.ip}
        memory_info = {
            'memory_area': self.memory_area_config[memory_area],
            'address_type': self.address_type_config[address_type]['type'],
            'address_length': self.address_type_config[address_type]['length'],
            'start_address': start_address
        }
        params = {'rcInfo': network_info, 'asMemory': memory_info}
        result = self.own_software.dispatch('read_memory_data', params)
        value = self.converter.convert_to_bin(result['asMemory'], 10, memory_info['address_length'] * 8)

        return value

    def force(self, memory_area, address_type, start_address=0, bit=None, value=0):
        """Force a value to a memory on PLC
        Args:
            memory_area           type(str)            memory area type: v
            address_type          type(str)            address type: word
            start_address         type(int)            start address
            bit                   type(int)            range(8)
            value                 type(int)            the value to be forced
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """
        if (address_type == 'byte') and (bit is not None):
            current_value = self.read_memory_data(memory_area, address_type, start_address)
            length = self.address_type_config[address_type]['length'] * 8
            value = self.converter.change_byte(current_value, 10, length, bit, value)
            value = self.convert_type_config[10](value, 2)

        network_info = {'ip': self.own_software.ip}
        memory_info = {
            'memory_area': self.memory_area_config[memory_area],
            'address_type': self.address_type_config[address_type]['type'],
            'address_length': self.address_type_config[address_type]['length'],
            'start_address': start_address,
            'address_value': value
        }
        params = {'rcInfo': network_info, 'asMemory': memory_info}
        result = self.own_software.dispatch('force', params)

        return result

    def unforce_all(self):
        """UnForce all memory on PLC
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        result = self.own_software.dispatch('unforce_all')

        return result
