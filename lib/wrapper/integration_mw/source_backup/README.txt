This is Micro/WIN executive interfaces wrapper for IT&ST, in this wrapper, all of the 700 executive interfaces have been wrapped for python.
This wrapper is implemented by SWIG(Simple Wrapper Interface Generator),for more information about SWIG, please visit http://www.swig.org/Doc4.0/Sections.html#Sections.


-->Why python couldn't call c++ interface(with class as input/output parameters) directly?
Root cause is, python support interfaces that only contains POD(Plain Old Data) data type as parameters, but standard c++ classes are non-POD data type.
For more information about what is POD, please visit:https://stackoverflow.com/questions/146452/what-are-pod-types-in-c.

--->Why use SWIG?
	1.SWIG is the most popular OPEN SOURCE tool used to wrap c++ classes/interfaces, many great companies(such as Google) are using SWIG for testing and prototyping.
	2.Simple,easy to use.
	3.Cross platform.
	4.Support multi-target language.

-->How to use this tool?
	STEP-1: Download& install python on your machine and add python.exe to "path" environment variable.
	STEP-2: Download& install swigwin on your machine and unzip it to a folder you like, then add swig.exe to "path" environment variable.
	STEP-3: Write your own .i files.
	STEP-4: Edit setup.py,add the items you need, for more details, please check the comments in setup.py.
	
	Note: 
	1.If you want to run SWIG on linux based platform, the steps is almost the same,don't need pay too much attention on platforms.
	2.Different python interpreter has different behavior, this framework has been tested under python3.6.8(32 bit), for other versions python, you may need to slightly adjust the .i file and setup script.
	
-->How to generate python extended module?
	STPE-1: Run command below to generate all of the wrapper code needed to build a python extension module.
		D:\Software\swigwin-4.0.1\swig -c++ -python -w362 -w389 -w325 -w312 -w401 -w503 -w509 -ID:\source\z003wact_smart_sw_c\S7JCYP_SMART_SW__SRC\Compass\code\inc -ID:\source\z003wact_smart_sw_c\S7JCYP_SMART_SW__SRC\Components\inc -ID:\source\z003wact_smart_sw_c\S7JCYP_SMART_SW__SRC\Common\inc -ID:\source\z003wact_smart_sw_c\S7JCYP_SMART_SW__SRC\Compass\utils\inc -I".\include" -I"D:\source\z003wact_smart_sw_c\S7JCYP_SMART_SW__SRC\Compass\utils\Interface Classes" MicroWinExecInterface.i
	Note:
		1. -w362 means suppress No.362 warning which indicates "the operator= of this class will be ignored"
		2. -w389 means suppress No.389 warning which indicates "the operator[] of this class will be ignored"
		3. -w325&-w312 means suppress No.325 warning which indicates "Nested struct not currently supported".
		4. -w401 means suppress No.401 warning which indicates "Nothing known about base class of the wrapped class".
		5. -w503 means suppress No.503 warning which indicates "specified operator can't be wrapped".
		6. -w509 means suppress No.509 warning which indicates "overloaded method is effectively ignored".
	STEP-2: Run command below to generate python module based on the wrapper code generated in STEP-1.	
		C:\Users\z003wact\AppData\Local\Programs\Python\Python36-32\python setup.py build_ext --inplace 
	
-->How to run python with calling to these wrapped interfaces?
	STEP-1: Copy copy file "SMART_MODULE_DATA.bin" to python.exe folder,such as "C:\Users\xxx\AppData\Local\Programs\Python\Python37-32".
	STEP-2: Run your python script, please refer to "sample_test.py"(in this folder) for how to use generated module.

-->Remaining problems.
	1. User needs to input the absolute path when execute "swig -c++ -python xxx" command.
	2. Need to put .dll into the same folder as python script folder, extra copy&paste work is needed. 
	3. support for CString and Array.
	4. Why there are so many warnings?

-->Important notes:
	1. No wrapping for MFC CString class because it's way too complicated.But,no CString wrapping doesn't means we can't use CString, actually we can use CString very easily, just check what I do in sample_test.py.
	2. Be aware that certain operators don't map cleanly to Python. For instance, overloaded assignment operators don't map to Python semantics and 
	will be ignored, so there are many Warnings with No.362 and No.389. 


-->Release Note:
2019-09-17 Add support for default parameters in execinterface.
2019-09-17 Add support for retrieve pointer type value.
2019-09-18 Add MWNetworkInfo class wrapper.
2019-09-18 fixed the bugs in download project.
2019-09-21 Add support for simple instructions.
2019-09-21 Add test cases for simple instructions.
2019-09-23 Add support for update firmware by ".upd" file.
2019-09-24 Add Interfaces for PN data maniplulation.
2019-09-27 Add tutorial to demostrate hot to create instructions from a totally new project, see "test_instruction.py".
2019-10-09 Add support for compare. 
2019-10-22 Add support for auto select NIC.
2019-10-22 Add support for force function.
2019-10-24 Add support for SDB data manipulation.
2019-11-04 Add support for CPU information manipulation.
2019-11-05 Add support for read Micro/WIN version.











 

