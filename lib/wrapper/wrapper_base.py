#!/usr/bin/env python

from lib.base.framework.has_interface.has_interface import HasInterface


class WrapperBase(HasInterface):
    """The parent class of wrapper.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """

    def __init__(self, params=None):
        super(WrapperBase, self).__init__()
        self.interface = self.converter.interface
        self.register_interface(params)
        self.version_config = dict()

    def register_interface(self, params=None):
        """Create a socket object.
        Args:
            ip                  type(str)           ip address
            port                type(str)           port number
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        if params is None:
            params = dict()

        # register public interface
        modules = self.get_public_interface()
        self.common.register_functions(self, modules)

        # register version interface
        if params.get('version'):
            modules = self.get_version_interface(params['version'])
            self.common.register_functions(self, modules)

    def get_public_interface(self):
        """Create a socket object.
        Args:
            ip                  type(str)           ip address
            port                type(str)           port number
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        return list()

    def get_version_interface(self, version=''):
        """Create a socket object.
        Args:
            version         type(str)         the version of micro win
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """

        return list()

    def check_params(self, params, template): 
        """check params.
        Args:
            params         type(dict)         the parameters used to invoke the interface
            template       type(dict)         wrapper method default parameter information
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-26
        """
        # clear the str list
        self.converter.str_list.RemoveAll()

        if params is None:
            params = dict()
        # add default parameter value
        for k, v in template.items():
            if k not in params and v.get('default', None) is not None:
                params[k] = v['default']

        # convert parameter data type
        self.logger.info('Params: %s.' % params)
        for k, v in params.items():
            to_type = template[k]['to_type']
            params[k] = self.converter.convert_data_type(v, to_type)

        # check special type
        special_type = dict()
        for k in params:
            if not template[k]['to_type'].startswith('p_'):
                special_type[k] = template[k]['to_type']
        params['special_type'] = special_type

    @staticmethod
    def check_function(code):
        """Check the interface called status code
        Args:
            code        type(str)        interface called status code.
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        return code
