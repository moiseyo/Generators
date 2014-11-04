__author__ = 'mgo4943'
import setpath
from mod_file import  *

import re

setpath.addToPath(r'..\..\..\..\..\projects')
setpath.addToPath(r'..\.')
from Gizmo.dbAccess.common import *

class makePython(BaseEditor):
  def __init__(self):
    pass
  def replaceModuleName(self ,le, mn):
    s1=r"\b%s\b"%mn
    s2='%s${module_name}'%mn
    le=re.sub(s1,s2, le)
    return le

  def makeBody(self, fn):
    ht = self.makeTitleStr(fn)
    st='''
  <obout:Column ID="Col${fn}" DataField="${fn}" ReadOnly="false" HeaderText="${ht}" Width="100" runat="server">
                    <TemplateSettings TemplateId="tpl_${fn}" />
    </obout:Column>

    <obout:GridTemplate runat="server" ID="tpl_${fn}">
                    <Template>
                        <asp:TextBox runat="server" ID="txt${fn}" ReadOnly="false" CssClass="excel-textbox" Text='<%# Container.Value %>'
                            onfocus="markAsFocused(this)" onblur="markAsBlured(this)" />
                    </Template>
    </obout:GridTemplate>
'''
    st= self.replaceBody(st,locals())

    return st

  def makeFindControl(self, fn):
    ht =fn.lower()
    st='''
    if ((!findControlObout(E2e_performance_grid_edit,i,"txt${fn}",ref ret)) ||((string.IsNullOrEmpty(ret))))
        {
          error_text = String.Format("Cannot Find '{0}' in Row #{1}", "txt${fn}", i);
          continue;
        }

        new_bean.$ht = ret;

  '''
    st= self.replaceBody(st,locals())

    return st



if __name__ == '__main__':
  mp = makePython()

  ifname ='SITE_ID'

  body = mp.makeBody(ifname)
  body = mp.makeFindControl(ifname)
  print body
