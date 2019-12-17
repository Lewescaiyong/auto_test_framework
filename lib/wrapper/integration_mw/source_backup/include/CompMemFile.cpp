// CompArchive.cpp: implementation of the CCompMemFile class.
//
//////////////////////////////////////////////////////////////////////

//TODO: Deduplicate this file

#include "stdafx.h"
#include "zLib.h"
#include "CompMemFile.h"
#include "AfxOle.h"
#include "atlbase.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif
//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////

CCompMemFile::~CCompMemFile()
{
   delete Detach();
   delete m_pDataBuffer;
   m_pDataBuffer = NULL;
}

int CCompMemFile::ReadFromFile(CFile &rInFile)
{
   // read from CFile into this object
   m_nTotalBytes = (int)rInFile.GetLength(); // get length of file
   if(m_nTotalBytes)
   {
      int nGrowBytes = m_nGrowBytes;
      BYTE *pData = new BYTE[m_nTotalBytes];  // allocate a buffer to read in to
      if(pData)
      {
         // read the data to uncompress later
         rInFile.Read(pData, m_nTotalBytes);
         Attach(pData, m_nTotalBytes, nGrowBytes);
         pData = NULL;
         SetLength(m_nTotalBytes);
      }
      else
         m_nTotalBytes = 0;
   }
   SeekToBegin();
   return m_nTotalBytes;
}
int CCompMemFile::WriteFile(CFile &rOutFile)
{
   int nTotalBytes = (int)GetLength();
   if(nTotalBytes)
   {
      BYTE *pData = Detach();
   
      if(pData)
      {
         // write it to the output
         rOutFile.Write(pData, nTotalBytes);
      
         // release memory
         delete pData;
         m_nTotalBytes = 0;
      }
   }
   return nTotalBytes;
}

void CCompMemFile::ReadAhead(CString &rstrDest, int nLength)
{
   // Read ahead into a CString as storage of a string by the specfied
	// length. Preserve the position of the file
	//
   char *pData = rstrDest.GetBuffer((DWORD) nLength+1);
	long lPosition = (long)GetPosition();
   Read(pData, (DWORD) nLength);
	Seek(lPosition, CFile::begin);
   
	pData[nLength] = 0;   // null terminate
   rstrDest.ReleaseBuffer(nLength);
}

void CCompMemFile::ReadBStrBYTELen(CString &rstrDest)
{
   // read into a CString as storage of WORD length followed by
   // non-NULL terminated string
   BYTE bySize;
   *this >> bySize;
   char *pData = rstrDest.GetBuffer((DWORD) bySize+1);
   Read(pData, (DWORD) bySize);
   pData[bySize] = 0;   // null terminate

   rstrDest.ReleaseBuffer(bySize);
}

void CCompMemFile::ReadBStrWORDLen(CString &rstrDest)
{
   // read into a CString as storage of WORD length followed by
   // non-NULL terminated string
   WORD wSize;
   *this >> wSize;
   char *pData = rstrDest.GetBuffer((DWORD) wSize+1);
   Read(pData, (DWORD) wSize);
   pData[wSize] = 0;   // null terminate
   rstrDest.ReleaseBuffer(wSize);
}

void CCompMemFile::WriteBStrWORDLen(const CString &rstrSrc)
{
   // write CString as WORD len followed by non-NULL terminiated
   // string
   WORD wSize = (WORD) rstrSrc.GetLength();
   *this << wSize;
   Write((LPCTSTR) rstrSrc, (DWORD) wSize);
}
void CCompMemFile::WriteBStrBYTELen(const CString &rstrSrc)
{
   // write CString as WORD len followed by non-NULL terminiated
   // string
   BYTE bySize = (BYTE) rstrSrc.GetLength();
   *this << bySize;
   Write((LPCTSTR) rstrSrc, (DWORD) bySize);
}
BOOL CCompMemFile::AppendFromDataObject(COleDataObject &rDataObject, CLIPFORMAT cfClipFormat, FORMATETC *pFetc)
{
   BYTE *pData = NULL;
   STGMEDIUM stg = {0};
   stg.tymed = TYMED_HGLOBAL;
   if(rDataObject.GetData(cfClipFormat, &stg, pFetc))
   {
      pData = (BYTE *) GlobalLock(stg.hGlobal);
   }
   else
      return FALSE;

   if(!pData) return FALSE;
   
   int nBytes = GlobalSize(stg.hGlobal);

   if(nBytes)
      Write(pData, nBytes);
   
   GlobalUnlock(stg.hGlobal);
   GlobalFree(stg.hGlobal);
   SeekToBegin();
   return TRUE;
}
BOOL CCompMemFile::AppendFromClipboard(CLIPFORMAT cfClipFormat, FORMATETC *pFetc)
{
   COleDataObject cDataObject;

   cDataObject.AttachClipboard();
   
   if(!cDataObject.IsDataAvailable(cfClipFormat, pFetc))
      return FALSE;
   
   return AppendFromDataObject(cDataObject, cfClipFormat, pFetc);
}
BOOL CCompMemFile::IsFormatAvailable(CLIPFORMAT cfClipFormat, FORMATETC *pFetc)
{
   COleDataObject cData;
   return cData.IsDataAvailable(cfClipFormat, pFetc);
}
BOOL CCompMemFile::CopyToDataObject(COleDataSource &rDataSource, CLIPFORMAT cfClipFormat, FORMATETC *pFetc)
{
   BOOL           bRetVal     = TRUE;   
   int            nSize       = (int)GetLength();
   BYTE          *pGlobalData = NULL;
   
   if(nSize)      // if there is data to copy to the clipboard
   {
      // create global memory for the clipbloard
      HGLOBAL hGlobalMem = GlobalAlloc(GMEM_MOVEABLE, nSize);
      pGlobalData = (BYTE *) GlobalLock(hGlobalMem);
      if (pGlobalData == NULL) // if it did not lock 
         bRetVal = FALSE;

      if(bRetVal) // get source data from this CCompMemFile 
      {
         Read(pGlobalData, nSize);
      }
      if(bRetVal)
      {
         // bind the global data to the data source object
         rDataSource.CacheGlobalData(cfClipFormat, hGlobalMem, pFetc);
         GlobalUnlock(hGlobalMem);
      }
   }
   return bRetVal;
   
}
BOOL CCompMemFile::CopyToClipboard(CLIPFORMAT cfClipFormat, FORMATETC *pFetc, COleDataSource *pCallerDataSource)
{
   // if copying multiple CB objects, the caller will supply his COleDataSource. If this is NULL,
   // then we will supply one AND THEN call SetClipboard!!!!


   COleDataSource *pDataSource = pCallerDataSource;
   if(!pDataSource)                       // caller did not supply
      pDataSource = new COleDataSource;

   if(pDataSource)
   {
      if(CopyToDataObject(*pDataSource, cfClipFormat, pFetc))
      {
         if(!pCallerDataSource)              // if we created the object here...
            pDataSource->SetClipboard();     // ...the object is now owned by the clipboard
         return TRUE;
      }
   }
   return FALSE;
}
BOOL CCompMemFile::InsertAt(int nByteOffset, BYTE *pDataToInsert, int nDataLen)
{
   BOOL bRetVal = TRUE;
   int nTotalBytes = (int)GetLength();  // get the total data len
   if(nTotalBytes > nByteOffset)   // if truly an "insert"
   {
      int nGrowBytes = m_nGrowBytes;
      BYTE *pData = Detach();
      
      CCompMemFile cTemp;
      
      if(nByteOffset > nTotalBytes)  // can't insert past the end
         bRetVal = FALSE;
      else
      {
         // if inserting not at the start of the buffer
         // insert data before the insertion point
         if(nByteOffset)                      
         {
            cTemp.Write(pData, nByteOffset);
            nTotalBytes -= nByteOffset;
         }
         // insert the new data
         cTemp.Write(pDataToInsert, nDataLen);
         // if not actually appending data then copy the data after insertion
         if(nTotalBytes)
         {
            cTemp.Write(pData, nTotalBytes);
         }
         // get the length of the new data
         nTotalBytes = (int)cTemp.GetLength();    
         
         delete [] pData; // release previous buffer (leak found by Scott Phillips). 
         // get the temp buffer
         pData = cTemp.Detach();
         // attach it to us
         Attach(pData, nTotalBytes, nGrowBytes);
         pData = NULL;
         SetLength(nTotalBytes);
      }
   }
   else
   {
      if(nByteOffset < nTotalBytes)         // cant insert past end
         bRetVal = FALSE;
      else
         Write(pDataToInsert, nDataLen);
   }
   return TRUE;
}  

int CCompMemFile::Compress(int nCompOffset, CFile *pOpenOutputFile)
{
   BOOL bRetVal = FALSE;
   ASSERT(m_pDataBuffer == NULL);

   m_nCompOffset = nCompOffset;
   int nGrowBytes    = m_nGrowBytes;
   bRetVal           = CompressBuffer();   // compress the buffer of this memfile
   
   if(bRetVal)
   {
      Attach(m_pDataBuffer, m_nTotalBytes, nGrowBytes);
      m_pDataBuffer = NULL;
      SetLength(m_nTotalBytes);

      if(pOpenOutputFile)
      {
         m_nTotalBytes = WriteFile(*pOpenOutputFile);
      }
   }
   else
      m_nTotalBytes = 0;
   
   return m_nTotalBytes;      
}
BOOL CCompMemFile::CompressBuffer()
{
   //
   // Compress the data. Leave m_nCompOffset bytes uncompressed which
   // includes at the end, the uncompressed length stored as a DWORD
   //
   ASSERT(m_pDataBuffer == NULL);

   BYTE *pUncompData = NULL;
   int nCompBytes    = 0;
   int nUncompBytes  = (int)GetLength();   // get length of data
   nUncompBytes      -= m_nCompOffset;  // get the length of "uncompressed" data
   
   // get the uncompressed data (pUncompData)
   pUncompData = Detach();
   if(!pUncompData) return FALSE;

   if(m_nCompOffset > 0 && m_nCompOffset < 4)
      return FALSE;

   // Calculate the compressed buffer size to create
   nCompBytes = nUncompBytes + (nUncompBytes / 100) + 12;
   
   // Create our compressed buffer with (potential) uncompressed header area
   m_pDataBuffer = new BYTE[nCompBytes+m_nCompOffset];

   if(m_nCompOffset)    // if there is an uncompressed header
   {
      // copy the uncompressed header data
      memcpy_s(m_pDataBuffer, m_nCompOffset, pUncompData, m_nCompOffset); 
      // get a pointer to the uncompressed size entry in dest buffer
      DWORD *pdwUncompSize = (DWORD *) &m_pDataBuffer[m_nCompOffset];
      pdwUncompSize--;                          // move back to the uncompressed length entry in header
      *pdwUncompSize = (DWORD) (nUncompBytes);  // write in the original uncompressed data size
   }

   // Compress the buffer into dest past header
   BOOL bResult = TRUE;//(compress(&m_pDataBuffer[m_nCompOffset], (DWORD *) &nCompBytes, &pUncompData[m_nCompOffset], nUncompBytes) == Z_OK);

   // We're done with the original buffer
   delete pUncompData;
   
   // get total bytes
   m_nTotalBytes = m_nCompOffset+nCompBytes;
   return bResult;
}

int CCompMemFile::Uncompress(int nCompOffset, int nUncompBytes, CFile *pOpenInputFile)
{
   BOOL bRetVal = FALSE;
   ASSERT(m_pDataBuffer == FALSE);
   int nOffset = (int)GetPosition();
   // if a valid open file was passed in...
   if(pOpenInputFile)
   {
      m_nCompOffset = nCompOffset;        // save the compression offset
      m_nTotalBytes = ReadFromFile(*pOpenInputFile);
      bRetVal = TRUE;
   }
   else
   {
      // get the size of this Memfile remaining
      m_nTotalBytes = (int)GetLength();
      m_nCompOffset = nOffset;

      // get the buffer to uncompress
      bRetVal = TRUE;
   }
   m_pDataBuffer = Detach();
   
   if(bRetVal)
      bRetVal = UncompressBuffer(nUncompBytes);
   
   Seek(nOffset, CFile::begin);
   if(!bRetVal)
      m_nTotalBytes = 0;

   if(m_pDataBuffer)
      LocalFree(m_pDataBuffer);
   
   m_pDataBuffer = NULL;

   return m_nTotalBytes;      
}
BOOL CCompMemFile::UncompressBuffer(int nUncompBytes)
{
   
   //
   // Uncompress the data. The first m_nCompOffset bytes are not compressed 
   // so exclude them in the uncompression. The DWORD at the end of the 
   // uncompressed data header is the length of the original uncompressed
   // data area and should match decompressed buffer size;
   // The data to uncompress is in m_pDataBuffer and the output will go into 
   // the memfile storage
   //
   int nCompBytes    = m_nTotalBytes - m_nCompOffset;
   int nGrowBytes    = m_nGrowBytes;
   
   if(m_pDataBuffer == NULL)
      return FALSE;

   if((m_nCompOffset > 0) && (m_nCompOffset < 4))
      return FALSE;
   
   // get the uncompressed data (m_pDataBuffer)
   
   if(!nUncompBytes)
   {
      // get the original uncompressed data area size
      int *pdwUncompSize = (int *) &m_pDataBuffer[m_nCompOffset-sizeof(DWORD)];
      nUncompBytes       = *pdwUncompSize;       // copy in the original uncompressed data size
   }

   // Check for bad buffer initialization sizes
   if ((nUncompBytes < 0) || (m_nCompOffset < 0) || ((nUncompBytes + m_nCompOffset) == 0))
   {
	   return FALSE;
   }

   // Check for integer overflow
   if ((m_nCompOffset > 0) && (nUncompBytes > (INT_MAX - m_nCompOffset)))
   {
	   return FALSE;
   }

   // Create our uncompress buffer
   BYTE *pDataBuffer = new BYTE[nUncompBytes+m_nCompOffset];
   
   // copy the uncompressed header data (if any)
   if(m_nCompOffset)
      memcpy_s(pDataBuffer, m_nCompOffset, m_pDataBuffer, m_nCompOffset); 

   int nRslt = Z_OK;//uncompress(&pDataBuffer[m_nCompOffset], (DWORD *) &nUncompBytes, &m_pDataBuffer[m_nCompOffset], nCompBytes);
   
   // Uncompress our buffer
   BOOL bResult = (nRslt == Z_OK);

   // We're done with the original buffer
   delete m_pDataBuffer;
   m_pDataBuffer = NULL;
   
   // restore the archive with the new uncompressed data
   // reattach the uncompressed buffer...CMemFile will delete it when closed
   m_nTotalBytes = nUncompBytes + m_nCompOffset;

   Attach(pDataBuffer, m_nTotalBytes, nGrowBytes);
   pDataBuffer = NULL; // CMemfile will delete

   SetLength(m_nTotalBytes);
   return bResult;
}
void CCompMemFile::Dump( CDumpContext& dc )
{
   dc << "\nm_nFileSize = " << m_nFileSize;
   dc << "\nm_nBufferSize = " << m_nBufferSize;
   dc << "\nm_nPosition = " << m_nPosition;
   dc << "\nm_nGrowBytes = " << m_nGrowBytes;

   int nBytes     = (int)GetLength();
   int nByteIndex = 0;
   int nLineSize  = 0;
   int nLineIndex = 0;
   
   BYTE *pData    = new BYTE[nBytes];
   if(pData == NULL) return;

   CString strText, strAscii, strChar;
   
   BYTE *pTmp = NULL;
   void *pTmpMax = NULL;
   int nPosition = (int)GetPosition();
   Seek(0, CFile::begin);
   GetBufferPtr(CMemFile::bufferRead, 0, (void **) &pTmp, &pTmpMax);
   if(pTmp)
   {
      memcpy_s(pData, nBytes, pTmp, nBytes);
   }
   Seek(nPosition, CFile::begin);
   
   dc << "\n\t CCompMemFile Object Bytes:" << nBytes << "\n";

   for(nByteIndex; nByteIndex < nBytes; nByteIndex += 16)
   {
      nLineSize = min(16, nBytes-nByteIndex);
      strText.Format("%04X: ", nByteIndex);
      strAscii.Empty();
      
      for(nLineIndex = 0; nLineIndex < 16; nLineIndex++)
      {
         if(nLineIndex < nLineSize)
         {
            int nChar = pData[nByteIndex+nLineIndex];
            strChar.Format("%02X ", (nChar & 0xff));
            strText +=  strChar;
            if(isprint(nChar))
               strChar.Format("%c", nChar);
            else
               strChar = ".";

            strAscii += strChar;

            if(nLineIndex == 7)
            {
               strAscii += " ";
               strText += "  ";
            }
         }
         else
         {
            strText += "   ";
            strAscii += " ";
         }
         
      }
      strText += " ";
      strText += strAscii;
      strText += "\n";
      dc << strText;
   }
   delete [] pData;
   dc << "\n";
}