#!/usr/bin/env python

import re
import threading
from importlib import import_module

from lib.component.component_base import ComponentBase
from lib.exceptions.check_exception import CheckException
from lib.exceptions.not_found_exception import NotFoundException


class SoftwareBase(ComponentBase):
    """Software parent class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    lock = threading.RLock()

    def __init__(self, params):
        self.upgrade_version = params.get('Version', '')
        self.views = dict()
        self.register_wrapper()
        super(SoftwareBase, self).__init__(params)

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
        if params is None:
            params = dict()
        # get wrapper info
        wrapper_info = self.get_wrapper_info(wrapper)
        # invoke the interface
        interface_info = wrapper_info['function'](params)
        special_type = interface_info['params'].pop('special_type')
        self.logger.info('Wrapper name: %s' % wrapper)
        code = self.invoke_interface(interface_info)
        # process special type params
        result = self.process_special_type_obj(params, special_type)
        result['code'] = code
        # check status code
        check_function = interface_info.get('check_function') or self.check_status_code
        check_function(code)

        return result

    def invoke_interface(self, interface_info):
        """Invoke interface
        Args:
            interface_info             type(dict)            interface information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        no_session = ('InitEnv', 'CreateSession', 'LoadInstructionLibs', 'GetMicroWinVersion')

        with self.lock:
            for i in range(3):
                if not re.search('|'.join(no_session), str(interface_info['interface'])):
                    self.create_session()
                    log_str = self.log_str
                    self.logger.info(log_str)
                if interface_info.get('args_order'):
                    args = self.get_args_by_order(interface_info)
                    code = interface_info['interface'](*args)
                else:
                    code = interface_info['interface'](**interface_info['params'])

                if code in (-1609007018, -1609007059, -1609007101):
                    self.set_connect_plc()
                    continue
                break

        return code

    def create_session(self, plc=None):
        """create connection with plc
        Args:
            plc            type(lib.component.plc.plc.PLC)      PLC to be connected to Micro/WIN.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

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

        return 'Starting invoking interface...'

    @staticmethod
    def get_args_by_order(interface_info):
        """Get parameters from params dict by order
        Args:
            interface_info             type(dict)            interface information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-27
        """

        args = list()
        for i in interface_info['args_order']:
            args.append(interface_info['params'][i])

        return tuple(args)

    def set_connect_plc(self, plc=None):
        """Set connection info of plc
        Args:
            plc            type(lib.component.plc.plc.PLC)      PLC to be connected to Micro/WIN.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

    def check_status_code(self, code):
        """Check the interface called status code
        Args:
            code        type(str)        interface called status code.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        if code != 0:
            raise CheckException('The status code returned after calling the interface is %s not 0.' % code)
        self.logger.info('Interface called successfully.')

    def process_special_type_obj(self, params, special_type):
        """process special c_type obj
        Args:
            params        type(dict)        the params dict after calling the interface.
            special_type  type(dict)        a dictionary that records all special types of parameters
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        result = dict()
        for k, v in special_type.items():
            result[k] = self.converter.get_special_type_value(params[k], v)
            self.converter.destroy_special_type_obj(params[k], v)

        return result

    def get_wrapper_info(self, wrapper):
        """Find wrapper information from the registered views
        Args:
            wrapper             type(str)            the function name of wrapper
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        wrapper_info = dict()
        for k, v in self.views.items():
            if getattr(v, wrapper, None):
                wrapper_info['view'] = v
                wrapper_info['function'] = getattr(v, wrapper)
                break
        else:
            raise NotFoundException('The wrapper[%s] was not found in the registered view' % wrapper)

        return wrapper_info

    def register_wrapper(self):
        """register interface wrapper
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        # get wrapper views needs to register
        views = self.register_views
        for view_class, module_path in views.items():
            self.register(view_class, module_path)

    def register(self, view_class, module_path):
        """register single wrapper view
        Args:
            view_class          type(str)            the class name of wrapper view
            module              type(str)            the module path for import
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        # get view class object
        module = import_module(module_path)
        class_obj = getattr(module, view_class)
        # get register params
        params = self.register_params
        # register
        view = class_obj(params)
        self.views[view.view] = view

    @property
    def register_views(self):
        """The wrapper views needs to register
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        return dict()

    @property
    def register_params(self):
        """The parameters used to register wrapper view
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        return dict()

    @property
    def version(self):
        """The version of software.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        return ''

    def upgrade(self, upgrade_file='', is_task_server=True):
        """Upgrade software
        Args:
            upd_file        type(str)         the abspath of upgrade file
            is_task_server  type(bool)        is the task server calling
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        updater = self.find('upgrade')
        result = updater.upgrade(upgrade_file, is_task_server)

        return result
