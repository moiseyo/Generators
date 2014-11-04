__author__ = 'mgo4943'

import setpath

from mod_msc import *
from mod_file import *
import  os
def makePageProperty(type, name,output_dir):
    name=name.strip()
    temp='''
    public $type $name {
        get {
          object  v_${name}= ViewState["$name"];
          if (v_${name} != null)
          {
         return ($type) ViewState["$name"];
         }
          return (default($type));
          }
        set { ViewState["$name"] = value; }
      }

    '''

    '''    public string Format$name(object objPrice)
    {
      if (objPrice.Equals(DBNull.Value))
      {
        return "N/A";
      }
      else
      {
        string cn = "";
        if (!dic${name}.get(Convert.ToString(objPrice), ref cn))
        {
          return "N/A";
        }
        return cn;
      }
    }


    '''


    so = map_raplace(temp, locals())
    output_dir+=os.sep+"properties"
    if not os.path.exists(output_dir):
          os.makedirs(output_dir)
    output_file_name=output_dir+os.sep+"properties"+ name+".aspx"
    saveToFile(output_file_name,so)
    saveToFile(output_file_name,so)
    return replaceTemplate(temp,locals())

if __name__ == '__main__':
    #  print tables_list
      output_dir=r'c:\temp\short\test\properies'
      type='Dictionary<string, QDictionary<string, string>>'
      # type='Dictionary<string, Commitment_detail_bean>'
      # type=' List<E2e_sla_test_bean>'
      # type='string'
      # type='Stack'
      # type='Credit_request_bean'
      # type='bool'
      # type='int'
      name="ProductAccessTypes"

      print makePageProperty(name=name,type=type ,output_dir=output_dir)


