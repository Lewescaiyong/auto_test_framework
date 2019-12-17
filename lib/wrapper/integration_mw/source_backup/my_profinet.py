#!/usr/bin/env python

import lib.wrapper.integration_mw.source.MicroWinExecInterface as Interface


str_list = Interface.CStringList()
msg = str_list.GetAt(str_list.AddTail(""))
ip_i_device = str_list.GetAt(str_list.AddTail("192.168.2.12"))
ip_controller = str_list.GetAt(str_list.AddTail("192.168.2.11"))
sub_net_mask = str_list.GetAt(str_list.AddTail("255.255.255.0"))

# init test env
Interface.test_InitEnv(msg)
Interface.PRJ_LoadInstructionLibs()

# ***************************  create i-device  ***************************
# create session
Interface.test_CreateSession(ip_i_device, sub_net_mask, msg)
# new project
project_path01 = r'D:\\project\\smart200\\lib\\resource\\project\\i_device.smart'
Interface.PRJ_New(project_path01, 'MWSMART', Interface.create_pWORD(1), msg, msg)
Interface.PRJ_InitNewMwProject()

# set cpu type
sdb_data = Interface.PRJ_GetSystemBlockData(Interface.SDBData())
