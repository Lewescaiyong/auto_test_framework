#!/usr/bin/python 
# _*_ coding: UTF-8 _*_  

import MicroWinExecInterface as MW
import time

################################################################################################################
#Notes:
#1.Return value of ALL interfaces defined in execinterface.h is integer, 0 means success, 
#other value means error, please check the definition of the error codes in errdefs.h&CommCompassDefs.h
#2.Please call infrastructural methods for pointers manipulation and printing of CString object.
#3.Every time when we create a new project or open a new project, current connection will be closed,
#that means if you want to connect to PLC again, please do establishment first.
################################################################################################################

#Those codes shows how to create my CString

#Use CString,STEP-1:create a CStringList, this works as a container of CString objects.
strList = MW.CStringList()

#Use CString,STEP-2:Add my string objects to the container,
#if I want to use CString object as an input&output parameter 
#of a C++ interface, then I just add an empty string object to the container.
p_IP         = strList.AddTail("172.168.2.33")
p_subnetmask = strList.AddTail("255.255.255.0")
#I will just add an empty object to the container because error message is the output 
#parameter of the c++ interface that I'm going to call.
p_errMsg     = strList.AddTail("") 
#the 'r' mark tells the python compiler this string should be interpreted as unicode string.
p_prjName    = strList.AddTail(r"C:\Users\z003wact\Desktop\project with password123.smart")
p_prjPswd    = strList.AddTail("")
p_EntryPoint = strList.AddTail("MWSMART")
p_strExt1    = strList.AddTail("error")
p_strExt2    = strList.AddTail("err")


#ALWAYS init env before test.
#Use CString,STEP-3:Call GetAt function to retrieve a specific object. 
status_code = MW.test_InitEnv(strList.GetAt(p_errMsg))

if status_code != 0 :
    print("init test env failed,error message is:")
    #Use CString,STEP-4:Call GetAt function to retrieve a specific object.
    #and call print_CString to print CString object.
    MW.print_CString(strList.GetAt(p_errMsg))

#I will also need to load Micro/WIN's instructions&libraries.
status_code = MW.PRJ_LoadInstructionLibs()

if status_code != 0 :
    print("load instructions&libraries failed...")
	
#OK, Micro/WIN is ready, I can play with it now...

################################################################################################################
#case 1: direct connect to PLC and set it to RUN mode.	
################################################################################################################

status_code = MW.test_CreateSession(strList.GetAt(p_IP),strList.GetAt(p_subnetmask),strList.GetAt(p_errMsg))
if status_code != 0:
    print("connect to PLC failed, error message is:")
	#ALWAYS call print_CString to print CString object.
    MW.print_CString(strList.GetAt(p_errMsg))

status_code = MW.COM_SetOpMode(0)

pOpMode = MW.create_pWORD(0)

MW.COM_GetOpMode(pOpMode)
if status_code !=0:
    print("set CPU to run mode failed.")
else:	
    print("operation mode is:",MW.get_pWORDValue(pOpMode))

MW.destroy_pWORD(pOpMode)

#show how to do a simple CString compare.
src = strList.GetAt(p_strExt1)
dst = strList.GetAt(p_strExt2)

status_code = MW.compare_CString4(src,dst,2)

################################################################################################################
#case 2:Open an existing project and add some instructions to it and then save it to another location.	
################################################################################################################
pMWinProject = MW.create_pWORD(1)
status_code = MW.PRJ_Open(strList.GetAt(p_prjName),strList.GetAt(p_prjPswd),strList.GetAt(p_EntryPoint),pMWinProject)

if status_code !=0:
    print("Open project failed, error code:",status_code)
else:
    print("create project success.")
	
MW.destroy_pWORD(pMWinProject)
					
status_code = MW.PRJ_SaveAs(r"C:\Users\z003wact\Desktop\TestCase2-instruction.smart")
if status_code !=0:
    print("save as project failed, error code:",status_code)

################################################################################################################
#case 3:Download the project to PLC.
#since I've opened a new project, now the connection with the PLC has been closed, so I have to tell 
#Micro/WIN what the remote address(PLC address) is,again.	
################################################################################################################
#indirect establishment.
networkInfo = MW.MWNetworkInfo()
networkInfo.SetNetworkType(2)
networkInfo.SetIPAddress(strList.GetAt(p_IP))
networkInfo.SetSubnet(4294967040)#255.255.255.0
networkInfo.SetGateway(0)

#test_OpenConnection is exactly the same as test_CreateSession, the only difference is 
#they have different input parameters.
status_code = MW.test_OpenConnection(networkInfo,strList.GetAt(p_EntryPoint),0,True)
if status_code !=0:
    print("test_OpenConnection failed, error code:",status_code)
else:
    print("test_OpenConnection success")
	
status_code = MW.PRJ_PreCheckDownload(True)
if status_code !=0:
    print("pre check download failed, error code:",status_code)
else:
    print("pre check download success")

#please ignore the memory leak warning of HWNDHWND, actually, there's no memory leak.
hwnd = MW.get_defaultHWND()	
status_code = MW.PRJ_Download(8,hwnd)
if status_code !=0:
    print("download project failed, error code:",status_code)
else:
    print("download project success.")	

################################################################################################################
#Case 4:manipulation sdb data.
################################################################################################################
sDBStartup = MW.SDBStartup()
sDBStartup.SetCPUMode(MW.eDEVICECOMPASS_POWER_UP_IN_LAST)

sdbCommon = MW.SDBCommon()
sdbCommon.m_startup = sDBStartup

sdbData = MW.SDBData()
sdbData.m_common = sdbCommon
#....more manipulation as you needed.


print("exit sample test ")