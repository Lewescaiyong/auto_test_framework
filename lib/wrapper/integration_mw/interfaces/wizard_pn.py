#!/usr/bin/env python


def pn_get_configuration(self, params=None):
    """Get the configuration of PN wizard
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rData          type(dict)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-23
    """

    template = {
        'rData': {'to_type': 'wizard_pn_data', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.WIZ_PNGetConfiguration}


def pn_set_configuration(self, params=None):
    """Set the configuration of PN wizard
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rData          type(dict)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-25
    """

    template = {
        'rData': {'to_type': 'wizard_pn_data', 'option': False}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.WIZ_PNSetConfiguration}


def pn_set_network_info(self, params=None):
    """Set the network information of PN wizard
    Args:
        params            type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        plcRole           type(int)
        isFixedIP         type(bool)
        plcIP             type(str)
        subNetMask        type(str)
        startupTime       type(int)
        plcName           type(str)
        strType           type(str)
        strVer            type(c_str)
        paraDisallowed    type(bool)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-25
    """

    template = {
        'plcRole': {'to_type': 'p_int', 'option': False},
        'isFixedIP': {'to_type': 'p_bool', 'default': False, 'option': True},
        'plcIP': {'to_type': 'c_str', 'default': '', 'option': True},
        'subNetMask': {'to_type': 'c_str', 'default': '255.255.255.0', 'option': True},
        'startupTime': {'to_type': 'p_int', 'default': 10000, 'option': True},
        'plcName': {'to_type': 'c_str', 'default': '', 'option': True},
        'strType': {'to_type': 'c_str', 'option': False},
        'strVer': {'to_type': 'c_str', 'option': False},
        'paraDisallowed': {'to_type': 'p_bool', 'default': False, 'option': True},
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_SetPLCPDEVProperties}


def validate_wizard_pn(self, params=None):
    """Validate wizard pn
    Args:
        params                   type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rData                    type(wizard_pn_data)
        targetErrorObject        type(str)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-25
    """

    template = {
        'rData': {'to_type': 'c_type', 'option': False},
        'targetErrorObject': {'to_type': 'c_str', 'default': '', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.WIZ_PNConfigurationValidation,
            'check_function': self.check_function}


def validate_wizard_pn_auto(self, params=None):
    """Validate wizard pn auto test
    Args:
        params                   type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        targetErrorObject        type(str)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-25
    """

    template = {
        'targetErrorObject': {'to_type': 'c_str', 'default': '', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.WIZ_PNConfigurationValidationAutoTest,
            'check_function': self.check_function}


def pn_config_complete(self, params=None):
    """PN configuration complete
    Args:
        params                   type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        isShowMsgBox             type(bool)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-25
    """

    template = {
        'isShowMsgBox': {'to_type': 'p_bool', 'default': False, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.WIZ_PNConfigurationComplete}


def pn_is_support(self, params=None):
    """Whether can configuration pn wizard
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rIsSupported   type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-18
    """

    template = {
        'rIsSupported': {'to_type': 'bool_pointer', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_IsProfinetSupported}


def controller_is_support(self, params=None):
    """Whether can configuration pn wizard
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rIsSupported   type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-18
    """

    template = {
        'rIsSupported': {'to_type': 'bool_pointer', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_IsProfinetControllerSupported}


def add_transfer_area_to_controller(self, params=None):
    """Add transfer area to controller
    Args:
        params                  type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        deviceId                type(int)
        slotNum                 type(int)
        subslotNubmer           type(int)
        submoduleIDstr          type(int)
        submoduleIdentNumber    type(int)
        ioType                  type(int)
        address                 type(int)
        length                  type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-29
    """

    template = {
        'deviceId': {'to_type': 'p_int', 'default': 1, 'option': True},
        'slotNum': {'to_type': 'p_int', 'default': 1, 'option': True},
        'subslotNubmer': {'to_type': 'p_int', 'option': False},
        'submoduleIDstr': {'to_type': 'c_str', 'option': False},
        'submoduleIdentNumber': {'to_type': 'p_int', 'option': False},
        'ioType': {'to_type': 'p_int', 'option': False},
        'address': {'to_type': 'p_int', 'option': False},
        'length': {'to_type': 'p_int', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_AddPNTransferAreaSubModule}


def i_device_is_support(self, params=None):
    """Whether can configuration pn wizard
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rIsSupported   type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-18
    """

    template = {
        'rIsSupported': {'to_type': 'bool_pointer', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_IsProfinetIDeviceSupported}


def add_transfer_area_to_i_device(self, params=None):
    """Add transfer area to i-device
    Args:
        params          type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        subslotNubmer   type(int)
        ioType          type(int)
        address         type(int)
        length          type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-29
    """

    template = {
        'subslotNubmer': {'to_type': 'p_int', 'option': False},
        'ioType': {'to_type': 'p_int', 'option': False},
        'address': {'to_type': 'p_int', 'option': False},
        'length': {'to_type': 'p_int', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_AddTransferAreaToIDevice}


def add_io_device(self, params=None):
    """Add IO device to controller device.
    Args:
        params                   type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        strGSDFullPathName       type(str)
        nDapModuleIDstr          type(str)
        dapModuleIdentNumber     type(int)
        deviceNumber             type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-28
    """

    template = {
        'strGSDFullPathName': {'to_type': 'c_str', 'option': False},
        'nDapModuleIDstr': {'to_type': 'c_str', 'option': False},
        'dapModuleIdentNumber': {'to_type': 'c_int_s', 'option': False},
        'deviceNumber': {'to_type': 'p_int', 'option': False}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_AddPNDevice}


def set_io_device_properties(self, params=None):
    """Set IO device properties.
    Args:
        params                   type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        strGSDFullPathName       type(str)
        nDapModuleIDstr          type(str)
        dapModuleIdentNumber     type(int)
        deviceNumber             type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-28
    """

    template = {
        'deviceNumber': {'to_type': 'p_int', 'option': False},
        'isIPFixed': {'to_type': 'p_int', 'option': False},
        'deviceIP': {'to_type': 'c_str', 'default': '', 'option': True},
        'deviceUpdateTime': {'to_type': 'p_int', 'default': 4, 'option': True},
        'watchdog': {'to_type': 'p_int', 'default': 3, 'option': True},
        'deviceName': {'to_type': 'c_str', 'option': False},
        'paraDisallowed': {'to_type': 'p_type', 'default': False, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_SetPNDeviceProperties}
