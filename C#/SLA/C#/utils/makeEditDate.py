import setpath, sys

from mod_msc import *
from mod_file import *


def makeEditDate( name, table, output_dir,  validation_group=""):
    cName=name.capitalize()

    st='''
    <asp:TextBox ID="txt${name}" runat="server" Width="130px" MaxLength="12" style="text-align:justify" ${validation_group} />
        <asp:ImageButton ID="ImgBntCalc${name}" runat="server" ImageUrl="~/images/mini-calendar.gif"
         CausesValidation="False" />
        <ajaxToolkit:MaskedEditExtender ID="MaskedEditExtender${name}" runat="server"
            TargetControlID="txt${name}"
            Mask="99/99/9999"
            MessageValidatorTip="true"
            OnFocusCssClass="MaskedEditFocus"
            OnInvalidCssClass="MaskedEditError"
            MaskType="Date"
            DisplayMoney="Left"
            AcceptNegative="Left"
            ErrorTooltipEnabled="True" />
        <ajaxToolkit:MaskedEditValidator ID="MaskedEditValidator${name}" runat="server"
            ControlExtender="MaskedEditExtender${name}"
            ControlToValidate="txt${name}"
            EmptyValueMessage="Date is required"
            InvalidValueMessage="Date is invalid"
            Display="Dynamic"
            TooltipMessage="Input a date"
            EmptyValueBlurredText="*"
            InvalidValueBlurredMessage="*"
            ${validation_group} />
         <ajaxToolkit:CalendarExtender ID="CalExt${name}" runat="server" TargetControlID="txt${name}"
          PopupButtonID="ImgBntCalc${name}" />
    '''

    gs=hash(st)
    gs=`gs`.replace('-','_')
    so = map_raplace(st, locals())
    output_dir+=os.sep+"makeEditDate"
    if not os.path.exists(output_dir):
          os.makedirs(output_dir)
    fname=output_dir+os.sep+"makeEditDate"+ table+"_%s.aspx"%name
    saveToFile(fname,so)
    return so


if __name__ == '__main__':
#  print tables_list
    output_dir=r'c:\temp\short\makeEditDate'
    makeEditDate(name='tabl',table="TNL",output_dir=output_dir, validation_group='')

