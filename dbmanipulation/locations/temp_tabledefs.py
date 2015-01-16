from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session
from dbconnect.parameters import *
import base64

decpass = base64.b64decode(dbpass)

connectstring = 'mssql+pyodbc://' + dbuser + ':' + decpass + '@' + dbserver + '/' + db + ';Trusted_Connection=Yes' 
Base = declarative_base()
engine = create_engine(connectstring)
metadata = MetaData(bind=engine)
session = create_session(bind=engine)

class AMCREW(Base):
	__table__ = Table('AMCREW', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrew, __table__.c.orgid]}

class AREASAFFECTED(Base):
	__table__ = Table('AREASAFFECTED', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.areasaffectedid, __table__.c.siteid, __table__.c.wonum]}

class ASSET(Base):
	__table__ = Table('ASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.siteid]}

class ASSETHIERARCHY(Base):
	__table__ = Table('ASSETHIERARCHY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.siteid, __table__.c.wonum]}

class ASSETLOCCOMM(Base):
	__table__ = Table('ASSETLOCCOMM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetloccommid]}

class ASSETLOCRELATION(Base):
	__table__ = Table('ASSETLOCRELATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetrelationnum, __table__.c.linearassetlocrelationid, __table__.c.sourceassetnum, __table__.c.targetassetnum]}

class ASSETLOCRELHIST(Base):
	__table__ = Table('ASSETLOCRELHIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetlocrelhistid]}

class ASSETLOCUSERCUST(Base):
	__table__ = Table('ASSETLOCUSERCUST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.location, __table__.c.personid, __table__.c.siteid]}

class ASSETSTATUS(Base):
	__table__ = Table('ASSETSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetstatusid]}

class ASSETTRANS(Base):
	__table__ = Table('ASSETTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assettransid]}

class ASSETUSERCUST(Base):
	__table__ = Table('ASSETUSERCUST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.location, __table__.c.personid, __table__.c.siteid]}

class AUTOATTRUPDATE(Base):
	__table__ = Table('AUTOATTRUPDATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.autoattrupdateid]}

class CI(Base):
	__table__ = Table('CI', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cinum]}

class COLLECTDETAILS(Base):
	__table__ = Table('COLLECTDETAILS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.collectdetailsid]}

class COMPANIES(Base):
	__table__ = Table('COMPANIES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.company, __table__.c.orgid]}

class CONTASSETMETER(Base):
	__table__ = Table('CONTASSETMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contassetmeterid]}

class CONTLINEASSET(Base):
	__table__ = Table('CONTLINEASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contlineassetid]}

class CONTRACTASSET(Base):
	__table__ = Table('CONTRACTASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractassetid]}

class FAVITEM(Base):
	__table__ = Table('FAVITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.description, __table__.c.itemnum, __table__.c.itemsetid, __table__.c.personid, __table__.c.storeroom, __table__.c.storeroomsite]}

class INCIDENT(Base):
	__table__ = Table('INCIDENT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ticketid]}

class INVBALANCES(Base):
	__table__ = Table('INVBALANCES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.binnum, __table__.c.conditioncode, __table__.c.itemnum, __table__.c.itemsetid, __table__.c.location, __table__.c.lotnum, __table__.c.siteid]}

class INVCOST(Base):
	__table__ = Table('INVCOST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.conditioncode, __table__.c.itemnum, __table__.c.itemsetid, __table__.c.location, __table__.c.siteid]}

class INVENTORY(Base):
	__table__ = Table('INVENTORY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.itemsetid, __table__.c.location, __table__.c.siteid]}

class INVLIFOFIFOCOST(Base):
	__table__ = Table('INVLIFOFIFOCOST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contentuid]}

class INVLOT(Base):
	__table__ = Table('INVLOT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.location, __table__.c.lotnum, __table__.c.siteid]}

class INVOICECOST(Base):
	__table__ = Table('INVOICECOST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.costlinenum, __table__.c.invoicelinenum, __table__.c.invoicenum, __table__.c.siteid]}

class INVRESERVE(Base):
	__table__ = Table('INVRESERVE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.requestnum, __table__.c.siteid]}

class INVSTATUS(Base):
	__table__ = Table('INVSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invstatusid]}

class INVTRANS(Base):
	__table__ = Table('INVTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invtransid, __table__.c.siteid]}

class INVUSE(Base):
	__table__ = Table('INVUSE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invusenum, __table__.c.siteid]}

class INVUSELINE(Base):
	__table__ = Table('INVUSELINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invuselinenum, __table__.c.invusenum, __table__.c.siteid]}

class INVUSELINESPLIT(Base):
	__table__ = Table('INVUSELINESPLIT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contentuid]}

class JOBITEM(Base):
	__table__ = Table('JOBITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobitemid]}

class JOBMATERIAL(Base):
	__table__ = Table('JOBMATERIAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobitemid]}

class JOBSERVICE(Base):
	__table__ = Table('JOBSERVICE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobitemid]}

class JOBTOOL(Base):
	__table__ = Table('JOBTOOL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobitemid]}

class JPASSETSPLINK(Base):
	__table__ = Table('JPASSETSPLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jpassetsplinkid]}

class KPIOEE(Base):
	__table__ = Table('KPIOEE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.oeedate, __table__.c.partnum, __table__.c.siteid]}

class LABOR(Base):
	__table__ = Table('LABOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.laborcode, __table__.c.orgid]}

class LABTRANS(Base):
	__table__ = Table('LABTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.laborcode, __table__.c.labtransid, __table__.c.siteid]}

class LOCANCESTOR(Base):
	__table__ = Table('LOCANCESTOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ancestor, __table__.c.location, __table__.c.siteid, __table__.c.systemid]}

class LOCATIONMETER(Base):
	__table__ = Table('LOCATIONMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.metername, __table__.c.siteid]}

class LOCATIONMNTSKD(Base):
	__table__ = Table('LOCATIONMNTSKD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.ophrs, __table__.c.siteid, __table__.c.startdatetime]}

class LOCATIONOPSKD(Base):
	__table__ = Table('LOCATIONOPSKD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.ophrs, __table__.c.siteid, __table__.c.startdatetime]}

class LOCATIONS(Base):
	__table__ = Table('LOCATIONS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.siteid]}

class LOCATIONSPEC(Base):
	__table__ = Table('LOCATIONSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.location, __table__.c.section, __table__.c.siteid]}

class LOCATIONUSERCUST(Base):
	__table__ = Table('LOCATIONUSERCUST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.location, __table__.c.personid, __table__.c.siteid]}

class LOCAUTH(Base):
	__table__ = Table('LOCAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.location, __table__.c.siteid]}

class LOCHIERARCHY(Base):
	__table__ = Table('LOCHIERARCHY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.parent, __table__.c.siteid, __table__.c.systemid]}

class LOCKOUT(Base):
	__table__ = Table('LOCKOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.lockoutid, __table__.c.siteid]}

class LOCLEADTIME(Base):
	__table__ = Table('LOCLEADTIME', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.siteid]}

class LOCMETERREADING(Base):
	__table__ = Table('LOCMETERREADING', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.meterreadingid, __table__.c.siteid]}

class LOCOPER(Base):
	__table__ = Table('LOCOPER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.siteid]}

class LOCSTATUS(Base):
	__table__ = Table('LOCSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.locstatusid]}

class MATRECTRANS(Base):
	__table__ = Table('MATRECTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.matrectransid]}

class MATUSETRANS(Base):
	__table__ = Table('MATUSETRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.matusetransid, __table__.c.siteid]}

class MEASUREMENT(Base):
	__table__ = Table('MEASUREMENT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.measurementid]}

class MEASUREPOINT(Base):
	__table__ = Table('MEASUREPOINT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pointnum, __table__.c.siteid]}

class MR(Base):
	__table__ = Table('MR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mrnum, __table__.c.siteid]}

class MRLINE(Base):
	__table__ = Table('MRLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mrlineid, __table__.c.siteid]}

class MULTIASSETLOCCI(Base):
	__table__ = Table('MULTIASSETLOCCI', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.multiid]}

class NAMEDUSERS(Base):
	__table__ = Table('NAMEDUSERS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.namedusersid]}

class PERSCOMMODITY(Base):
	__table__ = Table('PERSCOMMODITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.commodity, __table__.c.itemsetid, __table__.c.location, __table__.c.orgid, __table__.c.personid, __table__.c.siteid]}

class PERSON(Base):
	__table__ = Table('PERSON', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.personid]}

class PLUSCDSASSETLINK(Base):
	__table__ = Table('PLUSCDSASSETLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscdsassetlinkid]}

class PLUSCJPDATASHEET(Base):
	__table__ = Table('PLUSCJPDATASHEET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscjpdatasheetid]}

class PLUSCWODS(Base):
	__table__ = Table('PLUSCWODS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscwodsid]}

class PM(Base):
	__table__ = Table('PM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pmnum, __table__.c.siteid]}

class PMMETER(Base):
	__table__ = Table('PMMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.metername, __table__.c.pmnum, __table__.c.siteid]}

class PO(Base):
	__table__ = Table('PO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ponum, __table__.c.revisionnum, __table__.c.siteid]}

class POLINE(Base):
	__table__ = Table('POLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.polineid]}

class PR(Base):
	__table__ = Table('PR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.prnum, __table__.c.siteid]}

class PRLINE(Base):
	__table__ = Table('PRLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.prlineid]}

class REORDERMUTEX(Base):
	__table__ = Table('REORDERMUTEX', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.mrnum, __table__.c.siteid, __table__.c.type]}

class REORDERPAD(Base):
	__table__ = Table('REORDERPAD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.itemsetid, __table__.c.location, __table__.c.mrlinenum, __table__.c.mrnum, __table__.c.siteid, __table__.c.usrname, __table__.c.wpitemid]}

class REPFACAUTH(Base):
	__table__ = Table('REPFACAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.repairfacility, __table__.c.siteid]}

class RFQLINE(Base):
	__table__ = Table('RFQLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rfqlineid]}

class ROUTE_STOP(Base):
	__table__ = Table('ROUTE_STOP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.route, __table__.c.routestopid, __table__.c.siteid]}

class SAFETYLEXICON(Base):
	__table__ = Table('SAFETYLEXICON', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.safetylexiconid, __table__.c.siteid]}

class SERVRECTRANS(Base):
	__table__ = Table('SERVRECTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.servrectransid]}

class SHIPMENTLINE(Base):
	__table__ = Table('SHIPMENTLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.shipmentid, __table__.c.shipmentlineid, __table__.c.siteid]}

class SKDACTIVITYQBE(Base):
	__table__ = Table('SKDACTIVITYQBE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class SKDPROJECT(Base):
	__table__ = Table('SKDPROJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.name]}

class SLAASSETLOC(Base):
	__table__ = Table('SLAASSETLOC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.assettype, __table__.c.location, __table__.c.siteid, __table__.c.slanum]}

class SLROUTE(Base):
	__table__ = Table('SLROUTE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.slrouteid]}

class SPRELATEDASSET(Base):
	__table__ = Table('SPRELATEDASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.sprelatedassetid]}

class SPWORKASSET(Base):
	__table__ = Table('SPWORKASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.spworkassetid]}

class TAGOUT(Base):
	__table__ = Table('TAGOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.tagoutid]}

class TOOLINV(Base):
	__table__ = Table('TOOLINV', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.itemsetid, __table__.c.location, __table__.c.siteid]}

class TOOLTRANS(Base):
	__table__ = Table('TOOLTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.siteid, __table__.c.tooltransid]}

class UNASSIGNEDWORKVIEW(Base):
	__table__ = Table('UNASSIGNEDWORKVIEW', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wonum]}

class WARRANTYASSET(Base):
	__table__ = Table('WARRANTYASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetid, __table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum, __table__.c.warrantyassetid]}

class WOACTIVITY(Base):
	__table__ = Table('WOACTIVITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class WOASSETUSERCUST(Base):
	__table__ = Table('WOASSETUSERCUST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.location, __table__.c.personid, __table__.c.siteid]}

class WOCHANGE(Base):
	__table__ = Table('WOCHANGE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class WOCONTRACT(Base):
	__table__ = Table('WOCONTRACT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wocontractid]}

class WOGEN(Base):
	__table__ = Table('WOGEN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.runid, __table__.c.runorder, __table__.c.siteid]}

class WOLOCKOUT(Base):
	__table__ = Table('WOLOCKOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wolockoutid]}

class WOLOCUSERCUST(Base):
	__table__ = Table('WOLOCUSERCUST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.location, __table__.c.personid, __table__.c.siteid]}

class WOMATSTATUSSYNC(Base):
	__table__ = Table('WOMATSTATUSSYNC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.itemsetid, __table__.c.location, __table__.c.siteid]}

class WORELEASE(Base):
	__table__ = Table('WORELEASE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class WORKORDER(Base):
	__table__ = Table('WORKORDER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class WOSAFETYLINK(Base):
	__table__ = Table('WOSAFETYLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wosafetylinkid]}

class WOTAGOUT(Base):
	__table__ = Table('WOTAGOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.tagoutid, __table__.c.wonum, __table__.c.wosafetydatasource]}

class WPITEM(Base):
	__table__ = Table('WPITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wpitemid]}

class WPMATERIAL(Base):
	__table__ = Table('WPMATERIAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wpitemid]}

class WPSERVICE(Base):
	__table__ = Table('WPSERVICE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wpitemid]}

class WPTOOL(Base):
	__table__ = Table('WPTOOL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wpitemid]}


class SYCLOLOCANCESTORUP(Base):
    __table__ = Table('SYCLOLOCANCESTORUP', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.LOCATION]}


