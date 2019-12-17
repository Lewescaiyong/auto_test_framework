#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading


class SingleInstance(type):
    """Single instance father class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-12
    """

    def __call__(cls, *args, **kwargs):
        cls._instance_lock = threading.Lock()
        with cls._instance_lock:
            if not hasattr(cls, '_instance'):
                cls._instance = super(SingleInstance, cls).__call__(*args, **kwargs)

        return cls._instance
