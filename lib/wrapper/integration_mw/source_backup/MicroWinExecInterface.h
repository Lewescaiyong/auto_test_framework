//define some requisites to run micro/WIN.
#define _AFXDLL
#define WIN32 1
#define __RPCNDR_H_VERSION__
#define EXTERN_C    extern "C"
#include "stdafx.h"
#include "execinterface.h"

#define wchar_t char

WORD* create_pWORD(WORD value );
void print_pWORDValue(WORD* pValue);
WORD get_pWORDValue(WORD* pValue);
void destroy_pWORD(WORD* pValue);

unsigned int* create_puint(unsigned int value);
void print_puintValue(unsigned int* pValue);
int get_puintValueS(unsigned int* pValue);
unsigned int get_puintValueU(unsigned int* pValue);
void destroy_puint(unsigned int* pValue);

int* create_pint(int value);
void print_pintValue(int* pValue);
int get_pintValue(int* pValue);
void destroy_pint(int* pValue);

BOOL* create_pBOOL(BOOL value);
void print_pBOOL(BOOL* pValue);
BOOL get_pBOOLValue(BOOL* pValue);
void destroy_pBOOL(BOOL* pValue);

void print_CString(CString& value);
int compare_CString1(CString& value1,CString& value2);
int compare_CString2(LPTSTR value1,LPTSTR value2);
int compare_CString3(CString& value1,LPTSTR value2);
int compare_CString4(CString& src,CString dst,int nLen);

BYTE get_pByteBYTE(byte* pValue);
WORD get_pByteWord(byte* pValue);
DWORD get_pByteDWORD(byte* pValue);

byte* create_pByte(int value, int nType);
void destroy_pByte(byte* pValue);

int UpdateFW(CString strFilePath);

HWND get_defaultHWND();
