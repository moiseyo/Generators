import setpath
setpath.addToPath(r'..\..\..\..\projects')
from Gizmo.dbAccess.tables import  *
from Gizmo.dbAccess.common import *
from mod_file import  *
from package1 import *
from SLA_tables import  *


class Misc(BaseEditor):
  def __init__(self , __tbl):
    super(Misc, self).__init__(__tbl)
    self.b_name= package_name +'.bean'
    self.d_name= package_name +'.dao'
    self.get_by_name=''
  def make(self):
    i=0
    for c in self.fieldsNoPK():
      nm = c.getCname()
      nm_l =nm.lower()
      s='''
      if ( c_${nm} < args.Length)
      {
      breach_bean.${nm_l}=  args[c_${nm}];
      }
      '''
      s=self.replaceBody(s, locals())
      print s,

    pass

  def makec(self):
    i=0

    for c in self.fieldsNoPK():
      nm = c.getCname()
      nm_l =nm.lower()
      s=''' const int c_${nm}=$i;
'''
      s=self.replaceBody(s, locals())
      i+=1
      print s,

    pass

  def makeDeleteRunBody(self):
    out ='''   LinkButton lb = (LinkButton)sender;
      string ar = lb.CommandArgument;
      string[] a = ar.Split(',' );
    '''
    i=0


    for c in self.fieldsPK():
      nm = c.getCname()
      nm_l =nm.lower()
      s='''
      const int c_${nm}=$i;'''
      i+=1
      st=self.replaceBody(s, locals())
      out+=st
    i=0
    for c in self.fieldsPK():
      nm = c.getCname()
      nm_l =nm.lower()
      s='''
      if ( c_${nm} < args.Length)
      {
      bean.${nm_l}=  args[c_${nm}];
      }
      '''
      st=self.replaceBody(s, locals())
      out+=st

    return  out



  def makeCommandLineArgument(self):
    st =''' CommandArgument='<%#'''
    i=0

    for c in self.fieldsPK():
      nm = c.getCname()
      nm_u =nm.upper()
      if i>0:
        st +='+","+'
      st +='Eval("%s")'%nm_u
      i+=1
    st+=" %>'"
    return st





if __name__ == '__main__':
  w_table_name="USER_ACL_XREF"
  tbl = tables_list[w_table_name]
  output_dir += os.sep + tbl.tname
  out = Misc(tbl)
  # out.demo('SLA_MGMT','SLA Management')
  # out.makec();
  # out.make();
  print out.makeCommandLineArgument()
  print out.makeDeleteRunBody()
