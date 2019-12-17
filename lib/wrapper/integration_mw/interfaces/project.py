#!/usr/bin/env python


def project_new(self, params=None):
    """Create a new project on Micro/WIN
    Args:
        params           type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        pProjectPath     type(str)          the abspath of the new project
        strEntryPoint    type(str)
        hMWinProject     type(int)
        rstrType         type(str)
        rstrVersion      type(str)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'pProjectPath': {'to_type': 'p_str', 'option': False},
        'pEntryPoint': {'to_type': 'p_str', 'default': 'MWSMART', 'option': True},
        'hMWinProject': {'to_type': 'word_pointer', 'default': 1, 'option': True},
        'rstrType': {'to_type': 'c_str', 'default': '', 'option': True},
        'rstrVersion': {'to_type': 'c_str', 'default': '', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_New}


def project_init(self, params=None):
    """Initialize project
    Args:
        params           type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-11-25
    """

    self.check_params(params, dict())

    return {'params': params, 'interface': self.interface.PRJ_InitNewMwProject}


def project_open(self, params=None):
    """Open a local project
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        strFileName    type(str)          the abspath of local project file
        strPassword    type(str)
        strEntryPoint  type(str)
        hMWinProject   type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'strFileName': {'to_type': 'c_str', 'option': False},
        'strPassword': {'to_type': 'c_str', 'default': '', 'option': True},
        'strEntryPoint': {'to_type': 'c_str', 'default': 'MWSMART', 'option': True},
        'hMWinProject': {'to_type': 'word_pointer', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_Open}


def project_validate(self, params=None):
    """Check the password of the project
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        strFileName    type(str)          the abspath of local project file
        strPassword    type(str)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'strFileName': {'to_type': 'c_str', 'option': False},
        'strPassword': {'to_type': 'c_str', 'default': '', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_ValidateProjectFile}


def project_download(self, params=None):
    """download project
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        eBlockType     type(str)          download type: BLOCK_TYPE_INVALID, BLOCK_TYPE_OB, BLOCK_TYPE_DB,
                                                        BLOCK_TYPE_SDB, BLOCK_TYPE_ALL
        hMainWnd       type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'eBlockType': {'to_type': 'struct_arg', 'default': 'BLOCK_TYPE_ALL', 'option': True},
        'hMainWnd': {'to_type': 'hwnd', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_Download}


def project_upload(self, params=None):
    """Upload project
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        eBlockType     type(int)          upload type: BLOCK_TYPE_INVALID, BLOCK_TYPE_OB, BLOCK_TYPE_DB,
                                                       BLOCK_TYPE_SDB, BLOCK_TYPE_ALL
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'eBlockType': {'to_type': 'struct_arg', 'default': 'BLOCK_TYPE_ALL', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_Upload}


def project_upload_data_log(self, params=None):
    """Upload data log
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        strFolder      type(str)          the local path for save the data log file
        rOptions       type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'strFolder': {'to_type': 'c_str', 'option': False},
        'rOptions': {'to_type': 'c_type', 'option': False}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.WIZ_DataLogUpload}


def project_data_log_get_upload_options(self, params=None):
    """Get options of the data log
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rOptions       type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'rOptions': {'to_type': 'data_log_upload_options', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.WIZ_DataLogGetUploadOptions}


def project_save(self, params=None):
    """Save the project file
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    self.check_params(params, dict())

    return {'params': params, 'interface': self.interface.PRJ_Save}


def project_save_as(self, params=None):
    """Save the project file as
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        pProjectPath   type(str)          the abspath for save the project
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-17
    """

    template = {
        'pProjectPath': {'to_type': 'p_str', 'option': False}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_SaveAs}


def project_set_editor(self, params=None):
    """Set the editor type of project
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        EditorType     type(int)          editor type: (S7_LAD, S7_STL, S7_FBD, IEC_LD, IEC_FBD, S7_NONE, MAX_EDITOR,
                                                       IEC_STL)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-10
    """

    template = {
        'EditorType': {'to_type': 'struct_arg', 'default': 'S7_LAD', 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_SetEditor}


def project_close(self, params=None):
    """Close the opened project.
    Args:
        params         type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        hMWinProject   type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-21
    """

    template = {
        'hMWinProject': {'to_type': 'p_int', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_Close}


def project_export(self, params=None):
    """Export the opened project.
    Args:
        params              type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        sPouId              type(dict)         e_type: POU_BASE, POU_MAIN, POU_SBR, POU_INT, POU_ALL, POU_VIEW
        pExportFilePath     type(str)          the abspath for export the project
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-21
    """

    template = {
        'sPouId': {'to_type': 'mw_id', 'default': {'e_type': 'POU_MAIN'}, 'option': True},
        'pExportFilePath': {'to_type': 'p_str', 'option': False}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_Export}


def project_import(self, params=None):
    """Export the opened project.
    Args:
        params              type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        pImportFilePath     type(str)          the abspath for import the awl file
        pwErrorCount        type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-21
    """

    template = {
        'pImportFilePath': {'to_type': 'p_str', 'option': False},
        'pwErrorCount': {'to_type': 'word_pointer', 'default': 0, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_Import}


def project_compile(self, params=None):
    """Compile project.
    Args:
        params              type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        rErrorCount         type(str)
        rSize               type(int)
        bReLoad             type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-21
    """

    template = {
        'rErrorCount': {'to_type': 'word_pointer', 'default': 0, 'option': True},
        'rSize': {'to_type': 'word_pointer', 'default': 0, 'option': True},
        'bReLoad': {'to_type': 'p_type', 'default': True, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.POU_CompilePous}


def project_set_password(self, params=None):
    """Set the password for project.
    Args:
        params              type(dict)         the parameters used to invoke the interface
        ------------------------------------------------------------------------------
        params detail:
        strPassword         type(str)
        bIsSha512           type(int)
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-09-21
    """

    template = {
        'strPassword': {'to_type': 'c_str', 'option': False},
        'bIsSha512': {'to_type': 'p_int', 'default': 1, 'option': True}
    }
    self.check_params(params, template)

    return {'params': params, 'interface': self.interface.PRJ_SetPassword}
