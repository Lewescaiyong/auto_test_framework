#!/usr/bin/env python

from lib.base.framework.has_interface.has_interface import HasInterface


class ComponentBase(HasInterface):
    """component parent class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    def __init__(self, params=None):
        super(ComponentBase, self).__init__()
        self.params = params or dict()
        self.add_properties()
        self.businesses = dict()
        self.register_businesses()

    def add_properties(self, properties=None):
        """Add properties
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        if properties is None:
            properties = self.properties_config
            for k, v in properties.items():
                if k not in self.params:
                    self.params[k] = v
        else:
            for k, v in properties.items():
                self.params[k] = v

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        return dict()

    def register_businesses(self):
        """register business
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """

        for business_type in self.business_config:
            self.add(business_type)

    @property
    def business_config(self):
        """Config the businesses type that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        return tuple()

    def add(self, business_type, params=None, need_init=False):
        """Get registered business by business type
        Args:
            business_type    type(str)          business type: pou_main, pou_sbr, pou_int, network, instruction
            params           type(dict)         the business initialize parameters
            need_init        type(bool)         new_project: True, open_project: False
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """
        from lib.component.business.business_base import BusinessBase

        if params is None:
            params = dict()
        if isinstance(self, BusinessBase):
            params['own_business'] = self

        class_name = self.add_config[business_type]
        business = class_name(self.own_software, params)
        if need_init:
            business.initialize()
        self.record(business, business_type)

        return business

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        return dict()

    @property
    def own_software(self):
        """Get own software to invoke the interface
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """

        return self

    def initialize(self):
        """Initialize the business.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-25
        """

    def record(self, business, business_type):
        """Add the POU to self.pou_dict.
        Args:
            business         type(lib.component.business.business_base.BusinessBase)       business object
            business_type    type(str)          business type: pou_main, pou_sbr, pou_int, network, instruction
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        if business_type not in self.find_dict:
            self.find_dict[business_type] = business
        else:
            if not isinstance(self.find_dict[business_type], list):
                self.find_dict[business_type] = [self.find_dict[business_type]]
            self.find_dict[business_type].append(business)

    @property
    def find_dict(self):
        """The dictionary used to record business object
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        return self.businesses

    def find(self, find_type, properties=None):
        """Get registered business by business type
        Args:
            find_type        type(str)          business type: Project, pou_main, pou_sbr, pou_int, network, instruction
            properties       type(dict)         filters when finding pou
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """

        result = None

        find_type = find_type.lower()
        find_result = list()
        if self.find_dict.get(find_type):
            find_result = self.find_dict.get(find_type, list())
        if not isinstance(find_result, list):
            find_result = [find_result]

        for i in find_result:
            if self.compare_properties(i, properties):
                result = i
                break

        return result

    @staticmethod
    def compare_properties(business_object, properties=None):
        """Compare the business_object and properties
        Args:
            business_object     type(lib.component.business.business_base.BusinessBase)          business object
            properties          type(dict)                                                       properties dict
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-23
        """

        result = True
        if properties is None:
            properties = dict()

        for k, v in properties.items():
            if business_object.get_property(k) != v:
                result = False
                break

        return result

    def get_properties(self, properties_name=tuple()):
        """Get the properties of the business object.
        Args:
            properties_name       type(tuple)         properties name tuple
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        result = dict()

        for i in properties_name:
            result[i] = self.get_property(i)

    def get_property(self, property_name):
        """Get the property of the business object.
        Args:
            property_name       type(str)         property name
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        return self.params.get(property_name, None)

    @property
    def block_type_config(self):
        """Block type config
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-14
        """

        config = {
            'ob': 'BLOCK_TYPE_OB',
            'db': 'BLOCK_TYPE_DB',
            'sdb': 'BLOCK_TYPE_SDB',
            'all': 'BLOCK_TYPE_ALL',
            'invalid': 'BLOCK_TYPE_INVALID',
        }

        return config
