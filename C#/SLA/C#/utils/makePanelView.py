import setpath, sys

from mod_msc import *
from mod_file import *


def makeAutoComplite( name, table, output_dir ):
    cName=name.capitalize()
    name_l=name.lower()
    table_l=table.lower()
    pnl_name='pnl'+name
    funName='get'+cName
    lbl_name2 ='lbl'+name+'_Data'
    script='~/AutoComplete/AutoCompleteTest.asmx'

    st='''
  <asp:Panel ID="${pnl_name}" runat="server">
        <table  class="table_credit">
         <tr>
            <td>
              <asp:Label ID="lbl${name}" meta:resourcekey="${table}_${name}" runat="server" Text="<%$ Resources:SLA, ${table}_${name}  %>"></asp:Label>:
            </td>
            <td>
              <asp:Label ID="$lbl_name2" runat="server" Text=""></asp:Label>
            </td>
          </tr>
        </table>
  </asp:Panel>

  //

  ${lbl_name2}.Text =${table_l}_bean.${name_l};

  ${pnl_name}.Visible= true;
    '''

    gs=hash(st)
    gs=`gs`.replace('-','_')
    so = map_raplace(st, locals())
    output_dir+=os.sep+"makepanel"
    if not os.path.exists(output_dir):
          os.makedirs(output_dir)
    fname=output_dir+os.sep+"makepanel"+ table+"_%s.aspx"%name
    saveToFile(fname,so)
    return so


if __name__ == '__main__':
#  print tables_list
    output_dir=r'c:\temp\short\make_panel'
    print makeAutoComplite(name='MEASURED_PERFORMANCE',table="BREACH",output_dir=output_dir)

