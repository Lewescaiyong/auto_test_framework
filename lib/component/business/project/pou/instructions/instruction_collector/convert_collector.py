#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.convert.round import Round
from lib.component.business.project.pou.instructions.convert.decode import Decode
from lib.component.business.project.pou.instructions.convert.encode import Encode
from lib.component.business.project.pou.instructions.convert.segment import Segment
from lib.component.business.project.pou.instructions.convert.truncate import Truncate
from lib.component.business.project.pou.instructions.convert.real_to_ascii import RealToASCII
from lib.component.business.project.pou.instructions.convert.real_to_string import RealToString
from lib.component.business.project.pou.instructions.convert.string_to_real import StringToReal
from lib.component.business.project.pou.instructions.convert.byte_to_integer import ByteToInteger
from lib.component.business.project.pou.instructions.convert.integer_to_byte import IntegerToByte
from lib.component.business.project.pou.instructions.convert.integer_to_ascii import IntegerToASCII
from lib.component.business.project.pou.instructions.convert.integer_to_string import IntegerToString
from lib.component.business.project.pou.instructions.convert.string_to_integer import StringToInteger
from lib.component.business.project.pou.instructions.convert.ascii_to_hexadecimal import ASCIIToHexadecimal
from lib.component.business.project.pou.instructions.convert.hexadecimal_to_ascii import HexadecimalToASCII
from lib.component.business.project.pou.instructions.convert.double_integer_to_real import DoubleIntegerToReal
from lib.component.business.project.pou.instructions.convert.double_integer_to_ascii import DoubleIntegerToASCII
from lib.component.business.project.pou.instructions.convert.string_to_double_integer import StringToDoubleInteger
from lib.component.business.project.pou.instructions.convert.double_integer_to_string import DoubleIntegerToString
from lib.component.business.project.pou.instructions.convert.integer_to_double_integer import IntegerToDoubleInteger
from lib.component.business.project.pou.instructions.convert.double_integer_to_integer import DoubleIntegerToInteger
from lib.component.business.project.pou.instructions.convert.binary_coded_decimal_to_integer import \
    BinaryCodedDecimalToInteger
from lib.component.business.project.pou.instructions.convert.integer_to_binary_coded_decimal import \
    IntegerToBinaryCodedDecimal


class ConvertCollector(BusinessBase):
    """Convert instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-05
    """

    def __init__(self, own_software, params=None):
        super(ConvertCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-05
        """

        config = {
            'byte_to_integer': ByteToInteger,
            'integer_to_byte': IntegerToByte,
            'integer_to_double_integer': IntegerToDoubleInteger,
            'integer_to_string': IntegerToString,
            'double_integer_to_integer': DoubleIntegerToInteger,
            'double_integer_to_real': DoubleIntegerToReal,
            'double_integer_to_string': DoubleIntegerToString,
            'binary_coded_decimal_to_integer': BinaryCodedDecimalToInteger,
            'integer_to_binary_coded_decimal': IntegerToBinaryCodedDecimal,
            'round': Round,
            'truncate': Truncate,
            'real_to_string': RealToString,
            'integer_to_ascii': IntegerToASCII,
            'double_integer_to_ascii': DoubleIntegerToASCII,
            'real_to_ascii': RealToASCII,
            'ascii_to_hexadecimal': ASCIIToHexadecimal,
            'hexadecimal_to_ascii': HexadecimalToASCII,
            'string_to_integer': StringToInteger,
            'string_to_double_integer': StringToDoubleInteger,
            'string_to_real': StringToReal,
            'decode': Decode,
            'encode': Encode,
            'segment': Segment
        }

        return config
