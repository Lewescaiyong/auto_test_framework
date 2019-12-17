"""
This file mainly contains dialog title,
and button name, input control name on it
"""
import os


class Title(object):
    """
    define some constant str for dialog title.
    """
    WIN_SMART = 'STEP 7-Micro/WIN SMART'
    SAVE = 'Save|保存'
    SAVE_AS = 'Save As|另存为'
    CONFIRM_SAVE_AS = 'Confirm Save As'
    OPEN = 'Open|打开'
    COMMUNICATIONS = 'Communications|通信'
    RUN = 'RUN'
    STOP = 'STOP'
    PLC = 'PLC Information|PLC 信息'
    SYS_BLOCK = 'System Block|系统块'
    STATUS_BAR = 'Ready'
    STATUS_CHART = 'Status Chart'
    STATUS_CHART_ZH = '状态图表'
    VARIABLE_TAB = 'Variable Table'
    IMPORT_POU = 'Import Program Block|导入程序块'
    EXPORT_POU = 'Export Program Block|导出程序块'
    ADD_GSD = 'Manage general station description files|GSDML 管理'
    IMPORT_GSD = 'Import GSDML files|导入 GSDML 文件'
    GIRD = 'AfxWnd140'
    DOWNLOAD = 'Download|下载'
    UPLOAD = 'Upload|上传'
    PLC_Tree = 'SysTreeView32'
    TREE = PLC_Tree
    BROWSE_FOLDER = 'Browse For Folder'

    FIND_PN_DEVICE = 'Find PROFINET Devices'
    PN_CFG_WIZARD = 'PROFINET Configuration Wizard'
    DATALOG_WIZARD = 'Data Log Wizard'
    FIND_DEVICES = 'Find Devices'
    COMB = 'ComboBox'

    HSC_CFG_WIZARD = 'High Speed Counter Wizard'

    TOOL_BAR = 'Afx:ToolBar'

    UPLOAD_DATALOG = 'Upload Data Log'
    CLEAR = 'Clear|清除'
    MAIN = 'Main'
    SET_PROJ_PASSWD = 'Set Project Password'
    SET_POU_PASSWD = 'Properties'
    PROJ_PASSWD = 'Project Password'
    EDIT = 'Edit'
    STATIC = 'Static'
    WARNING = 'Warning'

    PROGRAM_MEM_CARD = 'Program Memory Card'
    COMPARE = 'Compare Project to CPU|比较项目与 CPU'
    WARM_START = 'Warm Start'
    SET_CLOCK = 'CPU Clock Operations'


class Button(object):
    """
    define some constant str for button identifier.
    """
    OPEN = 'Open'
    NO = 'No'
    CANCEL = 'Cancel'
    YES = 'Yes'
    OK = 'OK'
    SAVE = 'Save'
    BROWSE = 'Browse'
    DELETE = 'Delete'
    ADD = 'Add'
    DOWNLOAD = 'Download'
    UPLOAD = 'Upload'
    CLOSE = 'Close'
    NEXT = 'Next >'
    HSC0 = 'HSC0'
    GENERATE = 'Generate'
    BUTTON = 'Button'
    DATALOG0 = 'Data Log 0'
    CLEAR = 'Clear'
    AUTHORIZE = 'Authorize'
    PROGRAM = 'Program'
    MAKE_NEW_FOLDER = 'Make New Folder'
    BEGIN = 'Begin'
    RESTART = 'Restart'
    READ_PC = 'Read PC'
    SET = 'Set'
    FIND_DEVICES = 'Find Devices'
    CONTROLLER = 'Controller'
    I_DEVICE = 'I-Device'
    FIX_IP = 'Fixed IP address and name'
    EXPORT = 'Export'


GSD_PATH = 'C:\\Users\\Public\\Documents\\'
PROJECT_PATH = GSD_PATH + 'Siemens\\STEP 7-MicroWIN SMART\\Projects\\'
SOURCE_PATH = GSD_PATH + 'Siemens\\STEP 7-MicroWIN SMART\\Source\\'
GSDML_FOLDER = GSD_PATH + 'Siemens\\STEP 7-MicroWIN SMART\\GSDML\\'
MW_SMART_PATH = os.environ['MW_SMART_PATH'] + os.sep + "MWSmart.exe"

OPT_CLOSE = 'Close dialog on success'
OPT_RESET = 'Reset to factory defaults'
OPT_RUN = 'Prompt on STOP to RUN'
OPT_PROTECT = 'Password-protect this project'
OPT_PROTECT_POU = 'Password protect this block'
OPT_RM_PASSWD = 'Permanently remove password'
