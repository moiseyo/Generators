import setpath
setpath.addToPath(r'..\..\..\..\projects')
from Gizmo.dbAccess.tables import  * 
from Gizmo.dbAccess.common import *
from mod_file import  *
from package1 import *
from SLA_tables import  *


class DaoClass(BaseEditor):
  def __init__(self , __tbl):
    super(DaoClass, self).__init__(__tbl)
    self.b_name= package_name +'.bean'
    self.d_name= package_name +'.dao'
    self.get_by_name=''

  def _makeUpdateStatement(self, perf=''):
    sout = ' UPDATE %s  ' % ' " +  getTableName() + "'
    
    sout += ' SET '
    i = 0
    for c in self.fieldsNoPK():
      if i > 0:
        sout += " , " 
      sout += " %s=:%s" % (c.cname, c.cname)
      i += 1
      
    i = 0
    sout += self.makeWhere( self.fieldsPK())
    return sout  
  #################################################
  def makeWhere2(self,ls):
    where = " WHERE "
    i = 0
    for fn in ls:
        fn = fn.cname.lower()
        pr = ''
        if i > 0:
            pr = ' AND '
        where += "  %s%s=:%s " % (pr, fn, fn)
        i += 1
    return  where
  ###################################
  def makeVars(self):
    res = []
    for c in self.collons:
      nm = c.getCname()
      tp = getVarType(c)
      s = "public    %s as %s" % (nm, tp)
      res.append(s)
    return res
  ##############################
  def makePkHeaderVars(self):
     j=0
     st=''
     for c in self.fieldsPK():
        if j > 0:
          st += ' , '
        j += 1
        name = c.getCname()
        l_name = name.lower()
        st += getVarType(c) + ' ' + name + "  "
     return st


  ############################################
  def makeInsertStatement(self, perf=''):
    sout = ' INSERT into   %s  "  \n        + "   ( ' % ' " +  getTableName() + "'
    
    i = 0
    for c in self.fields():
      if i > 0:
        sout += " , " 
      sout += " %s" % (c.cname)
      i += 1
      
    i = 0
    sout += " )\"   \n     + \" VALUES ( "
    for c in self.fields():
      if i > 0:
        sout += " ," 
      sout += " :%s" % (c.cname)
      i += 1
    sout += ")"  
    return sout  
   
 #######################################
  def makeFields(self):
    s = '''
       _names..Clear();
        for (int i = 0 .i < reader.FieldCount - 1; i++)
        {
         _names[i] = reader.GetName(i);
        }
    '''
    return s;
    
          
######################################      
  def makeParam(self, c, vname='been', cname='cmd'):
      name = c.getCname();
      name_l = name.lower()
      # type = getVarType(c).upper()

      if isDecimal(c):
        st = '''       
           $cname.Parameters.Add(":$name", OracleType.Double) .Value = ${vname}.${pref}${name_l};
        '''
        so = self.replaceBody(st, locals())
        return  so
      elif isInteger(c):
        st = '''
           $cname.Parameters.Add(":$name", OracleType.Int32) .Value = ${vname}.${pref}${name_l};
        '''
        so = self.replaceBody(st, locals())
        return  so
      elif (isNumber(c)):
        size = c.getWidth()
        st = '''       
          $cname.Parameters.Add(":${name}", OracleType.Number) .Value = ${vname}.${pref}${name_l};
        '''
        so = self.replaceBody(st, locals())
        return so
      
      elif (isString(c)):
        size = c.getWidth()
        st = '''
          if ( ! string.IsNullOrEmpty(${vname}.${pref}${name_l}))
          {       
             $cname.Parameters.Add(":${name}", OracleType.VarChar, $size) .Value=${vname}.${pref}${name_l};
          }
          else
          {
             $cname.Parameters.Add(":${name}", OracleType.VarChar) .Value = OracleString.Null;
         } 
        '''
        so = self.replaceBody(st, locals())
        return so
      elif (isDate(c)):
        size = c.getWidth()
        st = '''
              if (! (${vname}.${pref}${name_l}== null)) {
              $cname.Parameters.Add(":${name}", OracleType.DateTime) .Value=${vname}.${pref}${name_l};
              }
             else
             {
               $cname.Parameters.Add(":${name}", OracleType.DateTime) .Value= OracleDateTime.Null;
             }   
        '''
        
        so = self.replaceBody(st, locals())
        return so 
      elif (isLong(c)):
        size = c.getWidth()
        st = '''
              if ( string.IsNullOrEmpty(bean.${pref}$name_l) ){
              $cname.Parameters.Add(":$name", OracleType.Clob) .Value=${vname}.${name_l};
              }
             else
             {
               $cname.Parameters.Add(":$name", OracleType.Blob) .Value= OracleDateTime.Null;
          }
        '''
        
        so = self.replaceBody(st, locals())
        return so 
 
      else:
        raise Exception("Unknown type [%s].[%s].[%s]  " % (type, c.cname,c.tname))
        st = '''
        error[ $type]
        '''
        so = self.replaceBody(st, locals())
        print so
        sys.exit(1)
        
#########################################
        
  def _makeParmetersList(self, cols, name=''):
    i = 0;res = []
    for  c in cols:
      res.append(self.makeParam(c, name))
     
    return res
 #######################################      
  def makeWhere(self, ls):
    i = 0
    sout = " WHERE "
    for c in ls:
      if i > 0:
        sout += " and " 
      sout += " %s=:%s" % (c.cname, c.cname)
      i += 1
    return sout  
      
        
  ##########################################################

  # def deleteByPk(self):
  #     if len(tbl.getPkCols()) < 1:
  #         return ''
  #     res = []
  #     out_str = '         '
  #     gs = self.makeGs('deleteByPk')
  #
  #     where = self.makeWhere( tbl.getPkCols())
  #
  #
  #     out = """bool DeleteRecordByPk()
  #
  #             string ewm_lookup_query  = "DELETE   " +  getTableName() + " " +
  #               " $where";
  #              lastError="";
  #              oracle_conn = dbcon.getDBConn();
  #              if (oracle_conn== null)
  #              {
  #                return false;
  #              }
  #             OracleTransaction transaction ;
  #             transaction = oracle_conn.BeginTransaction(IsolationLevel.ReadCommitted);
  #
  #        try
  #        {
  #             // Get Database Connection
  #
  #             // Create the OracleCommand object
  #             OracleCommand cmd  = new OracleCommand(ewm_lookup_query);
  #             cmd.Transaction = transaction ;
  #
  #             cmd.Connection = oracle_conn
  #             cmd.CommandType = CommandType.Text
  #
  #       """
  #     so = self.replaceBody(out, locals())
  #     so = self.replaceBody(so, self.__dict__)
  #     res.append(so)
  #     ls = self._makeParmetersList(tbl.getPkCols())
  #     res.append(listToText(ls))
  #
  #     so = """
  #
  #    cmd.ExecuteNonQuery();
  #   transaction.Commit();
  #    dbcon.closeConnection(ref oracle_conn);
  #      return true;
  #     }  catch (System.Exception ex)  {
  #      lastError=ex.Message;
  #           transaction.Rollback();
  #            dbcon.closeConnection(ref oracle_conn);
  #            AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name & "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  + ex.StackTrace  + ""  +"\\n " +"");
  #             AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
  #
  #       return false;
  #     }
  #    return true;
  #   }
  #
  #    """
  #     res.append(so)
  #     return res
  # ###################################

  
  
  def makeAssingValues(self, all=False):
    global tbl
    i = 0;res = []
    for  c in tbl.__columns__:
      name = c.getCname();
      name_l = name.lower()
      
      type = getVarType(c).upper()
      if (type in ['STRING', 'CHAR']) or all:
        size = c.getWidth()
        name1 = name.lower()
        st = '''                            ${lookup_name}.$name_l = reader.GetFieldAsString("$name");     '''
        so = self.replaceBody(st, locals())
        # so = self.replaceBody(so, self.__dict__)
        res.append(so)
      elif (type in ['DATE', 'DATETIME']) or all:
        size = c.getWidth()
        name1 = name.lower()
        st = '''                           ${lookup_name}.$name_l = reader.GetFieldDateTime("$name");                           '''
        so = self.replaceBody(st, locals())
       # // so = self.replaceBody(so, self.__dict__)
        res.append(so)
   
      elif (type in ['int','INT','NUMBER']):
        st = '''                           ${lookup_name}.$name_l = (int)reader.GetFieldInteger("$name");      '''
        so = self.replaceBody(st, locals())
        # so = self.replaceBody(so, self.__dict__)
        
        res.append(so)
      elif (type in ['LONG']):
        st = '''          
         ${lookup_name}.$name_l = reader.GetFieldInteger("$name");   '''
        so = self.replaceBody(st, locals())
        # so = self.replaceBody(so, self.__dict__)
        
        res.append(so)
      elif (type.lower() in ['DOUBLE',"FLOAT", "SINGLE"]):
        st = '''          
         ${lookup_name}.$name_l = reader.GetFieldAsDouble("$name"):  '''
        so = self.replaceBody(st, locals())
        # so = self.replaceBody(so, self.__dict__)
        
        res.append(so)
     
      else:
        st = '''
        Error: $ty  pe
        '''
        so = self.replaceBody(st, locals())
        # so = self.replaceBody(so, self.__dict__)
        raise Exception("Unknown type [%s].[%s].[%s]  " % (type,c.cname, c.tname))
        res.append(so)
        sys.exit(1)
  
    return res
    
    
    
  ##########################################
  def  makeListView(self):
    
    res = []
    assinglist = listToText(self.makeAssingValues(0))
    gs = self.makeGs('getListView')
    sql_name = "sql_query"
    detail_list=self.data_been_class+"list"
    st = '''
    public  List <${data_been_class}> List()
    {
     return List("");
    }
    public  List <${data_been_class}> List(string where= "")
    {
        List < ${data_been_class}> $detail_list = new List < ${data_been_class}>();
        lastError="";
        try {
  
             
              string $sql_name=  "Select * from    " +  getTableName() + " ";
              
             if (! string.IsNullOrEmpty(where)) {
                $sql_name =  $sql_name  + "   WHERE   "  + where;
            }
            if( ! string.IsNullOrEmpty(sortExpresion)) {
                $sql_name =  $sql_name  + " Order BY "  + sortExpresion;
            }

              AppShared.TraceVar("$sql_name:" + $sql_name);
              //Get Database Connection
              oracle_conn =  dbcon.getDBConn();
              if (oracle_conn== null)
               {
               lastError = "No Oracle Connection:" + dbcon.lastError;
                 return  $detail_list;
               }
  
              //Create the OracleCommand object
              OracleCommand cmd=  new OracleCommand($sql_name);
              cmd.Connection =  oracle_conn;
              cmd.CommandType =  CommandType.Text;
              //Execute command, create OracleDataReader object
              OracleDataReader reader=  cmd.ExecuteReader();
              if (reader.HasRows) {
                  ${get_by_name}
                    while (reader.Read())
                    {
                      $data_been_class  ${lookup_name} = new $data_been_class();
$assinglist  
                      //Add Each Record object to ArrayList
                      $detail_list.Add(${lookup_name});
  
                 }

              //------------------
              }
              reader.Close();
              dbcon.closeConnection(ref oracle_conn);
              return $detail_list;
          }  catch (System.Exception ex)  {
              AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"", ex);
               AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
              lastError= ex.Message ;
              dbcon.closeConnection(ref oracle_conn);
          }
          return $detail_list;
      }
  '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
  
    return res
  #################################################################

  def  make_getCount(self):

    res = []
    assinglist = listToText(self.makeAssingValues(0))
    gs = self.makeGs('getListView')
    sql_name = "count_query"
    detail_list=self.data_been_class+"list"
    st = '''
    public  long getCount(string where= "")
    {
        long  count = -1;
        lastError="";
        try {


              string $sql_name=  "Select count(*) from    " +  getTableName() + " ";

             if (! string.IsNullOrEmpty(where)) {
                $sql_name =  $sql_name  + "   WHERE   "  + where;
            }
              AppShared.TraceVar("$sql_name:" + $sql_name);
              //Get Database Connection
              oracle_conn =  dbcon.getDBConn();
              if (oracle_conn== null)
               {
                lastError = "No Oracle Connection:" + dbcon.lastError;
                return  count;
               }

              //Create the OracleCommand object
              OracleCommand cmd=  new OracleCommand($sql_name);
              cmd.Connection =  oracle_conn;
              cmd.CommandType =  CommandType.Text;
              //Execute command, create OracleDataReader object
              OracleDataReader reader=  cmd.ExecuteReader();
              if (reader.HasRows) {
                    while (reader.Read())
                    {
                     count = reader.GetInt64(1);
                    }

              //------------------
              }
              reader.Close();
              dbcon.closeConnection(ref oracle_conn);
              return count;
          }  catch (System.Exception ex)  {
              AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"", ex);
               AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
              lastError= ex.Message ;
              dbcon.closeConnection(ref oracle_conn);
          }
          return count;
      }
  '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)

    return res
  #################################################################


  def  makeMapView(self):
    
    res = []
    assinglist = listToText(self.makeAssingValues(0))
    gs = self.makeGs('getMapView')
    sql_name = "sql_query"
    detail_list="map_list"
    st = '''
     public   Dictionary< string, ${data_been_class}> Map()
     {
      return Map("");
     }

    public   Dictionary< string, ${data_been_class}> Map( string where = "")
     {
        lastError= "";
          try {
  
           Dictionary<string, ${data_been_class}>  $detail_list= new Dictionary<string, ${data_been_class}> () ;
            string $sql_name=  "Select * from   " +  getTableName() + " ";
              
             if ( !string.IsNullOrEmpty(where)) {
                $sql_name =  $sql_name  + "  WHERE  "  + where;
            }
            if ( !string.IsNullOrEmpty(sortExpresion)) {
                $sql_name =  $sql_name  + "Order BY "  + sortExpresion;
            }

              AppShared.TraceVar("$sql_name:" + $sql_name);
              //Get Database Connection
              oracle_conn =  dbcon.getDBConn();
              if (oracle_conn== null)
               {
               lastError = "No Oracle Connection:" + dbcon.lastError;
                 return null;
               }
  
              //Create the OracleCommand object
              OracleCommand cmd=  new OracleCommand($sql_name);

              cmd.Connection =  oracle_conn;
              cmd.CommandType =  CommandType.Text;
              //Execute command, create OracleDataReader object
              OracleDataReader reader=  cmd.ExecuteReader();
              if (reader.HasRows) {
              ${get_by_name}
                       while (reader.Read()) {
                      $data_been_class  ${lookup_name} = new $data_been_class();
$assinglist  
                      //Add Each Record object to DictionaryList
                      ${detail_list}[${lookup_name}.buildKey()]= ${lookup_name};
  
                 }
              }
              reader.Close();
              dbcon.closeConnection(ref oracle_conn);
              return $detail_list;
          }  catch (System.Exception ex)  {
              AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"", ex);
               AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
              lastError= ex.Message ;
              dbcon.closeConnection(ref oracle_conn);
          }
           return null;
      }
  '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
  
    return res
  #################################################################

  def getPkPars(self):
    res = []
    j = 0
    st=''' public   $data_been_class  getPk(


     '''
    st += self.makePkHeaderVars()
    st += ''') {
      $data_been_class var = new $data_been_class();
    '''

    for c in  tbl.getPkCols():
        j += 1
        name = c.getCname()
        l_name = name.lower()
        st += 'var.%s=%s;\n'%(l_name,l_name)

    st+='''
      if (getPk(ref var)){
         return var;
      }
      return null;
  }

    '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    return res;

  def  makePkView(self):
    
    res = []
    assinglist = listToText(self.makeAssingValues())

    gs = self.makeGs('getPkView')
    
    pls = self._makePkVarList()
    where = " WHERE "
    i = 0
    for fn in tbl.getPkCols():
        fn = fn.cname.lower()
        pr = ''
        if i > 0:
            pr = ' AND '
        where += "  %s%s=:%s " % (pr, fn, fn)
        i += 1
   
    ls = self._makeParmetersList(tbl.getPkCols(), self.lookup_name)
    pars = (listToText(ls))

    tn=self.tname
    st = '''
    public  bool getPk(ref $data_been_class  ${lookup_name} )
    {
         lastError="";
          try {
              string ewm_lookup_query=  "Select * from  "  + getTableName()   + " $where ";
              //Get Database Connection
              oracle_conn =  dbcon.getDBConn();
              if (oracle_conn== null)
               {
               lastError = "No Oracle Connection:" + dbcon.lastError;
                 return false;
               }
              //Create the OracleCommand object
              OracleCommand cmd=  new OracleCommand(ewm_lookup_query);
              cmd.Connection =  oracle_conn;
              cmd.CommandType =  CommandType.Text;
               
  $pars
              
                
              //Execute command, create OracleDataReader object
              OracleDataReader reader=  cmd.ExecuteReader();
              if (!reader.HasRows) {
              // TODO
              }
              ${get_by_name}

             bool ok = false;
            if (reader.Read()){
            $assinglist
                ok=true;

            }
             reader.Close();
             dbcon.closeConnection(ref oracle_conn);
             return ok;
          }  catch (System.Exception ex)  {
                lastError= ex.Message ;
                AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"",ex);
                 AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
                dbcon.closeConnection(ref oracle_conn);
          }
          return false;
      }
      

  '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
  
    return res
########################################################################

  def  makePk(self):

    res = []
    assinglist = listToText(self.makeAssingValues())

    gs = self.makeGs('getPk')

    pls = self._makePkVarList()
    where = self.makeWhere(tbl.getPkCols())
    ln='${lookup_name}'
    ln=self.replaceBody(ln,locals())

    vrs = " "
    vrd=''
    i = 0
    for fn in tbl.getPkCols():
        fn_l = fn.cname.lower()
        pr = ''
        if i > 0:
           pr = ' , '
        vrs += "  %s %s %s " % (pr,getVarType( fn), fn_l)
        i += 1
        vrd += "%s.%s=%s;\n"%( ln,fn_l,fn_l)

    ls = self._makeParmetersList(tbl.getPkCols(), self.lookup_name)
    pars = (listToText(ls))

    tn=self.tname
    st = '''
    public  $data_been_class getPk($vrs  )
    {
        $data_been_class  ${lookup_name} = new $data_been_class();
        $vrd
         lastError="";
          try {
              string ewm_lookup_query=  "Select * from  "  + getTableName()   + " $where ";
              //Get Database Connection
              oracle_conn =  dbcon.getDBConn();
              if (oracle_conn== null)
               {
               lastError = "No Oracle Connection:" + dbcon.lastError;
                 return null;
               }
              //Create the OracleCommand object
              OracleCommand cmd=  new OracleCommand(ewm_lookup_query);
              cmd.Connection =  oracle_conn;
              cmd.CommandType =  CommandType.Text;

  $pars


              //Execute command, create OracleDataReader object
              OracleDataReader reader=  cmd.ExecuteReader();
              if (!reader.HasRows) {
              // TODO
              }
              ${get_by_name}

             bool ok = false;
            if (reader.Read()){
            $assinglist
                ok=true;

            }
             reader.Close();
             dbcon.closeConnection(ref oracle_conn);
             return ${ln};
          }  catch (System.Exception ex)  {
                lastError= ex.Message ;
                AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"",ex);
                 AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
                dbcon.closeConnection(ref oracle_conn);
          }
          return null;
      } // get Pk Vars


  '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)

    return res
########################################################################

  def  makeIsThere(self):

    res = []
    if not len(self.fieldsWhere()):
      return res

    gs = self.makeGs('getIsThere')

    pls = self._makePkVarList()
    where = self.makeWhere(self.fieldsWhere())
    assinglist = listToText(self.makeAssingValues())

    ls = self._makeParmetersList(self.fieldsWhere(), self.lookup_name)
    pars = (listToText(ls))

    tn=self.tname
    st = '''
    public  bool isNamesThere(ref $data_been_class  ${lookup_name} )
    {
         bool ok = false;
         lastError="";
          try {
              string isNamesThere_query=  "Select * from   " + getTableName()   +" $where ";
              //Get Database Connection
              oracle_conn =  dbcon.getDBConn();
              if (oracle_conn== null)
               {
               lastError = "No Oracle Connection:" + dbcon.lastError;
                 return true;
               }
              //Create the OracleCommand object
              OracleCommand cmd=  new OracleCommand(isNamesThere_query);
              cmd.Connection =  oracle_conn;
              cmd.CommandType =  CommandType.Text;

  $pars


              //Execute command, create OracleDataReader object
              OracleDataReader reader=  cmd.ExecuteReader();
              if (reader.HasRows) {
               ok=true;
               reader.Read();
                 $assinglist
              }


             reader.Close();
             dbcon.closeConnection(ref oracle_conn);
             return ok;
          }  catch (System.Exception ex)  {
                lastError= ex.Message ;
                AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"",ex);
                 AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
                dbcon.closeConnection(ref oracle_conn);
          }
          return false;
      }


  '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)

    return res

  


  
  def _makePkVarList(self):
    res = []
    collons = self.fieldsPK()
    i = 0
    so = ''
    for c in collons:
      if i > 0:
        so += ' , '
      name = c.getCname();
      type = getVarType(c).upper()
      
      
      if (type in ['int', 'STRING', 'CHAR', 'DATE', 'DATETIME',"INT","LONG"]):
        size = c.getWidth()
        name1 = name.lower()
        st = ''' $type  $name1         '''
        so += self.replaceBody(st, locals())
        so = self.replaceBody(so, self.__dict__)
      else:
        raise Exception("Unknown type [%s]  " % type)
    return so
######################################################

  def makeDeleteByPk(self, pref='bean'):
    res = []
    where = self.makeWhere( self.getPkCols())
    assinglist = listToText(self.makeAssingValues())
    assinglist2 = listToText(self._makeParmetersList(self.fieldsPK(), pref))
    gs = self.makeGs('makeDeleteByPk')

    st = '''
  
  public  bool deleteByPk($data_been_class bean ) {
    string  add_query=  "DELETE    " +  getTableName() + " $where ";
    lastError= "";
      oracle_conn =  dbcon.getDBConn();
      if (oracle_conn== null)
               {
               lastError = "No Oracle Connection:" + dbcon.lastError;
                 return false;
               }
      OracleTransaction transaction ;
      transaction =  oracle_conn.BeginTransaction(IsolationLevel.ReadCommitted);

    try {
      //Create the OracleCommand object
      OracleCommand  cmd=  new OracleCommand(add_query);
      cmd.Transaction =  transaction  ;
      
       $assinglist2 
      cmd.Connection =  oracle_conn;
      cmd.CommandType =  CommandType.Text;
      //Execute command, create OracleDataReader object
      cmd.ExecuteNonQuery();
    transaction.Commit();
       dbcon.closeConnection(ref oracle_conn);
     return true;
    }  catch (System.Exception ex)  {
      transaction.Rollback();
      lastError= ex.Message ;
       dbcon.closeConnection(ref oracle_conn);
       AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"", ex);
        AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
      return false;
    }


  }
    '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    
    return res


  def makeControlFile(self, pref='bean'):
    res = []
    where = self.makeWhere()
    assinglist = listToText(self.makeAssingValues())
    assinglist2 = listToText(self._makeParmetersList(self.fieldsPK(), pref))
    gs = self.makeGs('makeDeleteByPk')

    st = '''
      '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    
    return res

  def makeTrunkete(self, pref=''):
    res = []
    where = self.makeWhere()
    assinglist = listToText(self.makeAssingValues())
    assinglist2 = listToText(self._makeParmetersList(self.fieldsPK(), pref))
    gs = self.makeGs('makeDeleteByPk')

    st = '''
  
  public  bool truncate() { 
        string  add_query= "DELETE    " +  getTableName() + " ";
        lastError= "";
        oracle_conn =  dbcon.getDBConn();
        if (oracle_conn== null)
               {
               lastError = "No Oracle Connection:" + dbcon.lastError;
                 return false;
               }
        OracleTransaction transaction ;
        transaction =  oracle_conn.BeginTransaction(IsolationLevel.ReadCommitted);

    try {
      //Create the OracleCommand object
      OracleCommand  cmd=  new OracleCommand(add_query);
     
      cmd.Connection =  oracle_conn;
      cmd.CommandType =  CommandType.Text;
      //Execute command, create OracleDataReader object
       cmd.Transaction =  transaction;
      cmd.ExecuteNonQuery();
    transaction.Commit();
       dbcon.closeConnection(ref oracle_conn);
     return true;
    }  catch (System.Exception ex)  {
      transaction.Rollback();
      lastError= ex.Message ;
       dbcon.closeConnection(ref oracle_conn);
       AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"", ex);
        AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
      return false;
    }


  }
    '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    
    return res

  def  Update(self, pref='bean'):
  
    res = []
#    pref = self.prefix_name 
    stlstr = self._makeUpdateStatement()
    assinglist = listToText(self._makeParmetersList(self.fieldsNoPK(), pref))
    assinglist2 = listToText(self._makeParmetersList(self.fieldsPK(), pref))
    gs = self.makeGs('Update')
    st = '''
    
    public  bool Update($data_been_class bean)
    {
      string  update_query= "$stlstr";
      lastError="" ;
      oracle_conn =  dbcon.getDBConn();
      if (oracle_conn== null)
               {
               lastError = "No Oracle Connection:" + dbcon.lastError;
                 return false;
               }
      OracleTransaction transaction;
      transaction =  oracle_conn.BeginTransaction(IsolationLevel.ReadCommitted);
      try {
        
        //Create the OracleCommand object
        OracleCommand  cmd=  new OracleCommand(update_query);
        cmd.Transaction =  transaction  ;
        
   $assinglist
   $assinglist2       
  
       
  
        cmd.Connection =  oracle_conn;
        cmd.CommandType =  CommandType.Text;
        //Execute command, create OracleDataReader object
    int  retCode= cmd.ExecuteNonQuery();
      transaction.Commit();
        dbcon.closeConnection(ref oracle_conn);
     
        return retCode >0;
      }  catch (System.Exception ex)  {
        transaction.Rollback();
        lastError= ex.Message ;
        dbcon.closeConnection(ref oracle_conn);
        AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"", ex);
         AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
        return false;
      }

  
  
    } // Update
    

      '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    
    return res

  def getTableName(self):
    res=[]
    st ='''
     public string getTableName()
     {
      return "$tname_u";
     }
    '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    return res


  def  InsertOrUpdate(self, pref='bean'):
  
    res = []

    st = '''
    
    public  bool InsertOrUpdate($data_been_class bean){

        $data_been_class bean_save = new $data_been_class ();
        bean_save.Copy(bean);
        bool  ok   =  getPk(ref bean_save);
        if (! ok)  {
    '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    if self.tbl.generate_auto_number:
        k_name=self.fieldsPK()[0].cname
        k_name_l=k_name.lower()
        st='''
          string $k_name = Code.tools.NextVal.nextVal("$tname_u");
          bean.$k_name_l=$k_name;
          '''
        so = self.replaceBody(st, locals())
        # so = self.replaceBody(so, self.__dict__)
        res.append(so)

    st='''
          Insert(bean);
          }
        else  {
          Update(bean);
        }
      return true;
    }
      '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    
    return res

  def makeFree(self):
    res = []
#    pref = self.prefix_name 
    gs = self.makeGs('makeFree')
    st = '''
    
    public void Free()  {
        dbcon.close();
   } 
      '''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    
    return res



  def makeInsert(self, pref='bean'):
    res = []
#    pref = self.prefix_name 
    stlstr = self.makeInsertStatement(pref)
    assinglist = listToText(self._makeParmetersList(self.fieldsNoPK(), pref))
    assinglist2 = listToText(self._makeParmetersList(self.fieldsPK(), pref))
    gs = self.makeGs('insert')

    st = '''
  public bool Insert($data_been_class bean )
  {
    OracleTransaction transaction;
     lastError= "" ;
    string  insert_query=   "$stlstr";
    oracle_conn =  dbcon.getDBConn();
    if (oracle_conn== null)
               {
               lastError = "No Oracle Connection:" + dbcon.lastError;
                 return false;
               }
    AppShared.TraceVar(insert_query);
    transaction =  oracle_conn.BeginTransaction(IsolationLevel.ReadCommitted);
    try {
      //Create the OracleCommand object
      OracleCommand  cmd=  new OracleCommand(insert_query);
         $assinglist
         $assinglist2       
      cmd.Transaction =  transaction  ;
      cmd.Connection =  oracle_conn;
      cmd.CommandType =  CommandType.Text;
      int  retCode = cmd.ExecuteNonQuery();
      transaction.Commit();
      dbcon.closeConnection(ref oracle_conn);
      return retCode >0;
    }  catch (System.Exception ex)  {
      transaction.Rollback();
      lastError= ex.Message ;
      AppShared.sendEmailAboutApplicationErrors(System.Reflection.MethodBase. GetCurrentMethod().Name  + "/"  + fname   +"\\n " +" $gs "  +"\\n "  + ex.Message  + ""  +"\\n " +""  +ex.StackTrace +"\\n" + SLACommon._user_id  + ""  +"\\n " +"",ex);
      AppShared.errorlog("$dao_class"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" + ex.StackTrace +"\\n" + SLACommon._user_id);
      dbcon.closeConnection(ref oracle_conn);
      return false;
    }

  }
'''
    so = self.replaceBody(st, locals())
    # so = self.replaceBody(so, self.__dict__)
    res.append(so)
    
    return res

##########################################
  def makeAssignSpace(self):
      res = []
      so = ''' '''
      res.append(so)
      for c in self.collons:
        name = c.getCname()
        l_name = name.lower()
        st = ' bean.EWM_Main_%s =""' % l_name 
        res.append(st)
      return res

  def makeMataDataAccess(self):
    res=[]
    out='''
       private  FixedIntIndexedPropertyInCSharp _names= new FixedIntIndexedPropertyInCSharp();

        public  Dictionary<int, string>  dname()
        {
           return _names.dict;
        }

    '''
    res.append(out)
    self.get_by_name=  self.makeFields()
    return res;

  def makeProperty(self):
      res=[]
      out='''
      #region Props
        private string _APPNAME="" ;
        public  string APP_NAME
        {
          get {

           return _APPNAME;

         `}
          set
          {
            _APPNAME = value;
          }
       }

    #endregion

      '''
      res.append(out)

      return res;





  def makeDataDAO(self):
    
    fn = tbl._tname.lower() + '_dao' + ".cs"
    fname = output_dir + os.sep + fn
#    edit.fname = fn
    body = '''
    using System.Data.OracleClient;
    using System.Collections.Generic;
    using System.IO;
    using System;
    using System.Data;
    using PEPSUtils;
    using PEPSUtils.Generic;
    using OracleSupport;
    using Gizmo;
    using $b_name;
   namespace $d_name {
    public class $dao_class {
          protected  Oracle_Connection dbcon;
          protected OracleConnection oracle_conn=  new OracleConnection();
          protected bool  bThrow= false;
          public string  sortExpresion= "";
          public string  lastError= "";
         
          string  fname= System.Reflection.MethodBase.GetCurrentMethod().DeclaringType.Name;
          public  $dao_class(string constr)
          {
            dbcon= new Oracle_Connection( constr);

         }
    '''
    body = self.replaceBody(body, (locals()))

      
    body += listToText(self.getTableName())
    body += listToText(self.makeInsert())
    body += listToText(self.makePkView())
    # body += listToText(self.getPkPars())
    body += listToText(self.Update())
    # body += listToText(self.makeTrunkete())

    body += listToText(self.makeDeleteByPk())
    body += listToText(self.makeListView())
    body += listToText(self.makePk())
    if self.tbl.isMap:
      body += listToText(self.makeMapView())
    body += listToText(self.InsertOrUpdate())
    body += listToText(self.makeIsThere())
    body += listToText(self.make_getCount())
    # body += listToText(self.make_getCount())
    # body += listToText(self.makeFree())
    
    body += "\n  } // End class"
    body += "\n} // End namespace"

   # print listToText(self.makeControlFile())
    print fname
    saveToFile(fname , body)
 

def makeDaoByName(name):   
  tbl = tables_list[name]
  output_dir += os.sep + tbl.tname
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
  testDupId(tbl)
  out = DaoClass(tbl)
  out.makeDataDAO();
  
if __name__ == '__main__':
#  print tables_list
  tbl = tables_list[w_table_name]
  output_dir += os.sep + tbl.tname

  if not os.path.exists(output_dir):
      os.makedirs(output_dir)

  # output_dir="C:\ProgramData\temp\MakeLOE\SLESopport"
  testDupId(tbl)
  out = DaoClass(tbl)
  out.makeDataDAO();

  
