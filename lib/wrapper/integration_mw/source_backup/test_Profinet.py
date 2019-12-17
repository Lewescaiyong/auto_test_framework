#test Profinet.
import MicroWinExecInterface as MW
strList = MW.CStringList()

p_IP         = strList.AddTail("172.168.2.133")
p_IPDevice   = strList.AddTail("172.168.2.134")
p_subnetmask = strList.AddTail("255.255.255.0")
p_errMsg     = strList.AddTail("") 
#the 'r' mark tells the python compiler this string should be interpreted as unicode string.
p_prjName    = strList.AddTail(r"C:\Users\z003wact\Desktop\test_instruction.smart")
p_stationName= strList.AddTail("xiaonianjuntest")
p_devname1   = strList.AddTail("motor1") 
p_EntryPoint = strList.AddTail("MWSMART")
p_CpuType    = strList.AddTail("CPU SR20")
p_CpuVer     = strList.AddTail("V02.04.00_00.00.00.00")
p_GSDMLPath  = strList.AddTail(r"C:\Users\Public\Documents\Siemens\STEP 7-MicroWIN SMART\GSDML\GSDML-V2.34-#Siemens-PLC200smart_CPU SR30-20191122-134933.xml")
p_DapModulestr = strList.AddTail(r"DAP1")


status_code = MW.test_InitEnv(strList.GetAt(p_errMsg))
if status_code != 0 :
    print("init test env failed")

status_code = MW.PRJ_LoadInstructionLibs()
if status_code != 0 :
    print("load instructions&libraries failed...")

pMWinProject = MW.create_pWORD(1)
status_code = MW.PRJ_New(r"C:\Users\z003wact\Desktop\test_instruction.smart","MWSMART",pMWinProject,strList.GetAt(p_CpuType),strList.GetAt(p_CpuVer))
MW.destroy_pWORD(pMWinProject)

if status_code !=0:
    print("Open project failed, error code:",status_code)

MW.PRJ_InitNewMwProject()

moduleIdentNumber = 0x80000301
puint = MW.create_puint(moduleIdentNumber)
sint = MW.get_puintValueS(puint)
deviceNumber = 1

sdbData = MW.SDBData()
pnWizard = MW.EX_PNWizardData()

status_code = MW.PRJ_GetSystemBlockData(sdbData)

sdbData.m_common.m_ethernet.SetStoreInProject(1)
sdbData.m_common.m_ethernet.SetIP(3232236034) #192.168.2.2
sdbData.m_common.m_ethernet.SetSubnetMask(4294967040)#255.255.255.0
sdbData.m_common.m_ethernet.SetDefaultGateway(3232236034)#same as IP address.
sdbData.m_common.m_ethernet.SetStationName(strList.GetAt(p_stationName))

MW.PRJ_SetSystemBlockData(sdbData)

status_code = MW.PRJ_SetPLCPDEVProperties(2,False,strList.GetAt(p_IP),strList.GetAt(p_subnetmask),10,strList.GetAt(p_stationName),strList.GetAt(p_CpuType),strList.GetAt(p_CpuVer),True)

if status_code !=0:
    print("error in PRJ_SetPLCPDEVProperties,code:%d"%(status_code))
	
status_code = MW.PRJ_AddPNDevice(strList.GetAt(p_GSDMLPath),strList.GetAt(p_DapModulestr),sint,deviceNumber)

if status_code !=0:
    print("error in PRJ_AddPNDevice,code:%d"%(status_code))

status_code = MW.PRJ_SetPNDeviceProperties(1,0,strList.GetAt(p_IPDevice),2,3,strList.GetAt(p_devname1),False)

if status_code !=0:
    print("error in PRJ_SetPNDeviceProperties,code:%d"%(status_code))
	
MW.WIZ_PNGetConfiguration(pnWizard)
status_code = MW.WIZ_PNConfigurationValidation(pnWizard,strList.GetAt(p_errMsg))

if status_code !=0:
    print("error in WIZ_PNConfigurationValidation,code:%d"%(status_code))
	
status_code = MW.WIZ_PNConfigurationComplete()

if status_code != 0:
    print("error in WIZ_PNConfigurationComplete,code:%d"%(status_code))	
	
status_code = MW.PRJ_SaveAs(r"C:\Users\z003wact\Desktop\test_profinet.smart");	
if status_code !=0:
    print("PRJ_SaveAs failed with error code:",status_code)	