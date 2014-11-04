import setpath, sys

from mod_msc import *
from mod_file import *


def makeHoverMenu( name, table, output_dir,  validation_group=""):
    cName=name.capitalize()

    st='''
      <asp:LinkButton ID=txt${name}" runat="server" Text="Article" PostBackUrl=""></asp:LinkButton>
        <asp:Panel ID="PanelHove${name}" runat="server" Style="visibility: hidden">
           <a href="http://www.c-sharpcorner.com">Click Here</a>
        </asp:Panel>
        <ajaxToolkit:HoverMenuExtender ID="HoverMenuExtender${name}" runat="server" TargetControlID="txt${name}"
                        PopupControlID="PanelHove${name}" PopupPosition="Top">
        </ajaxToolkit:HoverMenuExtender>
    '''

    gs=hash(st)
    gs=`gs`.replace('-','_')
    so = map_raplace(st, locals())
    output_dir+=os.sep+"makeHoverMenu"
    if not os.path.exists(output_dir):
          os.makedirs(output_dir)
    output_file_name=output_dir+os.sep+"makeHoverMenu"+ table+"_%s.aspx"%name
    saveToFile(output_file_name,so)
    return so


if __name__ == '__main__':
#  print tables_list
    output_dir=r'c:\temp\short\test\makeHoverMenu'
    makeHoverMenu(name='tabl',table="TNL",output_dir=output_dir, validation_group='')

