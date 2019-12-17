#!/usr/bin/env python

import re
import os

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.pou_collector import POUCollector
from lib.component.business.project.wizard.wizard_pn.wizard_pn import WizardPN
from lib.component.business.project.system_block.system_block import SystemBlock
from lib.component.business.project.symbol_table.symbol_table import SymbolTable


class Project(BusinessBase):
    """project business class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-20
    """

    def __init__(self, own_software, params=None):
        super(Project, self).__init__(own_software, params)

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

        business = ('pou_collector', 'system_block', 'wizard_pn', 'symbol_table')

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

        config = {'pou_collector': POUCollector, 'system_block': SystemBlock, 'wizard_pn': WizardPN,
                  'symbol_table': SymbolTable}

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

        config = {'password': ''}

        return config

    def initialize(self):
        """Initialize the project.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-25
        """

        # initialize project
        self.own_software.dispatch('project_init')
        # set cpu type in system block
        self.project_set_cpu_type()

    def project_new(self, project_name, save_path=''):
        """New a project on Micro/WIN
        Args:
            project_name          type(str)         the name of the new project
            save_path             type(str)         the local path to save the project
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        if not save_path:
            resource = self.information.get_resource_path()
            save_path = os.path.join(resource, 'project')

        project_file = os.path.join(save_path, project_name)
        self.own_software.dispatch('project_new', {'pProjectPath': project_file})
        self.initialize()

    def project_add_instruction(self, pou_type='pou_main', network_id=0, row_id=0, col_id=0,
                                instruction_type='normally_open', instruction_values=('SM0.0',)):
        """add a instruction in the project
        Args:
            pou_type               type(str)          pou type: pou_main, pou_sbr, pou_int
            network_id             type(int)          the network id in the pou where add instruction
            row_id                 type(int)          the row id in the network where add instruction
            col_id                 type(int)          the col id in the network where add instruction
            instruction_type       type(str)          instruction type: normally_open...
            instruction_values     type(tuple)        instruction values: ('SM0.0',)
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-25
        """

        # find the pou page collector
        pou_collector = self.find('pou_collector')
        # find the pou page
        pou_main = pou_collector.find(pou_type)
        # find the network collector
        network_collector = pou_main.find('network_collector')
        # add a network
        network = network_collector.add('network', {'id': network_id})
        # find the pou page collector
        instruction_collector = network.find('instruction_collector')
        # add the instruction
        instruction_collector.add(instruction_type, {'row_id': row_id, 'col_id': col_id, 'values': instruction_values},
                                  True)

    def project_open(self, prj_name, password=None):
        """open a local project
        Args:
            prj_name          type(str)         the name of the project file
            password          type(str)         the password of the project
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        if re.search(':', prj_name):
            file_name = prj_name
        else:
            source_path = self.information.get_resource_path()
            file_name = os.path.join(source_path, 'project', prj_name)

        # check password
        password = password if password is not None else self.params['password']
        self.own_software.dispatch('project_validate', {'strFileName': file_name, 'strPassword': password})

        result = self.own_software.dispatch('project_open', {'strFileName': file_name, 'strPassword': password})
        # set cpu type in system block
        self.project_set_cpu_type()

        return result

    def project_download(self, download_type='all'):
        """download project
        Args:
            download_type     type(str)          download type: ob, db, sdb, all, invalid
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        # set cpu type in system block
        self.project_set_cpu_type()
        # compile project
        self.project_compile()
        # set plc mode to stop
        self.own_software.conn_plc.set_plc_mode(0)
        # download project
        download_type = self.block_type_config[download_type]
        result = self.own_software.dispatch('project_download', {'eBlockType': download_type})

        return result

    def project_upload(self, upload_type='all'):
        """upload project
        Args:
            upload_type          type(str)         upload type: ob, db, sdb, all, invalid
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        upload_type = self.block_type_config[upload_type]
        result = self.own_software.dispatch('project_upload', {'eBlockType': upload_type})

        return result

    def project_upload_data_log(self, save_path=''):
        """upload data log
        Args:
            save_path          type(str)         the local path for save the data log file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        if not save_path:
            local_path = self.information.get_resource_path()
            save_path = os.path.join(local_path, 'data_log')

        options = self.own_software.dispatch('project_data_log_get_upload_options')['rOptions']
        result = self.own_software.dispatch('project_upload_data_log', {'strFolder': save_path, 'rOptions': options})

        return result

    def project_save(self):
        """Save the project file
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-20
        """
        # set project editor type
        self.own_software.dispatch('project_set_editor')
        # compile project
        self.project_compile()
        # save the project
        result = self.own_software.dispatch('project_save')

        return result

    def project_save_as(self, save_name, save_path=''):
        """Save the project file as
        Args:
            save_name          type(str)         the name of the project file
            save_path          type(str)         the local path for save the project
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-10
        """

        # set project editor type
        self.own_software.dispatch('project_set_editor')
        # compile project
        self.project_compile()

        if not save_path:
            local_path = self.information.get_resource_path()
            save_path = os.path.join(local_path, 'project')

        project_file = os.path.join(save_path, save_name)
        self.own_software.dispatch('project_save_as', {'pProjectPath': project_file})

        # check the result of save as
        result = self.file_options.file_is_exist(project_file)

        return result

    def project_close(self):
        """Close the opened project
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        result = self.own_software.dispatch('project_close')

        return result

    def project_export(self, export_name, export_path='', export_type='POU_MAIN'):
        """Export the opened project.
        Args:
            export_type         type(str)          export type: POU_BASE, POU_MAIN, POU_SBR, POU_INT, POU_ALL, POU_VIEW
            export_name         type(str)          the name of the awl file
            export_path         type(str)          the path for export the project
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        if not export_path:
            export_path = os.path.join(self.information.get_resource_path(), 'awl')
        awl_file = os.path.join(export_path, export_name)

        params = {'sPouId': {'e_type': export_type}, 'pExportFilePath': awl_file}
        self.own_software.dispatch('project_export', params)

        # check the result of export
        result = self.file_options.file_is_exist(awl_file)

        return result

    def project_import(self, import_name, import_path=''):
        """Import the awl file.
        Args:
            import_name         type(str)          the name of the awl file
            import_path         type(str)          the path for import the awl file
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-21
        """

        if not import_path:
            import_path = os.path.join(self.information.get_resource_path(), 'awl')
        awl_file = os.path.join(import_path, import_name)

        params = {'pImportFilePath': awl_file}
        result = self.own_software.dispatch('project_import', params)

        return result

    def project_compile(self):
        """Compile project.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-09-26
        """

        result = self.own_software.dispatch('project_compile')

        return result

    def project_set_protection(self, password='', is_clear=False):
        """Set project protection.
        Args:
            password          type(str)         the password of the project
            is_clear          type(str)         whether to clear the password
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-25
        """

        if is_clear:
            result = self.own_software.dispatch('project_set_password', {'strPassword': ''})
            self.logger.info('Clear the password of the project.')
            self.add_properties({'password': ''})
        else:
            result = self.own_software.dispatch('project_set_password', {'strPassword': password})
            self.logger.debug('Set the password for the project, password: [%s].' % password)
            self.add_properties({'password': password})

        return result

    def project_set_cpu_type(self, target_type=None):
        """Set cpu type in system block
        Args:
            target_type         type(str)          enum: ST30, SR30, ST20 ...
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-11-18 create
        """

        system_block = self.find('system_block')
        system_block.set_module_info({'cpu': {'cpu_type': target_type}})

    def check_after_clear(self):
        """Check the project on PLC after reset PLC
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-10-23
        """

        result = True
        # upload project
        self.project_upload()

        # check PN
        pn = self.find('wizard_pn')
        status = pn.check_after_clear()
        if not status:
            result = False

        # check SDB
        system_block = self.find('system_block')
        status = system_block.check_after_clear()
        if not status:
            result = False

        return result
