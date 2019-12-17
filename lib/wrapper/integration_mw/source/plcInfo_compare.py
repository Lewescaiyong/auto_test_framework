'''
Xiao Nian Jun
2019-09-24
'''
#!/usr/bin/python 
# _*_ coding: UTF-8 _*_  

import MicroWinExecInterface as MW

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
p_IP         = strList.AddTail("172.168.2.8")
p_subnetmask = strList.AddTail("255.255.255.0")
#I will just add an empty object to the container because error message is the output 
#parameter of the c++ interface that I'm going to call.
p_errMsg     = strList.AddTail("") 
#the 'r' mark tells the python compiler this string should be interpreted as unicode string.
p_prjName    = strList.AddTail(r"C:\Users\z003wact\Desktop\test case2-instruction.smart")
p_prjPswd    = strList.AddTail("")
p_EntryPoint = strList.AddTail("MWSMART")
p_stationName= strList.AddTail("xiaonianjun")
p_devType    = strList.AddTail("CPU SR20")


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

status_code = MW.test_CreateSession(strList.GetAt(p_IP),strList.GetAt(p_subnetmask),strList.GetAt(p_errMsg))
if status_code != 0:
    print("connect to PLC failed, error message is:")
    MW.print_CString(strList.GetAt(p_errMsg))
	
plc_info = MW.EX_PLCInformationData()
	
status_code = MW.COM_GetDeviceInformation(plc_info)

if status_code!=0:
    print("call COM_GetDeviceInformation failed.")
else:
    print("call COM_GetDeviceInformation success")

pname = plc_info.GetModuleName(0)

MW.print_CString(pname)

#get CPU error info.
MW.print_CString(plc_info.GetErrorStatus(0))

#case 2: compare my project to plc project.
cmpOpt = MW.COMPARE_DLG_OPTIONS()
cmpRst = MW.COMPARE_RESULTS()

networkInfo = MW.MWNetworkInfo()
networkInfo.SetNetworkType(2)
networkInfo.SetIPAddress(strList.GetAt(p_IP))
networkInfo.SetSubnet(4294967040)#255.255.255.0
networkInfo.SetGateway(0)

device_type = MW.CStringEx("CPU SR20")

cmpOpt.cNetInfo = networkInfo
cmpOpt.strDeviceType = device_type
cmpOpt.ProgramCodeBlock = True
cmpOpt.DataBlock = True
cmpOpt.SystemDataBlock = True
cmpOpt.Recipes = True
cmpOpt.DataLogs = True

status_code = MW.PRJ_ExecuteCompare(cmpOpt,cmpRst,False,True)

if status_code !=0:
    print("call PRJ_ExecuteCompare failed.")
else:
    print("call PRJ_ExecuteCompare success.")

print (cmpRst.cObResults.GetSize())

