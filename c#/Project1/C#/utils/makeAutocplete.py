import setpath, sys

from mod_msc import *
from mod_file import *


def makeAutoComplite( name, table, output_dir ):
    cName=name.capitalize()
    funName='get'+cName
    queryString ='get'+name +'_query'
    script='~/AutoComplete/AutoCompleteTest.asmx'

    st='''
    //---------------------------------------------------------------
      [WebMethod(EnableSession=true)]
      public string[] ${funName}(string prefixText, int count)
      {
        prefixText = AppShared.fixSqlQoters(prefixText.ToUpper());

         string    ${queryString}= "select distinct($name) from  ${table}   where UPPER($name) LIKE  '" + prefixText + "%'  order by $name";
          Object thisLock = new Object();
          lock (this)
          {

            try
            {
              List<string> get${name}_result = new List<string>();

              // Get Database Connection
              oracle_conn = dbcon.getDBConn();

              // Create the OracleCommand object
              OracleCommand cmd = new OracleCommand(${queryString});


              cmd.Connection = oracle_conn;
              cmd.CommandType = CommandType.Text;

              // Execute command, create OracleDataReader object
              OracleDataReader reader = cmd.ExecuteReader();

              int Counter = 0;
              while (reader.Read())
              {
                if ((Counter == count))
                  break;
                get${name}_result.Add(reader.GetFieldAsString("$name"));
                Counter += 1;
              }
              if (Counter == 0)
              {
                get${name}_result.Add("Not Found");
              }
              string[] ResultsArray = new string[get${name}_result.Count];
              ResultsArray = (string[])get${name}_result.ToArray();
              dbcon.closeConnection(ref oracle_conn);
              return ResultsArray;
            }
            catch (Exception ex)
            {
              AppShared.sendEmailAboutApplicationErrors("AutoComplete.${funName} "  + System.Reflection.MethodBase. GetCurrentMethod().Name +
               "\\n $gs  \\n " + "\\n" + ${queryString} + "\\n", ex);
              dbcon.closeConnection(ref oracle_conn);
              throw ex;
            }
          } // lock

        }
    //------------------------------------------------------------------------------



     <ajaxToolkit:AutoCompleteExtender runat="server" ID="autoComplete_$name" TargetControlID="txt$name"
                          ServiceMethod="${funName}" ServicePath="${script}" MinimumPrefixLength="1"
                        CompletionInterval="1000" CompletionSetCount="10" EnableCaching="true">
    </ajaxToolkit:AutoCompleteExtender>

    '''

    gs=hash(st)
    gs=`gs`.replace('-','_')
    so = map_raplace(st, locals())
    output_dir+=os.sep+"Autocomlete"
    if not os.path.exists(output_dir):
          os.makedirs(output_dir)
    fname=output_dir+os.sep+"autocomplete"+ table+"_%s.cs"%name
    saveToFile(fname,so)
    return so


if __name__ == '__main__':
#  print tables_list
    output_dir=r'c:\temp\short\AutoComplete'
    print makeAutoComplite(name='TICKET_NBR',table="TICKET_DETAIL",output_dir=output_dir)

