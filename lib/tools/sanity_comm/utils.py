__author__ = 'wangxingyu 20190613'

from ctypes import cdll
from pywinauto.application import Application, WindowSpecification
from pywinauto.keyboard import send_keys
from ctypes import c_char_p
import time

from lib.tools.sanity_comm.const_str import *
from lib.tools.sanity_comm.cmd import *
from lib.tools.public.information import Information

local_path = Information().get_framework_local_path()
dll_file = os.path.join(local_path, 'lib', 'tools', 'sanity_comm', 'SmartTestDLL.dll')
dll = cdll.LoadLibrary(dll_file)
app: Application = None

cpu_dic = {'st20': 0, 'st30': 1, 'st40': 2, 'st60': 3,
           'sr20': 4, 'sr30': 5, 'sr40': 6, 'sr60': 7,
           'cr20s': 8, 'cr30s': 9, 'cr40s': 10, 'cr60s': 11,
           'cr40': 12, 'cr60': 13}


def prepare_app() -> Application:
    """
    connect to Micro/WIN software, and load smart_test_library.
    :return: Application handler that connected to Micro/WIN software
    """
    time.sleep(1)
    global app
    # app = Application().connect(class_name='SmartApp')
    app = Application().start(MW_SMART_PATH)
    app.SmartApp.wait('exists', timeout=10).set_focus()
    time.sleep(3)
    return app


def close_app() -> bool:
    """
    close Micro/WIN software
    :return: if closed the window
    """
    # close the window
    if not app:
        raise ConnectionError('test app is not connected to Micro/WIN SMART.')
    success = exec_cmd(APP_CLOSE)
    time.sleep(0.5)
    if success:
        handle_popup_dialog(Title.WIN_SMART, Button.NO, btn_index=1)
        # app.SmartApp.wait_not('exists', timeout=10)
    time.sleep(1)
    return success


def exec_cmd(cmd: int) -> bool:
    """
    use dll lib to execute cmd, return the result.
    :param cmd: an integer operation cmd.
    :return: if execute successfully return True, else return False.
    """
    success = dll.Misc_ExecuteCommand(cmd)
    if success:
        return True
    return False


def handle_popup_dialog(title: str, btn_opt: str, btn_index: int = None, timeout: int = 10) -> bool:
    """
    when a  popup dialog appears, click Yes or No to dismiss it.
    :param title: popup dialog title.
    :param btn_opt: Yes/No/OK/Cancel button.
    :param btn_index: btn index.
    :param timeout: timeout time after which, stop the test.
    :return: True if handled popup dialog, False if no popup dialog appears.
    """
    time.sleep(0.5)
    dialog = app.windows(title_re=title)
    if not dialog:
        return False

    dialog = app.window(title_re=title)
    dialog.set_focus()
    time.sleep(0.5)
    close_dialog_with_button(dialog, btn_opt, btn_index=btn_index)
    dialog.wait_not('exists', timeout=timeout)
    return True


def close_dialog_with_button(dlg: WindowSpecification, btn: str, btn_index: int = None, timeout: int = 10) -> None:
    """
    click button on the dialog to close the dialog.
    :param dlg: dialog window.
    :param btn: button to be clicked.
    :param btn_index: btn index.
    :param timeout: timeout time after which, stop the test.
    :return: None to return.
    """
    time.sleep(0.5)
    dlg.set_focus()
    if btn_index is not None:
        btn = dlg.child_window(class_name="Button", ctrl_index=btn_index)
    else:
        btn = dlg[btn]
    btn.set_focus()
    time.sleep(0.5)
    btn.click()
    dlg.wait_not('exists', timeout=timeout)


def wait_window_exists(title: str, timeout: int = 10) -> WindowSpecification:
    """
    wait for target window get exists.
    :param title: window title.
    :param timeout: timeout time after which no window appears, raise Error.
    :return: return target window.
    """
    win = app.window(title_re=title)
    win.wait('exists', timeout=timeout)
    win.set_focus()
    return win


def set_window_addr(wnd: WindowSpecification, path: str):
    """
    set open file window address.
    :param wnd: popup window to choose file
    :param path: address of directory for file to choose
    :return: None
    """
    time.sleep(0.5)
    addr_bar = wnd.child_window(class_name='ReBarWindow32')
    toolbar = addr_bar.child_window(class_name='ToolbarWindow32', ctrl_index=2)
    toolbar.set_focus()
    time.sleep(0.5)
    toolbar.click()
    path = path.split(' ')
    for part in path:
        send_keys(part)
        send_keys('{SPACE}')
    send_keys('{ENTER}')


def get_grid_text(row: int, col: int, ctrl_index: int = 0, grid: WindowSpecification = None) -> str:
    """
    get text of a grid table.
    :param row: row of the table.
    :param col: column of the table.
    :param ctrl_index: index of grid.
    :param grid: grid table control.
    :return: the text of th cell.
    """
    if not grid:
        app.top_window().child_window(class_name=Title.GIRD, ctrl_index=ctrl_index).set_focus()
    else:
        grid.set_focus()
    p_str = c_char_p(b'\0'*128)
    success = dll.Grid_GetCellText(0, row, col, p_str, 128)
    if success:
        return p_str.value.decode()
    return None


def set_grid_text(row: int, col: int, value: str, grid: WindowSpecification = None) -> bool:
    """
    set grid text value
    :param row: row of the table.
    :param col: column of the table.
    :param value: new value.
    :param grid: grid table control.
    :return: True if set, or False if not set
    """
    if not grid:
        app.top_window().child_window(class_name=Title.GIRD, ctrl_index=0).set_focus()
    else:
        grid.set_focus()
    p_str = c_char_p(value.encode('utf-8')+b'\0')
    success = dll.Grid_SetCellText(0, row, col, p_str, len(value)+1)
    if success:
        return True
    return False


def get_plc_connection() -> str:
    """
    get connection info of PLC device
    :return: status of device connection
    """
    pass


def get_plc_status() -> str:
    """
    get status of PLC device
    :return: status of PLC device
    """
    p_str = c_char_p(b'\0' * 32)
    status_bar = app.SmartApp.Ready
    status_bar.set_focus()
    time.sleep(0.5)
    success = dll.StatusBar_GetText(20303, p_str, 32)
    if success:
        return p_str.value.decode()
    return None


def set_check_box(wnd: WindowSpecification, opt: str, index: int = None):
    """
    check an option
    :param wnd: window for handle
    :param opt: check box to choose
    :param index: index of check option
    :return:
    """
    if index:
        check_box = wnd.child_window(class_name="Button", ctrl_index=index)
    else:
        check_box = wnd[opt]
    is_checked = check_box.is_checked()
    if not is_checked:
        check_box.set_focus()
        time.sleep(0.5)
        check_box.click()


def select_dropdown_item(comb: WindowSpecification, item: int):
    """
    select an option for the dropdown list
    :param comb: dropdown control
    :param item: index of the item
    :return:
    """
    comb.set_focus()
    time.sleep(0.5)
    comb.click()
    comb.select(item)


def click_btn(btn: WindowSpecification):
    """
    just click a button
    :param btn: button control
    :return:
    """
    btn.set_focus()
    time.sleep(0.5)
    btn.click()


def get_toolbar_btn(container_title: str, btn_index: int) -> WindowSpecification:
    """
    get toolbar button by index.
    :param container_title: toolbar parent container title.
    :param btn_index: button index base on 0.
    :return: button control.
    """
    p = app.SmartApp[container_title]
    tool_bar = p.window(class_name_re=Title.TOOL_BAR)
    btn = tool_bar.button(btn_index)
    return btn


def get_connect_with_plc(which: str = None) -> bool:
    """
    create connect with a PLC device.
    :param which: PLC ip address.
    :return: True if connection is ok or False if not ok.
    """
    # send `Communication` command
    success = exec_cmd(COMMUNICATION)
    if not success:
        return success
    # get communications window
    comm_win = wait_window_exists(Title.COMMUNICATIONS)
    comb_opt = comm_win.CombBox
    comb_opt.select('Realtek PCIe GBE Family Controller.TCPIP.Auto.1')

    time.sleep(10)
    if which:
        found_cpus = comm_win.child_window(class_name=Title.TREE).set_focus()
        has_find = False
        items = found_cpus.texts()
        index = 0
        for i, e in enumerate(items):
            if e.startswith(which):
                which = e
                index = i
                has_find = True
                break
        if has_find:
            found_cpus.select((0, index-2))
            # found_cpus.select('\\Found CPUs\\'+which)
        else:
            raise Exception('Not find CPU with IP address:'+which)

    # close communications window by click `OK` button
    close_dialog_with_button(comm_win, Button.OK, btn_index=4)
    return success


def set_plc_stop() -> bool:
    """
    set connected PLC in `STOP` mode.
    :return: True if stopped or False if not.
    """
    success = exec_cmd(PLC_STOP)
    if not success:
        return success

    # get popup window, click yes button to stop PLC
    stop_win = wait_window_exists(Title.STOP)
    close_dialog_with_button(stop_win, Button.YES, btn_index=0)

    time.sleep(5)

    # check if PLC`s status is stop
    # status = get_plc_status()
    # return status == Title.STOP
    return True


def set_plc_run() -> bool:
    """
    set connected PLC in `RUN` mode.
    :return: True if run or False if not.
    """
    success = exec_cmd(PLC_RUN)
    if not success:
        return success

    # get popup `RUN` window, and click `Yes` button
    run_win = wait_window_exists(Title.RUN)
    close_dialog_with_button(run_win, Button.YES, btn_index=0)

    time.sleep(5)

    # check if PLC`s status is run
    # status = get_plc_status()
    # return status == Title.RUN
    return True


def download_to_plc(down_opt: int = PLC_DOWNLOAD) -> bool:
    """
    download all to connected PLC device.
    :param down_opt: download cmd option choose which part to download: ALL, Program block, and so on.
    :return: True if downloaded or False if not.
    """
    success = exec_cmd(down_opt)
    if not success:
        return success

    # click `Download` button, choose 'Close dialog on success' option
    down_win = wait_window_exists(Title.DOWNLOAD)
    set_check_box(down_win, OPT_CLOSE, index=5)
    close_dialog_with_button(down_win, Button.DOWNLOAD, btn_index=6)
    return True


def upload_from_plc(up_opt: int = PLC_UPLOAD) -> bool:
    """
    upload all from connected PLC device.
    :param up_opt: upload cmd option choose which part to upload: ALL, Program block, and so on.
    :return: True if uploaded or False if not.
    """
    success = exec_cmd(up_opt)
    if not success:
        return success

    # not save changes
    handle_popup_dialog(Title.WIN_SMART, Button.NO, btn_index=1)
    # popup upload window, click `Upload` button, choose 'Close dialog on success' option
    upload_win = wait_window_exists(Title.UPLOAD)
    set_check_box(upload_win, OPT_CLOSE, index=3)
    close_dialog_with_button(upload_win, Button.UPLOAD, btn_index=4)
    return True


def clear_download() -> bool:
    """
    make sure the current project is connected to PLC,
    clear downloaded and temp settings to PLC, restore PLC to empty state.
    :return: True if clear success, False if not.
    """
    success = exec_cmd(CLEAR_ALL)
    if not success:
        return success

    # clear system block window operation
    handle_popup_dialog(Title.WIN_SMART, Button.NO, btn_index=1)

    clear_win = wait_window_exists(Title.CLEAR)

    # choose 'Close dialog on success' option
    set_check_box(clear_win, OPT_CLOSE)

    # click `Clear` button to close the window
    close_dialog_with_button(clear_win, Button.CLEAR, btn_index=0)
    return True


def set_system_block_type(typ: str) -> bool:
    """
    set project system block to match type of PLC device
    :param typ: PLC device type, like 'SR20', 'ST30', etc.
    :return: True or False
    """
    success = exec_cmd(TOOLBAR_SYS_BLOCK)
    if not success:
        return False

    # CPU settings, choose cpu type and latest firmware version
    sb_win = wait_window_exists(Title.SYS_BLOCK)
    grid = sb_win.child_window(class_name=Title.GIRD)
    grid.set_focus()
    send_keys("{RIGHT 1}""{DOWN 1}""{SPACE}")
    key = "{DOWN " + str(cpu_dic[typ.lower()]) + "}"
    send_keys(key)
    send_keys("{ENTER}")
    time.sleep(1)
    handle_popup_dialog(Title.WIN_SMART, Button.OK, btn_index=0)
    close_dialog_with_button(sb_win, Button.OK, btn_index=1)

    time.sleep(1)
    return True
