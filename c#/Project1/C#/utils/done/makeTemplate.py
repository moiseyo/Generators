__author__ = 'mgo4943'
import setpath
from mod_file import *
setpath.addToPath('../.')
from package1 import *
setpath.addToPath(r'..\..\..\..\projects')
from SLA_tables import  *
from mod_file import  *
from Gizmo.dbAccess.common import *



from searchAndReplace import searchAndReplace

new_name="1"

path =r'C:\temp\1AT\editor'
targetPath =r"c:\temp\short"
main_file='editorSelect'

files=(
  '.aspx',
  '.aspx.cs',
  '.aspx.designer.cs',
)

class makeTemplate(BaseEditor):
    debug=False
    def __init__(self , __tbl={}):
 #     self.__start_it__=False
      super(makeTemplate, self ).__init__(__tbl)
      self.tbl=__tbl;
      self.collons=__tbl.__columns__
      tname= __tbl.tname.upper()
      self.tname=tname
			rep_word={}
			#self.control_name
			rep_word['pnl_edit_Triage_mail_t']=self.editPanel
			rep_word['Triage_mail_t_view']=tbl.editControl
			rep_word['GridViewPanel']=self.viewPanel
			rep_word['GridView1']=self.gridControl
			rep_word['Triage_mail_t_bean']= self.data_been_class
			rep_word['Triage_mail_t_dao']='${dao_class}'
			rep_word['\bdao\b']=self.dao_class
			rep_word['Default1']='${page_name}'
			rep_word['Default']='${page_name}'
			rep_word['trage_malt_t_view']='${tname}'
			rep_word['trage_malt_t_view']=self.data_been_class

			self.rep_word=rep_word



    def convertCode(self, ls):
      lu=[]
      for l in ls:
          if not l:
            lu.append(l)
            continue
          for key in self.rep_word:
            st = searchAndReplace(l,key ,self.rep_word[key])
            if st:
              l=st
          lu.append(l)
      return lu

    def makeFiles(self):

      for fn in files:
        fname = path + os.sep +  main_file + fn
        ls =readFileAsList(fname)
        lo=self.convertCode(ls)



if __name__ =="__main__":
  tbl = tables_list[w_table_name]

  m =makeTemplate(tbl)
  m.makeFiles()



