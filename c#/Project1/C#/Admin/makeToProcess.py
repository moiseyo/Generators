__author__ = 'mgo4943'
import setpath
from mod_file import  *

import re

setpath.addToPath(r'..\..\..\..\..\projects')
setpath.addToPath(r'..\.')
from SLA_tables import  *
from Gizmo.dbAccess.common import *

class makePython(BaseEditor):
  def __init__(self):
    pass
  def replaceModuleName(self ,le, mn):
    s1=r"\b%s\b"%mn
    s2='%s${module_name}'%mn
    le=re.sub(s1,s2, le)
    return le

  def process_file(self, f_name):
    fn =''
    res =[];
    sh = re.compile('\s*(protected\s+)?\w+\s+([\w,_]+)\s*\(.*\)')
    ls =readFileAsList(f_name)
    for l in ls:
      if not l.strip(): continue
      if not fn:
        m= sh.search(l)
        if m:
          fn= m.group(2)
      le=re.sub(r"\bdao\b",'${dao_name}', l)
      le=re.sub(r"\bbean_test_e2e\b",'${bean_name}', le)
      le=re.sub(r"\bE2e_sla_test_bean\b",'${data_been_class}', le)
      le=re.sub(r"\bE2e_sla_test_grid\b",' ${editControl}', le)
      le=re.sub(r"Commitment_detail_grid",' ${editControl}', le)
      le=re.sub(r"\bE2e_sla_test_dao\b",'${dao_class}', le)
      le=re.sub(r"\be2e_sla_test_data\b",'${tname_l}_data', le)
      le=re.sub(r"\bTEST_ID\b",'${pk_name}', le)
      le=re.sub(r"\btest_id\b",'${pk_name_l}', le)
      le=re.sub(r"\bmetric_delay\b",'${pk_name}', le)
      le=re.sub(r"\saveDataToOracle\b",'saveDataToOracle${module_name}', le)
      le=re.sub(r"\bjumpBack\b",'jumpBack${module_name}', le)
      le=re.sub(r"\bSaveToNewBean\b",'SaveToNewBean${module_name}', le)
      le=self.replaceModuleName(le,'claenEmptyEntryes')

      le=le.replace("E2e_sla_test_grid",'${gridControl}')
      res.append(le)

    return fn, res
  def makeBody(self, fname):
    fn, res= mp.process_file(fname)
    fn=fn.replace("E2e_sla_test_grid_",'')
    fn=fn.replace("Commitment_detail_grid_",'')
    body ='''
  def ${fn}( self):
    res=[]
    st="""
'''
    body =self.replaceBody(body,locals())
    body += "\n".join(res)
    st='''
    // end  $fn
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End ${fn}


     body += listToText(self.$fn())

    '''
    st =self.replaceBody(st,locals())
    body +=st
    return  body


fname=r'C:\temp\short\1.txt'


if __name__ == '__main__':
  mp = makePython()

  fname =r'c:\temp\short\2.py'
  ifname =r'c:\temp\short\1.txt'

  body = mp.makeBody(ifname)
  saveToFile(fname, body)
