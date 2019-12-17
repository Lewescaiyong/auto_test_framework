#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.network.network_collector import NetworkCollector


class POUBase(BusinessBase):
    """The pou page base class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-21
    """

    def __init__(self, own_software, params=None):
        super(POUBase, self).__init__(own_software, params)

    @property
    def business_config(self):
        """Config the businesses type that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-22
        """

        business = ('network_collector',)

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

        config = {'network_collector': NetworkCollector}

        return config

    @property
    def properties_config(self):
        """Config the properties that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        config = {'pou_type': '', 'mw_id': None, 'rectangle': None, 'password': ''}

        return config

    @property
    def own_project(self):
        """Get own project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        return self.params['own_business'].params['own_business']

    def get_mw_id(self):
        """Get the mw_id of the POU.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        if not self.params['mw_id']:
            mw_id = self.converter.convert_data_type({'e_type': self.params['pou_type']}, 'mw_id')
            self.add_properties({'mw_id': mw_id})

        return self.params['mw_id']

    def get_rectangle(self):
        """Get the grid rectangle of the POU.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        if not self.params['rectangle']:
            self.add_properties({'rectangle': self.own_software.dispatch('grid_rectangle')['code']})

        return self.params['rectangle']

    def pou_set_protection(self, password='', is_clear=False):
        """Set pou protection.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-25
        """

        if is_clear:
            result = self.pou_authorize(is_clear=is_clear)
            self.logger.info('Clear the password of the pou [%s].' % self.params['pou_type'])
            self.add_properties({'password': ''})
        else:
            result = self.own_software.dispatch(
                'pou_set_password', {'rPouId': {'e_type': self.params['pou_type']}, 'rPassword': password})
            self.logger.debug('Set the password for the pou [%s], password: [%s].' % (
                self.params['pou_type'], password))
            self.add_properties({'password': password})

        return result

    def pou_is_protected(self):
        """Whether the pou is protected..
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-25
        """

        result = self.own_software.dispatch('pou_is_protected', {'rId': {'e_type': self.params['pou_type']}})['rStyle']

        return result

    def pou_authorize(self, password=None, is_clear=False):
        """POU authorize.
        Args:
            password          type(str)         the password of the pou
            is_clear          type(str)         whether to clear the password
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-25
        """

        is_clear = 1 if is_clear else 0
        password = password if password is not None else self.params['password']
        result = self.own_software.dispatch(
            'pou_authorize', {'rPouId': {
                'e_type': self.params['pou_type']}, 'rPassword': password, 'bPermanent': is_clear})
        self.logger.debug('Set the password for the pou [%s], password: [%s].' % (self.params['pou_type'], password))

        return result
