# test Profinet

import MicroWinExecInterface as MW
from test_case.task.test_200smart_full_idevice_006 import Test200SmartFullIdevice006

self = Test200SmartFullIdevice006()
self.setup_class()
self.PLC['1'].create_session()

strList = MW.CStringList()

p_IP = strList.AddTail("192.168.2.11")
p_IPDevice = strList.AddTail("192.168.2.12")
p_subnetmask = strList.AddTail("255.255.255.0")
p_errMsg = strList.AddTail("")
# the 'r' mark tells the python compiler this string should be interpreted as unicode string.
p_prjName = strList.AddTail(r"D:\project\smart200\lib\resource\project\test_instruction.smart")
p_stationName = strList.AddTail("xiaonianjuntest")
p_devname1 = strList.AddTail("motor1")
p_EntryPoint = strList.AddTail("MWSMART")
p_CpuType = strList.AddTail("ST30")
p_CpuVer = strList.AddTail("V02.05.00_00.00.07.00")
p_GSDMLPath = strList.AddTail(
    r"C:\Users\Public\Documents\Siemens\STEP 7-MicroWIN SMART\GSDML\GSDML-V2.34-#Siemens-PLC200smart_CPU SR30-20191122-134933.xml")
p_DapModulestr = strList.AddTail(r"DAP1")

# status_code = MW.test_InitEnv(strList.GetAt(p_errMsg))
# if status_code != 0 :
#     print("init test env failed")
#
# status_code = MW.PRJ_LoadInstructionLibs()
# if status_code != 0 :
#     print("load instructions&libraries failed...")

# pMWinProject = MW.create_pWORD(1)
status_code = MW.PRJ_New(r"D:\project\smart200\lib\resource\project\test_instruction.smart","MWSMART",pMWinProject,strList.GetAt(p_CpuType),strList.GetAt(p_CpuVer))
# MW.destroy_pWORD(pMWinProject)
self.PROJECT.project_new('test_instruction.smart')

# MW.PRJ_InitNewMwProject()

moduleIdentNumber = 0x80000301
puint = MW.create_puint(moduleIdentNumber)
sint = MW.get_puintValueS(puint)
deviceNumber = 1

pnWizard = MW.EX_PNWizardData()

# sdbData = MW.SDBData()
# status_code = MW.PRJ_GetSystemBlockData(sdbData)
# sdbData.m_common.m_ethernet.SetStoreInProject(1)
# sdbData.m_common.m_ethernet.SetIP(3232236034) #192.168.2.2
# sdbData.m_common.m_ethernet.SetSubnetMask(4294967040)#255.255.255.0
# sdbData.m_common.m_ethernet.SetDefaultGateway(3232236034)#same as IP address.
# sdbData.m_common.m_ethernet.SetStationName(strList.GetAt(p_stationName))
# MW.PRJ_SetSystemBlockData(sdbData)
#
# status_code = MW.PRJ_SetPLCPDEVProperties(2, True, strList.GetAt(p_IP), strList.GetAt(p_subnetmask), 10,
#                                           strList.GetAt(p_stationName), strList.GetAt(p_CpuType),
#                                           strList.GetAt(p_CpuVer), True)
#
# if status_code != 0:
#     print("error in PRJ_SetPLCPDEVProperties,code:%d" % (status_code))
wizard_pn = self.PROJECT.find('wizard_pn')
wizard_pn.set_network_info(self.role)

status_code = MW.PRJ_AddPNDevice(strList.GetAt(p_GSDMLPath), strList.GetAt(p_DapModulestr), sint, deviceNumber)

if status_code != 0:
    print("error in PRJ_AddPNDevice,code:%d" % (status_code))
#
status_code = MW.PRJ_SetPNDeviceProperties(1, 1, strList.GetAt(p_IPDevice), 2, 3, strList.GetAt(p_devname1), False)

if status_code != 0:
    print("error in PRJ_SetPNDeviceProperties,code:%d" % (status_code))


# system_block = self.PROJECT.find('system_block')
self.PROJECT.project_set_cpu_type()
# self.PROJECT.project_compile()
# system_block.set_communication({'fixed_ip': True, 'role': self.role})


MW.WIZ_PNGetConfiguration(pnWizard)
status_code = MW.WIZ_PNConfigurationValidation(pnWizard, strList.GetAt(p_errMsg))

if status_code != 0:
    print("error in WIZ_PNConfigurationValidation,code:%d" % (status_code))

status_code = MW.WIZ_PNConfigurationComplete()

if status_code != 0:
    print("error in WIZ_PNConfigurationComplete,code:%d" % (status_code))

status_code = MW.PRJ_SaveAs(r"D:\project\smart200\lib\resource\project\test_profinet.smart")
if status_code != 0:
    print("PRJ_SaveAs failed with error code:", status_code)