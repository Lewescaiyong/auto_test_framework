#!/usr/bin/env python


def destroy_special_type_obj(self, obj, c_type='word_pointer'):
    """destroy the special c_type object
    Args:
        obj        type(word_pointer,)        c_type object.
        c_type     type(str)                  the type of object
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    if c_type == 'int_pointer':
        self.interface.destroy_pint(obj)
    elif c_type == 'word_pointer':
        self.interface.destroy_pWORD(obj)
    elif c_type == 'bool_pointer':
        self.interface.destroy_pBOOL(obj)
    elif c_type == 'byte_pointer':
        self.interface.destroy_pByte(obj)
    elif c_type == 'memory_info':
        self.interface.destroy_pByte(obj.m_pData)
