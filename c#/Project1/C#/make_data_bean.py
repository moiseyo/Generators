import setpath, sys

setpath.addToPath(r'..\..\..\..\projects')
from package1 import *
from Gizmo.dbAccess.tables import *
from Gizmo.dbAccess.common import *
from mod_file import *
from SLA_tables import *


class BeanClass(BaseEditor):
  def __init__(self, __tbl):
  #    print 1
    super(BeanClass, self).__init__(__tbl)
    self.p_name = package_name + '.bean'

  def makeCassStart(self):
    res = []
    so = '''

using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Globalization;
using Gizmo;

namespace ${p_name}{

[Serializable()]  public class $data_been_class {
'''

    so = map_raplace(so, locals())
    so = map_raplace(so, self.__dict__)
    res.append(so)
    return res

  def makeMembers(self):
    res = []
    so = '#region "Private Member Variables"'
    res.append(so)
    for c in self.collons:
      name = c.getCname()
      l_name = name.lower()
      st = " private %s _%s;  " % (getVarType(c), l_name)
      res.append(st)
    so = '#endregion'
    res.append(so)
    return res;
  def makeProperties(self):
    res = []
    for c in self.collons:
      name = c.getCname()
      l_name = name.lower()
      st = '''
    public $tp  $l_name
    {
      get
      {
        return _$l_name;
      }
      set
      {
      _$l_name = value;
      }
    }
    '''
      tp =getVarType(c)
      so = self.replaceBody(st, locals())

      res.append(so)
    return  res


  def makeConstrictors(self):
    res = []
    so = '''
    public  $data_been_class (){
    }
    '''
    so = replaceTemplate(so, locals())
    so = map_raplace(so, self.__dict__)
    res.append(so)
    if False:
      st = '  public %s (' % self.data_been_class
      j = 0
      for c in self.collons:
        if j > 0:
          st += ' , '
        j += 1
        name = c.getCname()
        l_name = name.lower()
        st += getVarType(c) + ' ' + name + "  "
      st += '){'

      res.append(st)

      for c in self.collons:
        name = c.getCname()
        l_name = name.lower()
        st = '''   this._$l_name=$name;'''

        so = replaceTemplate(st, locals())
        so = map_raplace(so, self.__dict__)
        res.append(so)
      so = '''
       }
   '''
      res.append(so)
    return res;
    #######################################
  def makeCopy(self):
    res=[]
    so='''
  public  void  Copy(  $data_been_class  other  ){
  '''
    so = map_raplace(so, locals())
    so = map_raplace(so, self.__dict__)
    res.append(so)
    for c in self.collons:
      name = c.getCname()
      l_name = name.lower()
      st = '''this._$l_name = other.$l_name;'''
      so = replaceTemplate(st, locals())
      so = map_raplace(so, self.__dict__)
      res.append(so)


    so='''
}
'''
    res.append(so)
    return res
  def makeCopyConstructor(self):
    res = []
    so = '''
    public   $data_been_class ( $data_been_class other    ){
    '''
    so = map_raplace(so, locals())
    so = map_raplace(so, self.__dict__)
    res.append(so)
    so = '''
      Copy(other);
      }
      '''
    res.append(so)
    return res
  def makeClear(self):
    res = []
    st='  public void  Clear(){'
    res.append(st)
    j=0

    for c in self.collons:
      name = c.getCname()
      l_name = name.lower()
      if isString(c):
        st = '        this._$l_name = "";  '
      elif isDate(c):
           st = '''   this._$l_name = DateTime.Now;  '''
      elif isNumber(c):
          st = '''       this._$l_name = 0;    '''
      elif isLong(c):
            continue

      so = replaceTemplate(st, locals())
      so = map_raplace(so, self.__dict__)
      res.append(so)


    so='''
  }
  '''
    res.append(so)
    return res

  def makeInitData(self):
    res = []
    so='''public void initData(){  '''
    out=''
    res.append(so)
    for c in self.collons:
      fn = '_'+c.cname.lower()
      type = c.coltype
      fun=''
      if isString (type):
        out +='           %s="";\n'%fn
      elif isDate(type):
        out +='      %s=DateTime.Now;\n'%fn
      elif isInteger(c):
        out +='      %s=0;\n'%fn
      elif isNumber(c):
        out +='      %s=0;\n'%fn
      else:
        raise  Exception("Wrong [%s].[%s].[%s]"%(type,c.cname, c.tname))


    out += """
  }"""
    res.append(out)
    return res
  def makeFixData(self):
    res = []
    so='''public void fixData(){  '''
    out=''
    res.append(so)
    for c in self.collons:
      fn = '_'+c.cname.lower()
      type = c.coltype
      fun=''
      if isString (type):
        st ='''
         if ( string.IsNullOrEmpty($fn))
         {
         $fn="";
         }'''
      if isDate(type):
        st='''  if ( $fn==null) {
          $fn=DateTime.Now;
        }'''

      out+= self.replaceBody(st,locals())
    out += """
  }"""
    res.append(out)
    return res


  def makeBuildKey(self):
    global className, cl
    res=[]
    sout = """
    public string  buildKey () {
      StringBuilder sb= new StringBuilder();
    """

    for c in self.collons :
        if c.pkpos:
            s1 = "        sb.Append(%s.Trim());  //%s \n" % (makeTabColumnFormat(c), "")
            # s1 = "        sb.Append(%s.Trim());  //%s \n" % (makeTabColumnFormat(c), c.comments)
            sout += s1
    sout += """      return sb.ToString ();
    }
    """
    res.append(sout)
    return res

  def makeToTabString (self):  # TODO
    global className, cl
    res=[]
    sout = """
    public string  toTabOut() {
     StringBuilder  sb =  new StringBuilder();
    """
    for c in self.collons  :
        s = c.cname.lower();
        if (isLong(c)):
            continue;
        t = makeTabColumnFormat(c)
        s1 = '    sb.Append(%s  +"\t");    //  %s \n' % (t, c.comments)
        sout += s1
    sout += """
        return sb.ToString ();
    }
    """
    res.append(sout)

    return res


  def makeToString (self):
    global className, cl
    res=[]
    sout = """
    public override string  ToString() {
     StringBuilder  sb =  new StringBuilder();
     sb.Append("%s [");
    """%self.data_been_class
    sout += """
        sb.Append(" ]");
        return sb.ToString ();
    }
    """
    for c in self.collons  :
        s = c.cname.lower();
        if (isLong(c)):
            continue;
        t = makeTabColumnFormat(c)
        s1 = '      sb.Append("%s=" +%s +"; ");    //  %s \n' % (c.cname, t, "")

        # s1 = '      sb.Append("%s=" +%s +"; ");    //  %s \n' % (c.cname, t, c.comments)
        sout += s1
    res.append(sout)

    return res

  def makeFree(self):
    sout = """

    public void   free(){
      initData();
    }
   """
    res=[]
    res.append((sout))
    return res




  def makeEquals(self):  # TODO
    global className, cl
    res=[]
    sout=''
    st = """

    public  bool   Equals( $data_been_class other  ) {
    if(other==null) {
      return false;
    }

    """
    so = replaceTemplate(st, locals())
    so = map_raplace(so, self.__dict__)
    sout+=so
    for c in self.collons  :
      s = c.cname.lower();

      st = ''' if ($s != other.$s)  {
    return false;
    }
    '''
    so = replaceTemplate(st, locals())
    so = map_raplace(so, self.__dict__)

    sout += so
    sout += """
      return true;
    }
    """
    res.append(sout)
    return sout

  ##################################################


def makeDataBeen( tbl):
    ed = BeanClass(tbl)

    fname = output_dir + os.sep + tbl.tname.lower() + '_bean' + ".cs"


    body = listToText(ed.makeCassStart())
    body += listToText(ed.makeMembers())
    body += listToText(ed.makeProperties())
    body += listToText(ed.makeConstrictors())
    body += listToText(ed.makeCopy())
    # body += listToText(ed.makeCopyConstructor())
    body += listToText(ed.makeClear())
    body += listToText(ed.makeInitData())
    body += listToText(ed.makeBuildKey())
    body += listToText(ed.makeFree())
    body += listToText(ed.makeToString())
    # body += listToText(ed.makeFixData())
    # body += listToText(ed.makeToTabString())
    # body += listToText(ed.makeEquals())
    body +='''
        }
     }      '''
    print fname
    saveToFile(fname , body)

############################################################

def makDataBeanName(name):
  tbl = tables_list[name]
  output_dir+= os.sep + tbl.tname
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  testDupId(tbl)
  #  ed = BeanClass(tbl)
  makeDataBeen(tbl)


if __name__ == '__main__':
  tbl = tables_list[w_table_name]

  tbl.noDataFun=True
  output_dir+= os.sep + tbl.tname
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  testDupId(tbl)
  #  ed = BeanClass(tbl)
  makeDataBeen(tbl)
