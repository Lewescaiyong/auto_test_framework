#include "MicroWinExecInterface.h"

void* g_hwnd = NULL;

WORD* create_pWORD(WORD value )
{
	return new WORD(value);
}
void destroy_pWORD(WORD* pValue)
{
	if(pValue)
	{
		delete pValue;
		pValue = nullptr;
	}
}
void print_pWORDValue(WORD* pValue)
{
	printf("%d",*pValue);
}
WORD get_pWORDValue(WORD* pValue)
{
	
	return *pValue;
}

int* create_pint(int value)
{
	return new int(value);
}
void destroy_pint(int* pValue)
{
	if(pValue)
	{
		
		delete pValue;
		pValue = nullptr;
	}
}
void print_pintValue(int* pValue)
{
	printf("%d",*pValue);
}
int get_pintValue(int* pValue)
{
	return *pValue;
}

//
unsigned int* create_puint(unsigned int value)
{
	return new unsigned int(value);
}
void destroy_puint(unsigned int* pValue)
{
	if(pValue)
	{
		
		delete pValue;
		pValue = nullptr;
	}
}
void print_puintValue(unsigned int* pValue)
{
	printf("%u",*pValue);
}
unsigned int get_puintValueU(unsigned int* pValue)
{
	return *pValue;
}
int get_puintValueS(unsigned int* pValue)
{
	return (int)*pValue;
}

//

BOOL* create_pBOOL(BOOL value)
{
	
	return new BOOL(value);
}
void destroy_pBOOL(BOOL* pValue)
{
	if(pValue)
	{
		delete pValue;
		pValue = nullptr;
	}
}
void print_pBOOL(BOOL* pValue)
{
	if(*pValue == 1)
		printf("True");
	else
		printf("False");
}
BOOL get_pBOOLValue(BOOL* pValue)
{
	return *pValue;
}

void print_CString(CString& value)
{
	const char* pValue =  (LPCTSTR)value;
	printf("%s",pValue);
}
int compare_CString1(CString& value1,CString& value2)
{
	return value1.Compare(value2);
}
int compare_CString2(LPTSTR value1,LPTSTR value2)
{
	CString cstring1(value1);
	CString cstring2(value2);
	return cstring1.Compare(value2);
}
int compare_CString3(CString& value1,LPTSTR value2)
{
	return value1.Compare(value2);
}
int compare_CString4(CString& src,CString dst,int nLen)
{
	CString src2,dst2;
	
	src2 = src.Left(nLen);
	dst2 = dst.Left(nLen);
	
	return src2.Compare(dst2);
}
HWND get_defaultHWND()
{
	return (HWND)g_hwnd;
}
int UpdateFW(CString strFilePath)
{
	CFile cSource;
	int errCode = 0;
	if (cSource.Open(strFilePath, CFile::modeRead))
	{
		int nBytes = static_cast<int>(cSource.GetLength());
		byte *pBinary = new byte[nBytes];
		cSource.Read(pBinary, nBytes);

		errCode = COM_UpdateFW(pBinary, nBytes);
				
		delete[] pBinary;	
	}	
	else
	{
		return IDS_HLINK_FILE_ERR;
	}
	
	return errCode;
}

BYTE get_pByteBYTE(byte* pValue)
{
	return *(BYTE*)pValue;
}
WORD get_pByteWord(byte* pValue)
{
	return *(WORD*)pValue;
}
DWORD get_pByteDWORD(byte* pValue)
{
	return *(DWORD*)pValue;
}
byte* create_pByte(int value, int nType)
{
	if(nType == 1) //byte
	{
		byte* pValue = new byte(value);
		return pValue;	
	}
	else if(nType == 2)//WORD
	{
		WORD* pValue = new WORD(value);
		return (byte*)pValue;			
	}	
	else if(nType == 3)//DWORD
	{
		DWORD* pValue = new DWORD(value);
		return (byte*)pValue;			
	}	
}
void destroy_pByte(byte* pValue)
{
	if(pValue)
	{
		delete pValue;
		pValue = nullptr;
	}
}