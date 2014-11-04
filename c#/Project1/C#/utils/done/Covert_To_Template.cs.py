__author__ = 'mgo4943'
import setpath
from mod_file import *
from mod_string import *
setpath.addToPath('../.')
from  package1 import *

from searchAndReplace import searchAndReplace




def convertCode(ls):
  lu=[]
  for l in ls:
    if not l :
      lu.append(l)
      continue
    for key in rep_word:
      st = searchAndReplace(l,key ,rep_word[key])
      if st :
        l=(st)
    lu.append(l)
  return lu


fname = r'C:\ProgramData\mgo4943\projects\1AT\SLA\demo\Default.aspx.cs'; debug=1
#fname = r'C:\temp\v7p\gizmo\3.pas'; debug=1
ls = readFileAsList(fname)
oo = convertCode(ls)

fun_name="template_cs"
output_dir=r'c:\temp\short\convert'
output_dir += os.sep + fun_name
if not os.path.exists(output_dir):
      os.makedirs(output_dir)
fout = output_dir + os.sep + fun_name + '.cs'
saveToFile(fout , "\n".join(oo))
fout = output_dir + os.sep + fun_name + '.save.cs'
saveToFile(fout , "\n".join(ls))



