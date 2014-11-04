__author__ = 'mgo4943'

import setpath, re, sys
from mod_file import  *
setpath.addToPath(r'..\..\..\..\..\projects')
setpath.addToPath(r'..\.')
from SLA_tables import  *
from Gizmo.dbAccess.common import *


class makeSession(BaseEditor):
    debug=False
    def __init__(self , __tbl={}):
 #     self.__start_it__=False
      super(makeSession, self ).__init__(__tbl)
      self.tbl=__tbl;
      self.collons=__tbl.__columns__
      tname= __tbl.tname.upper()
      self.tname=tname

    def makeConst(self):
      for c in self.collons:
        n = c.cname
        print 'public static const  string %s = "%s"; ' %(n,n)
    def makeSlaAssing(self):
      for c in self.collons:
        n = c.cname.lower()
        print 'SLACommon._%s = user_info.%s; ' %(n,n)
    def makeProperties(self):

      body='''
      public static string  _${n_l}
        {
          get {
              HttpSessionState s= getCurrentHttpSession();

            return (string)s[$n];
        }
          set {
            HttpSessionState s = getCurrentHttpSession();
            s[$n] = value;

          }
        }
	'''
      for c in self.collons:
        n_l = c.cname.lower()
        n = c.cname
        out = replaceTemplate(body, updateDic(locals()))
        print out




if __name__ =="__main__":
  tbl = tables_list['SLA_USER']

  m =makeSession(tbl)
  m.makeConst()
  m.makeProperties()
  # m.makeSlaAssing()
