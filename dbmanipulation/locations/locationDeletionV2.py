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
             'LABOR', 'LABTRANS', 'LOCANCESTOR', 'LOCATIONMETER', 'LOCATIONMNTSKD', 'LOCATIONOPSKD', 'LOCATIONS', 'LOCATIONSPEC', \
             'LOCATIONUSERCUST', 'LOCAUTH', 'LOCHIERARCHY', 'LOCKOUT', 'LOCLEADTIME', 'LOCMETERREADING', 'LOCOPER', 'LOCSTATUS', \
             'MATRECTRANS', 'MATUSETRANS', 'MEASUREMENT', 'MEASUREPOINT', 'MR', 'MRLINE', 'MULTIASSETLOCCI', 'NAMEDUSERS', \
             'PERSCOMMODITY', 'PERSON', 'PLUSCDSASSETLINK', 'PLUSCJPDATASHEET', 'PLUSCWODS', 'PM', 'PMMETER', 'PO', 'POLINE', 'PR', \
             'PRLINE', 'REORDERMUTEX', 'REORDERPAD', 'REPFACAUTH', 'RFQLINE', 'ROUTE_STOP', 'SAFETYLEXICON', 'SERVRECTRANS', \
             'SHIPMENTLINE', 'SKDACTIVITYQBE', 'SKDPROJECT', 'SLAASSETLOC', 'SLROUTE', 'SPRELATEDASSET', 'SPWORKASSET', \
             'TAGOUT', 'TOOLINV', 'TOOLTRANS', 'UNASSIGNEDWORKVIEW', \
             'WARRANTYASSET', 'WOACTIVITY', 'WOASSETUSERCUST', 'WOCHANGE', 'WOCONTRACT', 'WOGEN', 'WOLOCKOUT', 'WOLOCUSERCUST', \
             'WOMATSTATUSSYNC', 'WORELEASE', 'WORKORDER', 'WOSAFETYLINK', 'WOTAGOUT', 'WPITEM', 'WPMATERIAL', 'WPSERVICE', 'WPTOOL']
#tablelist = ['AMCREW']
with session_scope() as session:
    loclist =[]
    #define_table(tablelist)
    mymodule = __import__("temp_tabledefs")
    
    myfirsttb = getattr(mymodule, "LOCATIONS")
    mylocs = session.query(myfirsttb).filter(and_(myfirsttb.tulocation == None, myfirsttb.siteid == "CML")).all()
    #get same as values
    mysame = get_sameas("location", tablelist)
    
#     print len(mylocs)
    with open("deletion_history.txt", "wb") as f:
        for loc in mylocs:
            #f.write("Checking database for records for " + loc.location + "\n")
            #f.write("--------------------------------------------------\n")
            for k, v in mysame.iteritems():
                f.write("\tChecking table " + k + " for records\n")
                f.write("\t************************************************************\n")
                mytb = getattr(mymodule, k)
                for col in v:
                    f.write("\t\tChecking in column " + col + " for records\n")
                    f.write("\t\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
                    if k in ['FAVITEM', 'CI']:
                        theserecs = session.query(mytb).filter(and_(getattr(mytb, col.lower()) == loc.location,  mytb.itemsetid == 'CMLITEM')).all()
                    elif k in ['LABOR']:
                        theserecs = session.query(mytb).filter(and_(getattr(mytb, col.lower()) == loc.location,  mytb.worksite == 'CML')).all()
                    elif k in ['COMPANIES', 'SKDPROJECT', 'CONTRACTASSET', 'AMCREW', 'CONTASSETMETER', 'WARRANTYASSET', 'CONTLINEASSET', 'SLROUTE']:
                        theserecs = session.query(mytb).filter(and_(getattr(mytb, col.lower()) == loc.location, mytb.orgid == 'TUCML')).all()
                    elif k in ['PERSON']:
                        theserecs = session.query(mytb).filter(and_(getattr(mytb, col.lower()) == loc.location, mytb.locationsite == 'CML')).all()
                    else:
                        theserecs = session.query(mytb).filter(and_(getattr(mytb, col.lower()) == loc.location, mytb.siteid == "CML")).all()
                    if len(theserecs) > 0:
                        f.write("\t\t" + str(len(theserecs)) + " records found in '" + k + "' table for column " + col + " for location " + loc.location + "\n")
                        for rec in theserecs:
                            try:
                                session.delete(rec)
                                
                            except:
                                f.write("Error deleting record\n")
                                pass
                    else:
                        f.write("\t\tNo records found\n")
                        #exit
            #commit the changes for a whole location so records are not left inconsistent
            session.commit()
                #delete rows
        
    session.commit()