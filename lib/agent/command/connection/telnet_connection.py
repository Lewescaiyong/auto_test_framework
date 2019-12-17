#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import socket
import telnetlib

from lib.agent.command.connection.connection_base import ConnectionBase
from lib.exceptions.connecton_exception import ConnectionException


class TelnetConnection(ConnectionBase):
    """Telnet protocol connection class.
    Args:
        connect_info        type(dict)         connection information
        --------------------------------------------------
        connect_info details
        ip                  type(str)           ip address
        user                type(str)           username
        password            type(str)           password
        port                type(str)           port number
    Example:
        connect_info = {'ip': '127.127.0.1', 'user': 'admin', 'password': '123456', 'port': 23}
        conn = TelnetConnection(connect_info)
        conn.login()
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-23
    """

    def __init__(self, connect_info):
        super(TelnetConnection, self).__init__()
        self.ip = connect_info['ip']
        self.user = connect_info.get('user', '')
        self.password = connect_info.get('password', '')
        self.port = connect_info.get('port', 23)
        self.client = None
        self.sep = '\r\n'

    def login(self):
        """Login remote device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        if not self.client:
            self.client = self.create_client()
        self.authentication()

        # login status analysis
        self.login_analyze()

    def create_client(self):
        """Create a connection client to the remote device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        for i in range(3):
            try:
                client = telnetlib.Telnet(host=self.ip, port=self.port, timeout=10)
            except (socket.timeout, socket.error) as e:
                time.sleep(5)
                self.logger.warning(e)
            else:
                return client
        # throw the most recently caught exception
        raise

    def authentication(self):
        """Authentication.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        info, is_match, match_str = self.receive('login:')
        if not match_str:
            raise ConnectionException('login failed, can not find str: "login:"')
        info, is_match, match_str = self.execute(self.user, wait_str='password:')
        if not match_str:
            raise ConnectionException('login failed, can not find str: "password:"')
        self.execute(self.password)

    def login_analyze(self):
        """Login status analysis.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        info, is_match, match_str = self.execute('cd')
        if not match_str:
            self.wait_normal()

    def wait_normal(self, timeout=600):
        """Wait device normal.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        end_time = time.time() + timeout
        while time.time() < end_time:
            info, is_match, match_str = self.execute('dir')
            if match_str:
                break
        else:
            raise ConnectionException('wait for device[%s] normal timeout.' % self.ip)

    def close(self):
        """Logout remote device.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        if self.client:
            self.client.close()

        self.client = None

    def reconnect(self):
        """Login remote device again.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        self.close()
        self.login()

    def cmd(self, cmd_info):
        """Command send interface.
        Args:
            cmd_info            type(dict)          command info
            ---------------------------------------------------------
            cmd_info details
            command             type(str)           command str
            wait_str            type(str)           end identifier of command executing
            directory           type(str)           work directory
            input_list          type(list)          subsequent command: [cmd1, wait_str1, cmd2, wait_str2, ...]
            input_dict          type(dict)          subsequent command: {cmd1: wait_str1, cmd2: wait_str2, ...}
            timeout             type(int)           max wait time of command sending and echo receiving
            confirm             type(bool)          whether to automatically process y/yes
        Example:
            cmd_info = {'command': 'ls', 'wait_str': r'>'}
            result = conn.cmd(cmd_info)
        Return:
            result = {'stdout': info after execute cmd}
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        result = {'stdout': ''}

        # change work path
        if cmd_info.get('directory'):
            self.execute(command=re.search(r'\w:', cmd_info['directory']).group())
            self.execute(command='cd %s' % cmd_info['directory'])
        # get default wait_str
        default_wait_str = self.get_default_wait_str()
        # judge by "confirm" whether to automatically process y/yes
        confirm = cmd_info.get('confirm', True)
        # get max wait time of command sending and echo receiving
        timeout = cmd_info.get('timeout', 120)
        # summarize commands that need to be send sequentially
        commands = [(cmd_info['command'], cmd_info.get('wait_str') or default_wait_str)]
        if cmd_info.get('input_list'):
            input_list = cmd_info['input_list']
            for i in range(len(input_list), 2):
                if i == len(input_list) - 1:
                    commands.append((input_list[i], default_wait_str))
                else:
                    commands.append((input_list[i], input_list[i + 1]))
        # send command
        if cmd_info.get('input_dict'):
            input_dict = cmd_info['input_dict']
            wait_str = str(commands[0][1]) + '|' + '|'.join(input_dict.keys())
            info, is_match, match_str = self._cmd(commands[0][0], wait_str, timeout, confirm)
            while is_match and input_dict.get(match_str):
                result['stdout'] += info
                info, is_match, match_str = self._cmd(input_dict[match_str], wait_str, timeout, confirm)
            result['stdout'] += info
        else:
            for c, w in commands:
                info, is_match, match_str = self._cmd(c, w, timeout, confirm)
                result['stdout'] += info

        return result

    def _cmd(self, command, wait_str=r'\w:\\\w*', timeout=120, confirm=True):
        """Process where 'y/n' is encountered by send command.
        Args:
            command             type(str)           command str
            wait_str            type(str)           end identifier of command executing
            timeout             type(int)           max wait time of command sending and echo receiving
            confirm             type(bool)          whether to automatically process y/yes
        Example:
            info, is_match, match_str = conn._cmd('ls')
        Return:
            info, is_match, match_str = receive_info, True, '>'
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        all_info = ''
        if confirm:
            wait_str += '|y/n|yes/no'
        info, is_match, match_str = self.execute(command, wait_str, timeout)
        while match_str == 'y/n' and confirm:
            all_info += info
            info, is_match, match_str = self.execute('y', wait_str, timeout)
        while match_str == 'yes/no' and confirm:
            all_info += info
            info, is_match, match_str = self.execute('yes', wait_str, timeout)

        all_info += info

        return info, is_match, match_str

    def execute(self, command, wait_str=r'\w:(?:\\\w+)*>$|\w:\\>$', timeout=120):
        """Send single command and receive echo.
        Args:
            command             type(str)           command str
            wait_str            type(str)           end identifier of command executing
            timeout             type(int)           max wait time of command sending and echo receiving
        Example:
            info, is_match, match_str = conn.execute('ls')
        Return:
            info, is_match, match_str = receive_info, True, '>'
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        if not self.send(command, timeout):
            return None, None, None

        info, is_match, match_str = self.receive(wait_str, timeout)

        return info, is_match, match_str

    def send(self, command, timeout=120):
        """Send single command.
        Args:
            command             type(str)           command str
            timeout             type(int)           max wait time of command sending and echo receiving
        Example:
            result = conn.send('ls')
        Return:
            result = True or False
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                self.client.write(self.encode(command + self.sep))
                self.logger.info('send cmd: "%s".' % command)
            except socket.timeout:
                self.logger.info('send cmd: "%s" timeout.' % command)
                time.sleep(2)
            else:
                return True

        return False

    def receive(self, wait_str=r'\w:(?:\\\w+)*>$|\w:\\>$', timeout=120):
        """Receive echo.
        Args:
            wait_str            type(str)           end identifier of command executing
            timeout             type(int)           max wait time of command sending and echo receiving
        Example:
            info, is_match, match_str = conn.receive('>')
        Return:
            info, is_match, match_str = receive_info, True, '>'
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        info = ''
        is_match = False
        match_str = None
        end_time = time.time() + timeout
        while time.time() < end_time:
            receive = ''
            try:
                receive = self.client.expect([self.encode('smart200 framework')], .1)[2]
                receive = self.decode(receive)
            except socket.timeout:
                pass
            if receive:
                info += receive
            searcher = re.search(wait_str, receive)
            if searcher:
                is_match = True
                match_str = searcher.group()
                break
        # culling color character
        info = re.sub(r'\x1b\[(?:\d{1,2};)?\d{0,2}m|\x1b\]\d{1,2};', '', info)
        self.logger.info('Receive: \n %s.' % info)

        return info, is_match, match_str

    @staticmethod
    def get_default_wait_str():
        """Get default wait str.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        return r'\w:(?:\\\w+)*>$|\w:\\>$'

    def is_active(self):
        """Get connection status.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        if self.client:
            try:
                self.client.read_eager()
            except (EOFError, AttributeError):
                return False
            else:
                return True

        return False

    @staticmethod
    def encode(a_str):
        """Encode str.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        return a_str.encode('utf-8')

    @staticmethod
    def decode(a_str):
        """Decode str.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-23
        """

        return a_str.decode('gbk')
