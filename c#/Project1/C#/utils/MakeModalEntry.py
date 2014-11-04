
import setpath, sys

from mod_msc import *
from mod_file import *



name='newCommitmentDetail'

st='''

<asp:Label ID="lbl_target_${name}" runat="server" />
   <ajaxToolkit:ModalPopupExtender ID="MPE${name}" runat="server" Enabled="True" TargetControlID="lbl_target_${name}"
      PopupControlID="popup_${name}" DropShadow="false" BehaviorID="MPE_${name}"
      BackgroundCssClass="ModalPopupBG" CancelControlID="btnCancelMPE_${name}">
    </ajaxToolkit:ModalPopupExtender>
    <asp:Panel ID="popup_${name}" runat="server" CssClass="modalPopup" BackColor="White"
      Style="display: none;" EnableViewState="False">
      <table style="background-color: #33CCFF" width="100%">
        <tr>
          <td style="color: White">
            <b>${name}</b>
          </td>
          <td>
            <asp:HyperLink ID="btnCancelMPE_${name}" runat="server">
              <asp:ImageButton ID="img_${name}Images_cross_icon_normal_png" runat="server" ImageUrl="~/Images/cross_icon_normal.png"
                AlternateText="_${name}Images_cross_icon_normal_png" Style="width: 16px; height: 14px" />
            </asp:HyperLink>
          </td>
        </tr>
      </table>
      <h4>Confirm</h4>
      <asp:Panel ID="popup_${name}_1" runat="server" HorizontalAlign="Center">
				<asp:Button ID="btn${name}_confirm" runat="server" Text="${name}" OnClick="clik_Ok_${name}" />
				<asp:Button ID="btn${name}_cancel" runat="server" OnClientClick="$find('MPE_${name}').hide();"		Text="Cancel" />
        </asp:Panel>
    </asp:Panel>
    
    
     <div id="id${name}e_div" align="right">
            <asp:LinkButton ID="lnk${name}" runat="server" Text="${name} " OnClientClick="$find('MPE_${name}').show(); return false;"></asp:LinkButton>
     </div>

'############################################################
'

 protected void   clik_Ok_${name}(object sender, EventArgs e)
    {

    Response.Write(" clik_Ok_${name}(");
    //TODO

    return ;
  }


'''

name='FullDeny'
so = map_raplace(st, locals())
print so