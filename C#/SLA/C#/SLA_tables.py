__author__ = 'mgo4943'
import setpath, sys
setpath.addToPath(r'..\..\..\..\projects')
from  mod_schema  import  *

project = "1AT"
# col_names = None
# cl = None
# tname = None
# tname_u = None
# className = None
# classNameUsage = None
# def_map = {}
# template = ""
tables_list={}
tbl=None

tblc_SLA_TEST_SLA_SEQ =( #  Wed Jun 11 08:08:11 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('SLA_SEQ',1,'SEQ_NAME_TEXT','VARCHAR2',20,None,None,'NOT NULL',None,1,'N/A'),
   TColumn('SLA_SEQ',2,'VAL','INTEGER',22,None,None,'NOT NULL','Sequence name',None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_SLA_SEQ)
tbl.setExtraAttrib('SEQ_NAME_TEXT','v_name','')
tbl.setExtraAttrib('VAL','v_name','')
tables_list['SLA_SEQ']=tbl

tblc_SLA_TEST_SLA_USER =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('SLA_USER',1,'USER_ID','VARCHAR2',20,None,None,'NOT NULL',None,1,None),
   TColumn('SLA_USER',2,'FIRST_NAME','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('SLA_USER',3,'LAST_NAME','VARCHAR2',30,None,None,'NULL',None,None,None),
   TColumn('SLA_USER',4,'EMAIL_ADDRESS','VARCHAR2',60,None,None,'NULL',None,None,None),
   TColumn('SLA_USER',5,'LAST_LOGIN_DATE','DATE',7,None,None,'NULL',None,None,None),
   TColumn('SLA_USER',6,'COMMENT_TEXT','VARCHAR2',100,None,None,'NULL',None,None,None),
   TColumn('SLA_USER',7,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('SLA_USER',8,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
   TColumn('SLA_USER',9,'SUPERVISOR_ID','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('SLA_USER',10,'ACTIVE_FLAG','VARCHAR2',1,None,None,'NULL',None,None,None),
)

tbl=CTable(tblc_SLA_TEST_SLA_USER)
tbl.setExtraAttrib('ACTIVE_FLAG',"dispType",'DD')
tbl.setExtraAttrib('USER_ID',"dispType",'DD')
tbl.setExtraAttrib('USER_ID',"lookup",'Y')
tables_list['SLA_USER']=tbl


tblc_SLA_TEST_SLA_ROLE =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('SLA_ROLE',1,'ROLE_NAME','VARCHAR2',30,None,None,'NOT NULL',None,1,None),
   TColumn('SLA_ROLE',2,'ROLE_DESCRIPTION','VARCHAR2',120,None,None,'NULL',None,None,None),
   TColumn('SLA_ROLE',3,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('SLA_ROLE',4,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
   TColumn('SLA_ROLE',5,'ACTIVE_FLAG','VARCHAR2',1,None,None,'NULL',None,None,None),
)

tbl=CTable(tblc_SLA_TEST_SLA_ROLE)
tables_list['SLA_ROLE']=tbl

tblc_SLA_TEST_USER_ROLE_XREF =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('USER_ROLE_XREF',1,'USER_ID','VARCHAR2',20,None,None,'NOT NULL',None,1,None),
   TColumn('USER_ROLE_XREF',2,'ROLE_NAME','VARCHAR2',30,None,None,'NOT NULL',None,2,None),
   TColumn('USER_ROLE_XREF',3,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('USER_ROLE_XREF',4,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
)

tbl=CTable(tblc_SLA_TEST_USER_ROLE_XREF)
tables_list['USER_ROLE_XREF']=tbl


tblc_SLA_TEST_CUSTOMER =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('CUSTOMER',1,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NOT NULL','CUSTOMER_NBR',1,None),
   TColumn('CUSTOMER',2,'CUSTOMER_H4','VARCHAR2',10,None,None,'NOT NULL',None,0,None),
   TColumn('CUSTOMER',3,'CUSTOMER_H1','VARCHAR2',10,None,None,'NULL',None,None,None),
   TColumn('CUSTOMER',4,'CUSTOMER_NAME','VARCHAR2',60,None,None,'NULL',None,None,None),
   TColumn('CUSTOMER',5,'ADDRESS1','VARCHAR2',40,None,None,'NULL',None,None,None),
   TColumn('CUSTOMER',6,'ADDRESS2','VARCHAR2',40,None,None,'NULL',None,None,None),
   TColumn('CUSTOMER',7,'CITY','VARCHAR2',40,None,None,'NULL',None,None,None),
   TColumn('CUSTOMER',8,'STATE','VARCHAR2',2,None,None,'NULL',None,None,None),
   TColumn('CUSTOMER',9,'ZIPCODE','VARCHAR2',10,None,None,'NULL',None,None,None),
   TColumn('CUSTOMER',10,'COUNTRY_CD','VARCHAR2',2,None,None,'NULL',None,None,None),
   TColumn('CUSTOMER',11,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('CUSTOMER',12,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
)


tbl=CTable(tblc_SLA_TEST_CUSTOMER)
tbl.generate_auto_number='CUSTOMER_NBR'
tbl.setExtraAttrib('COUNTRY_CD',"dispType",'DD')
tbl.setExtraAttrib('STATE',"dispType",'DD')
tbl.setExtraAttrib('COUNTRY_CD',"lookup",'Y')
tbl.setExtraAttrib('CUSTOMER_H4','is_there_name','1')
tables_list['CUSTOMER']=tbl

tblc_SLA_TEST_PRODUCT =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('PRODUCT',1,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL',None,1,None),
   TColumn('PRODUCT',2,'PRODUCT_NAME','VARCHAR2',20,None,None,'NOT NULL',None,0,None),
   TColumn('PRODUCT',3,'DESCRIPTION','VARCHAR2',60,None,None,'NULL',None,None,None),
   TColumn('PRODUCT',4,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('PRODUCT',5,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
)

tbl=CTable(tblc_SLA_TEST_PRODUCT)

tables_list['PRODUCT']=tbl
tbl.generate_auto_number='PRODUCT_NBR'
tblc_SLA_TEST_COUNTRY =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('COUNTRY',1,'COUNTRY_CD','VARCHAR2',2,None,None,'NOT NULL',None,1,None),
   TColumn('COUNTRY',2,'COUNTRY_NAME','VARCHAR2',50,None,None,'NOT NULL',None,None,None),
)

tbl=CTable(tblc_SLA_TEST_COUNTRY)
tables_list['COUNTRY']=tbl

tblc_SLA_TEST_COUNTRY_CLASS_XREF =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('COUNTRY_CLASS_XREF',1,'COUNTRY_CD','VARCHAR2',2,None,None,'NOT NULL',None,1,None),
   TColumn('COUNTRY_CLASS_XREF',2,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL','PRODUCT_NBR',2,None),
   TColumn('COUNTRY_CLASS_XREF',3,'COUNTRY_CLASS','VARCHAR2',1,None,None,'NOT NULL',None,None,None),
   TColumn('COUNTRY_CLASS_XREF',4,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('COUNTRY_CLASS_XREF',5,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),

)

tbl=CTable(tblc_SLA_TEST_COUNTRY_CLASS_XREF)
tbl.setExtraAttrib('COUNTRY_CD',"dispType",'DD')
tbl.setExtraAttrib('PRODUCT_NBR',"dispType",'DD')
tbl.setExtraAttrib('COUNTRY_CLASS',"dispType",'DD')
tbl.setExtraAttrib('COUNTRY_CD',"lookup",'Y')
tbl.setExtraAttrib('PRODUCT_NBR',"lookup",'Y')
tbl.setExtraAttrib('COUNTRY_CLASS',"lookup",'Y')


tables_list['COUNTRY_CLASS_XREF']=tbl




# tblc_SLA_TEST_SITE =(
#    #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
#    TColumn('SITE',1,'SITE_NBR','VARCHAR2',20,None,None,'NOT NULL',None,0,None),
#    TColumn('SITE',2,'CUSTOMER_H6','VARCHAR2',10,None,None,'NOT NULL',None,None,None),
#    TColumn('SITE',3,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NOT NULL',None,1,None),
#    TColumn('SITE',4,'SITE_NUA','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('SITE',5,'SITE_NAME','VARCHAR2',30,None,None,'NOT NULL',None,2,None),
#    TColumn('SITE',6,'ADDRESS1','VARCHAR2',40,None,None,'NULL',None,None,None),
#    TColumn('SITE',7,'ADDRESS2','VARCHAR2',40,None,None,'NULL',None,None,None),
#    TColumn('SITE',8,'CITY','VARCHAR2',40,None,None,'NULL',None,None,None),
#    TColumn('SITE',9,'STATE','VARCHAR2',2,None,None,'NULL',None,None,None),
#    TColumn('SITE',10,'ZIPCODE','VARCHAR2',10,None,None,'NULL',None,None,None),
#    TColumn('SITE',11,'COUNTRY_CD','VARCHAR2',2,None,None,'NULL',None,None,None),
#    TColumn('SITE',12,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('SITE',13,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
# )

tblc_SLA_TEST_SITE =( #  Tue Jun 03 06:28:31 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('SITE',1,'SITE_NBR','VARCHAR2',10,None,None,'NOT NULL','Uniquely identifies the SITE record',1,'N/A'),
   TColumn('SITE',2,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the customer to which the Site belongs - originates from the CUSTOMER table',0,'N/A'),
   TColumn('SITE',3,'SITE_NAME','VARCHAR2',30,None,None,'NOT NULL','Site Name',0,'N/A'),
   TColumn('SITE',4,'ADDRESS1','VARCHAR2',40,None,None,'NULL','Site Address - Line 1',None,'N/A'),
   TColumn('SITE',5,'ADDRESS2','VARCHAR2',40,None,None,'NULL','Site Address - Line 2',None,'N/A'),
   TColumn('SITE',6,'CITY','VARCHAR2',40,None,None,'NULL','Site City',None,'N/A'),
   TColumn('SITE',7,'STATE','VARCHAR2',2,None,None,'NULL','Two-character abbreviation of the Site State',None,'N/A'),
   TColumn('SITE',8,'ZIPCODE','VARCHAR2',10,None,None,'NULL','Site Zip code',None,'N/A'),
   TColumn('SITE',9,'COUNTRY_CD','VARCHAR2',2,None,None,'NULL','Two-character abbreviation of the Site country - originates from the COUNTRY table ',None,'N/A'),
   TColumn('SITE',10,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('SITE',11,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent update to this record',None,'N/A'),
)
tbl=CTable(tblc_SLA_TEST_SITE)
tbl.generate_auto_number= 'SITE_NBR'
tbl.setExtraAttrib('COUNTRY_CD',"dispType",'DD')
tbl.setExtraAttrib('CUSTOMER_NBR',"dispType",'DD')
tbl.setExtraAttrib('STATE',"dispType",'DD')

tbl.setExtraAttrib('CUSTOMER_NBR','is_there_name','1')
tbl.setExtraAttrib('SITE_NAME','is_there_name','1')

tables_list['SITE']=tbl



tblc_SLA_TEST_SITE_PRODUCT_XREF =( #  Tue Jun 03 12:46:36 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('SITE_PRODUCT_XREF',1,'SITE_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the site to which the record applies - originates from the SITE table',1,'N/A'),
   TColumn('SITE_PRODUCT_XREF',2,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the product to which the record applies - originates from the PRODUCT table',2,'N/A'),
   TColumn('SITE_PRODUCT_XREF',3,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NULL','Identifies the customer to which the record applies - originates from the CUSTOMER table',None,'N/A'),
   TColumn('SITE_PRODUCT_XREF',4,'CUSTOMER_H6','VARCHAR2',10,None,None,'NULL','Customer H6 number',None,'N/A'),
   TColumn('SITE_PRODUCT_XREF',5,'SITE_PRODUCT_NUA','VARCHAR2',20,None,None,'NULL','The Network Universal Address of the Site for this Product',None,'N/A'),
   TColumn('SITE_PRODUCT_XREF',6,'SPRINT_POP','VARCHAR2',20,None,None,'NULL','Nearest Sprint POP Facility Location - used for Homing',None,'N/A'),
   TColumn('SITE_PRODUCT_XREF',7,'ACCESS_TYPE','VARCHAR2',20,None,None,'NULL','Specifies the type of access at the site for this product',None,'N/A'),
   TColumn('SITE_PRODUCT_XREF',8,'PORT_SPEED','VARCHAR2',20,None,None,'NULL','Specifies the port speed at this site for this product',None,'N/A'),
   TColumn('SITE_PRODUCT_XREF',9,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('SITE_PRODUCT_XREF',10,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent update to this record',None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_SITE_PRODUCT_XREF)
tbl.setExtraAttrib('SITE_NBR',"dispType",'DD')
tbl.setExtraAttrib('PRODUCT_NBR',"dispType",'DD')
tbl.setExtraAttrib('ACCESS_TYPE',"dispType",'DD')
tbl.setExtraAttrib('CUSTOMER_NBR',"dispType",'DD')
tbl.setExtraAttrib('SPRINT_POP',"dispType",'DD')

tbl.setExtraAttrib('SITE_NBR',"lookup",'Y')
tbl.setExtraAttrib('PRODUCT_NBR',"lookup",'Y')
tbl.setExtraAttrib('CUSTOMER_NBR',"lookup",'Y')
tbl.setExtraAttrib('ACCESS_TYPE',"lookup",'Y')
tbl.setExtraAttrib('SPRINT_POP',"lookup",'Y')


# tbl.setExtraAttrib('CUSTOMER_NBR','is_there_name','1')
tbl.setExtraAttrib('PRODUCT_NBR','is_there_name','1')
tbl.setExtraAttrib('SITE_PRODUCT_NUA','is_there_name','1')
# tbl.setExtraAttrib('SITE_NBR','is_there_name','1')

tables_list['SITE_PRODUCT_XREF']=tbl

tblc_SLA_TEST_USER_ACL_XREF =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('USER_ACL_XREF',1,'USER_ID','VARCHAR2',20,None,None,'NOT NULL',None,1,None),
   TColumn('USER_ACL_XREF',2,'ACL_TYPE','VARCHAR2',20,None,None,'NOT NULL',None,2,None),
   TColumn('USER_ACL_XREF',3,'CUSTOMER_NBR','VARCHAR2',20,None,None,'NULL',None,3,None),
   TColumn('USER_ACL_XREF',4,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('USER_ACL_XREF',5,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
)

tbl=CTable(tblc_SLA_TEST_USER_ACL_XREF)
tbl.setExtraAttrib('USER_ID',"dispType",'DD')
tbl.setExtraAttrib('ACL_TYPE',"dispType",'DD')
tbl.setExtraAttrib('ACL_TYPE',"check_dd_size",'Y')
tbl.setExtraAttrib('CUSTOMER_NBR',"dispType",'DD')
tbl.setExtraAttrib('CUSTOMER_NBR',"check_dd_size",'DD')
tbl.setExtraAttrib('USER_ID',"lookup",'Y')
tbl.setExtraAttrib('ACL_TYPE',"lookup",'Y')
tbl.setExtraAttrib('CUSTOMER_NBR',"lookup",'Y')

tables_list['USER_ACL_XREF']=tbl


tblc_SLA_TEST_ACCESS_TYPE =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('ACCESS_TYPE',1,'ACCESS_TYPE','VARCHAR2',20,None,None,'NOT NULL',None,1,None),
   TColumn('ACCESS_TYPE',2,'DESCRIPTION','VARCHAR2',80,None,None,'NULL',None,None,None),
   TColumn('ACCESS_TYPE',3,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('ACCESS_TYPE',4,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
)

tbl=CTable(tblc_SLA_TEST_ACCESS_TYPE)
tables_list['ACCESS_TYPE']=tbl

# tblc_SLA_TEST_COMMITMENT_SITE_AVAILABILITY =(
#    #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
#    TColumn('COMMITMENT_SITE_AVAILABILITY',1,'PRODUCT_NBR','VARCHAR2',20,None,None,'NOT NULL',None,1,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',2,'ACCESS_TYPE','VARCHAR2',20,None,None,'NOT NULL',None,3,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',3,'CUSTOMER_NBR','VARCHAR2',20,None,None,'NOT NULL',None,2,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',4,'COMMITMENT_METRIC','VARCHAR2',20,None,None,'NOT NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',5,'INITL_NTVL_START_VALUE','VARCHAR2',20,None,None,'NOT NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',6,'INITL_NTVL_END_VALUE','VARCHAR2',20,None,None,'NOT NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',7,'INITL_NTVL_PORT_CREDIT_PCT','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',8,'INITL_NTVL_LOC_LOOP_CREDIT_PCT','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',9,'ADDL_NTVL_START_VALUE','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',10,'ADDL_NTVL_DURATION_VALUE','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',11,'ADDL_NTVL_PORT_CREDIT_PCT','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',12,'ADDL_NTVL_LOC_LOOP_CREDIT_PCT','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',13,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_AVAILABILITY',14,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
# )
#
# tbl=CTable(tblc_SLA_TEST_COMMITMENT_SITE_AVAILABILITY)
#
# tbl.setExtraAttrib('PRODUCT_NBR',"dispType",'DD')
# tbl.setExtraAttrib('ACCESS_TYPE',"dispType",'DD')
# tbl.setExtraAttrib('CUSTOMER_NBR',"dispType",'DD')
# tbl.setExtraAttrib('PRODUCT_NBR',"lookup",'Y')
# tbl.setExtraAttrib('ACCESS_TYPE',"lookup",'Y')
# tbl.setExtraAttrib('CUSTOMER_NBR',"lookup",'Y')
#
#
# tables_list['COMMITMENT_SITE_AVAILABILITY']=tbl
#
# tblc_SLA_TEST_COMMITMENT_SITE_INSTALL =(
#    #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
#    TColumn('COMMITMENT_SITE_INSTALL',1,'PRODUCT_NBR','VARCHAR2',20,None,None,'NOT NULL',None,1,None),
#    TColumn('COMMITMENT_SITE_INSTALL',2,'CUSTOMER_NBR','VARCHAR2',20,None,None,'NOT NULL',None,2,None),
#    TColumn('COMMITMENT_SITE_INSTALL',3,'CIRCUIT_TYPE','VARCHAR2',20,None,None,'NOT NULL',None,3,None),
#    TColumn('COMMITMENT_SITE_INSTALL',4,'COMMITMENT_INTVL_TEXT','VARCHAR2',40,None,None,'NOT NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_INSTALL',5,'COMMITMENT_METRIC','VARCHAR2',20,None,None,'NOT NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_INSTALL',6,'CREDIT_PCT','VARCHAR2',20,None,None,'NOT NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_INSTALL',7,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_INSTALL',8,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
# )
#
# tbl=CTable(tblc_SLA_TEST_COMMITMENT_SITE_INSTALL)
# tbl.setExtraAttrib('PRODUCT_NBR',"dispType",'DD')
# tbl.setExtraAttrib('CIRCUIT_TYPE',"dispType",'DD')
# tbl.setExtraAttrib('CUSTOMER_NBR',"dispType",'DD')
# tbl.setExtraAttrib('PRODUCT_NBR',"lookup",'Y')
# tbl.setExtraAttrib('CIRCUIT_TYPE',"lookup",'Y')
# tbl.setExtraAttrib('CUSTOMER_NBR',"lookup",'Y')
#
#
# tables_list['COMMITMENT_SITE_INSTALL']=tbl
#
#
#
# tblc_SLA_TEST_COMMITMENT_SITE_MTTR =(
#    #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
#    TColumn('COMMITMENT_SITE_MTTR',1,'PRODUCT_NBR','VARCHAR2',20,None,None,'NOT NULL',None,1,None),
#    TColumn('COMMITMENT_SITE_MTTR',2,'SERVICE_CLASS','VARCHAR2',1,None,None,'NOT NULL',None,3,None),
#    TColumn('COMMITMENT_SITE_MTTR',3,'DISPATCH_TYPE','VARCHAR2',1,None,None,'NOT NULL',None,4,None),
#    TColumn('COMMITMENT_SITE_MTTR',4,'CUSTOMER_NBR','VARCHAR2',20,None,None,'NOT NULL',None,2,None),
#    TColumn('COMMITMENT_SITE_MTTR',5,'COMMITMENT_METRIC','VARCHAR2',20,None,None,'NOT NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_MTTR',6,'CREDIT_PCT','VARCHAR2',20,None,None,'NOT NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_MTTR',7,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
#    TColumn('COMMITMENT_SITE_MTTR',8,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
# )
#
# tbl=CTable(tblc_SLA_TEST_COMMITMENT_SITE_MTTR)
#
# tbl.setExtraAttrib('PRODUCT_NBR',"dispType",'DD')
# tbl.setExtraAttrib('SERVICE_CLASS',"dispType",'DD')
# tbl.setExtraAttrib('DISPATCH_TYPE',"dispType",'DD')
# tbl.setExtraAttrib('CUSTOMER_NBR',"dispType",'DD')
#
# tbl.setExtraAttrib('PRODUCT_NBR',"lookup",'Y')
# tbl.setExtraAttrib('SERVICE_CLASS',"lookup",'Y')
# tbl.setExtraAttrib('CUSTOMER_NBR',"lookup",'Y')
# tbl.setExtraAttrib('DISPATCH_TYPE',"lookup",'Y')
#
#
# tables_list['COMMITMENT_SITE_MTTR']=tbl





tblc_SLA_TEST_SLA_GLOSSARY =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('SLA_GLOSSARY',1,'TERM_NBR','VARCHAR2',10,None,None,'NOT NULL',None,None,None),
   TColumn('SLA_GLOSSARY',2,'TERM_CLASS','VARCHAR2',20,None,None,'NOT NULL',None,1,None),
   TColumn('SLA_GLOSSARY',3,'TERM_ABBREV','VARCHAR2',20,None,None,'NOT NULL',None,2,None),
   TColumn('SLA_GLOSSARY',4,'DESCRIPTION','VARCHAR2',120,None,None,'NOT NULL',None,None,None),
   TColumn('SLA_GLOSSARY',5,'ACTIVE_FLAG','VARCHAR2',1,None,None,'NOT NULL',None,None,None),
   TColumn('SLA_GLOSSARY',6,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,None),
   TColumn('SLA_GLOSSARY',7,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,None),
)
tbl=CTable(tblc_SLA_TEST_SLA_GLOSSARY)
tbl.setExtraAttrib('TERM_CLASS',"dispType",'DD')
tbl.setExtraAttrib('TERM_CLASS',"lookup",'Y')

tbl.setExtraAttrib('ACTIVE_FLAG',"dispType",'DD')
tbl.setExtraAttrib('ACTIVE_FLAG',"lookup",'Y')

tbl.setExtraAttrib('TERM_ABBREV',"lookup",'Y')
tbl.setExtraAttrib('TERM_ABBREV',"lookup",'Y')
tbl.setExtraAttrib('DESCRIPTION',"lookup",'Y')

tbl.setExtraAttrib('TERM_CLASS','is_there_name','1')
tbl.setExtraAttrib('TERM_ABBREV','is_there_name','1')



tables_list['SLA_GLOSSARY']=tbl



# tblc_SLA_TEST_TICKET_DETAIL =( #  Wed Apr 16 09:22:55 CDT 2014
#    #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
#    TColumn('TICKET_DETAIL',1,'TICKET_NBR','VARCHAR2',20,None,None,'NOT NULL',None,1,'N/A'),
#    TColumn('TICKET_DETAIL',2,'TICKET_OPEN_DT','DATE',7,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',3,'CUSTOMER_H6','VARCHAR2',10,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',4,'SITE_NBR','VARCHAR2',20,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',5,'PRODUCT_NBR','VARCHAR2',10,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',6,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',7,'MEASUREMENT_PERIOD','VARCHAR2',6,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',8,'SPRINT_ACTION','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',9,'LEC_ACTION','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',10,'DISPATCH_DURATION','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',11,'NONDISPATCH_DURATION','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',12,'TICKET_MTTR','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',13,'TICKET_CUSTOMER_NME','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',14,'TICKET_ADDRESS','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',15,'TICKET_CITY','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',16,'TICKET_STATE','VARCHAR2',2,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',17,'TICKET_CLEAR_REMARKS','VARCHAR2',140,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',18,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',19,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,'N/A'),
# )
#
# tblc_SLA_TEST_TICKET_DETAIL =( #  Mon Apr 21 15:22:10 CDT 2014
#    #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
#    TColumn('TICKET_DETAIL',1,'TICKET_NBR','VARCHAR2',20,None,None,'NOT NULL',None,1,'N/A'),
#    TColumn('TICKET_DETAIL',2,'TICKET_OPEN_DT','DATE',7,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',3,'CUSTOMER_H6','VARCHAR2',10,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',4,'SITE_NBR','VARCHAR2',10,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',5,'PRODUCT_NBR','VARCHAR2',10,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',6,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',7,'MEASUREMENT_PERIOD','VARCHAR2',6,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',8,'SPRINT_ACTION','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',9,'LEC_ACTION','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',10,'DISPATCH_DURATION','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',11,'NONDISPATCH_DURATION','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',12,'TICKET_MTTR','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',13,'TICKET_CUSTOMER_NME','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',14,'TICKET_ADDRESS','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',15,'TICKET_CITY','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',16,'TICKET_STATE','VARCHAR2',2,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',17,'TICKET_CLEAR_REMARKS','VARCHAR2',140,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',18,'APPLICABLE_FLAG','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',19,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',20,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,'N/A'),
# )
# tblc_SLA_TEST_TICKET_DETAIL =( #  Tue Apr 22 07:18:54 CDT 2014
#    #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
#    TColumn('TICKET_DETAIL',1,'TICKET_NBR','VARCHAR2',20,None,None,'NOT NULL',None,1,'N/A'),
#    TColumn('TICKET_DETAIL',2,'TICKET_OPEN_DT','DATE',7,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',3,'CUSTOMER_H6','VARCHAR2',10,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',4,'SITE_NBR','VARCHAR2',10,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',5,'PRODUCT_NBR','VARCHAR2',10,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',6,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',7,'MEASUREMENT_PERIOD','VARCHAR2',6,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',8,'SPRINT_ACTION','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',9,'LEC_ACTION','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',10,'DISPATCH_DURATION','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',11,'NONDISPATCH_DURATION','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',12,'TICKET_MTTR','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',13,'TICKET_CUSTOMER_NME','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',14,'TICKET_ADDRESS','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',15,'TICKET_CITY','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',16,'TICKET_STATE','VARCHAR2',2,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',17,'TICKET_CLEAR_REMARKS','VARCHAR2',140,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',18,'TICKET_STATUS','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',19,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',20,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,'N/A'),
# )


# tblc_SLA_TEST_TICKET_DETAIL =( #  Tue Apr 22 13:58:52 CDT 2014
#    #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
#    TColumn('TICKET_DETAIL',1,'TICKET_NBR','VARCHAR2',20,None,None,'NOT NULL',None,1,'N/A'),
#    TColumn('TICKET_DETAIL',2,'TICKET_OPEN_DT','DATE',7,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',3,'CUSTOMER_H6','VARCHAR2',10,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',4,'SITE_NBR','VARCHAR2',10,None,None,'NOT NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',5,'PRODUCT_NBR','VARCHAR2',10,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',6,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',7,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',8,'MEASUREMENT_PERIOD','VARCHAR2',6,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',9,'SPRINT_ACTION','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',10,'LEC_ACTION','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',11,'DISPATCH_DURATION','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',12,'NONDISPATCH_DURATION','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',13,'TICKET_MTTR','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',14,'TICKET_CUSTOMER_NME','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',15,'TICKET_ADDRESS','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',16,'TICKET_CITY','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',17,'TICKET_STATE','VARCHAR2',2,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',18,'TICKET_CLEAR_REMARKS','VARCHAR2',140,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',19,'TICKET_STATUS','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',20,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
#    TColumn('TICKET_DETAIL',21,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,'N/A'),
# )

tblc_SLA_TEST_TICKET_DETAIL =( #  Mon May 05 13:41:07 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('TICKET_DETAIL',1,'TICKET_NBR','VARCHAR2',20,None,None,'NOT NULL','Uniquely identifies the TICKET_DETAIL record',1,'N/A'),
   TColumn('TICKET_DETAIL',2,'TICKET_OPEN_DT','DATE',7,None,None,'NOT NULL','Specifies when the ticket was opened',None,'N/A'),
   TColumn('TICKET_DETAIL',3,'CUSTOMER_H6','VARCHAR2',10,None,None,'NOT NULL','Identifies the customer H6 to which the record applies',None,'N/A'),
   TColumn('TICKET_DETAIL',4,'SITE_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the site to which the record applies - originates from the SITE table',None,'N/A'),
   TColumn('TICKET_DETAIL',5,'PRODUCT_NBR','VARCHAR2',10,None,None,'NULL','Identifies the product to which the record applies - originates from the PRODUCT table',None,'N/A'),
   TColumn('TICKET_DETAIL',6,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NULL','Identifies the customer to which the record applies - originates from the CUSTOMER table',None,'N/A'),
   TColumn('TICKET_DETAIL',7,'MEASUREMENT_PERIOD','VARCHAR2',6,None,None,'NULL','Measurement Period in which this record should apply - normally formatted as YYYYMM ',None,'N/A'),
   TColumn('TICKET_DETAIL',8,'SPRINT_ACTION','VARCHAR2',1,None,None,'NULL','Y/N Flag indicating whether corrective action was performed by Sprint to address this ticket',None,'N/A'),
   TColumn('TICKET_DETAIL',9,'LEC_ACTION','VARCHAR2',1,None,None,'NULL','Y/N Flag indicating whether corrective action was performed by the LEC to address this ticket',None,'N/A'),
   TColumn('TICKET_DETAIL',10,'DISPATCH_DURATION','VARCHAR2',20,None,None,'NULL','Duration of time for Non-Dispatch or SLA eligible Sprint outage',None,'N/A'),
   TColumn('TICKET_DETAIL',11,'NONDISPATCH_DURATION','VARCHAR2',20,None,None,'NULL','Duration of time for Dispatch or SLA eligible LEC outage',None,'N/A'),
   TColumn('TICKET_DETAIL',12,'TICKET_MTTR','VARCHAR2',20,None,None,'NULL','Future Use',None,'N/A'),
   TColumn('TICKET_DETAIL',13,'TICKET_CUSTOMER_NME','VARCHAR2',40,None,None,'NULL','Future Use',None,'N/A'),
   TColumn('TICKET_DETAIL',14,'TICKET_ADDRESS','VARCHAR2',40,None,None,'NULL','Future Use',None,'N/A'),
   TColumn('TICKET_DETAIL',15,'TICKET_CITY','VARCHAR2',40,None,None,'NULL','Future Use',None,'N/A'),
   TColumn('TICKET_DETAIL',16,'TICKET_STATE','VARCHAR2',2,None,None,'NULL','Future Use',None,'N/A'),
   TColumn('TICKET_DETAIL',17,'TICKET_CLEAR_REMARKS','VARCHAR2',140,None,None,'NULL','Ticket Summary Description',None,'N/A'),
   TColumn('TICKET_DETAIL',18,'TICKET_STATUS','VARCHAR2',20,None,None,'NULL','Indicates the workflow state of the TICKET_DETAIL record',None,'N/A'),
   TColumn('TICKET_DETAIL',19,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('TICKET_DETAIL',20,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent update to this record',None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_TICKET_DETAIL)
tbl.bean_name="ticket_bean"
tbl.setExtraAttrib('TICKET_STATE',"dispType",'DD')
tbl.setExtraAttrib('TICKET_STATE',"lookup",'Y')
tbl.setExtraAttrib('SPRINT_ACTION',"dispType",'DD')
tbl.setExtraAttrib('LEC_ACTION',"dispType",'DD')

tbl.setExtraAttrib('CUSTOMER_H6',"lookup",'Y')
tbl.setExtraAttrib('MEASUREMENT_PERIOD',"lookup",'Y')

tbl.setExtraAttrib('SPRINT_ACTION',"lookup",'Y')
tbl.setExtraAttrib('LEC_ACTION',"lookup",'Y')

tbl.setExtraAttrib('PRODUCT_NBR',"lookup",'Y')
tbl.setExtraAttrib('PRODUCT_NBR',"dispType",'DD')

tbl.setExtraAttrib('SITE_NBR',"lookup",'Y')
tbl.setExtraAttrib('SITE_NBR',"dispType",'DD')


# tbl.setExtraAttrib('COMMITMENT_NBR','lookup','Y')
# tbl.setExtraAttrib('COMMITMENT_NBR','dispType','DD')
#
tbl.setExtraAttrib('TICKET_STATUS','lookup','Y')
tbl.setExtraAttrib('TICKET_STATUS','dispType','DD')


tables_list['TICKET_DETAIL']=tbl

##########################################################################################

tblc_SLA_TEST_PRODUCT_COMMITMENT_XREF =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('PRODUCT_COMMITMENT_XREF',1,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL',None,1,'N/A'),
   TColumn('PRODUCT_COMMITMENT_XREF',2,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NOT NULL',None,2,'N/A'),
   TColumn('PRODUCT_COMMITMENT_XREF',3,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
   TColumn('PRODUCT_COMMITMENT_XREF',4,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_PRODUCT_COMMITMENT_XREF)
tbl.setExtraAttrib('PRODUCT_NBR','dispType','DD')
tbl.setExtraAttrib('COMMITMENT_NBR','dispType','DD')

tbl.setExtraAttrib('PRODUCT_NBR','lookup','Y')
tbl.setExtraAttrib('COMMITMENT_NBR','lookup','Y')
tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')
tables_list['PRODUCT_COMMITMENT_XREF']=tbl

###################################################################

tblc_SLA_TEST_COMMITMENT =( #  Wed Apr 23 10:01:04 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('COMMITMENT',1,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NOT NULL','Uniquely identifies the COMMITMENT record',1,'N/A'),
   TColumn('COMMITMENT',2,'COMMITMENT_NAME','VARCHAR2',40,None,None,'NOT NULL','Descriptive name of the Commitment',None,'N/A'),
   TColumn('COMMITMENT',3,'DESCRIPTION','VARCHAR2',30,None,None,'NULL','Detailed Description of the Commitment',None,'N/A'),
   TColumn('COMMITMENT',4,'DETAIL_TYPE','VARCHAR2',20,None,None,'NOT NULL','Detail type information for the COMMITMENT record - used when optional parameters are required to describe the commitment',None,'N/A'),
   TColumn('COMMITMENT',5,'SUBDETAIL_TYPE','VARCHAR2',20,None,None,'NOT NULL','Subdetail type information for the COMMITMENT record - used when optional parameters are required to describe the commitment',None,'N/A'),
   TColumn('COMMITMENT',6,'AGGREGATE_FLAG','VARCHAR2',1,None,None,'NOT NULL','Y/N Flag used to specify whether this COMMITMENT record describes a commitment that aggregates issues over a measurement period to determine a violation.',None,'N/A'),
   TColumn('COMMITMENT',7,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('COMMITMENT',8,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent updaet to this record',None,'N/A'),
)


tbl=CTable(tblc_SLA_TEST_COMMITMENT)
tbl.generate_auto_number=True

tbl.setExtraAttrib('DETAIL_TYPE','lookup','Y')
tbl.setExtraAttrib('DETAIL_TYPE','dispType','DD')

tbl.setExtraAttrib('SUBDETAIL_TYPE','lookup','Y')
tbl.setExtraAttrib('SUBDETAIL_TYPE','dispType','DD')

tbl.setExtraAttrib('AGGREGATE_FLAG','lookup','Y')
tbl.setExtraAttrib('AGGREGATE_FLAG','dispType','DD')


tables_list['COMMITMENT']=tbl
#################################################################
tblc_SLA_TEST_CUSTOMER_COMMITMENT_XREF =(
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('CUSTOMER_COMMITMENT_XREF',1,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NOT NULL',None,1,'N/A'),
   TColumn('CUSTOMER_COMMITMENT_XREF',2,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL',None,2,'N/A'),
   TColumn('CUSTOMER_COMMITMENT_XREF',3,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NOT NULL',None,3,'N/A'),
   TColumn('CUSTOMER_COMMITMENT_XREF',4,'CUSTOM_SLA','VARCHAR2',1,None,None,'NULL',None,None,'N/A'),
   TColumn('CUSTOMER_COMMITMENT_XREF',5,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
   TColumn('CUSTOMER_COMMITMENT_XREF',6,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_CUSTOMER_COMMITMENT_XREF)
tbl.setExtraAttrib('CUSTOMER_NBR','lookup','Y')
tbl.setExtraAttrib('PRODUCT_NBR','lookup','Y')
tbl.setExtraAttrib('COMMITMENT_NBR','lookup','Y')
tbl.setExtraAttrib('CUSTOM_SLA','lookup','Y')

tbl.setExtraAttrib('CUSTOMER_NBR','dispType','DD')
tbl.setExtraAttrib('PRODUCT_NBR','dispType','DD')
tbl.setExtraAttrib('COMMITMENT_NBR','dispType','DD')
tbl.setExtraAttrib('CUSTOM_SLA','dispType','DD')
tables_list['CUSTOMER_COMMITMENT_XREF']=tbl

###############################################################################


tblc_SLA_TEST_EXCLUSION =( #  Tue Apr 22 10:37:14 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('EXCLUSION',1,'EXCLUSION_NBR','VARCHAR2',10,None,None,'NULL',None,1,'N/A'),
   TColumn('EXCLUSION',2,'EXCLUSION_NAME','VARCHAR2',40,None,None,'NULL',None,None,'N/A'),
   TColumn('EXCLUSION',3,'DESCRIPTION','VARCHAR2',400,None,None,'NULL',None,None,'N/A'),
   TColumn('EXCLUSION',4,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
   TColumn('EXCLUSION',5,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_EXCLUSION)
tbl.generate_auto_number=1
tbl.setExtraAttrib('EXCLUSION_NBR','v_name','')
tbl.setExtraAttrib('EXCLUSION_NAME','v_name','')
tbl.setExtraAttrib('DESCRIPTION','v_name','')
tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')
tables_list['EXCLUSION']=tbl


#########################################

tblc_SLA_TEST_PRODUCT_EXCLUSION_XREF =( #  Wed Apr 23 08:25:20 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('PRODUCT_EXCLUSION_XREF',1,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the product to which the record applies - originates from the PRODUCT table',1,'N/A'),
   TColumn('PRODUCT_EXCLUSION_XREF',2,'EXCLUSION_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the exlusion to which the record applies - originates from the EXCLUSION table',2,'N/A'),
   TColumn('PRODUCT_EXCLUSION_XREF',3,'DETAIL_REQ_FLAG','VARCHAR2',1,None,None,'NOT NULL','Y/N Flag used to specify whether this reocrd describes a product-exclusion combination that requires additional details to be entered when used',None,'N/A'),
   TColumn('PRODUCT_EXCLUSION_XREF',4,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('PRODUCT_EXCLUSION_XREF',5,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent updat to this record',None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_PRODUCT_EXCLUSION_XREF)
tbl.generate_auto_number=1000000
tbl.setExtraAttrib('PRODUCT_NBR','v_name','')
tbl.setExtraAttrib('EXCLUSION_NBR','v_name','')
tbl.setExtraAttrib('DETAIL_REQ_FLAG','v_name','')
tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')
tables_list['PRODUCT_EXCLUSION_XREF']=tbl
##############################################################################
##############################################################################
tblc_SLA_TEST_COMMITMENT_DETAIL_o =( #  Wed Apr 23 09:07:28 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('COMMITMENT_DETAIL',1,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the commitment to which the COMMITMENT_DETAIL record applies - originates from the COMMITMENT table',1,'N/A'),
   TColumn('COMMITMENT_DETAIL',2,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the customer to which the record applies - originates from the CUSTOMER table',2,'N/A'),
   TColumn('COMMITMENT_DETAIL',3,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the product to which the record applies - originates from the PRODUCT table',3,'N/A'),
   TColumn('COMMITMENT_DETAIL',4,'DETAIL_TYPE_SELECT','VARCHAR2',20,None,None,'NOT NULL','Detail selected for the COMMITMENT_DETAIL record - used when optional detail type information is required and is driven by the DETAIL_TYPE from the COMMITMENT table',4,'N/A'),
   TColumn('COMMITMENT_DETAIL',5,'SUBDETAIL_TYPE_SELECT','VARCHAR2',20,None,None,'NOT NULL','Subdetail selected for the COMMITMENT_DETAIL record - used when optional subdetail type information is required and is driven by the SUBDETAIL_TYPE from the COMMITMENT table',5,'N/A'),
   TColumn('COMMITMENT_DETAIL',6,'COMMITMENT_TEXT','VARCHAR2',20,None,None,'NOT NULL','Text string used to specify the Commitment',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',7,'COMMITMENT_METRIC','VARCHAR2',20,None,None,'NULL','Metric used to specify the Commitment',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',8,'METRIC_UNIT','VARCHAR2',20,None,None,'NOT NULL','Unit of measure that applies to the metric',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',9,'CREDIT_TYPE','VARCHAR2',20,None,None,'NOT NULL','Credit type to apply to the credit amount if commitment is violated - like flat rate or percentage MRC/NRC',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',10,'CREDIT_AMOUNT','VARCHAR2',20,None,None,'NULL','Amount of credit to be issued if commitment is violated',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',11,'CREDIT_CAP_TYPE','VARCHAR2',20,None,None,'NOT NULL','Credit type to apply to the Cap Amount if commitment is violated - like flat rate or percentage MRC/NRC',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',12,'CREDIT_CAP_AMOUNT','VARCHAR2',20,None,None,'NULL','Maximum amount of credit to be issued if commitment is violated',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',13,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',14,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent updat to this record',None,'N/A'),
)

tblc_SLA_TEST_COMMITMENT_DETAIL =( #  Wed Apr 30 05:42:25 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('COMMITMENT_DETAIL',1,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the commitment to which the COMMITMENT_DETAIL record applies - originates from the COMMITMENT table',1,'N/A'),
   TColumn('COMMITMENT_DETAIL',2,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the customer to which the record applies - originates from the CUSTOMER table',2,'N/A'),
   TColumn('COMMITMENT_DETAIL',3,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the product to which the record applies - originates from the PRODUCT table',3,'N/A'),
   TColumn('COMMITMENT_DETAIL',4,'DETAIL_TYPE_SELECT','VARCHAR2',20,None,None,'NOT NULL','Detail selected for the COMMITMENT_DETAIL record - used when optional detail type information is required and is driven by the DETAIL_TYPE from the COMMITMENT table',4,'N/A'),
   TColumn('COMMITMENT_DETAIL',5,'SUBDETAIL_TYPE_SELECT','VARCHAR2',20,None,None,'NOT NULL','Subdetail selected for the COMMITMENT_DETAIL record - used when optional subdetail type information is required and is driven by the SUBDETAIL_TYPE from the COMMITMENT table',5,'N/A'),
   TColumn('COMMITMENT_DETAIL',6,'COMMITMENT_TEXT','VARCHAR2',40,None,None,'NULL','Text string used to specify the Commitment',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',7,'COMMITMENT_METRIC','VARCHAR2',20,None,None,'NULL','Metric used to specify the Commitment',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',8,'METRIC_UNIT','VARCHAR2',20,None,None,'NULL','Unit of measure that applies to the metric',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',11,'ADDITIONAL_METRIC_UNIT','VARCHAR2',20,None,None,'NULL','Unit of measure that applies to the additional metric',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',12,'CREDIT_TYPE','VARCHAR2',20,None,None,'NULL','Credit type to apply to the credit amount if commitment is violated - like flat rate or percentage MRC/NRC',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',13,'CREDIT_AMOUNT','VARCHAR2',20,None,None,'NULL','Amount of credit to be issued if commitment is violated',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',16,'CREDIT_CAP_TYPE','VARCHAR2',20,None,None,'NULL','Credit type to apply to the Cap Amount if commitment is violated - like flat rate or percentage MRC/NRC',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',17,'CREDIT_CAP_AMOUNT','VARCHAR2',20,None,None,'NULL','Maximum amount of credit to be issued if commitment is violated',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',9,'ADDITIONAL_TEXT','VARCHAR2',40,None,None,'NULL','Text string used to specify additional segments of the Commitment',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',10,'ADDITIONAL_METRIC','VARCHAR2',20,None,None,'NULL','Metric used to specify the additional segment of the Commitment',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',14,'ADDITIONAL_CREDIT_TYPE','VARCHAR2',20,None,None,'NULL','Credit type to apply to the additional credit amount if the additional segment of the commitment is violated - like flat rate or percentage MRC/NRC',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',15,'ADDITIONAL_CREDIT_AMOUNT','VARCHAR2',20,None,None,'NULL','Amount of credit to be issued if additional segment of the commitment is violated',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',18,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('COMMITMENT_DETAIL',19,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent update to this record',None,'N/A'),
)




tbl=CTable(tblc_SLA_TEST_COMMITMENT_DETAIL)
tbl.isMap=True
tbl.setExtraAttrib('COMMITMENT_NBR','v_name','')

tbl.setExtraAttrib('COMMITMENT_NBR','lookup','Y')
tbl.setExtraAttrib('COMMITMENT_NBR','dispType','DD')


tbl.setExtraAttrib('CUSTOMER_NBR','v_name','')

tbl.setExtraAttrib('CUSTOMER_NBR','lookup','Y')
tbl.setExtraAttrib('CUSTOMER_NBR','dispType','DD')

tbl.setExtraAttrib('PRODUCT_NBR','v_name','')

tbl.setExtraAttrib('PRODUCT_NBR','lookup','Y')
tbl.setExtraAttrib('PRODUCT_NBR','dispType','DD')


tbl.setExtraAttrib('DETAIL_TYPE_SELECT','v_name','')

tbl.setExtraAttrib('DETAIL_TYPE_SELECT','lookup','Y')
tbl.setExtraAttrib('DETAIL_TYPE_SELECT','dispType','DD')


tbl.setExtraAttrib('SUBDETAIL_TYPE_SELECT','v_name','')

tbl.setExtraAttrib('SUBDETAIL_TYPE_SELECT','lookup','Y')
tbl.setExtraAttrib('SUBDETAIL_TYPE_SELECT','dispType','DD')




tbl.setExtraAttrib('COMMITMENT_TEXT','v_name','')

tbl.setExtraAttrib('COMMITMENT_METRIC','v_name','')
# tbl.setExtraAttrib('COMMITMENT_METRIC','lookup','Y')
# tbl.setExtraAttrib('COMMITMENT_METRIC','dispType','DD')


tbl.setExtraAttrib('METRIC_UNIT','v_name','')
tbl.setExtraAttrib('METRIC_UNIT','lookup','Y')
tbl.setExtraAttrib('METRIC_UNIT','dispType','DD')


tbl.setExtraAttrib('CREDIT_TYPE','v_name','')

tbl.setExtraAttrib('CREDIT_TYPE','lookup','Y')
tbl.setExtraAttrib('CREDIT_TYPE','dispType','DD')

tbl.setExtraAttrib('ADDITIONAL_CREDIT_TYPE','lookup','Y')
tbl.setExtraAttrib('ADDITIONAL_CREDIT_TYPE','dispType','DD')

tbl.setExtraAttrib('ADDITIONAL_METRIC_UNIT','dispType','DD')





tbl.setExtraAttrib('CREDIT_AMOUNT','v_name','')

tbl.setExtraAttrib('CREDIT_CAP_TYPE','v_name','')

tbl.setExtraAttrib('CREDIT_CAP_TYPE','lookup','Y')
tbl.setExtraAttrib('CREDIT_CAP_TYPE','dispType','DD')




tbl.setExtraAttrib('CREDIT_CAP_AMOUNT','v_name','')


tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')




tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')
tables_list['COMMITMENT_DETAIL']=tbl

###########################################################################

tblc_SLA_TEST_BREACH =( #  Fri Apr 25 07:05:12 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('BREACH',1,'BREACH_NBR','VARCHAR2',10,None,None,'NOT NULL','Uniquely identifies the BREACH record',1,'N/A'),
   TColumn('BREACH',8,'COMMITMENT_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the commitment to which the record applies - originates from the COMMITMENT table',None,'N/A'),
   TColumn('BREACH',2,'BREACH_STATUS','VARCHAR2',20,None,None,'NOT NULL','Indicates the workflow state of the BREACH record',None,'N/A'),
   TColumn('BREACH',3,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the customer to which the record applies - originates from the CUSTOMER table',None,'N/A'),
   TColumn('BREACH',5,'SITE_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the site to which the record applies - originates from the SITE table',None,'N/A'),
   TColumn('BREACH',6,'SITE_B_NBR','VARCHAR2',10,None,None,'NULL','When applicable, identifies the secondary site to which the record applies - originates from the SITE table',None,'N/A'),
   TColumn('BREACH',7,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the product to which the record applies - originates from the PRODUCT table',None,'N/A'),
   TColumn('BREACH',16,'BREACH_DESCRIPTION','VARCHAR2',200,None,None,'NULL','Text description of the Breach',None,'N/A'),
   TColumn('BREACH',4,'MEASUREMENT_PERIOD','VARCHAR2',6,None,None,'NOT NULL','Measurement Period in which this BREACH record should apply - normally formatted as YYYYMM',None,'N/A'),

   TColumn('BREACH',9,'DETAIL_TYPE','VARCHAR2',20,None,None,'NULL','Detail type information for the BREACH record - used when optional parameters are required',None,'N/A'),
   TColumn('BREACH',10,'DETAIL_TYPE_SELECT','VARCHAR2',20,None,None,'NOT NULL','Detail selected for the BREACH record - used when optional detail type information is required',None,'N/A'),
   TColumn('BREACH',11,'SUBDETAIL_TYPE','VARCHAR2',20,None,None,'NULL','Subdetail type information for the BREACH record - used when optional parameters are required',None,'N/A'),
   TColumn('BREACH',12,'SUBDETAIL_TYPE_SELECT','VARCHAR2',20,None,None,'NOT NULL','Subdetail selected for the BREACH record - used when optional subdetail type information is required',None,'N/A'),
   TColumn('BREACH',13,'TARGET_METRIC','VARCHAR2',20,None,None,'NULL','Target value that has been violated',None,'N/A'),
   TColumn('BREACH',14,'METRIC_UNIT','VARCHAR2',20,None,None,'NOT NULL','Unit of measure that applies to the metric',None,'N/A'),
   TColumn('BREACH',15,'MEASURED_PERFORMANCE','VARCHAR2',20,None,None,'NULL','Measureed performance that violates the SLA target',None,'N/A'),

   TColumn('BREACH',17,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('BREACH',18,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent updat to this record',None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_BREACH)
tbl.generate_auto_number=1
tbl.setExtraAttrib('BREACH_NBR','v_name','')

tbl.setExtraAttrib('BREACH_STATUS','v_name','')
tbl.setExtraAttrib('BREACH_STATUS','lookup','Y')
tbl.setExtraAttrib('BREACH_STATUS','dispType','DD')



tbl.setExtraAttrib('CUSTOMER_NBR','v_name','')
tbl.setExtraAttrib('CUSTOMER_NBR','lookup','Y')
tbl.setExtraAttrib('CUSTOMER_NBR','dispType','DD')

tbl.setExtraAttrib('MEASUREMENT_PERIOD','v_name','')


tbl.setExtraAttrib('SITE_NBR','v_name','')

tbl.setExtraAttrib('SITE_NBR','lookup','Y')
tbl.setExtraAttrib('SITE_NBR','dispType','DD')

tbl.setExtraAttrib('SITE_B_NBR','v_name','')
tbl.setExtraAttrib('SITE_B_NBR','lookup','Y')
tbl.setExtraAttrib('SITE_B_NBR','dispType','DD')



tbl.setExtraAttrib('PRODUCT_NBR','v_name','')
tbl.setExtraAttrib('PRODUCT_NBR','lookup','Y')
tbl.setExtraAttrib('PRODUCT_NBR','dispType','DD')


tbl.setExtraAttrib('COMMITMENT_NBR','v_name','')
tbl.setExtraAttrib('COMMITMENT_NBR','lookup','Y')
tbl.setExtraAttrib('COMMITMENT_NBR','dispType','DD')



# tbl.setExtraAttrib('DETAIL_TYPE','a_name',' Enabled="false"') # from  Commitment

tbl.setExtraAttrib('DETAIL_TYPE_SELECT','v_name','')
tbl.setExtraAttrib('DETAIL_TYPE_SELECT','lookup','Y')
tbl.setExtraAttrib('DETAIL_TYPE_SELECT','dispType','DD')


# tbl.setExtraAttrib('SUBDETAIL_TYPE','a_name','  Enabled="false" ')


tbl.setExtraAttrib('SUBDETAIL_TYPE_SELECT','v_name','')  # ####
tbl.setExtraAttrib('SUBDETAIL_TYPE_SELECT','lookup','Y')
tbl.setExtraAttrib('SUBDETAIL_TYPE_SELECT','dispType','DD')

tbl.setExtraAttrib('TARGET_METRIC','v_name','')


tbl.setExtraAttrib('METRIC_UNIT','v_name','')
tbl.setExtraAttrib('METRIC_UNIT','lookup','Y')
tbl.setExtraAttrib('METRIC_UNIT','dispType','DD')

tbl.setExtraAttrib('MEASURED_PERFORMANCE','v_name','')

tbl.setExtraAttrib('BREACH_DESCRIPTION','v_name','')

tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')

tbl.setExtraAttrib('DETAIL_TYPE','is_there_name','1')
tbl.setExtraAttrib('SUBDETAIL_TYPE','is_there_name','1')


tables_list['BREACH']=tbl


tblc_SLA_TEST_CREDIT_REQUEST =( #  Mon Apr 28 06:45:42 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('CREDIT_REQUEST',1,'REQUEST_NBR','VARCHAR2',10,None,None,'NOT NULL','Uniquely identifies the CREDIT_REQUEST record',1,'N/A'),
   TColumn('CREDIT_REQUEST',2,'BREACH_NBR','VARCHAR2',10,None,None,'NULL','Identifies the breach to which the record applies - originates from the BREACH table',None,'N/A'),
   TColumn('CREDIT_REQUEST',3,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NULL','Identifies the customer to which the record applies - originates from the CUSTOMER table',None,'N/A'),
   TColumn('CREDIT_REQUEST',4,'REQUEST_STATUS','VARCHAR2',20,None,None,'NULL','Indicates the workflow state of the CREDIT_REQUEST record',None,'N/A'),
   TColumn('CREDIT_REQUEST',5,'REQUEST_TEXT','VARCHAR2',140,None,None,'NULL','Text note on the CREDIT_REQUEST record',None,'N/A'),
   TColumn('CREDIT_REQUEST',6,'RELEVANT_NRC','VARCHAR2',20,None,None,'NULL','The relevant NRC as it applies to this credit request',None,'N/A'),
   TColumn('CREDIT_REQUEST',7,'RELEVANT_MRC','VARCHAR2',20,None,None,'NULL','The relevant MRC as it applies to this credit request',None,'N/A'),
   TColumn('CREDIT_REQUEST',8,'CREDIT_AMOUNT','VARCHAR2',20,None,None,'NULL','The dollar amount of the credit request',None,'N/A'),
   TColumn('CREDIT_REQUEST',9,'RESOLUTION_DT','DATE',7,None,None,'NULL','Timestamp from the moment the CREDIT_REQUEST record moved to a resolved state (whether approved or rejected)',None,'N/A'),
   TColumn('CREDIT_REQUEST',10,'RESOLUTION_TEXT','VARCHAR2',140,None,None,'NULL','Text note added to the CREDIT_REQUEST record upon resolution',None,'N/A'),
   TColumn('CREDIT_REQUEST',11,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('CREDIT_REQUEST',12,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent update to this record',None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_CREDIT_REQUEST)

tbl.setExtraAttrib('REQUEST_NBR','v_name','')

tbl.setExtraAttrib('BREACH_NBR','v_name','')

tbl.setExtraAttrib('CUSTOMER_NBR','v_name','')
tbl.setExtraAttrib('CUSTOMER_NBR','lookup','Y')
tbl.setExtraAttrib('CUSTOMER_NBR','dispType','DD')


tbl.setExtraAttrib('REQUEST_STATUS','v_name','')
tbl.setExtraAttrib('REQUEST_STATUS','lookup','Y')
tbl.setExtraAttrib('REQUEST_STATUS','dispType','DD')

tbl.setExtraAttrib('REQUEST_TEXT','v_name','')
tbl.setExtraAttrib('REQUEST_TEXT','lookup','Y')

tbl.setExtraAttrib('RELEVANT_NRC','v_name','')
tbl.setExtraAttrib('RELEVANT_MRC','v_name','')
tbl.setExtraAttrib('CREDIT_AMOUNT','v_name','')
tbl.setExtraAttrib('RESOLUTION_DT','v_name','')

tbl.setExtraAttrib('RESOLUTION_TEXT','v_name','')
tbl.setExtraAttrib('RESOLUTION_TEXT','lookup','Y')

tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')

tables_list['CREDIT_REQUEST']=tbl

##############################################################


tblc_SLA_TEST_TICKET_EXCLUSION =( #  Mon Apr 28 07:27:06 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('TICKET_EXCLUSION',1,'TICKET_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the ticket to which the record applies - originates from the TICKET_DETAIL table ',1,'N/A'),
   TColumn('TICKET_EXCLUSION',2,'EXCLUSION_NBR','VARCHAR2',10,None,None,'NOT NULL','Identifies the exclusion to which the record applies - originates from the EXCLUSION table ',2,'N/A'),
   TColumn('TICKET_EXCLUSION',3,'EXCLUSION_TEXT','VARCHAR2',200,None,None,'NULL','Additional text explanation added to the ticket-exclusion, when required',None,'N/A'),
   TColumn('TICKET_EXCLUSION',4,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('TICKET_EXCLUSION',5,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent update to this record',None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_TICKET_EXCLUSION)
tbl.setExtraAttrib('TICKET_NBR','v_name','')
tbl.setExtraAttrib('TICKET_NBR','lookup','Y')
tbl.setExtraAttrib('TICKET_NBR','is_there_name','1')

tbl.setExtraAttrib('EXCLUSION_NBR','is_there_name','1')
tbl.setExtraAttrib('EXCLUSION_NBR','dispType','DD')
tbl.setExtraAttrib('EXCLUSION_NBR','lookup','Y')



tbl.setExtraAttrib('EXCLUSION_NBR','v_name','')
tbl.setExtraAttrib('EXCLUSION_TEXT','v_name','')
tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')
tables_list['TICKET_EXCLUSION']=tbl


tblc_SLA_TEST_CUSTOMER_CORP =( #  Mon Apr 28 07:45:23 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('CUSTOMER_CORP',1,'CUSTOMER_H1','VARCHAR2',10,None,None,'NULL','Customer H1 number',1,'N/A'),
   TColumn('CUSTOMER_CORP',2,'CUSTOMER_CORP_NAME','VARCHAR2',60,None,None,'NULL','Customer Corporation Name',None,'N/A'),
   TColumn('CUSTOMER_CORP',3,'UPDATE_BY','VARCHAR2',20,None,None,'NULL','User or Process that most recently updated this record',None,'N/A'),
   TColumn('CUSTOMER_CORP',4,'UPDATE_DT','DATE',7,None,None,'NULL','Timestamp of the most recent update to this record',None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_CUSTOMER_CORP)
tbl.setExtraAttrib('CUSTOMER_H1','v_name','')
tbl.setExtraAttrib('CUSTOMER_H1','lookup','Y')

tbl.setExtraAttrib('CUSTOMER_CORP_NAME','v_name','')
tbl.setExtraAttrib('CUSTOMER_CORP_NAME','is_there_name','1')
tbl.setExtraAttrib('CUSTOMER_CORP_NAME','lookup','Y')

tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')
tables_list['CUSTOMER_CORP']=tbl


tblc_SLA_TEST_E2E_SLA_TEST =( #  Tue May 06 08:58:09 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('E2E_SLA_TEST',1,'TEST_ID','VARCHAR2',10,None,None,'NULL',None,1,'N/A'),
   TColumn('E2E_SLA_TEST',2,'CUSTOMER_NBR','VARCHAR2',10,None,None,'NOT NULL',None,0,'N/A'),
   TColumn('E2E_SLA_TEST',10,'PRODUCT_NBR','VARCHAR2',10,None,None,'NOT NULL',None,0,'N/A'),
   TColumn('E2E_SLA_TEST',3,'SITE_A_ID','VARCHAR2',10,None,None,'NOT NULL',None,0,'N/A'),
   TColumn('E2E_SLA_TEST',4,'SITE_B_ID','VARCHAR2',10,None,None,'NOT NULL',None,None,'N/A'),
   TColumn('E2E_SLA_TEST',5,'METRIC_DELAY','VARCHAR2',20,None,None,'NOT NULL',None,None,'N/A'),
   TColumn('E2E_SLA_TEST',6,'METRIC_PACKET_LOSS','VARCHAR2',20,None,None,'NOT NULL',None,None,'N/A'),
   TColumn('E2E_SLA_TEST',7,'METRIC_JITTER','VARCHAR2',20,None,None,'NOT NULL',None,None,'N/A'),
   TColumn('E2E_SLA_TEST',8,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
   TColumn('E2E_SLA_TEST',9,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,'N/A'),
   TColumn('E2E_SLA_TEST',11,'ACTIVE_FLAG','VARCHAR2',1,None,None,'NOT NULL',None,None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_E2E_SLA_TEST)
tbl.generate_auto_number=1
tbl.bean_name="bean_test_e2e"
tbl.setExtraAttrib('TEST_ID','v_name','')
tbl.setExtraAttrib('CUSTOMER_NBR','v_name','')
tbl.setExtraAttrib('CUSTOMER_NBR','is_there_name','1')
tbl.setExtraAttrib('CUSTOMER_NBR','dispType','DD')

tbl.setExtraAttrib('SITE_A_ID','v_name','')
tbl.setExtraAttrib('SITE_A_ID','is_there_name','1')
tbl.setExtraAttrib('SITE_A_ID','dispType','DD')
tbl.setExtraAttrib('SITE_A_ID','lookup','Y')

tbl.setExtraAttrib('SITE_B_ID','v_name','')
tbl.setExtraAttrib('SITE_B_ID','is_there_name','1')
tbl.setExtraAttrib('SITE_B_ID','dispType','DD')
tbl.setExtraAttrib('SITE_B_ID','lookup','Y')

tbl.setExtraAttrib('PRODUCT_NBR','v_name','')
tbl.setExtraAttrib('PRODUCT_NBR','lookup','Y')
tbl.setExtraAttrib('PRODUCT_NBR','dispType','DD')
tbl.setExtraAttrib('PRODUCT_NBR','is_there_name','1')

tbl.setExtraAttrib('ACTIVE_FLAG','dispType','CHK')


tables_list['E2E_SLA_TEST']=tbl
################################################################

tblc_SLA_TEST_E2E_PERFORMANCE =( #  Mon May 12 08:25:06 CDT 2014
   #tname,colno,cname,coltype,width,scale,precision,nulls,comments, pkpos, defval
   TColumn('E2E_PERFORMANCE',1,'TEST_ID','VARCHAR2',10,None,None,'NULL',None,1,'N/A'),
   TColumn('E2E_PERFORMANCE',2,'MEASUREMENT_PERIOD','VARCHAR2',6,None,None,'NULL',None,2,'N/A'),
   TColumn('E2E_PERFORMANCE',3,'MEASURED_DELAY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
   TColumn('E2E_PERFORMANCE',4,'MEASURED_PACKET_LOSS','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
   TColumn('E2E_PERFORMANCE',5,'MEASURED_JITTER','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
   TColumn('E2E_PERFORMANCE',6,'UPDATE_BY','VARCHAR2',20,None,None,'NULL',None,None,'N/A'),
   TColumn('E2E_PERFORMANCE',7,'UPDATE_DT','DATE',7,None,None,'NULL',None,None,'N/A'),
)

tbl=CTable(tblc_SLA_TEST_E2E_PERFORMANCE)
tbl.setExtraAttrib('TEST_ID','v_name','')
tbl.setExtraAttrib('MEASUREMENT_PERIOD','is_there_name','1')
tbl.setExtraAttrib('TEST_ID','is_there_name','1')



tbl.setExtraAttrib('MEASUREMENT_PERIOD','v_name','')
tbl.setExtraAttrib('MEASURED_DELAY','v_name','')
tbl.setExtraAttrib('MEASURED_PACKET_LOSS','v_name','')
tbl.setExtraAttrib('MEASURED_JITTER','v_name','')
tbl.setExtraAttrib('UPDATE_BY','v_name','')
tbl.setExtraAttrib('UPDATE_DT','v_name','')
tables_list['E2E_PERFORMANCE']=tbl



if __name__ == '__main__':

  tbl_1=CTable(tblc_SLA_TEST_COMMITMENT_DETAIL)
  tbl_o=CTable(tblc_SLA_TEST_COMMITMENT_DETAIL_o)
  col_1=tbl_1.getColNames();
  col_o=tbl_o.getColNames();
  i=0
  for cn in col_o:
      i+=1
      if cn not in col_1:
        print i, cn
  i=0
  for cn in col_1:
      i+=1
      if cn not in col_o:
        print i, cn


