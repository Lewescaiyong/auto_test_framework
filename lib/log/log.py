#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
import shutil
import threading
import logging
import datetime
import logging.config


class Log(object):
    """Log info logging interface.
    Args:
        logger_name      type(str)        name of logger object
        add_console      type(str)        whether add a console handler
        add_file         type(str)        whether add a file handler
        date_type        type(int)        0: 20190827_094230; 1: 2019_08_27; 2: 10_30_20
        is_task          type(bool)       is it the process of executing automated scripts
    Example:
        logger = log.Log('log_name')
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-08-20
    """
    lock = threading.Lock()
    is_init = False
    log_path = ""
    local_path = ""
    date_type = 0
    is_task = False
    simple_format = "%(message)s"
    complex_format = "[%(asctime)s-%(thread)d-%(levelname)s]: %(message)s"

    def __init__(self, logger_name, add_console=True, add_file=True, date_type=0, is_task=False):
        Log.date_type = date_type
        Log.is_task = is_task
        self.name = logger_name
        self.add_console = add_console
        self.add_file = add_file
        self.instance_lock = threading.Lock()
        self.init_logger()
        self.logger = logging.getLogger(self.name)
        self.add_handlers()

    @classmethod
    def init_logger(cls, save_number=7):
        """init logger object.
        Args:
            save_number       type(int)        number of retained logs
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        with cls.lock:
            # only initialized once
            if cls.is_init:
                return
            # create log folder
            cls.local_path = os.path.dirname(__file__)
            cls.create_log_folder()
            # delete expired log
            cls.remove_log_file(save_number)
            # load log configuration
            with open(os.path.join(cls.local_path, 'config.yaml')) as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
            logging.config.dictConfig(config)
            cls.is_init = True

    @classmethod
    def create_log_folder(cls):
        """init logger folder.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        is_create = False

        if cls.is_task:
            cls.log_path = os.path.join(cls.local_path, 'logs', cls.get_date_str(1), cls.get_date_str(cls.date_type))
        else:
            cls.log_path = os.path.join(cls.local_path, 'logs', cls.get_date_str(cls.date_type))
        if not os.path.exists(cls.log_path):
            os.makedirs(cls.log_path)
            is_create = True

        return is_create

    @classmethod
    def get_date_str(cls, date_type=0):
        """init logger folder.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        if date_type == 0:
            date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        elif date_type == 1:
            date = datetime.datetime.now().strftime("%Y_%m_%d")
        else:
            date = datetime.datetime.now().strftime("%H_%M_%S")

        return date

    @classmethod
    def remove_log_file(cls, save_number=4):
        """delete expired log.
        Args:
            save_times       type(int)        number of retained logs
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """
        file_list = os.listdir(os.path.join(cls.local_path, 'logs'))
        rm_list = file_list[:-save_number]
        list(map(lambda log_path: shutil.rmtree(os.path.join(cls.local_path, 'logs', log_path)), rm_list))

    def add_handlers(self, format_type="complex"):
        """add log handlers.
        Args:
            file_name        type(str)        name of log file
            add_console      type(str)        whether add a console handler
            add_file         type(str)        whether add a file handler
            format_type      type(str)        log info format
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        self.logger.setLevel(logging.DEBUG)
        self.logger.handlers = list()
        if self.add_console:
            self.add_console_handler(format_type)
        if self.add_file:
            self.add_file_handler(format_type)

    def add_console_handler(self, format_type="complex"):
        """add console handler.
        Args:
            format_type      type(str)        log info format
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """
        if format_type == "complex":
            format_str = self.complex_format
        else:
            format_str = self.simple_format

        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(format_str)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def add_file_handler(self, format_type="complex"):
        """add file handler.
        Args:
            file_name        type(str)        name of log file
            format_type      type(str)        log info format
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """
        if format_type == "complex":
            format_str = self.complex_format
        else:
            format_str = self.simple_format

        log_file = os.path.join(self.log_path, '%s.txt' % self.name)
        handler = logging.FileHandler(log_file, "a", encoding="utf-8")
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(format_str)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @classmethod
    def info(cls, data):
        """Info level log printing interface.
        Args:
            data             type(str)        log info
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        cls.__log(data, 'info')

    @classmethod
    def debug(cls, data):
        """Debug level log printing interface.
        Args:
            data             type(str)        log info
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        cls.__log(data, 'debug')

    @classmethod
    def warning(cls, data):
        """Warn level log printing interface.
        Args:
            data             type(str)        log info
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        cls.__log(data, 'warning')

    @classmethod
    def error(cls, data):
        """Error level log printing interface.
        Args:
            data             type(str)        log info
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        cls.__log(data, 'error')

    @classmethod
    def __log(cls, data, level):
        """Info level log printing interface.
        Args:
            data             type(str)        log info
            level            type(str)        log level
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """
        th = threading.currentThread()
        logger = getattr(th, 'logger', None)
        if not logger:
            print(data)
        else:
            with logger.instance_lock:
                if level == "info":
                    logger.logger.info(data)
                elif level == "debug":
                    logger.logger.debug(data)
                elif level == "warning":
                    logger.logger.warning(data)
                elif level == "error":
                    logger.logger.error(data)

    @classmethod
    def release_log_file(cls):
        """release log file.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """
        th = threading.currentThread()
        logger = getattr(th, 'logger', None)
        if logger:
            logger.logger.handlers = list()

    @classmethod
    def reset_log_file(cls):
        """reset file handler.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-08-20
        """

        # get logger object of this thread
        th = threading.currentThread()
        logger = getattr(th, 'logger', None)
        if not logger:
            return

        with logger.instance_lock:
            # create log folder
            is_create = logger.create_log_folder()
            if is_create:
                # release log file
                logger.release_log_file()
                # add handler again
                logger.add_handlers()


if __name__ == '__main__':
    log = Log('test')
    threading.currentThread().logger = log
    # Log.release_log_file()
    # Log.debug('this is a test msg.')
