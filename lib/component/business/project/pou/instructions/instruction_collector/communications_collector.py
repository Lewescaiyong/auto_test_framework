#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.communications.receive import Receive
from lib.component.business.project.pou.instructions.communications.ouc_send import OUCSend
from lib.component.business.project.pou.instructions.communications.transmit import Transmit
from lib.component.business.project.pou.instructions.communications.network_get import NetworkGet
from lib.component.business.project.pou.instructions.communications.network_put import NetworkPut
from lib.component.business.project.pou.instructions.communications.ouc_connect import OUCConnect
from lib.component.business.project.pou.instructions.communications.ouc_receive import OUCReceive
from lib.component.business.project.pou.instructions.communications.get_ip_address import GetIPAddress
from lib.component.business.project.pou.instructions.communications.set_ip_address import SetIPAddress
from lib.component.business.project.pou.instructions.communications.ouc_disconnect import OUCDisconnect
from lib.component.business.project.pou.instructions.communications.get_port_address import GetPortAddress
from lib.component.business.project.pou.instructions.communications.set_port_address import SetPortAddress


class CommunicationsCollector(BusinessBase):
    """Communications instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-03
    """

    def __init__(self, own_software, params=None):
        super(CommunicationsCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-03
        """

        config = {
            'transmit': Transmit,
            'receive': Receive,
            'get_port_address': GetPortAddress,
            'set_port_address': SetPortAddress,
            'get_ip_address': GetIPAddress,
            'set_ip_address': SetIPAddress,
            'network_get': NetworkGet,
            'network_put': NetworkPut,
            'ouc_connect': OUCConnect,
            'ouc_send': OUCSend,
            'ouc_receive': OUCReceive,
            'ouc_disconnect': OUCDisconnect
        }

        return config
