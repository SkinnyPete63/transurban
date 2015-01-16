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

#     print len(mylocs)
    for loc in mylocs:
        loclist.append(loc.location)
#     print loclist

    
#     attribs = session.query(MAXATTRIBUTE).filter(and_(MAXATTRIBUTE.sameasattribute == 'LOCATION', MAXATTRIBUTE.persistent == 1))
#     mystr = ""
#     for attrib in attribs:
#         mystr = mystr + ", '" + attrib.objectname + "'"
#     print mystr
    sameasdict = get_sameas('location', tablelist)
    #print sameasdict
    #exit
    for k, v in sameasdict.iteritems():
        for col in v:
            mytb = getattr(mymodule, k)
            if k in ['FAVITEM', 'CI']:
                theseresults = session.query(mytb).filter(and_(getattr(mytb, col.lower()).in_(session.query(myfirsttb.location).filter(and_(myfirsttb.tulocation == None, myfirsttb.siteid == "CML")).all()) , mytb.itemsetid == 'CMLITEM')).all()
            elif k in ['LABOR']:
                theseresults = session.query(mytb).filter(and_(getattr(mytb, col.lower()).in_(['ABUTGE-GCVEAE']) , mytb.worksite == 'CML')).all()
            elif k in ['COMPANIES', 'SKDPROJECT', 'CONTRACTASSET', 'AMCREW', 'CONTASSETMETER', 'WARRANTYASSET', 'CONTLINEASSET', 'SLROUTE']:
                theseresults = session.query(mytb).filter(and_(getattr(mytb, col.lower()).in_(['ABUTGE-GCVEAE']) , mytb.orgid == 'TUCML')).all()
            elif k in ['PERSON']:
                theseresults = session.query(mytb).filter(and_(getattr(mytb, col.lower()).in_(['ABUTGE-GCVEAE']) , mytb.locationsite == 'CML')).all()
            else:
            #session.query(myfirsttb.location).filter(and_(myfirsttb.tulocation == None, myfirsttb.siteid == "CML")).all()
                theseresults = session.query(mytb).filter(and_(getattr(mytb, col.lower()).in_(['ABUTGE-GCVEAE']) , mytb.siteid == 'CML')).all()
            #print k, col, len(theseresults)
        
            if len(theseresults) > 0:
                outstring = "Deleting " + str(len(theseresults)) + " records from " + k + " where " + col + " has a value" 
                print outstring 
                for res in theseresults:
                    session.delete(res)
    session.commit()