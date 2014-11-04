__author__ = 'mgo4943'
from  MakeGridCode import *
class OnlineEditor( MakeAspxGrid):
  def onlineDataObject ( self):
    res=[]
    st="""
public List<${data_been_class}> ${tname_l}_data
    {
      get
      {
        object v_e2e_sla_test_data = ViewState["${tname_l}_data"];
        if (v_e2e_sla_test_data != null)
        {
          return (List<${data_been_class}>)ViewState["${tname_l}_data"];
        }
        return (default(List<${data_been_class}>));
      }
      set
      {
        ViewState["${tname_l}_data"] = value;
      }
    }
    // end
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st

  def Page_Load( self):
    res=[]
    st="""

    protected void Page_Load(object sender, EventArgs e)
    {
      ora = SLACommon.getMainOracleConnectionString();
      if (!SLACommon.testOracle())
      {
        pnl_grid_E2e_sla_test.Visible = false;
        return;
      }

      if (!SLACommon.isLoging())
      {
        ResponseHelper.Redirect("~/login/logout.aspx?message=Session+error");
      }

      if (!string.IsNullOrEmpty(ora))
      {
        //        SqlDataSource1.ConnectionString = ora;
        ${dao_name} = new ${dao_class}(ora);
      }
      else
      {
        ResponseHelper.Redirect("~/default.aspx?message=No+Valid+Oracle+connection");
      }
      if (!IsPostBack)
      {
        PopulateBean();
        LoadsControls();

        string customerh4 = Request["customer_h4"];
        if (string.IsNullOrWhiteSpace(customerh4))
        {
          if (Session["CustomerH4"] != null)
          {
            customerh4 = Convert.ToString(Session["CustomerH4"]);
          }
        }

        if (!string.IsNullOrWhiteSpace(customerh4))
        {
          Customer_dao custdao = null;
          custdao = new Customer_dao(ora);
          Customer_bean customerbean = new Customer_bean();
          customerbean.customer_h4 = customerh4;
          if (!custdao.getByH4(ref customerbean))
          {
            error_text = " Not Valid  Customer H4  data ";
            return;
          }

          customer_nbr = customerbean.customer_nbr;
          ${bean_name}.customer_nbr = customer_nbr;
        }
        else
        {
          error_text = " Not Valid  Customer H4";
          return;
        }
        product_nbr = Request["product_nbr"];
        if (string.IsNullOrWhiteSpace(product_nbr))
        {
          error_text = " Not Valid  Product information";
          return;
        }
        lblProduct.Text = FormatPRODUCT_NBR(product_nbr);
        BindOracleData();
      }
    }


    """
    res.append(st)
    return st
############################ End Page_Load
  def jumpBack( self):
    res=[]
    st="""
    protected void  jumpBack()
    {
     ResponseHelper.Redirect(Request.UrlReferrer.ToString());
    }
    // end  jumpBack
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End jumpBack
  def getPk( self):
    res=[]
    st="""
    private int getPk($data_been_class ${bean_name}, object sender = null)
    {
      GridView _e;
      if (sender != null)
      {
        _e = (GridView)sender;
      }
      else
      {
        _e = ${gridControl};
      }
      ${bean_name}.Clear();
      int index = _e.SelectedIndex;
      if (index < 0)
      {
        error_text = "No selected index";
        return -1;
      }
      if (index >= ${gridControl}.DataKeys.Count)
      {
        return -1;
      }
    """
    body = self.replaceBody(st,locals())
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
          return -1;
        }
           ${bean_name}.$fld_name_l =$fld_name ;
       '''
      body=self.replaceBody(body,locals())
      res.append(body)

    st="""

      return index;
    }
    // end  getPk
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return res



  def RowCancelingEdit( self):
    res=[]
    st="""
 protected void ${gridControl}_RowCancelingEdit(object sender, GridViewCancelEditEventArgs e)
    {
      jumpBack();
    }
    // end  E2e_sla_test_grid_RowCancelingEdit
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End E2e_sla_test_grid_RowCancelingEdit

  def startClass(self):

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
    private ${dao_class} ${dao_name} = null;
    ${data_been_class} ${bean_name}  = new ${data_been_class}();

    }

        '''
    body = self.replaceBody(body, locals())
    return body
  def BindOracleData( self):
    res=[]
    where = self.makeWhere(self.getPkCols())
    st="""
  private void BindOracleData${module_name}(${data_been_class} bean, bool ok = false)
    {
      if (${tname_l}_data == null || (${tname_l}_data.Count == 0))
      {
        ok = true;
      }
      if (ok)
      {
        string where = $where;
        ${tname_l}_data = ${dao_name}.List(where);
      }
       ${editControl}.DataSource = ${tname_l}_data;
      if (ok)
      {
         ${editControl}.EditIndex = -1;
      }
       ${editControl}.DataBind();
    }
    // end  BindOracleData${module_name}
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End BindOracleData
  def saveDataToOracle( self):
    res=[]
    st="""
    private bool saveDataToOracle${module_name}(Control grid)
    {
      clearMessages();
      ${data_been_class} new_bean = new ${data_been_class}();
      error_text = ControlValidation.validateInServer(grid);
      if (!string.IsNullOrEmpty(error_text))
      {
        return false;
      }
      if (!SaveToNewBean(grid, ref new_bean))
      {
        error_text = string.Format("Cannot Save Data '{0}'", new_bean);
        return false;
      }
      if (new_bean.site_a_id == new_bean.site_b_id)
      {
        error_text = string.Format("Site A and Site B Cannot be identical- Data integrity validation", new_bean.ToString());
        return false;
      }
      new_bean.product_nbr = product_nbr;
      new_bean.customer_nbr = customer_nbr;
      new_bean.test_id = test_id;
      isInsert = string.IsNullOrWhiteSpace(test_id);
      if (isInsert)
      {
        ${data_been_class} bean_save = new ${data_been_class}();
        bean_save.Copy(new_bean);
        if (${dao_name}.isNamesThere(new_bean))
        {
          error_text = string.Format("Record '{0}' has duplicates - Data integrity validation", new_bean.ToString());
          return false;
        }
        string TEST_ID = Code.tools.NextVal.nextVal("E2E_SLA_TEST");
        new_bean.test_id = TEST_ID;
        ${dao_name}.Insert(new_bean);
        if (!string.IsNullOrEmpty(${dao_name}.lastError))
        {
          error_text = ${dao_name}.lastError;
          return false;
        }
      }
      else
      {
        new_bean.test_id = test_id;
        bool ret = ${dao_name}.Update(new_bean);
        if (!string.IsNullOrEmpty(${dao_name}.lastError))
        {
          error_text = ${dao_name}.lastError;
          return false;
        }
      }
      jumpBack();
      return true;
    }
    // end  saveDataToOracle${module_name}
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End saveDataToOracle
  def SelectedIndexChanged( self):
    res=[]
    st="""
protected void ${gridControl}_SelectedIndexChanged(object sender, EventArgs e)
    {
      clearMessages();
    }
    // end  SelectedIndexChanged
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End SelectedIndexChanged
  def Sorted( self):
    res=[]
    st="""
protected void ${gridControl}_Sorted(object sender, EventArgs e)
    {
          clearMessages();
    }
    // end  Sorted

protected void ${gridControl}_Sorting(object sender, EventArgs e)
    {
          clearMessages();
    }
    // end  Sorting

    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End Sorted
  def PageIndexChanged( self):
    res=[]
    st="""
     protected void ${gridControl}_PageIndexChanged(object sender, EventArgs e)
    {
              clearMessages();
    }
    // end  PageIndexChanged
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End PageIndexChanged
  def RowCreated( self):
    res=[]
    st="""
 protected void ${gridControl}_RowCreated(object sender, GridViewRowEventArgs e)
    {
    }
    // end  RowCreated
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End RowCreated

  def PageIndexChanged( self):
    res=[]
    st="""
protected void ${gridControl}_PageIndexChanged(object sender, EventArgs e)
    {
    }
    // end  PageIndexChanged
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End PageIndexChanged
  def RowCommand( self):
    res=[]
    st="""
protected void ${gridControl}_RowCommand(object sender, GridViewCommandEventArgs e)
    {
      isInsert = false;
      clearMessages();
      if (e.CommandName.Equals("Insert"))
      {
        if (${tname_l}_data == null)
        {
          this.BindOracleData();
        }
        ${data_been_class} be = new ${data_been_class}();
        be.initData();
        ${tname_l}_data.Add(be);
        this.BindOracleData();
        int index =  ${editControl}.Rows.Count;
         ${editControl}.EditIndex = index;
         ${editControl}.SelectedIndex = index;
        ${gridControl}_RowEditing(sender, null);
      }
       if (e.CommandName == "Update")
      {
        int index =  ${editControl}.EditIndex;
        isInsert = false;
        Control control =  ${editControl}.Rows[index];
        Commitment_detail_bean new_bean = new Commitment_detail_bean();
        error_text = ControlValidation.validateInServer(control);
        if (!string.IsNullOrEmpty(error_text))
        {
          return;
        }
        new_bean = commitment_detail_data[index];
        if (!updateBeanValues(control, ref new_bean))
        {
          error_text = "Cannot save data into bean ";
          return;
        }
#if  one_line
        ${dao_name}.InsertOrUpdate(new_bean);
        commitment_detail_data[index] = new_bean;
        this.BindOracleData();
#endif
#if all_process
        commitment_detail_data[index] = new_bean;
         ${editControl}.EditIndex = -1;
        this.BindOracleData(bean);
#endif
        updateCustomiseFlag();
        commitment_detail_data[index] = new_bean;
         ${editControl}.EditIndex = -1;
        this.BindOracleData();
      }
      else
      {
        if (e.CommandName == "Edit")
        {
          this.BindOracleData();
        }
      }
    }
    // end  RowCommand
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End RowCommand

  def RowDataBound( self):
    res=[]
    st="""
protected void ${gridControl}_RowDataBound(object sender, GridViewRowEventArgs e)
    {
      //mayEditActivity = false;
      if (!mayEditActivity)
      {
        int index = 6; // Active flag possition
        if (index < e.Row.Cells.Count)
        {
          e.Row.Cells[index].Visible = false;
        }
      }
    }
    // end  RowDataBound
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End RowDataBound
  def RowDeleted( self):
    res=[]
    st="""
 protected void ${gridControl}_RowDeleted(object sender, GridViewDeletedEventArgs e)
    {
      ${bean_name}.test_id = (string)e.Keys["${pk_name}"];
      if (!string.IsNullOrWhiteSpace(${bean_name}.test_id))
      {
        if (!${dao_name}.deleteByPk(${bean_name}))
        {
          error_text = string.Format("Cannot delete : {0}", ${bean_name});
          return;
        }
        else
        {
          note_text = "Deleted";
          this.BindOracleData(true);
        }
      }
    }
    // end  RowDeleted
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End RowDeleted

  def RowDeleting( self):
    res=[]
    st="""
 protected void ${gridControl}_RowDeleting(object sender, GridViewDeleteEventArgs e)
    {
      ${bean_name}.test_id = (string)e.Keys["${pk_name}"];
      if (!string.IsNullOrWhiteSpace(${bean_name}.test_id))
      {
        if (!${dao_name}.deleteByPk(${bean_name}))
        {
          error_text = string.Format("Cannot delete : {0}", ${bean_name});
          return;
        }
        else
        {
          note_text = "Deleted";
          this.BindOracleData(true);
        }
      }
    }
    // end  RowDeleting
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End RowDeleting
  def RowEditing( self):
    res=[]
    st="""
protected void ${gridControl}_RowEditing(object sender, GridViewEditEventArgs e)
    {
      clearMessages();
      if (${gridControl}.EditIndex < 0)
      {
        ${gridControl}.EditIndex = e.NewEditIndex;
      }
      else
      {
        if (e != null)
        {
          jumpBack${module_name}();
          ${gridControl}.EditIndex = e.NewEditIndex;
        }
      }
      int index = ${gridControl}.EditIndex;
      if (index > -1 && (e != null))
      {
        $data_been_class readBean = new $data_been_class();
        ${gridControl}.SelectedIndex = index;
        if (getPk(${gridControl}, readBean) > -1)
        {
    """
    st=self.replaceBody(st,locals())
    res.append(st)
    pk = self.getPkField()
    for c in pk:
      fld_name = c.cname
      fld_name_l = c.cname.lower()
      body = '''

          if (string.IsNullOrWhiteSpace(readBean.${fld_name_l}))
          {
              error_text = "Cannot Load data From Grid [${fld_name}]  ";
              return;

         }
           '''
      body=self.replaceBody(body,locals())
      res.append(body)
    st="""
      if (!${dao_name}.getPk(ref readBean))
      {
         error_text = "Cannot Load data From Database ";
          return;
      }
      else
      {
        isInsert = true;
        ${bean_name} = ${tname_l}_data[${tname_l}_data.Count - 1];
      }
      this.BindOracleData();
      Populate_Control_Data(${gridControl}.Rows[index], ${bean_name});
      }
     }
    }
    """
    """
      else
      {
        if (e == null)
        {
          isInsert = true;
          if (index > 0)
          {
            index--;
          }
          else
          {
            index = ${gridControl}.Rows.Count - 1;
          }
          ${gridControl}.SelectedIndex = index;
          ${gridControl}.EditIndex = index;
          //${gridControl}.Rows[index].RowState = DataControlRowState.Edit;
          ${gridControl}.DataBind();
          Populate_DropDown_Data(${gridControl}.Rows[index], ${tname_l}_data[${tname_l}_data.Count - 1]);
        }
        else
        {
          error_text = "Cannot Load data from grid";
        }
      }
      if (string.IsNullOrWhiteSpace(error_text))
      {
        ${gridControl}.Controls.hideLinkOnControlCollection("Insert");
      }
    }
    // end  RowEditing
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return res
############################ End RowEditing

  def RowUpdated( self):
    res=[]
    st="""
 protected void ${gridControl}_RowUpdated(object sender, GridViewUpdatedEventArgs e)
    {
    }
    // end  RowUpdated
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End RowUpdated
  def RowUpdating( self):
    res=[]
    st="""
protected void ${gridControl}_RowUpdating(object sender, GridViewUpdateEventArgs e)
    {
      int index = ${gridControl}.EditIndex;
      isInsert = false;
      saveDataToOracle(${gridControl}.Rows[index]);
      ${gridControl}.EditIndex = -1;
      if (claenEmptyEntryes${module_name}())
      {
        this.BindOracleData();
      }
      //${gridControl}.Rows[index].RowState = DataControlRowState.Normal;
      //this.BindOracleData();
    }
    // end  RowUpdating
    """
    st= self.replaceBody(st,locals())
    res.append(st)
    return st
############################ End RowUpdating

  def makeGridEdit(self):
    gridView = tbl.gridControl
    res = []
    # self.search_panel = listToText(self.makeSearch())
    vt_name = self.makeTitleStr(self.tname)
    body = '''



        <asp:GridView ID="${gridControl}" runat="server" AllowPaging="True" AllowSorting="True"
            AutoGenerateColumns="False"
            BorderWidth="1px"
            Caption=""
          ` PageSize="20"

            $_data_fields
            OnPageIndexChanged="${gridView}_PageIndexChanged"
            OnSelectedIndexChanged="${gridView}_SelectedIndexChanged"
            OnRowCancelingEdit="${gridView}_RowCancelingEdit"
            OnRowCommand="${gridView}_RowCommand"
            OnRowCreated="${gridView}_RowCreated"
            OnRowDataBound="${gridView}_RowDataBound"
            OnRowDeleted="${gridView}_RowDeleted"
            OnRowEditing="${gridView}_RowEditing"
            OnRowUpdated="${gridView}_RowUpdated"
            OnRowUpdating="${gridView}_RowUpdating"
            OnSorted="${gridView}_Sorted"
            EnableModelValidation="True"
            Font-Size="Small"

            HeaderStyle-BorderStyle="Solid"
            RowStyle-BorderStyle="None"
            BorderStyle="Solid"
            BorderColor="Black">
            <Columns>
                <asp:TemplateField HeaderText="Edit" ShowHeader="False" HeaderStyle-HorizontalAlign="Left">
                    <EditItemTemplate>
                        <asp:LinkButton ID="lbkUpdate" runat="server" CausesValidation="True" CommandName="Update" Text="Update"></asp:LinkButton>
                        <asp:LinkButton ID="lnkCancel" runat="server" CausesValidation="False" CommandName="Cancel" Text="Cancel"></asp:LinkButton>
                    </EditItemTemplate>
                    <FooterTemplate>
                        <asp:LinkButton ID="lnkAdd" runat="server" CausesValidation="False" CommandName="Insert" Text="Insert"></asp:LinkButton>
                    </FooterTemplate>
                    <ItemTemplate>
                        <asp:LinkButton ID="lnkEdit" runat="server" CausesValidation="False" CommandName="Edit" Text="Edit"></asp:LinkButton>
                    </ItemTemplate>
                    <HeaderStyle HorizontalAlign="Left" />
                </asp:TemplateField>

    '''
    out = self.replaceBody(body,(locals()))
    res.append(out)

    body = '''

    '''
    # out = replaceTemplate(body, updateDic(locals()))
    # res.append(out)

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

      ''' + self.makEditArea(c) + '''
        </asp:TemplateField>
      '''


      out = self.replaceBody(body, updateDic(locals()))
      res.append(out)
    body = '''
          </Columns>
        </asp:GridView>
      </asp:Panel>

    '''
    out =self.replaceBody(body,(locals()))

    res.append(out)
    return res;

###############################################################



  def Main_CodePage(self):
    fn = self.tname + "_inline.cs"
    fn2 = self.tname + "_inline.aspx"
    fname = output_dir + os.sep + fn
    fname2 = output_dir + os.sep + fn2
    fn = self.tname + ".cs"
    body =self.startClass()
    body +='''
     #region Page_prop
    '''
    body += listToText(self.makeProps())
    body += listToText(self.onlineDataObject())
    body += listToText(self.makeDD_Dictionary())

    body += "#endregion \n\n"
    body +='''#region Page_Main\n\n '''

    body += listToText(self.Page_Load())
    body += listToText(self.clearMessages())
    body += listToText(self.BindOracleData())
    body += listToText(self.makeBindData())
    body += listToText(self.jumpBack())
    body += listToText(self.getPk())
    body += "#endregion \n\n"

    body +='''\n\n #region Page_Format\n\n '''

    body += listToText(self.makeLookupFunctions())
    body += listToText(self.FormatDate())
    body += "#endregion // Page Format \n\n"

    body +='''\n\n #region Page_edit_function\n\n '''
    body += listToText(self.RowCancelingEdit())
    body += listToText(self.SelectedIndexChanged())
    body += listToText(self.Sorted())
    body += listToText(self.RowCreated())
    body += listToText(self.RowDataBound())
    body += listToText(self.RowDeleted())
    body += listToText(self.RowEditing())
    body += listToText(self.RowUpdated())
    body += listToText(self.RowUpdating())
    body += listToText(self.PageIndexChanged())
    body += listToText(self.RowCommand())
    body += "#endregion // Page Edit function  \n\n"

    body +=''' #region Save_Object\n\n '''
    body += listToText(self.saveDataToOracle())
    body += listToText(self.Populate_DropDown_Data())
    body += listToText(self.SaveToNewBean())
    body += '\n   #endregion \n}\n////////  End Class ///////////////////////////\n}'
    saveToFile(fname, body)
    body = listToText(self.makeGridEdit())
    saveToFile(fname2, body)
  pass

if __name__ == '__main__':
  #  print tables_list
  tbl = tables_list[w_table_name]
  output_dir += os.sep + tbl.tname
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  out = OnlineEditor(tbl)
  out.Main_CodePage()
