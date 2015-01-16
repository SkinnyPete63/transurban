from dbconnect import session_scope
from dbconnect.tables import MAXATTRIBUTE
from sqlalchemy import and_
from dbconnect.defineRequiredTables import define_table
from dbconnect.maximo_attributes import get_sameas

#from dbconnect.defineRequiredTables import define_table

tablelist = ['AMCREW', 'AREASAFFECTED', 'ASSET', 'ASSETHIERARCHY', 'ASSETLOCCOMM', 'ASSETLOCRELATION', 'ASSETLOCRELHIST', \
             'ASSETLOCUSERCUST', 'ASSETSTATUS', 'ASSETTRANS', 'ASSETUSERCUST', 'AUTOATTRUPDATE', 'CI', 'COLLECTDETAILS', \
             'COMPANIES', 'CONTASSETMETER', 'CONTLINEASSET', 'CONTRACTASSET', 'FAVITEM', 'INCIDENT', 'INVBALANCES', 'INVCOST', \
             'INVENTORY', 'INVLIFOFIFOCOST', 'INVLOT', 'INVOICECOST', 'INVRESERVE', 'INVSTATUS', 'INVTRANS', 'INVUSE', \
             'INVUSELINE', 'INVUSELINESPLIT', 'JOBITEM', 'JOBMATERIAL', 'JOBSERVICE', 'JOBTOOL', 'JPASSETSPLINK', 'KPIOEE', \
             'LABOR', 'LABTRANS', 'LOCANCESTOR', 'LOCATIONMETER', 'LOCATIONMNTSKD', 'LOCATIONOPSKD', 'LOCATIONSPEC', \
             'LOCATIONUSERCUST', 'LOCAUTH', 'LOCHIERARCHY', 'LOCKOUT', 'LOCLEADTIME', 'LOCMETERREADING', 'LOCOPER', 'LOCSTATUS', \
             'MATRECTRANS', 'MATUSETRANS', 'MEASUREMENT', 'MEASUREPOINT', 'MR', 'MRLINE', 'MULTIASSETLOCCI', 'NAMEDUSERS', \
             'PERSCOMMODITY', 'PERSON', 'PLUSCDSASSETLINK', 'PLUSCJPDATASHEET', 'PLUSCWODS', 'PM', 'PMMETER', 'PO', 'POLINE', 'PR', \
             'PRLINE', 'REORDERMUTEX', 'REORDERPAD', 'REPFACAUTH', 'RFQLINE', 'ROUTE_STOP', 'SAFETYLEXICON', 'SERVRECTRANS', \
             'SHIPMENTLINE', 'SKDACTIVITYQBE', 'SKDPROJECT', 'SLAASSETLOC', 'SLROUTE', 'SPRELATEDASSET', 'SPWORKASSET', \
             'TAGOUT', 'TOOLTRANS', \
             'WARRANTYASSET', 'WOACTIVITY', 'WOASSETUSERCUST', 'WOCHANGE', 'WOCONTRACT', 'WOGEN', 'WOLOCKOUT', 'WOLOCUSERCUST', \
             'WOMATSTATUSSYNC', 'WORKORDER', 'WOSAFETYLINK', 'WOTAGOUT', 'WPITEM', 'WPMATERIAL', 'WPSERVICE', 'WPTOOL']
#tablelist = ['AMCREW']
loclist =[]
#define_table(tablelist)
#mymodule = __import__("temp_tabledefs")
def runsql(sqlstr):
    with session_scope() as session:
        session.execute(sqlstr)
        session.commit()
#get same as values
mysame = get_sameas("location", tablelist)
sqlpref = "delete from "
with open("deletion_history_v3.txt", "wb") as f:
    for k, v in mysame.iteritems():
        for col in v:
            if k in ['FAVITEM', 'CI']:
                whereclause = col + " in (select location from locations where tulocation is null and siteid = 'CML') and itemsetid = 'CMLITEM'"
            elif k in ['LABOR']:
                whereclause = col + " in (select location from locations where tulocation is null and siteid = 'CML') and worksite = 'CML'"
            elif k in ['COMPANIES', 'SKDPROJECT', 'CONTRACTASSET', 'AMCREW', 'CONTASSETMETER', 'WARRANTYASSET', 'CONTLINEASSET', 'SLROUTE']:
                whereclause = col + " in (select location from locations where tulocation is null and siteid = 'CML') and orgid = 'TUCML'"
            elif k in ['PERSON']:
                whereclause = col + " in (select location from locations where tulocation is null and siteid = 'CML') and locationsite = 'CML'"
            else:
                whereclause = col + " in (select location from locations where tulocation is null and siteid = 'CML') and siteid = 'CML'"
            sqlstring = sqlpref + k + " where " + whereclause
            print sqlstring
            runsql(sqlstring)