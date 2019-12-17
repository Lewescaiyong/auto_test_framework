#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.symbol_table.io_symbols.io_symbols import IOSymbols
from lib.component.business.project.symbol_table.pou_symbols.pou_symbols import POUSymbols
from lib.component.business.project.symbol_table.table_normal.table_normal import TableNormal
from lib.component.business.project.symbol_table.system_symbols.system_symbols import SystemSymbols


class SymbolTable(BusinessBase):
    """Symbol table class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-25
    """

    def __init__(self, own_software, params=None):
        super(SymbolTable, self).__init__(own_software, params)

    @property
    def business_config(self):
        """Config the businesses type that requires pre-registration
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        business = ('table_normal', 'io_symbols', 'pou_symbols', 'system_symbols')

        return business

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-20
        """

        config = {'table_normal': TableNormal, 'io_symbols': IOSymbols, 'pou_symbols': POUSymbols,
                  'system_symbols': SystemSymbols}

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

        return self.params['own_business']
