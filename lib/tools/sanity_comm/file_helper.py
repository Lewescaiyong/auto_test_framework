#!/usr/bin/env python

from lib.tools.sanity_comm.utils import *


def open_file(file: str = None, timeout: int = 10) -> bool:
    """
    use command `0xE101` to open an existed file if param `file` is given,
    or choose randomly a file in specific folder.
    :param file: file name.
    :param timeout: timeout time after which, stop the test.
    :return: True if successfully opened file, or False if something went wrong.
    """
    if not exec_cmd(FILE_OPEN):
        return False

    # handle_popup_dialog(Title.WIN_SMART, Button.NO, btn_index=1)
    time.sleep(0.5)
    # get opened window control
    open_win = wait_window_exists(Title.OPEN)
    addr_str = PROJECT_PATH
    # set_window_addr(open_win, PROJECT_PATH)
    # get default project dir

    if file:
        if not os.path.exists(file):
            raise FileNotFoundError(f'file: {file} not found.')
    else:
        # list all `.smart` file in this dir
        files = list(filter(lambda f: f.endswith('.smart'), os.listdir(addr_str)))
        if not files:
            raise FileNotFoundError(f'no `smart` found in{addr_str}.')
        file = PROJECT_PATH+files[-1]

    # input the last `.smart` file name and `click` Open button to open it
    open_win.Edit.type_keys(file, with_spaces=True)

    time.sleep(1)

    close_dialog_with_button(open_win, Button.OPEN, btn_index=0, timeout=timeout)

    # if save change dialog appears, click `No` button
    handle_popup_dialog(Title.WIN_SMART, Button.NO, btn_index=1)
    return True


def new_file(timeout: int = 10) -> bool:
    """
    use command `0xE100` to create a new project file.
    :param app: pywin32 application object used to get control or window dialog handler.
    :param timeout: timeout time after which, stop the test.
    :return: True if successfully created file, or False if something went wrong.
    """
    if not exec_cmd(FILE_NEW):
        return False

    # if save change dialog appears, click `No` button
    handle_popup_dialog(Title.WIN_SMART, Button.NO, btn_index=1)

    return True


def close_file(save: bool = False, timeout: int = 10) -> bool:
    """
    use command `20470` to close current project file in the editor area.
    :param save: save changes to the file, True is to save, False is not to save.
    :param timeout: timeout time after which, stop the test.
    :return: True if successfully closed file, or False if something went wrong.
    """
    if not exec_cmd(FILE_CLOSE):
        return False

    if save:
        # if save change dialog appears, click `Yes` button
        handle_popup_dialog(Title.WIN_SMART, Button.YES, btn_index=0, timeout=timeout)
    else:
        # if save change dialog appears, click `No` button
        handle_popup_dialog(Title.WIN_SMART, Button.NO, btn_index=1, timeout=timeout)

    return True


def save_as_file(name: str, save_as: bool = True, timeout: int = 10) -> bool:
    """
    to save the current project file as a new file or just save current file.
    :param name: file name to be saved.
    :param save_as: save the project or save as another project.
    :param timeout: timeout time after which, stop the test.
    :return: True if successfully saved file, or False if something went wrong.
    """
    cmd = FILE_SAVE_AS if save_as else FILE_SAVE
    if not save_as:
        return exec_cmd(cmd)

    if not exec_cmd(cmd):
        return False

    save_win = wait_window_exists(Title.SAVE_AS)
    # set_window_addr(save_win, PROJECT_PATH)
    # type new file name and click save button to save file copy
    save_win.Edit.type_keys(name, with_spaces=True)

    time.sleep(1)

    # click Save button
    btn = save_win.child_window(class_name="Button", ctrl_index=0)
    click_btn(btn)

    # if confirm save as dialog appears, click `Yes` button
    handle_popup_dialog(Title.CONFIRM_SAVE_AS, Button.YES, btn_index=0)

    save_win.wait_not('exists', timeout=timeout)
    return os.path.exists(name)


def import_pou(file: str = None, timeout: int = 10) -> bool:
    """
    use command to import POU data from `.awl` file
    :param file: pou file name to be imported.
    :param timeout: timeout time after which, stop the test.
    :return: True if successfully imported POU data, or False if something went wrong.
    """
    if not exec_cmd(IMPORT_POU):
        return False

    # if save change dialog appears, click `No` button
    handle_popup_dialog(Title.WIN_SMART, Button.NO)

    # get opened window control
    import_win = wait_window_exists(Title.IMPORT_POU)
    # get default project dir
    # addr_str = import_win.child_window(title_re='Address').window_text().split(':', 1)[-1].strip()

    if file:
        if not os.path.exists(file):
            raise FileNotFoundError(f'POU file {file} not found.')
    else:
        # list all `.awl` file in this dir, if have one or more, choose the last one to open
        files = list(filter(lambda f: f.endswith('.awl'), os.listdir(SOURCE_PATH)))
        if not files:
            raise FileNotFoundError('no POU file to open.')
        file = files[-1]

    # input the last `.awl` file name and `click` Open button to open it
    import_win.Edit.type_keys(file, with_spaces=True)

    time.sleep(1)

    close_dialog_with_button(import_win, Button.OPEN, btn_index=0, timeout=timeout)

    # if import error dialog appears, raise exception
    res = handle_popup_dialog(Title.WIN_SMART, Button.OK)
    if res:
        raise ImportError(f'POU file {file} is not correct.')

    return True


def export_pou(file: str, timeout: int = 10) -> bool:
    """
    use command to export current project file to POU file as format `.awl`.
    :param file: file name to be saved.
    :param timeout: timeout time after which, stop the test.
    :return: True if successfully exported POU data, or False if something went wrong.
    """
    if not exec_cmd(EXPORT_POU):
        return False

    # get export window control
    export_win = wait_window_exists(Title.EXPORT_POU)

    if not file:
        raise ValueError('not valid str.')

    export_win.Edit.type_keys(file, with_spaces=True)

    time.sleep(1)

    close_dialog_with_button(export_win, Button.SAVE, btn_index=0, timeout=timeout)

    # if confirm cover already existed file dialog appears, click `Yes` button
    handle_popup_dialog(Title.CONFIRM_SAVE_AS, Button.YES)

    return os.path.exists(file)


def add_gsd_file(file: str = None, timeout: int = 10) -> bool:
    """
    add a GSDML file to project.
    Args:
        arg1      type(str)     description
        arg2      type(str)     description
    Example:
        add_gsd_file
    Return:
        result = {}
    Author: wang, xing yu
    IsInterface: False
    ChangeTime: 2019-08-19
    """
    # send `add GSD file` command, and get result
    success = exec_cmd(ADD_GSD)
    if not success:
        return success

    # deal with unexpected error
    # handle_popup_dialog(Title.WIN_SMART, Button.OK, btn_index=0)

    # get import window control, click Browse button
    import_win = wait_window_exists(Title.ADD_GSD)
    browse = import_win.child_window(class_name="Button", ctrl_index=1)
    browse.set_focus()
    time.sleep(0.5)
    browse.click()

    # open file choose window, choose a file to import
    open_win = wait_window_exists(Title.IMPORT_GSD, timeout=timeout)
    files = list(filter(lambda s: s.endswith('.xml'), os.listdir(GSD_PATH)))
    if not files:
        raise FileNotFoundError('no GSD file to open.')

    if not file:
        file = files[-1]
    open_win.Edit.set_focus()
    open_win.Edit.type_keys(GSD_PATH+file, with_spaces=True)

    # add GSD file, click Open button
    close_dialog_with_button(open_win, Button.OPEN, btn_index=0)

    # if added, click OK button
    handle_popup_dialog(Title.WIN_SMART, Button.OK, btn_index=0)

    # click OK button to import
    close_dialog_with_button(import_win, Button.OK, btn_index=0)
    return success


def delete_gsd_file(file: str = None, timeout: int = 10) -> bool:
    """"
    delete GSDML file from added GSDML items.
    Args:
        arg1      type(str)     description
        arg2      type(str)     description
    Example:
        delete_gsd_file
    Return:
        result = {}
    Author: wang, xing yu
    IsInterface: False
    ChangeTime: 2019-08-19
    """
    success = exec_cmd(ADD_GSD)
    if not success:
        return False

    # deal with unexpected error
    # handle_popup_dialog(Title.WIN_SMART, Button.OK)

    # get import window control, click Browse button
    import_win = wait_window_exists(Title.ADD_GSD)
    import_win.set_focus()
    i = 1
    txt = get_grid_text(i, 2)
    while txt:
        send_keys("{SPACE}""{DOWN}")
        i += 1
        txt = get_grid_text(i, 2)

    delete_btn = import_win.child_window(class_name='Button', ctrl_index=2)
    if delete_btn.is_enabled():
        delete_btn.click()
        handle_popup_dialog(Title.WIN_SMART, Button.YES, btn_index=0)
    close_dialog_with_button(import_win, Button.OK, btn_index=0)
    return True
