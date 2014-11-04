__author__ = 'mgo4943'
# -*- coding: utf-8 -*-
import setpath
from mod_file import *
from mod_string import *
fname=r'C:\temp\1AT\greprslt.wgr'

lo=[]

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def funProcess3(dirName ,fileName, absolutePath):
  ls=readFileAsList( absolutePath)

  i=0; k=0
  for l in ls:
    i+=1
    if  l.upper().find(" WHERE ")>0:
      if k==0:
          k=1
          lo.append('\n')
          lo.append(fileName)
      lo.append( strip_non_ascii(l.strip())+ '\t%40s  (%d)'%( fileName,i))

def funFilter3(dirName ,fileName, absolutePath):
  #if (fileName <>'Global.asax.cs'): return 0
  if fileName.upper().endswith('.CS'):

    return 1

dirName=r'C:\ProgramData\mgo4943\projects\1AT\SLA'
processDir3( dirName, funProcess3, 1,funFilter3)
saveListToFile( r"c:\temp\short\1.txt" , lo)

