from dbconnect import session_scope
from dbconnect.tables import MAXATTRIBUTE
from sqlalchemy import and_
from dbconnect.defineRequiredTables import define_table
from dbconnect.maximo_attributes import get_sameas
import csv

#from dbconnect.defineRequiredTables import define_table
def runsql(sqlstr):
    with session_scope() as session:
        session.execute(sqlstr)
        session.commit()

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
mysame = get_sameas("location", tablelist)
with open("\\pch\\locations_for_deletion.txt") as f:
    reader = csv.reader(f)
    for row in reader:
        loc = row[0]
        print row[0]
    #define_table(tablelist)
    #mymodule = __import__("temp_tabledefs")
    #get same as values
    
        sqlpref = "delete from "
        for k, v in mysame.iteritems():
            for col in v:
                if k in ['FAVITEM', 'CI']:
                    whereclause = col + " ='" + loc + "' and itemsetid = 'CMLITEM'"
                elif k in ['LABOR']:
                    whereclause = col + " ='" + loc + "' and worksite = 'CML'"
                elif k in ['COMPANIES', 'SKDPROJECT', 'CONTRACTASSET', 'AMCREW', 'CONTASSETMETER', 'WARRANTYASSET', 'CONTLINEASSET', 'SLROUTE']:
                    whereclause = col + " ='" + loc + "' and orgid = 'TUCML'"
                elif k in ['PERSON']:
                    whereclause = col + " ='" + loc + "' and locationsite = 'CML'"
                else:
                    whereclause = col + " ='" + loc + "' and siteid = 'CML'"
                sqlstring = sqlpref + k + " where " + whereclause
                #print sqlstring
                runsql(sqlstring)