__author__ = 'mgo4943'
import setpath, re, sys
from mod_file import  *
setpath.addToPath(r'..\..\..\..\..\projects')


sh= re.compile('((public|private|protected)\s*(static)?\s*)?([^\s]+)\s+([^\s\(]*)(\([^\)]*\))\s*$')
fname=r'C:\temp\short\convert\template_cs\template_cs.cs'

def  saveFunToFile( res, fun="cc"):
    output_dir=r'c:\temp\short\functs'
    sg=re.compile('(\$\{.+\}_?)')
    m=sg.search(fun)
    if m:
      fun_name=fun.replace(m.group(1),"")
    else:
      fun_name=fun
    output_dir
    if not os.path.exists(output_dir):
      os.makedirs(output_dir)

    fn = fun_name + ".py"
    fname = output_dir + os.sep + fn
    o='   def %s(self):\n'%fun_name
    o+="    res=[]\n"
    o+='    body="""'
    for l in res:
      o +="    %s \n"% l
    o+='   """'
    o+='''
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################




    '''

    o+='''
      body += listToText(self.%s())
      '''%(fun_name)
    saveToFile(fname , o)

ls=readFileAsList(fname)
res=[]
name=''
old_name=''
for l in ls:
  m = sh.search(l)
  if m:
    name= m.group(5)
    if len(res)>0 and len(old_name)>0:
      saveFunToFile( res,old_name)
      # sys.exit(1)
    res=[]
    old_name=name
  res.append(l)

saveFunToFile( res,old_name)

  # else:
  #
  #     st=l.strip()
  #     if (st =='}'):
  #       pass