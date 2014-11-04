import setpath, sys

from mod_msc import *
from mod_file import *


def makeValidatorCalloutExtender( name, table, output_dir,  validation_group=""):
    cName=name.capitalize()
    control_name=""
    st='''

                  <asp:RequiredFieldValidator runat="server" ID="RFV_${name}"
                        ControlToValidate="${control_name}"
                        Display="None"
                        ErrorMessage="<b>Required Field Missing</b><br />A Value  is required." />
                    <ajaxToolkit:ValidatorCalloutExtender runat="Server" ID="NReqE_${name}"
                        TargetControlID="RFV_${name}"
                        HighlightCssClass="validatorCalloutHighlight" />

    '''

    gs=hash(st)
    gs=`gs`.replace('-','_')
    control_name=name
    if name.startswith('dd'):
      control_name=name
      name=control_name[2:]
    if name.startswith('txt'):
      control_name=name
      name=control_name[3:]

    so = map_raplace(st, locals())
    output_dir+=os.sep+"makeValidatorCalloutExtender"
    if not os.path.exists(output_dir):
          os.makedirs(output_dir)
    outpu_file_name=output_dir+os.sep+"makeValidatorCalloutExtender"+ table+"_%s.aspx"%name
    saveToFile(outpu_file_name,so)
    return so


if __name__ == '__main__':
#  print tables_list
    output_dir=r'c:\temp\short\test\makeValidatorCalloutExtender'
    print  makeValidatorCalloutExtender(name='DDtabl',table="TNL",output_dir=output_dir, validation_group='')

