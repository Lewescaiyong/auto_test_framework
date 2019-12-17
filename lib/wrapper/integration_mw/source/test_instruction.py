'''
an example to show how to use instructions 
'''
#!/usr/bin/python 
# _*_ coding: UTF-8 _*_  

import MicroWinExecInterface as MW
import time
import decimal
strList = MW.CStringList()

p_IP         = strList.AddTail("172.168.2.133")
p_subnetmask = strList.AddTail("255.255.255.0")
p_errMsg     = strList.AddTail("") 
#the 'r' mark tells the python compiler this string should be interpreted as unicode string.
p_prjName    = strList.AddTail(r"C:\Users\z003wact\Desktop\test_instruction.smart")
p_prjPswd    = strList.AddTail("")
p_EntryPoint = strList.AddTail("MWSMART")
p_CpuType    = strList.AddTail("CPU SR20")
p_CpuVer     = strList.AddTail("V02.04.00_00.00.00.00")


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
#case 2:Open an existing project and add some instructions to it and then save it to another location.	
################################################################################################################
pMWinProject = MW.create_pWORD(1)

status_code = MW.PRJ_New(r"C:\Users\z003wact\Desktop\test_instruction.smart","MWSMART",pMWinProject,strList.GetAt(p_CpuType),strList.GetAt(p_CpuVer))
MW.destroy_pWORD(pMWinProject)

if status_code !=0:
    print("Open project failed, error code:",status_code)
else:
    print("create project success.")

MW.PRJ_InitNewMwProject()
	
empty_MW_ID = MW.MW_ID()	

#status_code = MW.SYM_CreateS7200SymbolTable(empty_MW_ID)	
#if status_code !=0:
#    print("call SYM_CreateS7200SymbolTable failed with error code:",status_code)

#status_code = MW.SYM_CreateIOSymbolTable(empty_MW_ID)	
#if status_code !=0:
#    print("call SYM_CreateIOSymbolTable failed with error code:",status_code)	

#status_code = MW.TAB_Insert(MW.POU_SBR,empty_MW_ID)
#if status_code !=0:
#    print("call TAB_Insert(POU_SBR) failed with error code:",status_code)	
#
#status_code = MW.TAB_Insert(MW.POU_INT,empty_MW_ID)
#if status_code !=0:
#    print("call TAB_Insert(POU_INT) failed with error code:",status_code)	
#	
#status_code = MW.TAB_Insert(MW.POU_MAIN,empty_MW_ID)
#if status_code !=0:
#    print("call TAB_Insert(POU_MAIN) failed with error code:",status_code)	
#	
#status_code = MW.TAB_Insert(MW.SYM_USER,empty_MW_ID)
#if status_code !=0:
#    print("call TAB_Insert(SYM_USER) failed with error code:",status_code)	
#	
#status_code = MW.TAB_Insert(MW.CHT_USER,empty_MW_ID)
#if status_code !=0:
#    print("call TAB_Insert(CHT_USER) failed with error code:",status_code)		
#	
#status_code = MW.TAB_Insert(MW.DB_USER,empty_MW_ID)
#if status_code !=0:
#    print("call TAB_Insert(DB_USER) failed with error code:",status_code)		

	
#add instruction begin.
#STEP-1:create MW_ID for our "MAIN" block.
mw_id_main = MW.MW_ID(MW.POU_MAIN,0,MW.USER_NO_PROTECTION)
rect= MW.GRID_RECTANGLE()

					#########################################################
					#begin to add a "normally open" instruction
					#########################################################
#STEP-2:create prameters we need to add an instruction.
net_id = 0 #network number start from 0.
cell_loc_0_0 = MW.GRID_CELL_LOCATION(0,0)#row:0,col:0;
#refer to SigCompassDefs.h for instruction id definition.
inst_id = MW.NO_CONTACT #"normally open instruction".
inst_sub_id = 0 #-1 means this is a standard instruction id,not subroute POU and not library instruction.
grid_op_loc_0_0 = MW.GRID_OPERAND_LOCATION(0,0,0)#row:0,col:0;
pCanDrop = MW.create_pBOOL(False)

#STEP-3: call GRID_CanDropInstruction to tell if we can drop this instruction to the location specified.
status_code = MW.GRID_CanDropInstruction(mw_id_main,net_id,cell_loc_0_0,inst_id,inst_sub_id,MW.INSERT_MODE,pCanDrop)

#STEP-4: if the specified instruction can be draged/dropped, then drop it to the location specified.
if MW.get_pBOOLValue(pCanDrop) == 1:
    status_code = MW.GRID_SetElementInst(mw_id_main,net_id,grid_op_loc_0_0,inst_id,inst_sub_id,MW.INSERT_MODE,cell_loc_0_0,rect)
	#STEP-5:fill in operands of this instruction.
	#here I only need to set the first operand,grid_op_loc_0_0.
    MW.GRID_SetOperand(mw_id_main,net_id,grid_op_loc_0_0,"I0.4")
					#########################################################
					#end of adding "normally open" instruction.
					#begin to add DEQ_CONTACT instruction.
					#########################################################	
cell_loc_0_1 = MW.GRID_CELL_LOCATION(0,1)#row:0,col:1. this instructio locates after "normally open".
inst_id = MW.DEQ_CONTACT #"Dword equality check" instruction.
inst_sub_id = 0 #-1 means this is a standard instruction id,not subroute POU and not library instruction.
grid_op_loc_0_1 = MW.GRID_OPERAND_LOCATION(0,1,0) #row:0,col:1;

status_code = MW.GRID_CanDropInstruction(mw_id_main,net_id,cell_loc_0_1,inst_id,inst_sub_id,MW.INSERT_MODE,pCanDrop)	

if MW.get_pBOOLValue(pCanDrop) == 1:
    status_code = MW.GRID_SetElementInst(mw_id_main,net_id,grid_op_loc_0_1,inst_id,inst_sub_id,MW.INSERT_MODE,cell_loc_0_1,rect)
    #Set the first parameter.
    MW.GRID_SetOperand(mw_id_main,net_id,grid_op_loc_0_1,"VD200")
    next_op_loc = MW.GRID_OPERAND_LOCATION(0,1,2)
    MW.GRID_SetOperand(mw_id_main,net_id,next_op_loc,"VD204")
					#########################################################
					#end of adding DEQ_CONTACT instruction.
					#begin to add DNE_CONTACT instruction.
					#########################################################	
cell_loc_0_2 = MW.GRID_CELL_LOCATION(0,2) #row:0,col:2. this instruction locates after DEQ_CONTACT.
inst_id = MW.DNE_CONTACT #"Dword equality check" instruction.
inst_sub_id = 0 #-1 means this is a standard instruction id,not subroute POU and not library instruction.
grid_op_loc_0_2 = MW.GRID_OPERAND_LOCATION(0,2,0)#row:0,col:2;

status_code = MW.GRID_CanDropInstruction(mw_id_main,net_id,cell_loc_0_2,inst_id,inst_sub_id,MW.INSERT_MODE,pCanDrop)	

if MW.get_pBOOLValue(pCanDrop) == 1:
    status_code = MW.GRID_SetElementInst(mw_id_main,net_id,grid_op_loc_0_2,inst_id,inst_sub_id,MW.INSERT_MODE,cell_loc_0_2,rect)
    MW.GRID_SetOperand(mw_id_main,net_id,grid_op_loc_0_2,"VD208")
    next_op_loc = MW.GRID_OPERAND_LOCATION(0,2,2)
    MW.GRID_SetOperand(mw_id_main,net_id,next_op_loc,"VD212")
	
					#########################################################
					#end of adding DNE_CONTACT instruction.
					#begin to add "normally close" instruction.
					#########################################################	
cell_loc_0_3 = MW.GRID_CELL_LOCATION(0,3)#row:0,col:3.this instruction locates after DNE_CONTACT.
inst_id = MW.OUT_COIL
inst_sub_id = 0 #-1 means this is a standard instruction id,not subroute POU and not library instruction.
grid_op_loc_0_3 = MW.GRID_OPERAND_LOCATION(0,3,0)#row:0,col:3;

status_code = MW.GRID_CanDropInstruction(mw_id_main,net_id,cell_loc_0_3,inst_id,inst_sub_id,MW.INSERT_MODE,pCanDrop)	

if MW.get_pBOOLValue(pCanDrop) == 1:
    status_code = MW.GRID_SetElementInst(mw_id_main,net_id,grid_op_loc_0_3,inst_id,inst_sub_id,MW.INSERT_MODE,cell_loc_0_3,rect)
    MW.GRID_SetOperand(mw_id_main,net_id,grid_op_loc_0_3,"Q0.3")	

MW.destroy_pBOOL(pCanDrop)

					#########################################################
					#end of adding instruction.
					#########################################################	
#STEP-6:compile POU to check if our instruction can work or not.
pou_compile_err = MW.create_pWORD(0)
size = MW.create_pWORD(0)
status_code = MW.POU_CompilePous(pou_compile_err,size,True)
if status_code !=0:
    print("POU_CompilePous failed with error code:",status_code,",error count:",pou_compile_err)
else:
    print("ALL POU compiled successfully,size is:",MW.get_pWORDValue(size))

MW.destroy_pWORD(pou_compile_err)	
MW.destroy_pWORD(size)


#STEP-7:get POU protection attributes.
display_style = MW.create_pint(0)

status_code = MW.test_GetDisplayProtection(mw_id_main,display_style)
if status_code !=0:
    print("TAB_GetDisplayProtection failed with error code:",status_code)
else:
    print("TAB_GetDisplayProtection successfully.")
MW.destroy_pint(display_style)


status_code = MW.PRJ_SaveAs(r"C:\Users\z003wact\Desktop\test_instruction2.smart");	

if status_code !=0:
    print("PRJ_SaveAs failed with error code:",status_code)
else:
    print("ALL PRJ_SaveAs successfully.")

MW.WIZ_PNConfigurationValidationAutoTest(strList.GetAt(p_errMsg))