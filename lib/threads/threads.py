#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import traceback
import threading
from random import randrange
from threading import Thread


class Threads(Thread):
    """Overwrite the Thread class to record exception information for child threads.
    Args:
        target           type(callable object)        function to call.
        args             type(tuple)                  parameters passed when calling target
        kwargs           type(dict)                   parameters passed when calling target
        name             type(str)                    name of the child thread
        logger           type(lib.log.log.Log)        use when you need to specify a log object for the child thread
    Example:
    Return:
    Author: cai, yong
    IsInterface: True
    ChangeInfo: cai, yong 2019-08-20
    """
    th_ids = dict()

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, logger=None):
        super(Threads, self).__init__(group, target, name, args, kwargs)
        self.th_id = None
        self.message = ''
        self.logger = None
        self.get_th_id()
        self.get_logger(logger)

    def run(self):
        """execute function.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """
        try:
            super(Threads, self).run()
        except Exception as e:
            self.message = e
            self.logger.error(traceback.format_exc())
            raise

    def kill(self):
        """kill child thread.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: True
        ChangeInfo: cai, yong 2019-08-20
        """
        ret = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(self.ident), ctypes.py_object(SystemExit))

        return ret

    def get_th_id(self):
        """get th_id property.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        self.th_id = randrange(1E6)
        while self.th_id in Threads.th_ids:
            self.th_id = randrange(1E6)

        Threads.th_ids[self.th_id] = self

    def get_logger(self, logger=None):
        """get logger object for this thread.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        if hasattr(threading.currentThread(), 'logger'):
            logger = getattr(threading.currentThread(), 'logger')

        self.logger = logger
