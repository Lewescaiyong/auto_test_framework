#!/usr/bin/env python

"""
setup.py file for SWIG C\+\+/Python example
"""

from distutils.core import setup, Extension

MICRO_WIN_CODE_PATH = r'D:\Sources\gongweijia_smart_sw_c\S7JCYP_SMART_SW__SRC'
VS_CODE_PATH        = r'C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include'
MICRO_WIN_LIB_PATH  = r'D:\Sources\gongweijia_smart_sw_c\S7JCYP_SMART_SW__SRC\Compass\code\lib\release'
EXTERNAL_LIB        = r'D:\Sources\gongweijia_smart_sw_c\S7JCYP_SMART_SW__SRC\Components\external\zlib\projects\visualc6\Win32_LIB_Release'


extended_macros = [('_AFXDLL', 'None'),
				   ('WIN32','1'),
				   ('DATA_LOG_MAX_COUNTERS','4'),
				   ('MW_SWIG_WRAPPER','None')
				   ]

execinterface_module = Extension('_MicroWinExecInterface',
    sources       =['MicroWinExecInterface.cpp',
					'MicroWinExecInterface_wrap.cxx',
					'.\include\CompMemFile.cpp',
					MICRO_WIN_CODE_PATH + r'\Compass\code\executive\source\globaldefs.cpp'
				   ],
	define_macros = extended_macros,
	libraries     =['executive',
				    'systemdata',
				    "Interface Classes", 
					'compilers',
					'datamanagers',
					'evtmgr',
					'objectmanagers',
					'regmgr',
					'CmnReg',
					'storeretrieveverify',
					'zlib'],
	include_dirs  =[
					MICRO_WIN_CODE_PATH + r'\Compass\code\inc',
				    MICRO_WIN_CODE_PATH + r'\Components\inc',
				    MICRO_WIN_CODE_PATH + r'\Components\utils\inc',
				    MICRO_WIN_CODE_PATH + r'\Common\inc',
				    MICRO_WIN_CODE_PATH + r'\Compass\code\user',
				    MICRO_WIN_CODE_PATH + r'\Compass\utils\inc',
				    MICRO_WIN_CODE_PATH + r'\Compass\code\executive\inc',
				    MICRO_WIN_CODE_PATH + r'\Compass\utils\Interface Classes',
					MICRO_WIN_CODE_PATH + r'\Components\external\zlib'
					],
	library_dirs  =[MICRO_WIN_LIB_PATH,EXTERNAL_LIB],
	#I don't know why it doesn't work...Finally I give up so we have to copy micro/win's dll
	#to user's foler...it should work...maybe my headache slow my brain down...who knows....
	#runtime_library_dirs =["C:\Program Files (x86)\Siemens\STEP 7-MicroWIN SMART"],
)

setup (
    name         = 'MicroWinExecInterface',
    version      = '0.5.5',
    author       = "Xiao Nian Jun",
	author_email = "nianjun.xiao@siemens.com",  
    description  = """wrapped Micro/WIN interfaces""",
    ext_modules  = [execinterface_module],
    py_modules   = ["MicroWinExecInterface"],
)
