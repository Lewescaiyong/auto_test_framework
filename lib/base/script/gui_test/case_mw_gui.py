#!/usr/bin/env python
import os
import shutil

from lib.base.script.case_base import CaseBase
from lib.tools.public.information import Information
from lib.tools.sanity_comm.utils import prepare_app, close_app
from lib.tools.sanity_comm.const_str import GSD_PATH, PROJECT_PATH, SOURCE_PATH


class CaseMWGUI(CaseBase):
    """ The parent class of micro win gui test.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-10-30
    """

    plc_info = ''
    smart_app = ''

    def prepare(self):
        """the preparation before executing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-10-30 create
        """
        super(CaseMWGUI, self).prepare()
        local_path = Information.get_framework_local_path()
        source_path = os.path.join(local_path, 'test_case', 'no_piling', 'sanity_ui', 'source')
        if not os.path.exists(GSD_PATH + os.sep + 'GSDML-V2.3-Siemens-ET200M-20121214.xml'):
            shutil.copy(source_path + os.sep + 'GSDML-V2.3-Siemens-ET200M-20121214.xml', GSD_PATH)
        if not os.path.exists(SOURCE_PATH + 'MOV.awl'):
            shutil.copy(source_path + os.sep + 'MOV.awl', SOURCE_PATH)

        smart_files = os.listdir(source_path)
        for file in smart_files:
            if file.endswith('.smart'):
                if not os.path.exists(PROJECT_PATH + file):
                    shutil.copy(source_path + os.sep + file, PROJECT_PATH)

        plc_info = self.resource.test_bed_info['PLCs']['PLC']
        self.plc_info = plc_info[0]['PLCInfo'] if isinstance(plc_info, list) else plc_info['PLCInfo']
        self.smart_app = prepare_app()

    def cleanup(self):
        """clean up after performing the test steps
        Args:
        Example:
        Return:
        Author: Cai, Yong
        IsInterface: False
        ChangeInfo: Cai, Yong 2019-10-30 create
        """
        super(CaseMWGUI, self).cleanup()
        close_app()
