#!/usr/bin/env python

import os
import pytest
import datetime

from lib.tools.public.information import Information


@pytest.hookimpl(tryfirst=True)
def pytest_cmdline_main(config):
    local_path = Information.get_framework_local_path()
    report = '%s/%s.html' % (os.path.join(local_path, 'report'), datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
    config.option.htmlpath = report
