__author__ = 'mgo4943'
from mod_file import *


file_name=r'C:\ProgramData\mgo4943\projects\1AT\SLA\Admin\SLA_GLOSSARY.aspx'

def processEditTags(file_name):
  ls = readFileAsList(file_name)
  show=1
  for l in ls:
      li=l.strip()
      if li.startswith('<EditItemTemplate>'):
         show=0
      if li.startswith('</EditItemTemplate>'):
         show=1
         continue
      if  show:
        print l



processEditTags(file_name)