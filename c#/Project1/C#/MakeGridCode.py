__author__ = 'mgo4943'
import setpath, sys

setpath.addToPath(r'..\..\..\..\projects')
from SLA_tables import *
from mod_file import *
from package1 import *
from utils.makeAutocplete import *
from Gizmo.dbAccess.common import *
from utils.makeEditDate import makeEditDate
from utils.makeRequedFeldCallout import *
from utils.makeHoverMenut import *
from utils.makePageProperty import makePageProperty


class MakeGridCode(BaseEditor):
  debug = False

  def __init__(self, __tbl={}):
    #     self.__start_it__=False
    super(MakeGridCode, self).__init__(__tbl)
    self.tbl = __tbl;
    self.collons = __tbl.__columns__
    tname = __tbl.tname.upper()
    self.tname = tname
    self.p_name = package_name
    self.setReplace(data_methods)
    self._data_fields = self._makeDataKeys();
    ## Init settings
    if self.getVarByName("bean_name"):
      self.bean_name=self.getVarByName("bean_name")
    else:
      self.bean_name="bean"
    if self.getVarByName("dao_name"):
      self.dao_name=self.getVarByName("dao_name")
    else:
      self.dao_name="dao"

    if self.getVarByName("module_name"):
      self.bean_name=self.getVarByName("module_name")
    else:
      self.module_name=""




  def __str__(self):
    out = ""
    out += 'tbl=' + `self.tbl` + '\n';
    return out

  def makeGs(self, name):
    gs = hash(self.tname + name + `time.time()`)
    gs = `gs`.replace('-', '_')
    return gs

  ##################
  def _makeDataKeys(self):
    j = 0;
    st = 'DataKeyNames="'
    for c in self.fieldsPK():
      if j > 0: st += ','
      j += 1
      st += c.cname.upper()
    st += '"'
    return st
  ############################################
  def makeWhere(self, ls):
    i = 0
    sout = '"'
    for c in ls:
      if i > 0:
        sout += ' " and '

      sout += """ %s='" + bean.%s+"'" + """ % (c.cname, c.cname.lower())
      i += 1
    sout+'""'
    return sout
  ########################
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
#######################################



  def _makeLookupFunName(self, c):
    pref = 'tx'
    if c.dispType == 'DD':
      pref = 'lst'
    return pref + c.cname
    pass

  def makeInsertStatement(self, perf=''):
    sout = ' INSERT into " +  %s   \n        + "   ( ' % self.tname_u

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
      sout += " :%s" % (c.cname.lower())
      i += 1
    sout += ")"
    return sout

  #######################################
  def lnkCancel_Click(self):
    res = []
    body = """        protected void lnkCancel_Click(object sender, EventArgs e)
        {
          setPanelsVisible();
          note_text = "Cancel";

        }


        #region Bussines_Logic
       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def lnkDelete_Click(self):
    res = []

    body = """        protected void lnkDelete_Click(object sender, EventArgs e)
          {
            if (getPk())
            {
              if (!dao.deleteByPk(${bean_name}))
              {
                error_text = "Cannot delete";
                return;
              }
              else
              {
               note_text="Deleted";
              }
              ${gridControl}.DataBind();
            }
             setPanelsVisible();
            return;
          }

     """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;

  def makeLookupFunctions(self):
    res = []
    for c in self.colPkFirst:
      if c.dispType == "DD":
        fun_name = 'Format' + c.cname
        name = c.cname
        name_l=name.lower()
        out = '''
    public string ${fun_name}(object objVar)
      {
      if ( objVar == null)
      {
       objVar = ${bean_name}.${name_l};
      }
      if ( objVar == null)
      {
       return "";
      }
      if (objVar.Equals(DBNull.Value))
      {
        return "N/A";
      }
      else
      {
        string cn = "";
        if (!dic${name}.get(Convert.ToString(objVar), ref cn))
        {
          return "N/A";
        }
        return cn;
      }
    }'''
        out = self.replaceBody(out, locals());
        res.append(out)
    return res

  #####################################
  def _makeLookUpView(self, c):
    name = c.cname
    if (isDate(c)):
      out = '<%%#FormatDate(Eval("%s"))%%>' % ( name)
    elif c.dispType == 'DD':

      out = '<%%#Format%s(Eval("%s"))%%>' % ( name, name)
    else:
      out = '<%%#(Eval("%s"))%%>' % ( name)
    return out

    ######################################

  def LoadsControls(self):
    res = []
    body = """        private void LoadsControls()
            {

            ListItem lit;

       """
    out = self.replaceBody(body, locals())
    res.append(out)
    for c in self.colPkFirst:
      if c.dispType == 'DD':
        name = c.cname
        body = '''
            lst${name}.Items.Clear();
            lit = new ListItem("All", "%%");
            lst${name}.Items.Add(lit);
            foreach (KeyValuePair<string, string> pair in dic${name})
            {
                lst${name}.Items.Add(new ListItem(pair.Value, pair.Key));
              }
        '''
        out = self.replaceBody(body, locals())
        res.append(out)
    out = "}"
    res.append(out)
    return res;

  ######################################
  ##############
  def ModeChanged(self):
    res = []
    body = """        protected void ${editControl}_ModeChanged(object sender, EventArgs ei)
            {

            }
       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def ModeChanging(self):
    res = []
    body = """
    protected void ${editControl}_ModeChanging(object sender, DetailsViewModeEventArgs e)
      {
        if (e.CancelingEdit)
        {
          setPanelsVisible();
          note_text = "Edit Canceled";
          error_text = "";
          return;
        }
        this.getPk();
        isInsert=false;
        switch (e.NewMode)
        {
          case DetailsViewMode.Edit:
            ${editControl}.ChangeMode(DetailsViewMode.Edit);
            note_text = "Edit";
            setPanelsVisible(true);
            break;

          case DetailsViewMode.ReadOnly:
            ${editControl}.ChangeMode(DetailsViewMode.ReadOnly);
            setPanelsVisible(true);
            break;

          case DetailsViewMode.Insert:
            ${editControl}.ChangeMode(DetailsViewMode.Insert);
            note_text = "Add";
            isInsert=true;
            setPanelsVisible(true);
            return;

          default:
            error_text = ("${page_name} case");
            note_text = "";
            break;
        }

        if (!dao.getPk(ref ${bean_name}))
        {
          return;
        }

        BindData();
        Populate_DropDown_Data( ${bean_name});
        lnkCancel.Visible = false;
      }
     """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def NewRunning(self):
    res = []
    body = """
      protected void NewRunning(object sender, EventArgs e)
        {
          ${bean_name}.Clear();
          note_text = "New Item";
          ${editPanel}.Visible = true;
          ${editControl}.ChangeMode(DetailsViewMode.Insert);
          ${editControl}.DefaultMode = DetailsViewMode.Insert;
          BindData();
          isInsert=true;
          Populate_DropDown_Data(${bean_name});
          setPanelsVisible(true);
        }
       """
    out = self.replaceBody(body, locals())

    res.append(out)
    return res;

  def PageIndexChanged(self):
    res = []
    body = """        protected void ${gridControl}_PageIndexChanged(object sender, EventArgs e)
        {
          ${editControl}.ChangeMode(DetailsViewMode.ReadOnly);
          setPanelsVisible();

        }

       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;

  ######################################
  def PopulateBean(self):
    res = []
    body = """

        private bool PopulateBean()
          {
          // Load data  from Database
           string ora = SLACommon.getMainOracleConnectionString();
     """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    cols = self.colPkFirst
    for c in cols:
      if c.dispType == 'DD':
        name = self.makeDD_D_D_name(c.cname)
        st = '                  ' + name + ' = new  QDictionary<string, string>();'
        res.append(st)

    res.append("  return true; ")
    res.append("}// PopulateBean \n")

    return res;
    ######################################

  def setPanelsVisible(self):
    res = []
    body = """        void setPanelsVisible(bool ok = false)
            {
              ${editPanel}.Visible = ok;
              ${viewPanel}.Visible = !ok;
            }
       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def saveDataToOracle(self):
    res = []
    pk_name= self.fieldsPK()[0].cname
    pk_name_l=pk_name.lower()
    body = """
    bool saveDataToOracle()
                {
                  ${data_been_class} new_bean = new ${data_been_class}();

                  error_text = ControlValidation.validateInServer(${editControl});
                  if (!string.IsNullOrEmpty(error_text))
                  {
                    return false;
                  }
                  if (!SaveToNewBean(${editControl}ref new_bean))
                  {
                    return false;
                  }
                   if (dao.isNamesThere(new_bean))
                    {
                      error_text = string.Format("Record '{0}' has duplicates - Data integrity validation", new_bean.ToString());
                      return false;
                    }
                  if (isInsert)
                  {
                    $data_been_class bean_save = new $data_been_class ();
                    bean_save.Copy(new_bean);
                    bool  ok   =  dao.getPk(ref bean_save);
                    if (ok)
                    {
                        error_text = string.Format("Record '{0}' has duplicates- Primary key", new_bean.ToString());
                        return false;

                    }
                    if (dao.isNamesThere(new_bean))
                    {
                        error_text = string.Format("Record '{0}' has duplicates- Primary key", new_bean.ToString());
                        return false;
                    }


              """
    if self.tbl.generate_auto_number:
                 body +='''   string $pk_name = Code.tools.NextVal.nextVal("$tname_u");
                    new_bean.$pk_name_l=$pk_name;
                 '''
    body +="""
                    dao.Insert(new_bean);
                    if (!string.IsNullOrEmpty(dao.lastError))
                    {
                      error_text = dao.lastError;
                      return false;
                    }

                }
                else
                {
                    dao.Update(new_bean);
                    if (!string.IsNullOrEmpty(dao.lastError))
                    {
                      error_text = dao.lastError;
                      return false;
                    }

                }
                return true;
              }
           """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;

  ######################################


  def RowDeleting(self):
    res = []
    body = """
          protected void ${gridControl}_RowDeleting(object sender, GridViewDeleteEventArgs e)
            {
              ${editControl}.DataBind();
              //setPanelsVisible(true);
              //note_text = "Deleted";

            }

       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;

  ######################################


  def makeInsert(self):
    sout = ' InsertCommand=" INSERT into " +  %s   \n        + "   ( ' % self.tname_u

    i = 0
    for c in self.fields():
      if i > 0:
        sout += " , "
      sout += " %s" % (c.cname)
      i += 1

    i = 0
    sout += " ) VALUES ( "
    for c in self.fields():
      if i > 0:
        sout += " ,"
      sout += " :%s" % (c.cname.lower())
      i += 1
    sout += ')"'
    return sout

  ###############################################
  def clearMessages(self):
    res = []
    body = """        void clearMessages()
        {
          error_text = "";
          note_text = "";
        }//clearMessages


       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def DataBound(self):
    res = []
    body = """
        protected void ${editControl}_DataBound(object sender, EventArgs e)
        {
          if (${editControl}.CurrentMode == DetailsViewMode.Insert)
          {
          }// ${editControl}__DataBound
        }
       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def ItemCommand(self):
    res = []
    body = """
        protected void ${editControl}_ItemCommand(object sender, DetailsViewCommandEventArgs e)
          {
            if (e.CommandName == "Update")
            {
              if (saveDataToOracle())
              {
               ${gridControl}.DataBind();
                setPanelsVisible();
                note_text = "Data Updated";

              }
              else
              {
                return;
              }
            }
            else
            {
              if (e.CommandName == "Cancel")
              {
                setPanelsVisible();
                note_text = "Canceled Updated";
                return;
              }
            }

            if (e.CommandName == "Insert")
            {

            }
          } //${editControl}_ItemCommand

     """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def ItemDeleted(self):
    res = []
    body = """
        protected void ${editControl}_ItemDeleted(object sender, DetailsViewDeletedEventArgs e)
          {
          }

     """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def ItemDeleting(self):
    res = []
    body = """        protected void ${editControl}_ItemDeleting(object sender, DetailsViewDeleteEventArgs e)
          {

          }
     """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def ItemInserted(self):
    res = []
    body = """
        protected void ${editControl}_ItemInserted(object sender, DetailsViewInsertedEventArgs e)
        {
        }

       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def ItemInserting(self):
    res = []
    body = """
        protected void ${editControl}_ItemInserting(object sender, DetailsViewInsertEventArgs e)
          {
            ${editControl}_ItemUpdating(sender, null);
          }
         """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;

  #######################################
  def ItemUpdated(self):
    res = []
    body = """
      protected void ${editControl}_ItemUpdated(object sender, DetailsViewUpdatedEventArgs e)
        {
        }

       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def ItemUpdating(self):
    res = []
    body = """

      protected void ${editControl}_ItemUpdating(object sender, DetailsViewUpdateEventArgs e)
        {
          if (saveDataToOracle())
          {
         ${gridControl}.DataBind();
          setPanelsVisible();
          if (e != null)
          {
            note_text = "Data Updated";
          }
          else
          {
            note_text = "Data Inserted";
          }


          }

        }//${editControl}_ItemUpdating
      """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;

  ######################################

  def makeBindData(self):
    res = []
    body = '''
    private void BindData()
    {

      List<${data_been_class}> ls = new List<${data_been_class}>(1);
      ls.Add(${bean_name});
      ${editControl}.DataSource = ls;
      ${editControl}.DataBind();
    }//BindData
'''
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)

    res.append(out)
    return res;

  def makeDD_D_D_name(self, name):
    return "dic" + name

  def makeDD_Dictionary(self):
    cols = self.colPkFirst
    res = []
    for c in cols:
      if c.dispType == 'DD':
        name = self.makeDD_D_D_name(c.cname)
        st = makePageProperty(name=name, type=' QDictionary<string, string>', output_dir=output_dir)
        res.append(st)
    return res


  def SelectedIndexChanged(self):
    res = []
    body = """        protected void ${gridControl}_SelectedIndexChanged(object sender, EventArgs e)
            {
           // System.Web.UI.WebControls.GridViewSelectEventArgs _e=(System.Web.UI.WebControls.GridViewSelectEventArgs)e;
              clearMessages();
              if (!getPk())
              {
                return;
              }
              if (dao.getPk(ref ${bean_name}))
              {
                //${editControl}.ChangeMode(DetailsViewMode.ReadOnly);
                ${editControl}.ChangeMode(DetailsViewMode.Edit);
                BindData();
                Populate_DropDown_Data();

                setPanelsVisible(true);
                lnkCancel.Visible = true;
                 ${editControl}.Controls.hideLinkOnControlCollection( "New");
              }
            } // void ${gridControl}_SelectedIndexChanged

       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################


  def Sorted(self):
    res = []
    body = """
         protected void  ${gridControl}_Sorted(object sender, EventArgs e)
            {
              ${editControl}.ChangeMode(DetailsViewMode.ReadOnly);
              setPanelsVisible();
            }//${gridControl}_Sorted

       """
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res;
    ######################################

  def  Populate_Control_Data_call(self):
    res = []
    st='''
    void Populate_Control_Data_call( Control contol)
    {
    '''
    res.append(st)
    for c in self.colPkFirst:
      cname = c.cname
      st='''
        Populate_Control_Data( control,"$cname", bean);
      '''
      st=self.replaceBody(st,locals())
      res.append(st)
    st='''
      }//Populate_Control_Data_call

       '''
    return res



  def Populate_Control_Data(self):
    res = []
    st = '''
    void Populate_Control_Data(Control control, string name, $data_been_class  bean)
    {
      clearMessages();
       ListItem  selItem;
      try
      {
    '''
    st=self.replaceBody(st,locals())
    res.append(st)
    pk = self.getPkField()
    for c in self.colPkFirst:
      type = c.getColtype()
      cname = c.cname
      cl = c.width
      cw = cl
      st='''
        if ( name =="$cname")
        {
      '''
      st=self.replaceBody(st,locals())
      res.append(st);
      cname = c.cname
      cname_l = cname.lower()
      if not c.dispType:
        body = '''
          TextBox  txt_${cname}_v   = (TextBox)(control.FindControl("txt${cname}"));
          if ( txt_${cname}_v == null) {
           error_text = "The Control [txt${cname}] does not exist ";
           return ;
          }
           txt_${cname}_v.CausesValidation = txt_${cname}_v.Visible && txt_${cname}_v.Enabled;
          '''
        if isDate(c):
          body += '''
             txt_${cname}_v.Text = bean.${cname_l}.ToShortDateString();
            '''
        else:
          body += '''
          txt_${cname}_v.Text = bean.${cname_l}.ToString();

        '''
        out =self.replaceBody(body, (locals()))
        res.append(out)
        #print out
      elif c.dispType == 'DD':
        ddname = 'dd' + cname
        dic_name = self.makeDD_D_D_name(cname)
        dd_name = 'dd_' + cname
        body = '''
          DropDownList ${dd_name}  = (DropDownList)(control.FindControl("$ddname"));

          if (  (${dd_name} == null) ) {
            error_text="The Control [${ddname}] does not exist";
            return ;
          }

         ${dd_name}.Items.Clear();
         ${dd_name}.CausesValidation = ${dd_name}.Visible && ${dd_name}.Enabled;
       '''
        if c.check_dd_size:
          body +='''if (${dic_name}.Count==1)
        {
           foreach (KeyValuePair<string, string> pair in ${dic_name})
          {
            ${dd_name}.Items.Add(new ListItem( pair.Value,pair.Key));
          }
          ${dd_name}.SelectedIndex=0;
        }
        else
        '''
        body+='''
        {
           ${dd_name}.Items.Add(new ListItem("Select", ""));
          foreach (KeyValuePair<string, string> pair in ${dic_name})
          {
            ${dd_name}.Items.Add(new ListItem( pair.Value,pair.Key));
          }
          selItem = ${dd_name}.Items.FindByValue(bean.${cname_l});
          if ((selItem != null))
          {
           ${dd_name}.SelectedIndex = ${dd_name}.Items.IndexOf(selItem);
          }
        }
        '''
        if c in self.getPkField():
          body += '''
           ${dd_name}.Enabled = isInsert;
        '''

        out = self.replaceBody(body, locals())

        res.append(out)
        pass
      elif  c.dispType == 'CHK':
       body='''
       CheckBox chk${cname}_v = (CheckBox)(control.FindControl("chk{cname}"));
        if (chkACTIVE_FLAG_v != null)
        {
          chk{cname}v.Checked = bean.${cname_l} == "Y";
        }
        else
        {
          error_text = "The Control [chk{cname}] does not exist ";
          return;
        }

       '''
       out = self.replaceBody(body, locals())

       res.append(out)

      else:
        raise Exception('Error no Type[%s] ' % c.dispType)
      st='                }'
      res.append(st)

    gs = self.makeGs(`res`)

    body = '''
        }
        catch (System.Exception ex)  {
          error_text = "Some Exception occurred.. " + ex.Message;
        AppShared.errorlog("Populate_drop down _data  '$className'"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" +  ex.StackTrace);
        }
      }  // Populate_Control_Data

    '''
    out = self.replaceBody(body, (locals()))


    res.append(out)
    return res


  #############################################################
  def Populate_DropDown_Data(self):
    res = []
    st = '''
    void Populate_DropDown_Data(Control control, $data_been_class  bean)
    {
      clearMessages();
       ListItem  selItem;
      try
      {
    '''
    st=self.replaceBody(st,locals())
    res.append(st)
    pk = self.getPkField()
    for c in self.colPkFirst:
      type = c.getColtype()
      cl = c.width
      cw = cl

      cname = c.cname
      cname_l = cname.lower()
      if not c.dispType:
        body = '''
          TextBox  txt_${cname}_v   = (TextBox)(control.FindControl("txt${cname}"));
          if ( txt_${cname}_v == null) {
           error_text = "The Control [txt${cname}] does not exist ";
           return ;
          }
           txt_${cname}_v.CausesValidation = txt_${cname}_v.Visible && txt_${cname}_v.Enabled;
          '''
        if isDate(c):
          body += '''
             txt_${cname}_v.Text = bean.${cname_l}.ToShortDateString();
            '''
        else:
          body += '''
          txt_${cname}_v.Text = bean.${cname_l}.ToString();

        '''
        if  not tbl.generate_auto_number:
          if c in self.getPkField():
            body += '''
              txt_${cname}_v.Enabled = isInsert;
          '''
        out = velocityReplace(body, updateDic(locals()))
        res.append(out)
        #print out
      elif c.dispType == 'DD':
        ddname = 'dd' + cname
        dic_name = self.makeDD_D_D_name(cname)
        dd_name = 'dd_' + cname
        body = '''
          DropDownList ${dd_name}  = (DropDownList)(control.FindControl("$ddname"));

          if (  (${dd_name} == null) ) {
            error_text="The Control [${ddname}] does not exist";
            return ;
          }

         ${dd_name}.Items.Clear();
         ${dd_name}.CausesValidation = ${dd_name}.Visible && ${dd_name}.Enabled;
       '''
        if c.check_dd_size:
          body +'''if (${dic_name}.Count==1)
        {
           foreach (KeyValuePair<string, string> pair in ${dic_name})
          {
            ${dd_name}.Items.Add(new ListItem( pair.Value,pair.Key));
          }
          ${dd_name}.SelectedIndex=1;
        }
        else
        '''
        body+='''
        {
           ${dd_name}.Items.Add(new ListItem("Select", ""));
          foreach (KeyValuePair<string, string> pair in ${dic_name})
          {
            ${dd_name}.Items.Add(new ListItem( pair.Value,pair.Key));
          }
          selItem = ${dd_name}.Items.FindByValue(bean.${cname_l});
          if ((selItem != null))
          {
           ${dd_name}.SelectedIndex = ${dd_name}.Items.IndexOf(selItem);
          }
        }
        '''
        if c in self.getPkField():
          body += '''
           ${dd_name}.Enabled = isInsert;
        '''

        out = self.replaceBody(body, locals())

        res.append(out)
        pass
      elif  c.dispType == 'CHK':
       body='''
       CheckBox chk${cname}_v = (CheckBox)(control.FindControl("chk{cname}"));
        if (chkACTIVE_FLAG_v != null)
        {
          chk{cname}v.Checked = bean.${cname_l} == "Y";
        }
        else
        {
          error_text = "The Control [chk{cname}] does not exist ";
          return;
        }

       '''




      else:
        raise Exception('Error no Type[%s] ' % c.dispType)

    gs = self.makeGs(`res`)

    body = '''
        }
        catch (System.Exception ex)  {
          error_text = "Some Exception occurred.. " + ex.Message;
        AppShared.errorlog("Populate_drop down _data  '$className'"  + System.Reflection.MethodBase. GetCurrentMethod().Name, ex.Message+ "\\n" +  ex.StackTrace);
        }
      } //Populate_DropDown_Data

    '''
    out = replaceTemplate(body, updateDic(locals()))
    out = map_raplace(out, self.__dict__)

    res.append(out)
    return res

  def SaveToNewBean(self):
    dd_list = [];
    res = []
    funName = 'SaveToNewBean'
    body = 'bool $funName(Control control, ref $data_been_class  new_bean  ){'
    out = replaceTemplate(body, updateDic(locals()))
    out = map_raplace(out, self.__dict__)

    res.append(out)
    out = '''
        bool  result  = true;

      '''
    res.append(out)
    for c in self.collons:
      if c.cname in no_input:
        continue
      type = c.getColtype()
      cl = c.width
      cw = cl
      name = c.cname
      name_l = name.lower()
      if c.dispType == 'DD':
        body = '''
        DropDownList ${name}_v = (DropDownList)(control.FindControl("dd${name}"));
        if (${name}_v != null) {
          if(! string.IsNullOrEmpty( ${name}_v.Text)) {
            new_bean.$name_l =${name}_v.Text.Trim();
            }
          else {
           new_bean.$name_l = "";
          }
        }
      '''
      elif c.dispType=='CHK':
        body ='''
        CheckBox chk${name}_v= (CheckBox)(control.FindControl("chk${name}"));
      if (chk${name}_v != null)
      {
        new_bean.${name_l} = chk${name}_v.Checked ? "Y" : "N";
      }

        '''
      elif not c.dispType:
        if isString(c):
          body = '''
          TextBox  ${name}_v  = (TextBox)(control.FindControl("txt${name}"));
          if(!(${name}_v ==null)) {
            new_bean.$name_l= ${name}_v.Text.Trim();
            result=true;
          }

      '''
        elif isDate(c):
          body = '''
              TextBox  ${name}_v  = (TextBox)(control.FindControl("txt${name}"));
              if(!(${name}_v ==null)) {
                DateTime ${name}_dt;
                if (DateTime.TryParse(${name}_v.Text, out ${name}_dt))
                {
                  new_bean.$name_l= ${name}_dt;
                }
              }
          '''
        elif isDecimal(c):
          body = '''
              TextBox  ${name}_v  = (TextBox)(control.FindControl("txt${name}"));
              if(!(${name}_v ==null)) {
                float  ${name)_f;
                if (float.TryParse(${name}_v.Text, out ${name)_f))
                {
                 new_bean.$name_l=${name)_f;
                }
              }

          '''
        elif isNumber(c):
          body = '''
              TextBox  ${name}_v  = (TextBox)(control.FindControl("txt${name}"));
              if(!(${name}_v ==null)) {
                long  ${name}_l;
                if (long.TryParse(${name}_v.Text, out   ${name}_l))
                {
                 new_bean.$name_l =${name}_l;
                }
              }
          '''
        else:
          raise Exception('Error no type[%s] ' % c.getColtype())

          #    print out

      out = replaceTemplate(body, updateDic(locals()))
      out = map_raplace(out, self.__dict__)
      res.append(out)

    body = '''
          new_bean.update_by = SLACommon._user_id;
          new_bean.update_dt = DateTime.Now;
          '''
    res.append(body)
    res.append(' return result;')
    out = "} // SaveToNewBean"
    out = replaceTemplate(out, updateDic(locals()))
    out = map_raplace(out, self.__dict__)
    res.append(out)
    return res

  #############################
  def getPkField(self):
    collons = self.fieldsPK()
    pk = collons
    return pk

  def makeGetPk(self):
    res = []
    body = '''
  bool  getPk(object sender = null)
  {
    GridView _e;
    if (sender != null)
    {
      _e= (GridView)sender;
    }
    else
    {
     _e=$gridControl;
    }
    ${bean_name}.Clear();
    int index = _e.SelectedIndex;
    if (index <0)
    {
     error_text="No selected index";
      return false;
    }
  '''
    body = map_raplace(body, updateDic(locals()))
    body = map_raplace(body, self.__dict__)
    res.append(body)
    pk = self.getPkField()
    for c in pk:
      fld_name = c.cname
      fld_name_l = c.cname.lower()
      body = '''
        string $fld_name = $gridControl.DataKeys[index].Values["$fld_name"].ToString();
        if (string.IsNullOrEmpty($fld_name))
        {
         error_text="No selected value in [$fld_name]";
          return false;
        }
        ${bean_name}.$fld_name_l =$fld_name ;
        '''
      body = map_raplace(body, updateDic(locals()))
      body = map_raplace(body, self.__dict__)
      res.append(body)
    res.append('''
       return true;
      } //getPk
      ''')
    return res;

  def makeProps(self):
    res = []
    body = '''

    public string error_text
    {
      get
      {
        return Master.errors_text;
      }
      set
      {
        Master.errors_text = value;
      }
    }

    public string note_text
    {
      get
      {
        return Master.note_text;
      }
      set
      {
        Master.note_text = value;
      }
    }
   public bool isInsert
    {
      get
      {
        return (bool)ViewState["isInsert"];
      }
      set
      {
        ViewState["isInsert"] = value;
      }
    }
    public string ora
    {
      get
      {
        object v_ora = ViewState["ora"];
        if (v_ora != null)
        {
          return (string)ViewState["ora"];
        }
        return (default(string));
      }
      set
      {
        ViewState["ora"] = value;
      }
'''
    body = map_raplace(body, updateDic(locals()))
    body = map_raplace(body, self.__dict__)
    res.append(body)
    return res;

  def make_Page_Load(self):
    body = '''
      protected void Page_Load(object sender, EventArgs e)
      {
         string ora = SLACommon.getMainOracleConnectionString();
					if (!SLACommon.testOracle())
					{
						${editPanel}.Visible = false;
						${viewPanel}.Visible = false;
						return;
					}

				if (!string.IsNullOrEmpty(ora))
				{
					SqlDataSource1.ConnectionString = ora;
				}

				if (!SLACommon.isLoging())
				{

					ResponseHelper.Redirect("~/login/logout.aspx?message=Session+error");
				}

				if (!string.IsNullOrEmpty(ora))
				{

					SqlDataSource1.ConnectionString = ora;
					dao = new $dao_class(ora);
				}
				else
				{
				 	ResponseHelper.Redirect("~/default.aspx?message=No+Valid+Oracle+connection");

				}
      if (!IsPostBack)
      {
        PopulateBean();
        LoadsControls();
      }
      }// Page_Load
        '''
    body = map_raplace(body, updateDic(locals()))
    body = map_raplace(body, self.__dict__)
    res = []
    res.append(body)
    return res

  def makeSearchCode(self):
    res = []
    body = '''
    protected void btnSearch_Click(object sender, EventArgs e)
    {
     clearMessages();
    } //btnSearch_Click

    protected void btnClear_Click(object sender, EventArgs e)
    {
     clearMessages();
    '''
    res.append(body)
    for c in self.colPkFirst:
      name = c.cname
      if c.lookup:
        if c.dispType == 'DD':
          out = 'lst' + name + '.SelectedIndex = 0;'
        else:
          out = 'tx' + name + '.Text = "";'
        res.append(out)

    out = '''

    } // btnClear_Click

      '''

    res.append(out)
    return res

  def makeEmailGrid(self):
    res = []
    tname = self.tname_u
    out = '''
      protected void btnImage_Click(object sender, ImageClickEventArgs e)
    {
      try
      {
        SmtpMail mailer = new SmtpMail();
        System.Text.StringBuilder sb = new System.Text.StringBuilder();
        System.IO.StringWriter sw = new System.IO.StringWriter(sb);

        HtmlTextWriter hw = default(HtmlTextWriter);
        hw = new HtmlTextWriter(sw);

        $gridControl.RenderControl(hw);
        mailer.sendTo = SLACommon._email_address;
        mailer.bBodyHtml = true;
        mailer.sendFrom = AppShared.mailFrom;
         mailer.subject = string.Format(" Data Snapshot ${tname}  [ [{0}] ,  User [{1}]  Version[{1}]", Session["MAIN_TITLE"], SLACommon.getDisplayNeme(), SLACommon.Version());
        mailer.body = sw.ToString();
        mailer.sendMail();
        note_text = "Email sent to you";
      }
      catch (Exception ex)
      {
      }
    } // btnImage_Click

    public override void VerifyRenderingInServerForm(Control control)
    {

    }// VerifyRenderingInServerForm
      '''
    body = self.replaceBody(out, locals())
    res.append(body)
    return res

  def FormatDate(self):
    res = []
    out = '''
     protected string FormatDate(object date)
    {
      if (! (date is DateTime))
      {
       return "null";
      }

      return Convert.ToDateTime(date).ToString("MM/dd/yyyy");
    }  // FormatDate
        '''
    res.append(out)
    return res

  def Main_CodePage(self):

    className = self.tbl.tname.lower() + '_view'
    fn = self.tname + ".cs"
    fname = output_dir + os.sep + fn
    body = '''
using System;
using System.Collections.Generic;
using System.Web.UI.WebControls;
using PEPSUtils;
using PEPSUtils.Generic;
using System.Web.UI;
using ${p_name}.dao;
using ${p_name}.bean;
using PWebSupport.html;
using PEPSUtils.mail;

namespace  ${p_name}.editor
{

  public partial class ${tname} : System.Web.UI.Page
  {
    $dao_class dao= null;
    ${data_been_class} ${bean_name}  = new ${data_been_class}();
    #region Pageprop
    public bool isInsert
    {
      get
      {
        return (bool)ViewState["isInsert"];
      }
      set
      {
        ViewState["isInsert"] = value;
      }
    }


        '''
    body = map_raplace(body, updateDic(locals()))
    body = map_raplace(body, self.__dict__)
    body += listToText(self.makeDD_Dictionary())
    body += listToText(self.makeProps())
    body += "#endregion \n\n"
    body += listToText(self.make_Page_Load())
    body += "#region PageFormat \n\n"
    body += listToText(self.makeLookupFunctions())
    body += listToText(self.FormatDate())
    body += "#endregion \n\n"
    body += listToText(self.clearMessages())
    body += listToText(self.setPanelsVisible())
    body += listToText(self.DataBound())
    body += listToText(self.makeBindData())
    # body += listToText(self.getPk())
    body += listToText(self.lnkCancel_Click())
    body += listToText(self.lnkDelete_Click())
    body += listToText(self.LoadsControls())
    body += listToText(self.PopulateBean())
    body += listToText(self.Populate_DropDown_Data())
    body += listToText(self.ItemCommand())
    body += listToText(self.SelectedIndexChanged())
    body += listToText(self.Sorted())
    body += listToText(self.ItemDeleted())
    body += listToText(self.ItemDeleting())
    body += listToText(self.ItemInserted())
    body += listToText(self.ItemInserting())
    body += listToText(self.RowDeleting())
    body += listToText(self.PageIndexChanged())
    body += listToText(self.ItemUpdated())
    body += listToText(self.ItemUpdating())
    body += listToText(self.ModeChanged())
    body += listToText(self.ModeChanging())
    body += listToText(self.NewRunning())
    body += listToText(self.saveDataToOracle())
    body += listToText(self.makeGetPk())
    body += listToText(self.makeSearchCode())
    body += listToText(self.makeEmailGrid())
    body += listToText(self.SaveToNewBean())
    body += listToText(self.Populate_Control_Data())
    body += listToText(self.Populate_Control_Data_call())


    # body += listToText(self.makeCSPoulateDataBean())

    body += '\n   #endregion \n}\n///////////////////////////////////\n}'
    saveToFile(fname, body)


class MakeAspxGrid(MakeGridCode):
  def  makeListExtender(self, name):
    res=[]
    out ='''
    <ajaxToolkit:ListSearchExtender
                ID="ListSearch${name}"
                PromptText="Type to search"
                PromptPosition="Top"
                IsSorted="true"
                runat="server"
                TargetControlID="lst${name}"
                PromptCssClass="PromptCSS">
            </ajaxToolkit:ListSearchExtender>

    '''
    dt= self.replaceBody(out, locals())
    return ''

  def makeSearch(self):
    res = []
    out = '''
     <asp:Panel ID="pnlFilter" runat="server" HorizontalAlign="Left" BorderStyle="Groove" BorderWidth="1px">
            <asp:Label ID="LabeFilter" runat="server" Text="Filter:"></asp:Label>
            <table>
            <tr>

    '''
    res.append(out)
    count=0;
    for c in self.colPkFirst:
      name = c.cname
      if (c.lookup == 'Y'):
        count +=1
        vt_name= self.makeTitleStr(name)
        LookupFunName = self._makeLookupFunName(c)
        res.append('<td> <div style="float: right; text-align: right"> <!-- %d -->'%count)
        label =self.makeResourcesLabel(self.tname_u,name)
        if c.dispType == "DD":
          out = '''
            <asp:Label ID="lbl${name}" runat="server" Text="${vt_name}:"></asp:Label>
            ${label}
            <asp:DropDownList ID="lst${name}" runat="server" BorderStyle="Outset"
            BorderWidth="1"
            AutoPostBack="True"
            OnSelectedIndexChanged="btnSearch_Click">
            </asp:DropDownList>
          ''' + self.makeListExtender(name)

          out = self.replaceBody(out, locals())
          res.append((out))
        else:
          out = '''
          <asp:Label ID="lblSearch${name}" runat="server" Text="${vt_name}:"></asp:Label>
           ${label}
            <asp:TextBox ID="tx${name}" runat="server" AutoPostBack="True" OnTextChanged="btnSearch_Click"></asp:TextBox>
          '''
          '''
            <ajaxToolkit:AutoCompleteExtender runat="server" ID="autoComplete_${name}" TargetControlID="tx${name}"
                ServiceMethod="get${name}" ServicePath="~/AutoCoplete/AutocpleteTest.asmx" MinimumPrefixLength="1"
                CompletionInterval="1000" CompletionSetCount="10" EnableCaching="true">
            </ajaxToolkit:AutoCompleteExtender>


         '''
          out = self.replaceBody(out, locals())
          res.append(out)
        res.append("</div></td>")
    out = '''
          <td>
            <asp:Button ID="btnSearch" runat="server" Text="Search" OnClick="btnSearch_Click" />
            <asp:Button ID="btnClear" runat="server" Text="Clear" OnClick="btnClear_Click" />
                  &nbsp;&nbsp;
              <span ID="mailMe_tgt" style="align-content:flex-end" >
                         <asp:ImageButton ID="ImgMailMe" runat="server" CausesValidation="False" ImageUrl="~/Images/email/emails.jpg"
                             OnClick="btnImage_Click" Visible="true" Width="2%" ToolTip="Email with Grid text " />
                         <asp:Panel ID="PanelmailMe" runat="server" Style="visibility: hidden" BackColor="Yellow">
                             Send email with screen  context
                         </asp:Panel>
                         <ajaxToolkit:HoverMenuExtender ID="HoverMenuExtendermailMe" runat="server" TargetControlID="ImgMailMe"
                             PopupControlID="PanelmailMe" PopupPosition="Left">
                         </ajaxToolkit:HoverMenuExtender>
                     </span>
              </td>
             </tr>
           </table>
        </asp:Panel>

           '''
    res.append(out);
    return res;
  def makEditArea(self , c):
      res=[]
      pk_col = self.fieldsPK();
      type = c.getColtype()
      cl = c.width
      cw = cl
      if cw > 60:
        cw = 60
      cname = c.cname
      a_name =c.a_name
      ReadOnly = ''
      enabled = ''
      visible = ''
      valgroup = ""
      value = self._makeLookUpView(c)
      if not c.visible:
        visible = ' Visible="False" '
      if not c.enabled:
        enabled = ' Enabled="False"'

      if c.ReadOnly or c.cname in no_input:
        ReadOnly = ' ReadOnly="True" Enabled="False" '
      if isString(c):
        val = '^.{0,%d}' % (cl)
      else:
        val = '<%$ Resources:ewm, IntegerPositive %>'
      body = '            '
      if ReadOnly:
         body += '''

                      <ItemTemplate>
                        ${value}
                      </ItemTemplate>
                      <EditItemTemplate>
                        <asp:TextBox runat="server" ID="txt$cname"  ${ReadOnly}  />
                      </EditItemTemplate>
         '''
      else:
        if not c.dispType:
          if isDate(c):
            body += '''
                    <ItemTemplate>
                       ${value}
                    </ItemTemplate>
                <EditItemTemplate>
                '''
            body += makeEditDate(name=cname, table=self.tname, output_dir=output_dir, validation_group=valgroup)
            if c.nulls in ['NOT NULL']:
              body += makeValidatorCalloutExtender(name=cname, table=self.tname, output_dir=output_dir,
                                                   validation_group=valgroup)
            body += '''
                        </EditItemTemplate>
              '''
            pass
          else:
            body += '''
                    <ItemTemplate>
                         ${value}
                     </ItemTemplate>
                    <EditItemTemplate>
                        <asp:TextBox runat="server" ID="txt${cname}" Columns="$cw"  MaxLength ="$cl" $enabled  ${a_name} />
                '''
            if c.nulls in ['NOT NULL']:
              body += makeValidatorCalloutExtender(name='txt' + cname, table=self.tname, output_dir=output_dir,
                                                   validation_group=valgroup)

            body += '''
                      </EditItemTemplate>
                       '''
        else:
          if c.dispType == 'DD':
            body += '''
                        <ItemTemplate>
                           ${value}
                        </ItemTemplate>
                        <EditItemTemplate>
                          <asp:DropDownList runat="server" ID="dd${cname}" $enabled $a_name >
                          </asp:DropDownList>

              ''' + self.makeListExtender(cname)
            if c.nulls in ['NOT NULL']:
              body += makeValidatorCalloutExtender(name='dd' + cname, table=self.tname, output_dir=output_dir,
                                                   validation_group=valgroup)
            body += '''
                      </EditItemTemplate>
                      '''
          else:
            raise Exception("Unknown Display type [%s]" % c.dispType)
            pass
      out = self.replaceBody(body, locals())
      res.append(out)
      return out

  ####################################################
  def makeDataListView(self):
    res = []

    body = '''
      <asp:Panel runat="server" ID="${editPanel}" Visible="false">
        <asp:LinkButton ID="lnkCancel" runat="server" CausesValidation="False"
            CommandName="Cancel" Text="Cancel"  OnClick="lnkCancel_Click"></asp:LinkButton>
<table>
            <tr>
                <td>
        <asp:DetailsView ID="${editControl}" runat="Server" CellPadding="1" ForeColor="#DDDDFF"

            BorderColor="Yellow" BorderWidth="2px" GridLines="None" Width="500px" AutoGenerateRows="False"
            AutoGenerateEditButton="True" Font-Size="Medium" FooterStyle-BorderColor="Black"
            FooterStyle-BorderStyle="Double"
            Style="margin-right: 3px"
            $_data_fields
            OnItemDeleted="${editControl}_ItemDeleted"
            OnItemInserted="${editControl}_ItemInserted"
            OnModeChanging="${editControl}_ModeChanging"
            OnItemUpdating="${editControl}_ItemUpdating"
            OnItemDeleting="${editControl}_ItemDeleting"
            OnItemInserting="${editControl}_ItemInserting"
             AutoGenerateInsertButton="True"
            >
            <FooterStyle BackColor="#DDDDFF" Font-Bold="True" ForeColor="White" />
            <CommandRowStyle BackColor="#E2DED6" Font-Bold="True" />
            <EditRowStyle BackColor="#DDDDFF" />
            <RowStyle BackColor="#DDDDFF" ForeColor="#333333" />
            <PagerStyle BackColor="#284775" ForeColor="White" HorizontalAlign="Center" />
            <FieldHeaderStyle BackColor="#E9ECF1" Font-Bold="True" />
            <HeaderStyle BackColor="#DDDDFF" Font-Bold="True" ForeColor="White" />
            <AlternatingRowStyle BackColor="White" ForeColor="#284775" />
            <Fields>
              <asp:CommandField ButtonType="Link" ShowCancelButton="true" ShowEditButton="true" />

        '''
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(body, self.__dict__)
    res.append(out)

    for c in self.colPkFirst:
      pk_col = self.fieldsPK();
      type = c.getColtype()
      cl = c.width
      cw = cl
      if cw > 60:
        cw = 60
      cname = c.cname
      a_name =c.a_name
      ReadOnly = ''
      enabled = ''
      visible = ''
      valgroup = ""
      value = self._makeLookUpView(c)
      if not c.visible:
        visible = ' Visible="False" '
      if not c.enabled:
        enabled = ' Enabled="False"'

      if c.ReadOnly or c.cname in no_input:
        ReadOnly = ' ReadOnly="True" Enabled="False" '
      if isString(c):
        val = '^.{0,%d}' % (cl)
      else:
        val = '<%$ Resources:ewm, IntegerPositive %>'
      # makeAutoComplite(name=cname, table=self.tname, output_dir=output_dir)
      # makeHoverMenu(name=cname, table=self.tname, output_dir=output_dir)
      body = '            <asp:TemplateField HeaderText="<%$ Resources:${p_name}, ${tname}_${cname}   %>"  $visible   HeaderStyle-VerticalAlign="Top"  HeaderStyle-Width="250px" >'
      if ReadOnly:

        body += '''

                      <ItemTemplate>
                        ${value}
                      </ItemTemplate>
                      <EditItemTemplate>
                        <asp:TextBox runat="server" ID="txt$cname"  ${ReadOnly}  />
                      </EditItemTemplate>
         '''
      else:
        if not c.dispType:
          if isDate(c):
            body += '''
                    <ItemTemplate>
                       ${value}
                    </ItemTemplate>
                <EditItemTemplate>
                '''
            body += makeEditDate(name=cname, table=self.tname, output_dir=output_dir, validation_group=valgroup)
            if c.nulls in ['NOT NULL']:
              body += makeValidatorCalloutExtender(name=cname, table=self.tname, output_dir=output_dir,
                                                   validation_group=valgroup)
            body += '''
                        </EditItemTemplate>
              '''
            pass
          else:
            body += '''
                    <ItemTemplate>
                         ${value}
                     </ItemTemplate>
                    <EditItemTemplate>
                        <asp:TextBox runat="server" ID="txt${cname}" Columns="$cw"  MaxLength ="$cl" $enabled  ${a_name} />
                '''
            if c.nulls in ['NOT NULL']:
              body += makeValidatorCalloutExtender(name='txt' + cname, table=self.tname, output_dir=output_dir,
                                                   validation_group=valgroup)

            body += '''
                      </EditItemTemplate>
                       '''
        else:
          if c.dispType == 'DD':
            body += '''
                        <ItemTemplate>
                           ${value}
                        </ItemTemplate>
                        <EditItemTemplate>
                          <asp:DropDownList runat="server" ID="dd${cname}" $enabled $a_name >
                          </asp:DropDownList>

              ''' + self.makeListExtender(cname)
            if c.nulls in ['NOT NULL']:
              body += makeValidatorCalloutExtender(name='dd' + cname, table=self.tname, output_dir=output_dir,
                                                   validation_group=valgroup)
            body += '''
                      </EditItemTemplate>
                      '''
          elif  c.dispType == 'CHK':
             body += '''
                        <ItemTemplate>
                           ${value}
                        </ItemTemplate>
                        <EditItemTemplate>
                          <asp:CheckBox  runat="server" ID="chk${cname}" $enabled $a_name >
                          </asp:CheckBox>
                                                </EditItemTemplate>
              '''

          else:
            raise Exception("Unknown Display type [%s]" % c.dispType)
            pass
      body += '</asp:TemplateField>'
      out = replaceTemplate(body, updateDic(locals()))
      out = replaceTemplate(out, self.__dict__)
      res.append(out)
      out = ''
    # For
    res.append(out)
    res.append('''
              </Fields>
        </asp:DetailsView>
                        </td>
                <td style="text-align: left; width: 300px">
                    <div id="siteInfo">
                    </div>
                </td>
            </tr>
        </table>

        </asp:Panel>
        ''')
    return res
    ###################

  def makeGridView(self):
    gridView = tbl.gridControl
    res = []
    self.search_panel = listToText(self.makeSearch())
    vt_name = self.makeTitleStr(self.tname)
    command_line_delete =self.makeCommandLineArgument()
    body = '''
       <h2>$vt_name </h2>

    <asp:Panel runat="server" ID="${viewPanel}">

        $search_panel
        <asp:LinkButton ID="LinkNew" runat="server" CausesValidation="False"
            CommandName="New" Text="New" OnClick="NewRunning"></asp:LinkButton>

        <asp:GridView ID="${gridControl}" runat="server" AllowPaging="True" AllowSorting="True"
            AutoGenerateColumns="False"
            BorderWidth="1px"
            Caption=""
            DataSourceID="SqlDataSource1"  PageSize="20"
            AutoGenerateSelectButton="True"
            $_data_fields
            OnPageIndexChanged="${gridView}_PageIndexChanged"

            OnSelectedIndexChanged="${gridView}_SelectedIndexChanged"
            OnSorted="${gridView}_Sorted"
            EnableModelValidation="False"
            Font-Size="Small"
            AlternatingRowStyle-BackColor="#CCFFCC"
            AlternatingRowStyle-BorderStyle="Dotted"
            HeaderStyle-BackColor="#66FF99"
            HeaderStyle-BorderStyle="Solid"
            RowStyle-BorderStyle="None"
            BorderStyle="Solid"
            BorderColor="Black">
            <Columns>
                <asp:TemplateField>
                    <ItemTemplate>

                        <asp:LinkButton ID="lnkDelete" runat="server" CausesValidation="False"
                            CommandName="Delete" Text="Delete" OnClientClick="return confirm('Are you sure you want to delete this record');"
                            ${command_line_delete}
                             OnClick="lnkDelete_Click"></asp:LinkButton>
                    </ItemTemplate>
                </asp:TemplateField>

    '''
    out = self.replaceBody(body, (locals()))
    # out = replaceTemplate(out, self.__dict__)
    res.append(out)

    body = '''
           <asp:TemplateField>
            <ItemTemplate>
              <asp:LinkButton ID="lnkEdit" runat="server" CommandName="Edit" Text="Edit" />
  <%--            <asp:LinkButton ID="lnkDelete" runat="server" CommandName="Delete" Text="Delete" />--%>
            </ItemTemplate>
          </asp:TemplateField>
    '''
    # out = replaceTemplate(body, updateDic(locals()))
    # res.append(out)

    body = '''
             <asp:TemplateField HeaderText="">
                <HeaderStyle Width="1px" />
                    <ItemTemplate>
                      <asp:LinkButton ID="lnkKey" runat="server" CommandName="Confirm" Text="<%#Eval("$pk")%>" />
                    </ItemTemplate>
              </asp:TemplateField>

    '''
    # out = replaceTemplate(body, updateDic(locals()))
    # out = replaceTemplate(out, self.__dict__)
    #res.append(out)

    for c in self.collons:
      type = c.getColtype()
      cl = c.width
      cw = cl
      cname = c.cname
      ReadOnly = ''
      enabled = ''
      visible = ''
      value = self._makeLookUpView(c)
      body = '''
           <asp:TemplateField HeaderText="<%$ Resources:${p_name}, ${tname}_${cname} %>" SortExpression="$cname">
              <ItemTemplate>
                ${value}
              </ItemTemplate>
           </asp:TemplateField>
      '''

      out = self.replaceBody(body, updateDic(locals()))
      res.append(out)
    body = '''
          </Columns>
        </asp:GridView>
      </asp:Panel>

    '''
    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)

    res.append(out)
    return res;


  def makeResources(self):
    res = []
    collons = self.collons
    pk = 0
    res.append("")
    tname = tbl.getName()
    res.append('')
    res.append("<!-- Start '%s' -->"%tname)
    for c in collons:
      name = c.cname
      nameC= self.makeTitleStr(name)
      comments = c.comments
      if not comments:
        comments=name
      st = '''
    <data name="${tname}_${name}" xml:space="preserve">
      <value>$nameC</value>
      <comment>$comments</comment>
    </data>       '''
      out = velocityReplace(st, locals())
      res.append(out)
    res.append("<!-- End  '%s' -->"%tname)
    return res

  ##############################################
  def makeOracleSection(self):
    res = []
    pkf = self.getPkField()
    body = '''

    <asp:SqlDataSource ID="SqlDataSource1" runat="server"  ConnectionString="FakeStr" ProviderName="<%$ ConnectionStrings:ConnectionString2.ProviderName %>"
        SelectCommand="SELECT * FROM ${tname}  WHERE (1=1)    "
        DeleteCommand="DELETE FROM ${tname} WHERE  1=0 and     '''
    i = 0;
    for c in pkf:
      name = c.cname
      if i == 0: body + ' , '
      i += 1
      body += '%s  = {%d} ' % (name, i)
    body += '"\n'
    body += '     FilterExpression=" (  '
    i = 0;
    for c in self.colPkFirst:
      if not c.lookup == 'Y':
        continue

      if c.cname in no_input:
        continue
      name = c.cname;pref='%'
      if c.dispType == 'DD':
        pref = ''

      if i > 0: body += ' and (  '
      i += 1
      body += "%s like '{%d}%s'" % (name, i - 1,pref)
      if self.isNull(c):
        body +=' or  ( %s is null )'%name

      body +=' ) '
    body += '"\n         >\n'
    body += '   <DeleteParameters>\n';
    for c in pkf:
      name = c.cname
      body += '       <asp:Parameter Name="%s" Type="String" /> \n' % (name)
    body += '''
    </DeleteParameters>
        '''

    vr = '\n\n         <FilterParameters>\n'

    cols = pkf
    for c in self.colPkFirst:
      nm = c.cname
      if not c.lookup == 'Y':
        continue

      if c.cname in no_input:
        continue
      pref = 'tx'
      defl='%'
      if c.dispType == 'DD':
        pref = 'lst'
        defl='%%'

      vr += '            <asp:ControlParameter DefaultValue="%s" ControlID="%s%s" PropertyName="text" Name=":%s" ConvertEmptyStringToNull="False" />\n' % (
      defl,pref, nm, nm)

    vr += '        </FilterParameters>\n'
    body += vr
    body += '''
    </asp:SqlDataSource>
    '''

    out = replaceTemplate(body, updateDic(locals()))
    out = replaceTemplate(out, self.__dict__)
    res.append(out)
    return res
  ###############################################
  def makeResourcesLabel(self,table, name):
     st = ' <asp:Label ID="lbl${name}" meta:resourcekey="${table}_${name}" runat="server" Text="<%$ Resources:SLA, ${table}_${name}  %>"></asp:Label>:'
     st=self.replaceBody(st,locals())
     return st

  ####################################
  def  makeResourcesLabels(self):
    res=[]
    pkf = self.tbl.columns
    table =self.tbl.tname.upper()
    res.append("\n"*5)
    res.append("<%!--\n")
    for c in pkf:
      name =c.cname
      st = self.makeResourcesLabel(table,name)
      # st=self.replaceBody(st,locals())
      res.append(st)
    res.append("--%>")

    return res

  def makeAspPage(self):
    fn = self.tname + ".aspx"
    fname = output_dir + os.sep + fn
    body = '''


        '''
    body += listToText(self.makeGridView())
    body += listToText(self.makeDataListView())
    body += listToText(self.makeOracleSection())
    body += listToText(self.makeResourcesLabels())
    saveToFile(fname, body)
    print fname
    fn = self.tname + ".xml"
    fname = output_dir + os.sep + fn

    body = listToText(self.makeResources())
    saveToFile(fname, body)

    ########################################################


if __name__ == '__main__':
  #  print tables_list
  tbl = tables_list[w_table_name]
  output_dir += os.sep + tbl.tname
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  out = MakeGridCode(tbl)
  out.Main_CodePage()
  aspx = MakeAspxGrid(tbl)
  aspx.makeAspPage()


