from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session
from parameters import *
import base64

decpass = base64.b64decode(dbpass)

connectstring = 'mssql+pyodbc://' + dbuser + ':' + decpass + '@' + dbserver + '/' + db + ';Trusted_Connection=Yes' 
Base = declarative_base()
engine = create_engine(connectstring)
metadata = MetaData(bind=engine)
session = create_session(bind=engine)

class ACCOUNTDEFAULTS(Base):
	__table__ = Table('ACCOUNTDEFAULTS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dfltgroup, __table__.c.groupvalue, __table__.c.orgid]}

class ACTCI(Base):
	__table__ = Table('ACTCI', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.actcinum]}

class ACTCIRELATION(Base):
	__table__ = Table('ACTCIRELATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.relationnum, __table__.c.sourceci, __table__.c.targetci]}

class ACTCISPEC(Base):
	__table__ = Table('ACTCISPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.actcinum, __table__.c.assetattrid, __table__.c.section]}

class ACTION(Base):
	__table__ = Table('ACTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.action]}

class ACTIONGROUP(Base):
	__table__ = Table('ACTIONGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.action, __table__.c.member, __table__.c.sequence]}

class ACTIONSCFG(Base):
	__table__ = Table('ACTIONSCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.actionscfgid]}

class ADDRESS(Base):
	__table__ = Table('ADDRESS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.addresscode, __table__.c.orgid]}

class ALNDOMAIN(Base):
	__table__ = Table('ALNDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.domainid, __table__.c.orgid, __table__.c.siteid, __table__.c.value]}

class ALTITEM(Base):
	__table__ = Table('ALTITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.altitemnum, __table__.c.itemnum, __table__.c.itemsetid]}

class AMCREW(Base):
	__table__ = Table('AMCREW', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrew, __table__.c.orgid]}

class AMCREWLABOR(Base):
	__table__ = Table('AMCREWLABOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrew, __table__.c.amcrewlaborid, __table__.c.orgid, __table__.c.position]}

class AMCREWLABPOS(Base):
	__table__ = Table('AMCREWLABPOS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrew, __table__.c.orgid, __table__.c.position]}

class AMCREWMODAVAIL(Base):
	__table__ = Table('AMCREWMODAVAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrewmodavailid]}

class AMCREWQUAL(Base):
	__table__ = Table('AMCREWQUAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrew, __table__.c.orgid, __table__.c.position, __table__.c.qualificationid, __table__.c.tool]}

class AMCREWSTATHIS(Base):
	__table__ = Table('AMCREWSTATHIS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrew, __table__.c.changedate, __table__.c.orgid, __table__.c.status]}

class AMCREWT(Base):
	__table__ = Table('AMCREWT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrewtype, __table__.c.orgid]}

class AMCREWTOOL(Base):
	__table__ = Table('AMCREWTOOL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrew, __table__.c.effectivedate, __table__.c.orgid, __table__.c.toolseq]}

class AMCREWTOOLSQ(Base):
	__table__ = Table('AMCREWTOOLSQ', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrew, __table__.c.orgid, __table__.c.toolseq]}

class AMCREWWOLAB(Base):
	__table__ = Table('AMCREWWOLAB', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrewwolabid]}

class AMCREWWOTL(Base):
	__table__ = Table('AMCREWWOTL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrewwotlid]}

class AMCTCRAFT(Base):
	__table__ = Table('AMCTCRAFT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrewtype, __table__.c.orgid, __table__.c.position]}

class AMCTQUAL(Base):
	__table__ = Table('AMCTQUAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrewtype, __table__.c.orgid, __table__.c.position, __table__.c.qualificationid, __table__.c.tool]}

class AMCTSTATHIST(Base):
	__table__ = Table('AMCTSTATHIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amctstathistid, __table__.c.orgid]}

class AMCTTOOL(Base):
	__table__ = Table('AMCTTOOL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.amcrewtype, __table__.c.orgid, __table__.c.toolseq]}

class APPDOCTYPE(Base):
	__table__ = Table('APPDOCTYPE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.doctype]}

class APPFIELDDEFAULTS(Base):
	__table__ = Table('APPFIELDDEFAULTS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.attributename, __table__.c.grpname, __table__.c.objectname, __table__.c.siteid, __table__.c.username]}

class APPLICATIONAUTH(Base):
	__table__ = Table('APPLICATIONAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.groupname, __table__.c.optionname]}

class ARCHIVE(Base):
	__table__ = Table('ARCHIVE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.archivedate, __table__.c.module]}

class AREASAFFECTED(Base):
	__table__ = Table('AREASAFFECTED', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.areasaffectedid, __table__.c.siteid, __table__.c.wonum]}

class ASSET(Base):
	__table__ = Table('ASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.siteid]}

class ASSETANCESTOR(Base):
	__table__ = Table('ASSETANCESTOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ancestor, __table__.c.assetnum, __table__.c.siteid]}

class ASSETATTRIBUTE(Base):
	__table__ = Table('ASSETATTRIBUTE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.orgid, __table__.c.siteid]}

class ASSETFEASPECHIST(Base):
	__table__ = Table('ASSETFEASPECHIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.assetfeaturespecid, __table__.c.assetnum, __table__.c.createddate, __table__.c.feature, __table__.c.section, __table__.c.siteid]}

class ASSETFEATURE(Base):
	__table__ = Table('ASSETFEATURE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.feature, __table__.c.linearassetfeatureid, __table__.c.siteid]}

class ASSETFEATUREHIST(Base):
	__table__ = Table('ASSETFEATUREHIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetfeaturehistid]}

class ASSETFEATURESPEC(Base):
	__table__ = Table('ASSETFEATURESPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.assetnum, __table__.c.feature, __table__.c.linearassetfeaturespecid, __table__.c.section, __table__.c.siteid]}

class ASSETHIERARCHY(Base):
	__table__ = Table('ASSETHIERARCHY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.siteid, __table__.c.wonum]}

class ASSETHISTORY(Base):
	__table__ = Table('ASSETHISTORY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assethistoryid]}

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

class ASSETMETER(Base):
	__table__ = Table('ASSETMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.linearassetmeterid, __table__.c.metername, __table__.c.siteid]}

class ASSETMNTSKD(Base):
	__table__ = Table('ASSETMNTSKD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.ophrs, __table__.c.siteid, __table__.c.startdatetime]}

class ASSETOPSKD(Base):
	__table__ = Table('ASSETOPSKD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.ophrs, __table__.c.siteid, __table__.c.startdatetime]}

class ASSETSPEC(Base):
	__table__ = Table('ASSETSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.assetnum, __table__.c.linearassetspecid, __table__.c.section, __table__.c.siteid]}

class ASSETSPECHIST(Base):
	__table__ = Table('ASSETSPECHIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.assetnum, __table__.c.assetspecid, __table__.c.createddate, __table__.c.section, __table__.c.siteid]}

class ASSETSTATUS(Base):
	__table__ = Table('ASSETSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetstatusid]}

class ASSETTOPOCACHE(Base):
	__table__ = Table('ASSETTOPOCACHE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assettopocacheid]}

class ASSETTRANS(Base):
	__table__ = Table('ASSETTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assettransid]}

class ASSIGNMENT(Base):
	__table__ = Table('ASSIGNMENT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assignmentid]}

class ASTMSOVER(Base):
	__table__ = Table('ASTMSOVER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.name]}

class ASTSPECMSOVER(Base):
	__table__ = Table('ASTSPECMSOVER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.name]}

class ATTENDANCE(Base):
	__table__ = Table('ATTENDANCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.attendanceid]}

class AUTOATTRUPDATE(Base):
	__table__ = Table('AUTOATTRUPDATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.autoattrupdateid]}

class AUTOKEY(Base):
	__table__ = Table('AUTOKEY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.autokeyname, __table__.c.orgid, __table__.c.setid, __table__.c.siteid]}

class AUTOSCRIPT(Base):
	__table__ = Table('AUTOSCRIPT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.autoscript]}

class AUTOSCRIPTSTATE(Base):
	__table__ = Table('AUTOSCRIPTSTATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.autoscriptstateid]}

class AUTOSCRIPTVARS(Base):
	__table__ = Table('AUTOSCRIPTVARS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.autoscript, __table__.c.varname]}

class BBOARDAUDIENCE(Base):
	__table__ = Table('BBOARDAUDIENCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.bboardaudienceid]}

class BBOARDMSGSTATUS(Base):
	__table__ = Table('BBOARDMSGSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.bboardmsgstatusid]}

class BBSTATUSHISTORY(Base):
	__table__ = Table('BBSTATUSHISTORY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.bbstatushistoryid]}

class BILLTOSHIPTO(Base):
	__table__ = Table('BILLTOSHIPTO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.addresscode, __table__.c.orgid, __table__.c.siteid]}

class BOOKMARK(Base):
	__table__ = Table('BOOKMARK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.keyvalue, __table__.c.userid]}

class BULLETINBOARD(Base):
	__table__ = Table('BULLETINBOARD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.bulletinboardid]}

class CALENDAR(Base):
	__table__ = Table('CALENDAR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.calnum, __table__.c.orgid]}

class CALENDARBREAK(Base):
	__table__ = Table('CALENDARBREAK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.calendarbreakid, __table__.c.orgid]}

class CDMCITYPES(Base):
	__table__ = Table('CDMCITYPES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cdmcitypesid]}

class CHARPOINTACTION(Base):
	__table__ = Table('CHARPOINTACTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pointnum, __table__.c.siteid, __table__.c.value]}

class CHARTOFACCOUNTS(Base):
	__table__ = Table('CHARTOFACCOUNTS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.glaccount, __table__.c.orgid]}

class CI(Base):
	__table__ = Table('CI', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cinum]}

class CIRELATION(Base):
	__table__ = Table('CIRELATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.relationnum, __table__.c.sourceci, __table__.c.targetci]}

class CIRELATIONHIS(Base):
	__table__ = Table('CIRELATIONHIS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.relationnum, __table__.c.sourceci, __table__.c.startdate, __table__.c.targetci]}

class CISPEC(Base):
	__table__ = Table('CISPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.cinum, __table__.c.section]}

class CISPECHIS(Base):
	__table__ = Table('CISPECHIS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.cinum, __table__.c.section, __table__.c.startdate]}

class CISTATUS(Base):
	__table__ = Table('CISTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cistatusid]}

class CITEMPLATE(Base):
	__table__ = Table('CITEMPLATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.citemplateid]}

class CITYPESTATUS(Base):
	__table__ = Table('CITYPESTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.citypestatusid]}

class CLASSANCESTOR(Base):
	__table__ = Table('CLASSANCESTOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ancestor, __table__.c.classstructureid]}

class CLASSIFICATION(Base):
	__table__ = Table('CLASSIFICATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.classificationid, __table__.c.orgid, __table__.c.siteid]}

class CLASSSPEC(Base):
	__table__ = Table('CLASSSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.classstructureid, __table__.c.orgid, __table__.c.section, __table__.c.siteid]}

class CLASSSPECUSEWITH(Base):
	__table__ = Table('CLASSSPECUSEWITH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.classstructureid, __table__.c.objectname, __table__.c.orgid, __table__.c.section, __table__.c.siteid]}

class CLASSSTRUCTURE(Base):
	__table__ = Table('CLASSSTRUCTURE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.classstructureid]}

class CLASSUSEWITH(Base):
	__table__ = Table('CLASSUSEWITH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.classstructureid, __table__.c.objectname]}

class COLLECTDETAILS(Base):
	__table__ = Table('COLLECTDETAILS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.collectdetailsid]}

class COLLECTION(Base):
	__table__ = Table('COLLECTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.collectionnum]}

class COLLECTIONAUTH(Base):
	__table__ = Table('COLLECTIONAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.collectionnum, __table__.c.groupname]}

class COMMLOG(Base):
	__table__ = Table('COMMLOG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.commlogid]}

class COMMLOGDOCS(Base):
	__table__ = Table('COMMLOGDOCS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.commlogdocsid]}

class COMMODITIES(Base):
	__table__ = Table('COMMODITIES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.commodity, __table__.c.itemsetid]}

class COMMTEMPLATE(Base):
	__table__ = Table('COMMTEMPLATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.templateid]}

class COMMTEMPLATEDOCS(Base):
	__table__ = Table('COMMTEMPLATEDOCS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.doctype, __table__.c.templateid]}

class COMMTMPLTSENDTO(Base):
	__table__ = Table('COMMTMPLTSENDTO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.sendtovalue, __table__.c.templateid, __table__.c.type]}

class COMPANIES(Base):
	__table__ = Table('COMPANIES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.company, __table__.c.orgid]}

class COMPANYACCDEF(Base):
	__table__ = Table('COMPANYACCDEF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.type]}

class COMPCOMMODITY(Base):
	__table__ = Table('COMPCOMMODITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.compcommodityid]}

class COMPCONTACT(Base):
	__table__ = Table('COMPCONTACT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.company, __table__.c.contact, __table__.c.orgid]}

class COMPCONTACTMSTR(Base):
	__table__ = Table('COMPCONTACTMSTR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.company, __table__.c.companysetid, __table__.c.contact]}

class COMPMASTER(Base):
	__table__ = Table('COMPMASTER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.company, __table__.c.companysetid]}

class CONDITION(Base):
	__table__ = Table('CONDITION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.conditionnum]}

class CONTASSETMETER(Base):
	__table__ = Table('CONTASSETMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contassetmeterid]}

class CONTCOMMODITY(Base):
	__table__ = Table('CONTCOMMODITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contcommodityid]}

class CONTLINEASSET(Base):
	__table__ = Table('CONTLINEASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contlineassetid]}

class CONTLINEMETER(Base):
	__table__ = Table('CONTLINEMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contlinemeterid]}

class CONTRACT(Base):
	__table__ = Table('CONTRACT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum]}

class CONTRACTASSET(Base):
	__table__ = Table('CONTRACTASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractassetid]}

class CONTRACTAUTH(Base):
	__table__ = Table('CONTRACTAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.authorgid, __table__.c.authsiteid, __table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum, __table__.c.vendor]}

class CONTRACTDEFAULT(Base):
	__table__ = Table('CONTRACTDEFAULT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.maxcontracttype, __table__.c.propertyid]}

class CONTRACTLEASE(Base):
	__table__ = Table('CONTRACTLEASE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum]}

class CONTRACTLINE(Base):
	__table__ = Table('CONTRACTLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractlinenum, __table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum]}

class CONTRACTMASTER(Base):
	__table__ = Table('CONTRACTMASTER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum]}

class CONTRACTPROPERTY(Base):
	__table__ = Table('CONTRACTPROPERTY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.propertyid]}

class CONTRACTPURCH(Base):
	__table__ = Table('CONTRACTPURCH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum]}

class CONTRACTSFW(Base):
	__table__ = Table('CONTRACTSFW', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum]}

class CONTRACTSTATUS(Base):
	__table__ = Table('CONTRACTSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractstatusid]}

class CONTRACTSWLIC(Base):
	__table__ = Table('CONTRACTSWLIC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum]}

class CONTRACTTERM(Base):
	__table__ = Table('CONTRACTTERM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contracttermid]}

class CONTRACTTYPE(Base):
	__table__ = Table('CONTRACTTYPE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contracttypeid, __table__.c.orgid]}

class CONTRACTTYPETERM(Base):
	__table__ = Table('CONTRACTTYPETERM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contracttypetermid]}

class CONTSFWLIC(Base):
	__table__ = Table('CONTSFWLIC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contsfwlicid]}

class CONVERSION(Base):
	__table__ = Table('CONVERSION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.frommeasureunit, __table__.c.itemnum, __table__.c.itemsetid, __table__.c.tomeasureunit]}

class COSTTYPE(Base):
	__table__ = Table('COSTTYPE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.costtype]}

class CRAFT(Base):
	__table__ = Table('CRAFT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.craft, __table__.c.orgid]}

class CRAFTRATE(Base):
	__table__ = Table('CRAFTRATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractnum, __table__.c.craft, __table__.c.orgid, __table__.c.revisionnum, __table__.c.skilllevel, __table__.c.vendor]}

class CRAFTSKILL(Base):
	__table__ = Table('CRAFTSKILL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.craft, __table__.c.orgid, __table__.c.skilllevel]}

class CRONTASKDEF(Base):
	__table__ = Table('CRONTASKDEF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.crontaskname]}

class CRONTASKHISTORY(Base):
	__table__ = Table('CRONTASKHISTORY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.crontaskname, __table__.c.instancename, __table__.c.sequence]}

class CRONTASKINSTANCE(Base):
	__table__ = Table('CRONTASKINSTANCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.crontaskname, __table__.c.instancename]}

class CRONTASKPARAM(Base):
	__table__ = Table('CRONTASKPARAM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.crontaskname, __table__.c.instancename, __table__.c.parameter]}

class CROSSOVERDOMAIN(Base):
	__table__ = Table('CROSSOVERDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.destfield, __table__.c.domainid, __table__.c.orgid, __table__.c.siteid, __table__.c.sourcefield]}

class CTRLCONDITION(Base):
	__table__ = Table('CTRLCONDITION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.conditionnum, __table__.c.ctrlgroupid]}

class CTRLCONDPROP(Base):
	__table__ = Table('CTRLCONDPROP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.conditionresult, __table__.c.ctrlconditionid, __table__.c.property]}

class CTRLGROUP(Base):
	__table__ = Table('CTRLGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.groupname, __table__.c.optionname]}

class CURRENCY(Base):
	__table__ = Table('CURRENCY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.currencycode]}

class DEFAULTQUERY(Base):
	__table__ = Table('DEFAULTQUERY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.clausename, __table__.c.userid]}

class DEPLOYEDASSET(Base):
	__table__ = Table('DEPLOYEDASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid]}

class DMCFGGROUP(Base):
	__table__ = Table('DMCFGGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cfgobjgroup]}

class DMCFGOBJECT(Base):
	__table__ = Table('DMCFGOBJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cfgobject, __table__.c.cfgobjgroup]}

class DMCOLLAPPTOOLBAR(Base):
	__table__ = Table('DMCOLLAPPTOOLBAR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dmcollapptoolbarid]}

class DMCOLLECTION(Base):
	__table__ = Table('DMCOLLECTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.collection, __table__.c.source]}

class DMCOLLECTIONEXPORT(Base):
	__table__ = Table('DMCOLLECTIONEXPORT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dmcollectionobjectid, __table__.c.filename]}

class DMCOLLECTIONOBJECT(Base):
	__table__ = Table('DMCOLLECTIONOBJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.collection, __table__.c.object, __table__.c.objectid, __table__.c.source]}

class DMCOLLECTIONRELOBJ(Base):
	__table__ = Table('DMCOLLECTIONRELOBJ', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cfgobject, __table__.c.dmcollectionobjectid, __table__.c.object, __table__.c.objectid]}

class DMCOLLEVENTTRK(Base):
	__table__ = Table('DMCOLLEVENTTRK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.dmcollectionid, __table__.c.intobjectname]}

class DMCOLLLOOKUPRULE(Base):
	__table__ = Table('DMCOLLLOOKUPRULE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.lookuprule]}

class DMCOLLPACKAGEMAP(Base):
	__table__ = Table('DMCOLLPACKAGEMAP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dmcollpackagemapid]}

class DMCOLLPKGEXCEPTION(Base):
	__table__ = Table('DMCOLLPKGEXCEPTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.exception]}

class DMCOLLRELRULE(Base):
	__table__ = Table('DMCOLLRELRULE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.relrule]}

class DMCOLLRELRULECOLS(Base):
	__table__ = Table('DMCOLLRELRULECOLS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dmcollrelrulecolsid]}

class DMCOMPJOB(Base):
	__table__ = Table('DMCOMPJOB', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.compjobnum, __table__.c.pkgdefname, __table__.c.source]}

class DMCOMPRESRECORD(Base):
	__table__ = Table('DMCOMPRESRECORD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dmcompresrecordid]}

class DMCOMPRESULT(Base):
	__table__ = Table('DMCOMPRESULT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.compjobnum, __table__.c.localuniqueid, __table__.c.objectname, __table__.c.remoteuniqueid]}

class DMDEPENDENCY(Base):
	__table__ = Table('DMDEPENDENCY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dependentgroup, __table__.c.dependinggroup]}

class DMERROR(Base):
	__table__ = Table('DMERROR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.errordate, __table__.c.package, __table__.c.pkgdefname, __table__.c.source]}

class DMMAPDEF(Base):
	__table__ = Table('DMMAPDEF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.attributename, __table__.c.objectname, __table__.c.pkgdefname, __table__.c.source]}

class DMMESSAGE(Base):
	__table__ = Table('DMMESSAGE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dmmessageid]}

class DMPACKAGE(Base):
	__table__ = Table('DMPACKAGE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.package, __table__.c.pkgdefname, __table__.c.source]}

class DMPACKAGEDEF(Base):
	__table__ = Table('DMPACKAGEDEF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pkgdefname, __table__.c.source]}

class DMPKGCFGGRPDEF(Base):
	__table__ = Table('DMPKGCFGGRPDEF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cfgobjgroup, __table__.c.pkgdefname, __table__.c.source]}

class DMPKGCFGOBJDEF(Base):
	__table__ = Table('DMPKGCFGOBJDEF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cfgobject, __table__.c.cfgobjgroup, __table__.c.pkgdefname, __table__.c.source]}

class DMPKGCMPSRC(Base):
	__table__ = Table('DMPKGCMPSRC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cmpsrcfile, __table__.c.package, __table__.c.pkgdefname, __table__.c.source]}

class DMPKGCMPSRCDEF(Base):
	__table__ = Table('DMPKGCMPSRCDEF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cmpsrcfile, __table__.c.pkgdefname, __table__.c.source]}

class DMPKGDEFSTATUS(Base):
	__table__ = Table('DMPKGDEFSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dmpkgdefstatusid]}

class DMPKGDIST(Base):
	__table__ = Table('DMPKGDIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pkgdefname, __table__.c.source, __table__.c.targetname]}

class DMPKGDISTTRACK(Base):
	__table__ = Table('DMPKGDISTTRACK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.distributiondate, __table__.c.package, __table__.c.pkgdefname, __table__.c.source, __table__.c.targetname]}

class DMPKGDSTTRGT(Base):
	__table__ = Table('DMPKGDSTTRGT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.targetname]}

class DMPKGEVENTTRK(Base):
	__table__ = Table('DMPKGEVENTTRK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.action, __table__.c.object, __table__.c.objectid, __table__.c.pkgdefname, __table__.c.source]}

class DMPKGSTAGING(Base):
	__table__ = Table('DMPKGSTAGING', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cfgdataorder, __table__.c.package, __table__.c.pkgdefname, __table__.c.source, __table__.c.type]}

class DMPKGSTATUS(Base):
	__table__ = Table('DMPKGSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.package, __table__.c.pkgdefname, __table__.c.progressstatus, __table__.c.redistributesrc, __table__.c.source, __table__.c.status]}

class DMPKGTRACKHIST(Base):
	__table__ = Table('DMPKGTRACKHIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.action, __table__.c.object, __table__.c.objectid, __table__.c.pkgdefname, __table__.c.source]}

class DMRESTRICTION(Base):
	__table__ = Table('DMRESTRICTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.instancehost, __table__.c.instancename, __table__.c.instanceschema]}

class DMSAPISETTING(Base):
	__table__ = Table('DMSAPISETTING', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dmsname]}

class DOCINFO(Base):
	__table__ = Table('DOCINFO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.docinfoid]}

class DOCLINKS(Base):
	__table__ = Table('DOCLINKS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.docinfoid, __table__.c.doctype, __table__.c.ownerid, __table__.c.ownertable]}

class DOCTYPES(Base):
	__table__ = Table('DOCTYPES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.doctype]}

class DPACOMMDEVICE(Base):
	__table__ = Table('DPACOMMDEVICE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.deviceid]}

class DPACOMPUTER(Base):
	__table__ = Table('DPACOMPUTER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid]}

class DPACPU(Base):
	__table__ = Table('DPACPU', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cpuid]}

class DPADISK(Base):
	__table__ = Table('DPADISK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.diskid]}

class DPADISPLAY(Base):
	__table__ = Table('DPADISPLAY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.displayid]}

class DPAFILE(Base):
	__table__ = Table('DPAFILE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.fileid]}

class DPAIMAGEDEVICE(Base):
	__table__ = Table('DPAIMAGEDEVICE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.deviceid]}

class DPAIPX(Base):
	__table__ = Table('DPAIPX', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ipxid]}

class DPALOGICALDRIVE(Base):
	__table__ = Table('DPALOGICALDRIVE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.logicaldriveid]}

class DPAMADAPTER(Base):
	__table__ = Table('DPAMADAPTER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.adapterid]}

class DPAMADPTVARIANT(Base):
	__table__ = Table('DPAMADPTVARIANT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dpamadptvariantid]}

class DPAMEDIAADAPTER(Base):
	__table__ = Table('DPAMEDIAADAPTER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.adapterid]}

class DPAMMANUFACTURER(Base):
	__table__ = Table('DPAMMANUFACTURER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.manufacturerid]}

class DPAMMANUVARIANT(Base):
	__table__ = Table('DPAMMANUVARIANT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dpammanuvariantid]}

class DPAMOS(Base):
	__table__ = Table('DPAMOS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.osid]}

class DPAMOSVARIANT(Base):
	__table__ = Table('DPAMOSVARIANT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dpamosvariantid]}

class DPAMPROCESSOR(Base):
	__table__ = Table('DPAMPROCESSOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.processorid]}

class DPAMPROCVARIANT(Base):
	__table__ = Table('DPAMPROCVARIANT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dpamprocvariantid]}

class DPAMSOFTWARE(Base):
	__table__ = Table('DPAMSOFTWARE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.softwareid]}

class DPAMSWSUITE(Base):
	__table__ = Table('DPAMSWSUITE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.suitename]}

class DPAMSWSUITECOMP(Base):
	__table__ = Table('DPAMSWSUITECOMP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dpamswsuitecompid]}

class DPAMSWUSAGE(Base):
	__table__ = Table('DPAMSWUSAGE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.swdetectiontool]}

class DPAMSWUSAGERANGE(Base):
	__table__ = Table('DPAMSWUSAGERANGE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dpamswusagerangeid]}

class DPAMSWVARIANT(Base):
	__table__ = Table('DPAMSWVARIANT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dpamswvariantid]}

class DPANETADAPTER(Base):
	__table__ = Table('DPANETADAPTER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.adapterid]}

class DPANETDEVCARD(Base):
	__table__ = Table('DPANETDEVCARD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cardid]}

class DPANETDEVICE(Base):
	__table__ = Table('DPANETDEVICE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid]}

class DPANETPRINTER(Base):
	__table__ = Table('DPANETPRINTER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid]}

class DPAOS(Base):
	__table__ = Table('DPAOS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.osid]}

class DPASOFTWARE(Base):
	__table__ = Table('DPASOFTWARE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.softwareid]}

class DPASWSUITE(Base):
	__table__ = Table('DPASWSUITE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dpaswsuiteid]}

class DPATCPIP(Base):
	__table__ = Table('DPATCPIP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tcpipid]}

class DPAUSERINFO(Base):
	__table__ = Table('DPAUSERINFO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid, __table__.c.personid]}

class DUMMY_TABLE(Base):
	__table__ = Table('DUMMY_TABLE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dummy_aln]}

class EMAIL(Base):
	__table__ = Table('EMAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.emailaddress]}

class ESCALATION(Base):
	__table__ = Table('ESCALATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.escalation]}

class ESCNOTIFICATION(Base):
	__table__ = Table('ESCNOTIFICATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.escalation, __table__.c.refpointnum, __table__.c.templateid]}

class ESCREFPOINT(Base):
	__table__ = Table('ESCREFPOINT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.escalation, __table__.c.refpointnum]}

class ESCREPEATTRACK(Base):
	__table__ = Table('ESCREPEATTRACK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.escalation, __table__.c.objectname, __table__.c.ownerid, __table__.c.refpointid]}

class ESCSTATUS(Base):
	__table__ = Table('ESCSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.escstatusid]}

class EVENTRESPONSE(Base):
	__table__ = Table('EVENTRESPONSE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.erid]}

class EXCHANGE(Base):
	__table__ = Table('EXCHANGE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.currencycode, __table__.c.currencycodeto, __table__.c.expiredate, __table__.c.orgid]}

class EXCLUDEDACTIONS(Base):
	__table__ = Table('EXCLUDEDACTIONS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.excludedactionsid]}

class EXCLUDEPASSWORD(Base):
	__table__ = Table('EXCLUDEPASSWORD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.password]}

class FACONFIG(Base):
	__table__ = Table('FACONFIG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.faconfigid]}

class FAILURECODE(Base):
	__table__ = Table('FAILURECODE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.failurecode, __table__.c.orgid]}

class FAILURELIST(Base):
	__table__ = Table('FAILURELIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.failurelist, __table__.c.orgid]}

class FAILUREREMARK(Base):
	__table__ = Table('FAILUREREMARK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.ticketclass, __table__.c.ticketid, __table__.c.wonum]}

class FAILUREREPORT(Base):
	__table__ = Table('FAILUREREPORT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.failurereportid]}

class FAVITEM(Base):
	__table__ = Table('FAVITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.description, __table__.c.itemnum, __table__.c.itemsetid, __table__.c.personid, __table__.c.storeroom, __table__.c.storeroomsite]}

class FEATURES(Base):
	__table__ = Table('FEATURES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.feature]}

class FEATURESPEC(Base):
	__table__ = Table('FEATURESPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.feature, __table__.c.section]}

class FEATURESTATUS(Base):
	__table__ = Table('FEATURESTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.featurestatusid]}

class FINANCIALPERIODS(Base):
	__table__ = Table('FINANCIALPERIODS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.financialperiod, __table__.c.orgid]}

class FINCNTRL(Base):
	__table__ = Table('FINCNTRL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.fincntrlid, __table__.c.orgid]}

class FSNCLASS(Base):
	__table__ = Table('FSNCLASS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cid]}

class FSNCLASSQUAL(Base):
	__table__ = Table('FSNCLASSQUAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cqid]}

class FSNCLASSRELATION(Base):
	__table__ = Table('FSNCLASSRELATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.crid]}

class FSNLASTSCAN(Base):
	__table__ = Table('FSNLASTSCAN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mappingname, __table__.c.sourceid]}

class FSNMETHOD(Base):
	__table__ = Table('FSNMETHOD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mid]}

class FSNMETHODPARAM(Base):
	__table__ = Table('FSNMETHODPARAM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mpid]}

class FSNMTHDPARAMQUAL(Base):
	__table__ = Table('FSNMTHDPARAMQUAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mpqid]}

class FSNMTHDQUAL(Base):
	__table__ = Table('FSNMTHDQUAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mqid]}

class FSNOBJECT(Base):
	__table__ = Table('FSNOBJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.oid]}

class FSNOBJPROPERTY(Base):
	__table__ = Table('FSNOBJPROPERTY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.oid, __table__.c.pid]}

class FSNOBJRELATION(Base):
	__table__ = Table('FSNOBJRELATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.childoid, __table__.c.crid, __table__.c.parentoid]}

class FSNPROPERTY(Base):
	__table__ = Table('FSNPROPERTY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pid]}

class FSNPROPERTYQUAL(Base):
	__table__ = Table('FSNPROPERTYQUAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pqid]}

class FSNPROVIDER(Base):
	__table__ = Table('FSNPROVIDER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.provid]}

class FSNQUALIFIER(Base):
	__table__ = Table('FSNQUALIFIER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.qid]}

class FSNREFPROPERTY(Base):
	__table__ = Table('FSNREFPROPERTY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.crid, __table__.c.pid, __table__.c.refertocid, __table__.c.refertopid]}

class FSNSCHEMA(Base):
	__table__ = Table('FSNSCHEMA', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.sid]}

class FSNSQLCOLUMN(Base):
	__table__ = Table('FSNSQLCOLUMN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cid, __table__.c.pid, __table__.c.tid]}

class FSNSQLTABLE(Base):
	__table__ = Table('FSNSQLTABLE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.cid, __table__.c.tid]}

class FSNTABLEQUAL(Base):
	__table__ = Table('FSNTABLEQUAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tqid]}

class GLAUTH(Base):
	__table__ = Table('GLAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.glaccountfield, __table__.c.groupname, __table__.c.orgid]}

class GLCOMPONENTS(Base):
	__table__ = Table('GLCOMPONENTS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.compvalue, __table__.c.glorder, __table__.c.orgid]}

class GLCONFIGURE(Base):
	__table__ = Table('GLCONFIGURE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.glorder, __table__.c.orgid]}

# class GLNAVTEMPORG(Base):
# 	__table__ = Table('GLNAVTEMPORG', metadata, autoload=True)
# 	__mapper_args__ = {'primary_key':[__table__.c.orgid]}

class GROUPUSER(Base):
	__table__ = Table('GROUPUSER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.userid]}

class GRPREASSIGNAUTH(Base):
	__table__ = Table('GRPREASSIGNAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.userid]}

class HAZARD(Base):
	__table__ = Table('HAZARD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.hazardid, __table__.c.orgid]}

class HAZARDPREC(Base):
	__table__ = Table('HAZARDPREC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.hazardid, __table__.c.precautionid, __table__.c.siteid]}

class IBMCONTENTCATALOG(Base):
	__table__ = Table('IBMCONTENTCATALOG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ibmcontentcatalogid]}

class IBMCONTENTRECEIPTS(Base):
	__table__ = Table('IBMCONTENTRECEIPTS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ibmcontentreceiptsid]}

class IMGLIB(Base):
	__table__ = Table('IMGLIB', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.imglibid]}

class IMPROFILE(Base):
	__table__ = Table('IMPROFILE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.improfileid]}

class INBCOMMSECURITY(Base):
	__table__ = Table('INBCOMMSECURITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.emailaddress, __table__.c.mailserver, __table__.c.objectname]}

class INBOUNDCOMM(Base):
	__table__ = Table('INBOUNDCOMM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.inboundcommid]}

class INBOUNDCOMMCFG(Base):
	__table__ = Table('INBOUNDCOMMCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.emailaddress, __table__.c.mailserver]}

class INBXCONFIG(Base):
	__table__ = Table('INBXCONFIG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.inbxconfigid]}

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

class INVOICE(Base):
	__table__ = Table('INVOICE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invoicenum, __table__.c.siteid]}

class INVOICECOST(Base):
	__table__ = Table('INVOICECOST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.costlinenum, __table__.c.invoicelinenum, __table__.c.invoicenum, __table__.c.siteid]}

class INVOICELINE(Base):
	__table__ = Table('INVOICELINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invoicelinenum, __table__.c.invoicenum, __table__.c.siteid]}

class INVOICEMATCH(Base):
	__table__ = Table('INVOICEMATCH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invoicematchid]}

class INVOICESTATUS(Base):
	__table__ = Table('INVOICESTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invoicestatusid]}

class INVOICETERM(Base):
	__table__ = Table('INVOICETERM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invoicetermid]}

class INVOICETRANS(Base):
	__table__ = Table('INVOICETRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invoicetransid]}

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

class INVUSESTATUS(Base):
	__table__ = Table('INVUSESTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.invusestatusid]}

class INVVENDOR(Base):
	__table__ = Table('INVVENDOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.catalogcode, __table__.c.conditioncode, __table__.c.itemnum, __table__.c.itemsetid, __table__.c.manufacturer, __table__.c.modelnum, __table__.c.orgid, __table__.c.siteid, __table__.c.vendor]}

# class ISSUECURRENTITEM(Base):
# 	__table__ = Table('ISSUECURRENTITEM', metadata, autoload=True)
# 	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.itemnum, __table__.c.itemsetid, __table__.c.tositeid]}

class ITEM(Base):
	__table__ = Table('ITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.itemsetid]}

class ITEMCONDITION(Base):
	__table__ = Table('ITEMCONDITION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.conditioncode, __table__.c.itemnum, __table__.c.itemsetid]}

class ITEMORGINFO(Base):
	__table__ = Table('ITEMORGINFO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.itemsetid, __table__.c.orgid]}

class ITEMORGSTATUS(Base):
	__table__ = Table('ITEMORGSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemorgstatusid]}

class ITEMSPEC(Base):
	__table__ = Table('ITEMSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.itemnum, __table__.c.itemsetid, __table__.c.section]}

class ITEMSTATUS(Base):
	__table__ = Table('ITEMSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemstatusid]}

class ITEMSTRUCT(Base):
	__table__ = Table('ITEMSTRUCT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.instance, __table__.c.itemid, __table__.c.itemnum, __table__.c.itemsetid]}

class JOBITEM(Base):
	__table__ = Table('JOBITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobitemid]}

class JOBLABOR(Base):
	__table__ = Table('JOBLABOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.joblaborid]}

class JOBPLAN(Base):
	__table__ = Table('JOBPLAN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jpnum, __table__.c.orgid, __table__.c.pluscrevnum, __table__.c.siteid]}

class JOBPLANCLASS(Base):
	__table__ = Table('JOBPLANCLASS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobplanid, __table__.c.woclass]}

class JOBPLANSPEC(Base):
	__table__ = Table('JOBPLANSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.jpnum, __table__.c.orgid, __table__.c.pluscjprevnum, __table__.c.section, __table__.c.siteid]}

class JOBTASK(Base):
	__table__ = Table('JOBTASK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobtaskid]}

class JOBTASKSPEC(Base):
	__table__ = Table('JOBTASKSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.jpnum, __table__.c.jptask, __table__.c.orgid, __table__.c.pluscjprevnum, __table__.c.section, __table__.c.siteid]}

class JPASSETSPLINK(Base):
	__table__ = Table('JPASSETSPLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jpassetsplinkid]}

class JPTASKRELATION(Base):
	__table__ = Table('JPTASKRELATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jptaskrelationid]}

class KPIGCONFIG(Base):
	__table__ = Table('KPIGCONFIG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.kpigconfigid]}

class KPIHISTORY(Base):
	__table__ = Table('KPIHISTORY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.kpihistoryid]}

class KPILCONFIG(Base):
	__table__ = Table('KPILCONFIG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.kpilconfigid]}

class KPIMAIN(Base):
	__table__ = Table('KPIMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.kpiname]}

class KPIOEE(Base):
	__table__ = Table('KPIOEE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.oeedate, __table__.c.partnum, __table__.c.siteid]}

class KPITRENDCFG(Base):
	__table__ = Table('KPITRENDCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.kpitrendcfgid]}

class L_ALNDOMAIN(Base):
	__table__ = Table('L_ALNDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_ASSETATTRIBUTE(Base):
	__table__ = Table('L_ASSETATTRIBUTE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_COMMTEMPLATE(Base):
	__table__ = Table('L_COMMTEMPLATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_COMPANIES(Base):
	__table__ = Table('L_COMPANIES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_CONDITION(Base):
	__table__ = Table('L_CONDITION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_COSTTYPE(Base):
	__table__ = Table('L_COSTTYPE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_CTRLCONDPROP(Base):
	__table__ = Table('L_CTRLCONDPROP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_ITEM(Base):
	__table__ = Table('L_ITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_KPIMAIN(Base):
	__table__ = Table('L_KPIMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAPTIPMENU(Base):
	__table__ = Table('L_MAPTIPMENU', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXAPPS(Base):
	__table__ = Table('L_MAXAPPS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXATTRCFG(Base):
	__table__ = Table('L_MAXATTRCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXATTRIBUTE(Base):
	__table__ = Table('L_MAXATTRIBUTE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXDOMAIN(Base):
	__table__ = Table('L_MAXDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXINTOBJDETAIL(Base):
	__table__ = Table('L_MAXINTOBJDETAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXINTOBJECT(Base):
	__table__ = Table('L_MAXINTOBJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXLABELS(Base):
	__table__ = Table('L_MAXLABELS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXMENU(Base):
	__table__ = Table('L_MAXMENU', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXMESSAGES(Base):
	__table__ = Table('L_MAXMESSAGES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXMODULES(Base):
	__table__ = Table('L_MAXMODULES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXOBJECT(Base):
	__table__ = Table('L_MAXOBJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXOBJECTCFG(Base):
	__table__ = Table('L_MAXOBJECTCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MAXSERVICE(Base):
	__table__ = Table('L_MAXSERVICE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MFMAILCFG(Base):
	__table__ = Table('L_MFMAILCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MFMAILWF(Base):
	__table__ = Table('L_MFMAILWF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_MFMAILWFVALCFG(Base):
	__table__ = Table('L_MFMAILWFVALCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_NUMERICDOMAIN(Base):
	__table__ = Table('L_NUMERICDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_PALETTEITEM(Base):
	__table__ = Table('L_PALETTEITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_QUERY(Base):
	__table__ = Table('L_QUERY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_REPORT(Base):
	__table__ = Table('L_REPORT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_REPORTDESIGN(Base):
	__table__ = Table('L_REPORTDESIGN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_REPORTLABEL(Base):
	__table__ = Table('L_REPORTLABEL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_REPORTLOOKUP(Base):
	__table__ = Table('L_REPORTLOOKUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.l_reportlookupid]}

class L_SIGOPTION(Base):
	__table__ = Table('L_SIGOPTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_SKDACTION(Base):
	__table__ = Table('L_SKDACTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_SKDDATAGROUP(Base):
	__table__ = Table('L_SKDDATAGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_SKDPROPERTY(Base):
	__table__ = Table('L_SKDPROPERTY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_SKDRESOURCEVIEW(Base):
	__table__ = Table('L_SKDRESOURCEVIEW', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class L_SOLUTION(Base):
	__table__ = Table('L_SOLUTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.l_solutionid]}

class L_SYNONYMDOMAIN(Base):
	__table__ = Table('L_SYNONYMDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ownerid]}

class LABOR(Base):
	__table__ = Table('LABOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.laborcode, __table__.c.orgid]}

class LABORAUTH(Base):
	__table__ = Table('LABORAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.laborcode, __table__.c.orgid]}

class LABORCERTHIST(Base):
	__table__ = Table('LABORCERTHIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.laborcerthistid]}

class LABORCRAFTRATE(Base):
	__table__ = Table('LABORCRAFTRATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractnum, __table__.c.craft, __table__.c.laborcode, __table__.c.orgid, __table__.c.skilllevel, __table__.c.vendor]}

class LABORQUAL(Base):
	__table__ = Table('LABORQUAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.laborcode, __table__.c.orgid, __table__.c.qualificationid]}

class LABORQUALSTATUS(Base):
	__table__ = Table('LABORQUALSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.changedate, __table__.c.laborcode, __table__.c.orgid, __table__.c.qualificationid]}

class LABORSTATUS(Base):
	__table__ = Table('LABORSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.laborstatusid]}

class LABTRANS(Base):
	__table__ = Table('LABTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.laborcode, __table__.c.labtransid, __table__.c.siteid]}

class LANGUAGE(Base):
	__table__ = Table('LANGUAGE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.maxlangcode]}

class LAUNCHPOINTVARS(Base):
	__table__ = Table('LAUNCHPOINTVARS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.autoscript, __table__.c.launchpointname, __table__.c.varname]}

class LAYOUT(Base):
	__table__ = Table('LAYOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.layoutid]}

class LBSLOCATION(Base):
	__table__ = Table('LBSLOCATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.lbslocationid]}

class LDAPSYNCPARAMS(Base):
	__table__ = Table('LDAPSYNCPARAMS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.paramname, __table__.c.taskinstance, __table__.c.taskname]}

class LIMITTOLERANCE(Base):
	__table__ = Table('LIMITTOLERANCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.orgid]}

class LINEARREFMETHOD(Base):
	__table__ = Table('LINEARREFMETHOD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.lrm]}

# class LINESPLIT(Base):
# 	__table__ = Table('LINESPLIT', metadata, autoload=True)
# 	__mapper_args__ = {'primary_key':[__table__.c.contentuid]}

class LMO(Base):
	__table__ = Table('LMO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.lmoname, __table__.c.lmonamespace]}

class LMOATT(Base):
	__table__ = Table('LMOATT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.input, __table__.c.lmoname, __table__.c.lmonamespace, __table__.c.name]}

class LMOIMRLN(Base):
	__table__ = Table('LMOIMRLN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.imname, __table__.c.imversion, __table__.c.lmoname, __table__.c.lmonamespace]}

class LNRRECALIB(Base):
	__table__ = Table('LNRRECALIB', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.lnrrecalibid]}

class LNRRECALIBNONAF(Base):
	__table__ = Table('LNRRECALIBNONAF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.lnrrecalibnonafid]}

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

class LOCSYSTEM(Base):
	__table__ = Table('LOCSYSTEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.systemid]}

class LOGINBLOCK(Base):
	__table__ = Table('LOGINBLOCK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.loginblockid]}

class LOGINTRACKING(Base):
	__table__ = Table('LOGINTRACKING', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.logintrackingid]}

class LONGDESCRIPTION(Base):
	__table__ = Table('LONGDESCRIPTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.langcode, __table__.c.ldkey, __table__.c.ldownercol, __table__.c.ldownertable]}

class MAPMANAGER(Base):
	__table__ = Table('MAPMANAGER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mapname]}

class MAPSITES(Base):
	__table__ = Table('MAPSITES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mapname, __table__.c.siteid]}

class MAPTIP(Base):
	__table__ = Table('MAPTIP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mapname, __table__.c.objectname]}

class MAPTIPDEFAULTS(Base):
	__table__ = Table('MAPTIPDEFAULTS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.objectname]}

class MAPTIPMENU(Base):
	__table__ = Table('MAPTIPMENU', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.maptipmenuid]}

class MASTERPM(Base):
	__table__ = Table('MASTERPM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.masterpmnum]}

class MASTERPMMETER(Base):
	__table__ = Table('MASTERPMMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.masterpmnum, __table__.c.metername]}

class MASTERPMSEASONS(Base):
	__table__ = Table('MASTERPMSEASONS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.endday, __table__.c.endmonth, __table__.c.masterpmnum, __table__.c.startday, __table__.c.startmonth]}

class MASTERPMSEQ(Base):
	__table__ = Table('MASTERPMSEQ', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.interval, __table__.c.masterpmnum]}

class MATRECTRANS(Base):
	__table__ = Table('MATRECTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.matrectransid]}

class MATUSETRANS(Base):
	__table__ = Table('MATUSETRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.matusetransid, __table__.c.siteid]}

class MAXAPPS(Base):
	__table__ = Table('MAXAPPS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app]}

class MAXASYNCJOB(Base):
	__table__ = Table('MAXASYNCJOB', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobnum]}

class MAXASYNCJOBMSG(Base):
	__table__ = Table('MAXASYNCJOBMSG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobnum, __table__.c.sequence]}

class MAXASYNCJOBPARAM(Base):
	__table__ = Table('MAXASYNCJOBPARAM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobnum, __table__.c.name]}

class MAXATTRIBUTE(Base):
	__table__ = Table('MAXATTRIBUTE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.attributename, __table__.c.objectname]}

class MAXATTRIBUTECFG(Base):
	__table__ = Table('MAXATTRIBUTECFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.attributename, __table__.c.objectname]}

class MAXATTRIBUTESKIPCOPY(Base):
	__table__ = Table('MAXATTRIBUTESKIPCOPY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.attributename, __table__.c.objectname]}

class MAXCONDDETAIL(Base):
	__table__ = Table('MAXCONDDETAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.condition, __table__.c.condsequence, __table__.c.condtype, __table__.c.ifacename, __table__.c.intobjectname, __table__.c.procname, __table__.c.usewith]}

class MAXCONTROLVALUE(Base):
	__table__ = Table('MAXCONTROLVALUE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacecontrol, __table__.c.newvalue, __table__.c.value]}

class MAXDATAPREFIX(Base):
	__table__ = Table('MAXDATAPREFIX', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.prefix]}

class MAXDOMAIN(Base):
	__table__ = Table('MAXDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.domainid]}

class MAXDOMAINLINK(Base):
	__table__ = Table('MAXDOMAINLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.attributename, __table__.c.domainid, __table__.c.objectname]}

class MAXDOMVALCOND(Base):
	__table__ = Table('MAXDOMVALCOND', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.conditionnum, __table__.c.domainid, __table__.c.objectname, __table__.c.valueid]}

class MAXDYNAMICDOMLINK(Base):
	__table__ = Table('MAXDYNAMICDOMLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.attributename, __table__.c.domainwhere, __table__.c.objectname]}

class MAXENDPOINT(Base):
	__table__ = Table('MAXENDPOINT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.endpointname]}

class MAXENDPOINTDTL(Base):
	__table__ = Table('MAXENDPOINTDTL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.endpointname, __table__.c.property]}

class MAXEXTBOOLVAL(Base):
	__table__ = Table('MAXEXTBOOLVAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacecontrol, __table__.c.orgid, __table__.c.siteid]}

class MAXEXTCTLVAL(Base):
	__table__ = Table('MAXEXTCTLVAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacecontrol, __table__.c.orgid, __table__.c.siteid]}

class MAXEXTIFACEIN(Base):
	__table__ = Table('MAXEXTIFACEIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacename]}

class MAXEXTIFACEOUT(Base):
	__table__ = Table('MAXEXTIFACEOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacename]}

class MAXEXTLISTVAL(Base):
	__table__ = Table('MAXEXTLISTVAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacecontrol, __table__.c.value]}

class MAXEXTOVER(Base):
	__table__ = Table('MAXEXTOVER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacecontrol, __table__.c.orgid, __table__.c.siteid]}

class MAXEXTSYSCONTROL(Base):
	__table__ = Table('MAXEXTSYSCONTROL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacecontrol]}

class MAXEXTSYSTEM(Base):
	__table__ = Table('MAXEXTSYSTEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname]}

class MAXEXTXREFVAL(Base):
	__table__ = Table('MAXEXTXREFVAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacecontrol, __table__.c.newvalue, __table__.c.value]}

class MAXGROUP(Base):
	__table__ = Table('MAXGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname]}

class MAXHANDLER(Base):
	__table__ = Table('MAXHANDLER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.handlername]}

class MAXIFACECOND(Base):
	__table__ = Table('MAXIFACECOND', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.condition, __table__.c.ifacename, __table__.c.intobjectname, __table__.c.procname, __table__.c.usewith]}

class MAXIFACECONTROL(Base):
	__table__ = Table('MAXIFACECONTROL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacecontrol]}

class MAXIFACEIN(Base):
	__table__ = Table('MAXIFACEIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacename]}

class MAXIFACEINCNTL(Base):
	__table__ = Table('MAXIFACEINCNTL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacecontrol, __table__.c.ifacename]}

class MAXIFACEINDETAIL(Base):
	__table__ = Table('MAXIFACEINDETAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacename, __table__.c.intobjectname]}

class MAXIFACEINVOKE(Base):
	__table__ = Table('MAXIFACEINVOKE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacename]}

class MAXIFACEOUT(Base):
	__table__ = Table('MAXIFACEOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacename]}

class MAXIFACEOUTCNTL(Base):
	__table__ = Table('MAXIFACEOUTCNTL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacecontrol, __table__.c.ifacename]}

class MAXIFACEPROC(Base):
	__table__ = Table('MAXIFACEPROC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacename, __table__.c.intobjectname, __table__.c.procname, __table__.c.usewith]}

class MAXIFACETYPEPROP(Base):
	__table__ = Table('MAXIFACETYPEPROP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ifacename, __table__.c.param]}

class MAXIM(Base):
	__table__ = Table('MAXIM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.imname, __table__.c.imversion]}

class MAXIMPROP(Base):
	__table__ = Table('MAXIMPROP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.imname, __table__.c.imversion, __table__.c.property]}

class MAXINTERACTION(Base):
	__table__ = Table('MAXINTERACTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.interaction]}

class MAXINTERROR(Base):
	__table__ = Table('MAXINTERROR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.messageid]}

class MAXINTERROREXTRACT(Base):
	__table__ = Table('MAXINTERROREXTRACT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extractfileid]}

class MAXINTERRORMSG(Base):
	__table__ = Table('MAXINTERRORMSG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.messageid]}

class MAXINTLISTENER(Base):
	__table__ = Table('MAXINTLISTENER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.objectname]}

class MAXINTMAPPING(Base):
	__table__ = Table('MAXINTMAPPING', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.hierarchypath, __table__.c.interaction, __table__.c.intobjectname, __table__.c.isresponse]}

class MAXINTMAPPINGDETAIL(Base):
	__table__ = Table('MAXINTMAPPINGDETAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.attributename, __table__.c.hierarchypath, __table__.c.interaction]}

class MAXINTMSGTRK(Base):
	__table__ = Table('MAXINTMSGTRK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.meamsgid]}

class MAXINTMSGTRKDTL(Base):
	__table__ = Table('MAXINTMSGTRKDTL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.meamsgid, __table__.c.status]}

class MAXINTOBJALIAS(Base):
	__table__ = Table('MAXINTOBJALIAS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.maxintobjaliasid]}

class MAXINTOBJAPP(Base):
	__table__ = Table('MAXINTOBJAPP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.intobjectname, __table__.c.usewith]}

class MAXINTOBJCOLS(Base):
	__table__ = Table('MAXINTOBJCOLS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.intobjectname, __table__.c.intobjfldtype, __table__.c.name, __table__.c.objectname]}

class MAXINTOBJDETAIL(Base):
	__table__ = Table('MAXINTOBJDETAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.intobjectname, __table__.c.objectid]}

class MAXINTOBJECT(Base):
	__table__ = Table('MAXINTOBJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.intobjectname]}

class MAXINTPOLICY(Base):
	__table__ = Table('MAXINTPOLICY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.interaction, __table__.c.policyid]}

class MAXINTPOLICYPARAM(Base):
	__table__ = Table('MAXINTPOLICYPARAM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.interaction, __table__.c.param, __table__.c.policyid]}

class MAXLABELS(Base):
	__table__ = Table('MAXLABELS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.id, __table__.c.property]}

class MAXLAUNCHENTRY(Base):
	__table__ = Table('MAXLAUNCHENTRY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.launchentryname]}

class MAXLECONTEXT(Base):
	__table__ = Table('MAXLECONTEXT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.launchentryname, __table__.c.resourceclass, __table__.c.resourcetype]}

class MAXLISTOVERVAL(Base):
	__table__ = Table('MAXLISTOVERVAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacecontrol, __table__.c.orgid, __table__.c.siteid, __table__.c.value]}

class MAXLOGAPPENDER(Base):
	__table__ = Table('MAXLOGAPPENDER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appender]}

class MAXLOGGER(Base):
	__table__ = Table('MAXLOGGER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.logkey]}

class MAXLOOKUPMAP(Base):
	__table__ = Table('MAXLOOKUPMAP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.lookupattr, __table__.c.source, __table__.c.target, __table__.c.targetattr]}

class MAXMENU(Base):
	__table__ = Table('MAXMENU', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.elementtype, __table__.c.keyvalue, __table__.c.menutype, __table__.c.moduleapp]}

class MAXMESSAGES(Base):
	__table__ = Table('MAXMESSAGES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.msggroup, __table__.c.msgkey]}

class MAXMODULES(Base):
	__table__ = Table('MAXMODULES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.module]}

class MAXOBJECT(Base):
	__table__ = Table('MAXOBJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.objectname]}

class MAXOBJECTCFG(Base):
	__table__ = Table('MAXOBJECTCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.objectname]}

class MAXPRESENTATION(Base):
	__table__ = Table('MAXPRESENTATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app]}

class MAXPROCCOLS(Base):
	__table__ = Table('MAXPROCCOLS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.fieldname, __table__.c.ifacename, __table__.c.intobjectname, __table__.c.procname, __table__.c.usewith]}

class MAXPROP(Base):
	__table__ = Table('MAXPROP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.propname]}

class MAXPROPVALUE(Base):
	__table__ = Table('MAXPROPVALUE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.propname, __table__.c.serverhost, __table__.c.servername]}

class MAXQUEUE(Base):
	__table__ = Table('MAXQUEUE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.queuename]}

class MAXRELATIONSHIP(Base):
	__table__ = Table('MAXRELATIONSHIP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.name, __table__.c.parent]}

class MAXREPLACEPROC(Base):
	__table__ = Table('MAXREPLACEPROC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.fieldname, __table__.c.ifacename, __table__.c.intobjectname, __table__.c.procname, __table__.c.replacenull, __table__.c.usewith]}

class MAXROLE(Base):
	__table__ = Table('MAXROLE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.maxrole]}

class MAXROWSTAMP(Base):
	__table__ = Table('MAXROWSTAMP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tablename]}

class MAXSEQUENCE(Base):
	__table__ = Table('MAXSEQUENCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.name, __table__.c.tbname]}

class MAXSERVICE(Base):
	__table__ = Table('MAXSERVICE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.servicename]}

class MAXSERVSECURITY(Base):
	__table__ = Table('MAXSERVSECURITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.methodname, __table__.c.servicename]}

class MAXSESSION(Base):
	__table__ = Table('MAXSESSION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.maxsessionuid]}

class MAXSYSINDEXES(Base):
	__table__ = Table('MAXSYSINDEXES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.name]}

class MAXSYSKEYS(Base):
	__table__ = Table('MAXSYSKEYS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.colname, __table__.c.ixname]}

class MAXTABLE(Base):
	__table__ = Table('MAXTABLE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tablename]}

class MAXTABLECFG(Base):
	__table__ = Table('MAXTABLECFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tablename]}

class MAXTABLEDOMAIN(Base):
	__table__ = Table('MAXTABLEDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.domainid, __table__.c.orgid, __table__.c.siteid]}

class MAXTESTFIX(Base):
	__table__ = Table('MAXTESTFIX', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.aparnum, __table__.c.hflevel, __table__.c.product, __table__.c.version]}

class MAXTOKEN(Base):
	__table__ = Table('MAXTOKEN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.token, __table__.c.userid]}

class MAXTRANSFORMPROC(Base):
	__table__ = Table('MAXTRANSFORMPROC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.fieldname, __table__.c.ifacename, __table__.c.intobjectname, __table__.c.procname, __table__.c.transsequence, __table__.c.usewith]}

class MAXUSER(Base):
	__table__ = Table('MAXUSER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.userid]}

class MAXUSERSTATUS(Base):
	__table__ = Table('MAXUSERSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.maxuserstatusid]}

class MAXUSRDBAUTHINFO(Base):
	__table__ = Table('MAXUSRDBAUTHINFO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contentuid]}

class MAXVARS(Base):
	__table__ = Table('MAXVARS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.siteid, __table__.c.varname]}

class MAXVARTYPE(Base):
	__table__ = Table('MAXVARTYPE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.varname]}

class MAXVIEW(Base):
	__table__ = Table('MAXVIEW', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.viewname]}

class MAXVIEWCFG(Base):
	__table__ = Table('MAXVIEWCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.viewname]}

class MAXVIEWCOLUMN(Base):
	__table__ = Table('MAXVIEWCOLUMN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.viewcolumnname, __table__.c.viewname]}

class MAXVIEWCOLUMNCFG(Base):
	__table__ = Table('MAXVIEWCOLUMNCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.viewcolumnname, __table__.c.viewname]}

class MAXWSREGISTRY(Base):
	__table__ = Table('MAXWSREGISTRY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wsname]}

class MAXXREFOVERVAL(Base):
	__table__ = Table('MAXXREFOVERVAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extsysname, __table__.c.ifacecontrol, __table__.c.newvalue, __table__.c.orgid, __table__.c.siteid, __table__.c.value]}

class MEA_DUMMY_TABLE(Base):
	__table__ = Table('MEA_DUMMY_TABLE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mea_dummy_tableid]}

class MEASUREMENT(Base):
	__table__ = Table('MEASUREMENT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.measurementid]}

class MEASUREPOINT(Base):
	__table__ = Table('MEASUREPOINT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pointnum, __table__.c.siteid]}

class MEASUREUNIT(Base):
	__table__ = Table('MEASUREUNIT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.measureunitid, __table__.c.orgid, __table__.c.siteid]}

class METER(Base):
	__table__ = Table('METER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.metername]}

class METERGROUP(Base):
	__table__ = Table('METERGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname]}

class METERINGROUP(Base):
	__table__ = Table('METERINGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.metername]}

class METERREADING(Base):
	__table__ = Table('METERREADING', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.meterreadingid, __table__.c.siteid]}

class MFMAILCFG(Base):
	__table__ = Table('MFMAILCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mfmailcfgnum]}

class MFMAILST(Base):
	__table__ = Table('MFMAILST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mfmailstid]}

class MFMAILSTCFG(Base):
	__table__ = Table('MFMAILSTCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mfmailcfgnum, __table__.c.status]}

class MFMAILSTVALCFG(Base):
	__table__ = Table('MFMAILSTVALCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mfmailstvalcfgid]}

class MFMAILTRACK(Base):
	__table__ = Table('MFMAILTRACK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mfmailtrackid]}

class MFMAILWF(Base):
	__table__ = Table('MFMAILWF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mfmailwfid]}

class MFMAILWFNODECFG(Base):
	__table__ = Table('MFMAILWFNODECFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mfmailcfgnum, __table__.c.wfnode]}

class MFMAILWFVALCFG(Base):
	__table__ = Table('MFMAILWFVALCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mfmailwfvalcfgid]}

class MODAVAIL(Base):
	__table__ = Table('MODAVAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.modavailid]}

# class MODDOWNTIMEHIST(Base):
# 	__table__ = Table('MODDOWNTIMEHIST', metadata, autoload=True)
# 	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.enddate, __table__.c.siteid, __table__.c.startdate]}

class MR(Base):
	__table__ = Table('MR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mrnum, __table__.c.siteid]}

class MRCOST(Base):
	__table__ = Table('MRCOST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mrcostid, __table__.c.siteid]}

class MRLINE(Base):
	__table__ = Table('MRLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mrlineid, __table__.c.siteid]}

class MRSTATUS(Base):
	__table__ = Table('MRSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mrstatusseq, __table__.c.siteid]}

class MULTIASSETLOCCI(Base):
	__table__ = Table('MULTIASSETLOCCI', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.multiid]}

class MULTIASSETLOCCIPR(Base):
	__table__ = Table('MULTIASSETLOCCIPR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.multiassetlocciprid]}

class MXCOLLAB(Base):
	__table__ = Table('MXCOLLAB', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.owner1sysid, __table__.c.owner2sysid, __table__.c.pcid]}

class MXCOLLABREF(Base):
	__table__ = Table('MXCOLLABREF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pcid]}

class NAMEDUSERS(Base):
	__table__ = Table('NAMEDUSERS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.namedusersid]}

class NONWORKTIME(Base):
	__table__ = Table('NONWORKTIME', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.enddate, __table__.c.startdate]}

class NUMERICDOMAIN(Base):
	__table__ = Table('NUMERICDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.domainid, __table__.c.orgid, __table__.c.siteid, __table__.c.value]}

class NUMRANGEDOMAIN(Base):
	__table__ = Table('NUMRANGEDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.domainid, __table__.c.orgid, __table__.c.rangesegment, __table__.c.siteid]}

class OBJECTAPPAUTH(Base):
	__table__ = Table('OBJECTAPPAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.context, __table__.c.objectname]}

class OMP(Base):
	__table__ = Table('OMP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ompguid]}

class OMPCIRLN(Base):
	__table__ = Table('OMPCIRLN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ciguid, __table__.c.ompguid]}

class OMPIMLMORLN(Base):
	__table__ = Table('OMPIMLMORLN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.imname, __table__.c.imversion, __table__.c.lmoname, __table__.c.lmonamespace, __table__.c.ompguid]}

class OMPIMRLN(Base):
	__table__ = Table('OMPIMRLN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.imname, __table__.c.imversion, __table__.c.ompguid]}

class ORGANIZATION(Base):
	__table__ = Table('ORGANIZATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid]}

class OSLCDOMAIN(Base):
	__table__ = Table('OSLCDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.domainname]}

class OSLCINTERACTION(Base):
	__table__ = Table('OSLCINTERACTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.interactionname, __table__.c.providername]}

class OSLCLINK(Base):
	__table__ = Table('OSLCLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.oslclinkid]}

class OSLCNSPREFIX(Base):
	__table__ = Table('OSLCNSPREFIX', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nsuri]}

class OSLCPREFILLMAP(Base):
	__table__ = Table('OSLCPREFILLMAP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.interactionname, __table__.c.providername, __table__.c.respropname]}

class OSLCPROVIDER(Base):
	__table__ = Table('OSLCPROVIDER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.providername]}

class OSLCRESOURCE(Base):
	__table__ = Table('OSLCRESOURCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.intobjectname]}

class OSLCRESOURCEDETAIL(Base):
	__table__ = Table('OSLCRESOURCEDETAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.hierarchypath, __table__.c.intobjectname]}

class OSLCRESOURCETYPES(Base):
	__table__ = Table('OSLCRESOURCETYPES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.resourcetype]}

class OSLCSPDEFN(Base):
	__table__ = Table('OSLCSPDEFN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.providerobjname]}

class OSOSLCMAP(Base):
	__table__ = Table('OSOSLCMAP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.attributename, __table__.c.hierarchypath, __table__.c.intobjectname]}

class PALETTEITEM(Base):
	__table__ = Table('PALETTEITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.control]}

class PASSWORDHISTORY(Base):
	__table__ = Table('PASSWORDHISTORY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.changedate, __table__.c.userid]}

class PDSPEC(Base):
	__table__ = Table('PDSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.refobjectid, __table__.c.refobjectname, __table__.c.section]}

class PERSCOMMODITY(Base):
	__table__ = Table('PERSCOMMODITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.commodity, __table__.c.itemsetid, __table__.c.location, __table__.c.orgid, __table__.c.personid, __table__.c.siteid]}

class PERSON(Base):
	__table__ = Table('PERSON', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.personid]}

class PERSONANCESTOR(Base):
	__table__ = Table('PERSONANCESTOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ancestor, __table__.c.personid]}

# class PERSONAVAIL(Base):
# 	__table__ = Table('PERSONAVAIL', metadata, autoload=True)
# 	__mapper_args__ = {'primary_key':[__table__.c.personid, __table__.c.workdate]}

class PERSONCAL(Base):
	__table__ = Table('PERSONCAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.personid]}

class PERSONGROUP(Base):
	__table__ = Table('PERSONGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.persongroup]}

class PERSONGROUPTEAM(Base):
	__table__ = Table('PERSONGROUPTEAM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.persongroup, __table__.c.respparty, __table__.c.resppartygroup, __table__.c.usefororg, __table__.c.useforsite]}

class PERSONSTATUS(Base):
	__table__ = Table('PERSONSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.changedate, __table__.c.personid, __table__.c.status]}

class PHONE(Base):
	__table__ = Table('PHONE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.personid, __table__.c.phonenum, __table__.c.type]}

class PLUSCASSETSTATUS(Base):
	__table__ = Table('PLUSCASSETSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscassetstatusid]}

class PLUSCDSASSETLINK(Base):
	__table__ = Table('PLUSCDSASSETLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscdsassetlinkid]}

class PLUSCDSCONFIG(Base):
	__table__ = Table('PLUSCDSCONFIG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscdsconfigid]}

class PLUSCDSINSTR(Base):
	__table__ = Table('PLUSCDSINSTR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetfunction, __table__.c.dsplannum, __table__.c.revisionnum]}

class PLUSCDSPOINT(Base):
	__table__ = Table('PLUSCDSPOINT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscdspointid]}

class PLUSCDSSTATUS(Base):
	__table__ = Table('PLUSCDSSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscdsstatusid]}

class PLUSCJPDATASHEET(Base):
	__table__ = Table('PLUSCJPDATASHEET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscjpdatasheetid]}

class PLUSCJPSTATUS(Base):
	__table__ = Table('PLUSCJPSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscjpstatusid]}

class PLUSCPMEXTDATE(Base):
	__table__ = Table('PLUSCPMEXTDATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscpmextdateid]}

class PLUSCSPOTCHECK(Base):
	__table__ = Table('PLUSCSPOTCHECK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscspotcheckid]}

class PLUSCTEMPLATE(Base):
	__table__ = Table('PLUSCTEMPLATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.templateid]}

class PLUSCTPASSET(Base):
	__table__ = Table('PLUSCTPASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.plusctpassetid]}

class PLUSCTPDATASHEET(Base):
	__table__ = Table('PLUSCTPDATASHEET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.plusctpdatasheetid]}

class PLUSCTPHISTORY(Base):
	__table__ = Table('PLUSCTPHISTORY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.plusctphistoryid]}

class PLUSCTPMASTERPM(Base):
	__table__ = Table('PLUSCTPMASTERPM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.masterpmnum, __table__.c.orgid, __table__.c.templateid]}

class PLUSCTPMETER(Base):
	__table__ = Table('PLUSCTPMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.metername, __table__.c.orgid, __table__.c.templateid]}

class PLUSCTPSPAREPART(Base):
	__table__ = Table('PLUSCTPSPAREPART', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.plusctpsparepartid]}

class PLUSCTPSPEC(Base):
	__table__ = Table('PLUSCTPSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.orgid, __table__.c.section, __table__.c.templateid]}

class PLUSCWODS(Base):
	__table__ = Table('PLUSCWODS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscwodsid]}

class PLUSCWODSINSTR(Base):
	__table__ = Table('PLUSCWODSINSTR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscwodsinstrid]}

class PLUSCWODSPOINT(Base):
	__table__ = Table('PLUSCWODSPOINT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pluscwodspointid]}

class PLUSDSPLAN(Base):
	__table__ = Table('PLUSDSPLAN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.dsplannum, __table__.c.revisionnum]}

class PM(Base):
	__table__ = Table('PM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pmnum, __table__.c.siteid]}

class PMANCESTOR(Base):
	__table__ = Table('PMANCESTOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ancestor, __table__.c.pmnum, __table__.c.siteid]}

class PMFORECAST(Base):
	__table__ = Table('PMFORECAST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ltdpmcounter, __table__.c.pmnum, __table__.c.siteid]}

class PMFORECASTJP(Base):
	__table__ = Table('PMFORECASTJP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ltdpmcounter, __table__.c.pmnum, __table__.c.siteid]}

class PMMETER(Base):
	__table__ = Table('PMMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.metername, __table__.c.pmnum, __table__.c.siteid]}

class PMSEASONS(Base):
	__table__ = Table('PMSEASONS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.endday, __table__.c.endmonth, __table__.c.pmnum, __table__.c.siteid, __table__.c.startday, __table__.c.startmonth]}

class PMSEQUENCE(Base):
	__table__ = Table('PMSEQUENCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.interval, __table__.c.pmnum, __table__.c.siteid]}

class PO(Base):
	__table__ = Table('PO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ponum, __table__.c.revisionnum, __table__.c.siteid]}

class POCOST(Base):
	__table__ = Table('POCOST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pocostid]}

class POECOMSTATUS(Base):
	__table__ = Table('POECOMSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.poecomstatusid]}

class POINTWO(Base):
	__table__ = Table('POINTWO', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.pointnum, __table__.c.siteid, __table__.c.wonum]}

class POLINE(Base):
	__table__ = Table('POLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.polineid]}

class PORTLET(Base):
	__table__ = Table('PORTLET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.portletid]}

class PORTLETDISPLAY(Base):
	__table__ = Table('PORTLETDISPLAY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.portletdisplayid]}

class POSTATUS(Base):
	__table__ = Table('POSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.postatusid]}

class POTERM(Base):
	__table__ = Table('POTERM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.potermid]}

class PPCRAFTRATE(Base):
	__table__ = Table('PPCRAFTRATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.craft, __table__.c.orgid, __table__.c.premiumpaycode]}

class PPLABORRATE(Base):
	__table__ = Table('PPLABORRATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.craft, __table__.c.laborcode, __table__.c.orgid, __table__.c.premiumpaycode]}

class PR(Base):
	__table__ = Table('PR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.prnum, __table__.c.siteid]}

class PRCOST(Base):
	__table__ = Table('PRCOST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.prcostid]}

class PRECAUTION(Base):
	__table__ = Table('PRECAUTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.precautionid, __table__.c.siteid]}

class PREMIUMPAY(Base):
	__table__ = Table('PREMIUMPAY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.premiumpaycode]}

class PRICALC(Base):
	__table__ = Table('PRICALC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.findex, __table__.c.siteid]}

class PRLINE(Base):
	__table__ = Table('PRLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.prlineid]}

class PRODUCTUPDATE(Base):
	__table__ = Table('PRODUCTUPDATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.productupdateid]}

class PROPERTYASSOC(Base):
	__table__ = Table('PROPERTYASSOC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.maxcontracttype, __table__.c.propertyid]}

class PROPERTYDEFAULT(Base):
	__table__ = Table('PROPERTYDEFAULT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contracttypeid, __table__.c.orgid, __table__.c.propertyid]}

class PRSTATUS(Base):
	__table__ = Table('PRSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.prstatusid]}

class PRTERM(Base):
	__table__ = Table('PRTERM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.prtermid]}

class QUALCRAFTSKILL(Base):
	__table__ = Table('QUALCRAFTSKILL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.craft, __table__.c.orgid, __table__.c.qualificationid, __table__.c.skilllevel]}

class QUALIFICATION(Base):
	__table__ = Table('QUALIFICATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.qualificationid]}

class QUALSTATUS(Base):
	__table__ = Table('QUALSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.changedate, __table__.c.orgid, __table__.c.qualificationid]}

class QUERY(Base):
	__table__ = Table('QUERY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.clausename, __table__.c.owner]}

class QUOTATIONLINE(Base):
	__table__ = Table('QUOTATIONLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.quotationlineid, __table__.c.rfqlinenum, __table__.c.rfqnum, __table__.c.siteid, __table__.c.vendor]}

class RECONCOMPFILTER(Base):
	__table__ = Table('RECONCOMPFILTER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.filtertype, __table__.c.rulename, __table__.c.sequencenum]}

class RECONLINK(Base):
	__table__ = Table('RECONLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.reconlinkid]}

class RECONMULTILINK(Base):
	__table__ = Table('RECONMULTILINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.reconmultilinkid]}

class RECONRESULT(Base):
	__table__ = Table('RECONRESULT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.reconresultid]}

class RECONRULE(Base):
	__table__ = Table('RECONRULE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rulename, __table__.c.ruletype]}

class RECONRULECLAUSE(Base):
	__table__ = Table('RECONRULECLAUSE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rulename, __table__.c.ruletype, __table__.c.sequencenum]}

class RECONTASK(Base):
	__table__ = Table('RECONTASK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.taskname]}

class RECONTASKCOMP(Base):
	__table__ = Table('RECONTASKCOMP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.comprulename, __table__.c.taskname]}

class RECONTASKFILTER(Base):
	__table__ = Table('RECONTASKFILTER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.filtername]}

class RECONTASKFLTRVAL(Base):
	__table__ = Table('RECONTASKFLTRVAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.recontaskfltrvalid]}

class RECONTASKLINK(Base):
	__table__ = Table('RECONTASKLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.linkrulename, __table__.c.taskname]}

class RELATEDRECORD(Base):
	__table__ = Table('RELATEDRECORD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.relatedrecordid]}

class RELATEDSLA(Base):
	__table__ = Table('RELATEDSLA', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.childslanum, __table__.c.parentslanum]}

class RELATION(Base):
	__table__ = Table('RELATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.relationnum]}

class RELATIONRULES(Base):
	__table__ = Table('RELATIONRULES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.relationnum, __table__.c.sourceclass, __table__.c.targetclass]}

class RELATIONRULESEXT(Base):
	__table__ = Table('RELATIONRULESEXT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.relationrulesextid]}

class REORDERMUTEX(Base):
	__table__ = Table('REORDERMUTEX', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.mrnum, __table__.c.siteid, __table__.c.type]}

class REORDERPAD(Base):
	__table__ = Table('REORDERPAD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.itemsetid, __table__.c.location, __table__.c.mrlinenum, __table__.c.mrnum, __table__.c.siteid, __table__.c.usrname, __table__.c.wpitemid]}

class REPFACAUTH(Base):
	__table__ = Table('REPFACAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.repairfacility, __table__.c.siteid]}

class REPORT(Base):
	__table__ = Table('REPORT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.reportname]}

class REPORTADHOC(Base):
	__table__ = Table('REPORTADHOC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.reportname]}

class REPORTADHOCFIELD(Base):
	__table__ = Table('REPORTADHOCFIELD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.attributename, __table__.c.objectid, __table__.c.reportname]}

class REPORTAPPAUTH(Base):
	__table__ = Table('REPORTAPPAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.groupname, __table__.c.runtype]}

class REPORTAUTH(Base):
	__table__ = Table('REPORTAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.groupname, __table__.c.reportname]}

class REPORTDEPEND(Base):
	__table__ = Table('REPORTDEPEND', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.depreportname, __table__.c.reportname]}

class REPORTDESIGN(Base):
	__table__ = Table('REPORTDESIGN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.reportname]}

# class REPORTDIALOGDET(Base):
# 	__table__ = Table('REPORTDIALOGDET', metadata, autoload=True)
# 	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.groupname]}

class REPORTDS(Base):
	__table__ = Table('REPORTDS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.datasourcename]}

class REPORTDSPARAM(Base):
	__table__ = Table('REPORTDSPARAM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.datasourcename]}

class REPORTJOB(Base):
	__table__ = Table('REPORTJOB', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.reportjobid]}

class REPORTLABEL(Base):
	__table__ = Table('REPORTLABEL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.labelkey, __table__.c.reportname]}

class REPORTLISTCFG(Base):
	__table__ = Table('REPORTLISTCFG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.layoutid, __table__.c.reportname]}

class REPORTLOOKUP(Base):
	__table__ = Table('REPORTLOOKUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.parametername, __table__.c.reportname]}

class REPORTOSAUTH(Base):
	__table__ = Table('REPORTOSAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.intobjectname]}

class REPORTOUTPUT(Base):
	__table__ = Table('REPORTOUTPUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobnum]}

class REPORTOUTPUTAUTH(Base):
	__table__ = Table('REPORTOUTPUTAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.emailaddress, __table__.c.jobnum]}

class REPORTOUTPUTCNT(Base):
	__table__ = Table('REPORTOUTPUTCNT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.jobnum]}

class REPORTPARAM(Base):
	__table__ = Table('REPORTPARAM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.paramname, __table__.c.reportname]}

class REPORTPROCRESERVE(Base):
	__table__ = Table('REPORTPROCRESERVE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.day, __table__.c.reportname, __table__.c.startreserve]}

class REPORTPROCSCHED(Base):
	__table__ = Table('REPORTPROCSCHED', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.day, __table__.c.reportname, __table__.c.startschedulable]}

class REPORTRUNLOCK(Base):
	__table__ = Table('REPORTRUNLOCK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.reportrunqueueid]}

class REPORTRUNPARAM(Base):
	__table__ = Table('REPORTRUNPARAM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.reportrunparamid]}

class REPORTRUNQUEUE(Base):
	__table__ = Table('REPORTRUNQUEUE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.reportrunqueueid]}

class REPORTSCHED(Base):
	__table__ = Table('REPORTSCHED', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.crontaskname, __table__.c.instancename]}

class REPORTSECATTKEY(Base):
	__table__ = Table('REPORTSECATTKEY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.seqnumber]}

class REPORTUSAGELOG(Base):
	__table__ = Table('REPORTUSAGELOG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.reportusagelogid]}

class RESULTSETCOLS(Base):
	__table__ = Table('RESULTSETCOLS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.resultsetcolsid]}

class RFQ(Base):
	__table__ = Table('RFQ', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rfqnum, __table__.c.siteid]}

class RFQLINE(Base):
	__table__ = Table('RFQLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rfqlineid]}

class RFQSTATUS(Base):
	__table__ = Table('RFQSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rfqnum, __table__.c.rfqstatusseq, __table__.c.siteid]}

class RFQTERM(Base):
	__table__ = Table('RFQTERM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rfqtermid]}

class RFQVENDOR(Base):
	__table__ = Table('RFQVENDOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rfqnum, __table__.c.siteid, __table__.c.vendor]}

class RFQVENDORTERM(Base):
	__table__ = Table('RFQVENDORTERM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rfqvendortermid]}

class ROUTE_STOP(Base):
	__table__ = Table('ROUTE_STOP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.route, __table__.c.routestopid, __table__.c.siteid]}

class ROUTES(Base):
	__table__ = Table('ROUTES', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.route, __table__.c.siteid]}

class RSCONFIG(Base):
	__table__ = Table('RSCONFIG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.rsconfigid]}

class SAFETYLEXICON(Base):
	__table__ = Table('SAFETYLEXICON', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.safetylexiconid, __table__.c.siteid]}

class SAFETYPLAN(Base):
	__table__ = Table('SAFETYPLAN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.safetyplanid, __table__.c.siteid]}

class SAPMAIL(Base):
	__table__ = Table('SAPMAIL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.sapmailid]}

class SCCONFIG(Base):
	__table__ = Table('SCCONFIG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.userid]}

class SCHEDULE(Base):
	__table__ = Table('SCHEDULE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractlinenum, __table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum, __table__.c.schedulenum, __table__.c.schedulerev]}

class SCHEDULELINE(Base):
	__table__ = Table('SCHEDULELINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.scheduleid, __table__.c.schedulelineid]}

class SCRIPTLAUNCHPOINT(Base):
	__table__ = Table('SCRIPTLAUNCHPOINT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.autoscript, __table__.c.launchpointname]}

class SCTEMPLATE(Base):
	__table__ = Table('SCTEMPLATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.sctemplateid]}

class SECURITYRESTRICT(Base):
	__table__ = Table('SECURITYRESTRICT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.attributename, __table__.c.groupname, __table__.c.objectname, __table__.c.restriction, __table__.c.type]}

class SERVICEADDRESS(Base):
	__table__ = Table('SERVICEADDRESS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.addresscode, __table__.c.orgid]}

class SERVRECTRANS(Base):
	__table__ = Table('SERVRECTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.servrectransid]}

class SETS(Base):
	__table__ = Table('SETS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.setid]}

class SFWLICENSE(Base):
	__table__ = Table('SFWLICENSE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.sfwlicenseid]}

class SFWLINE(Base):
	__table__ = Table('SFWLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractlinenum, __table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum]}

class SHIFT(Base):
	__table__ = Table('SHIFT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.shiftnum]}

class SHIFTPATTERNDAY(Base):
	__table__ = Table('SHIFTPATTERNDAY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.patterndayseq, __table__.c.shiftnum]}

class SHIPMENT(Base):
	__table__ = Table('SHIPMENT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.fromsiteid, __table__.c.shipmentnum]}

class SHIPMENTLINE(Base):
	__table__ = Table('SHIPMENTLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.shipmentid, __table__.c.shipmentlineid, __table__.c.siteid]}

class SIGOPTFLAG(Base):
	__table__ = Table('SIGOPTFLAG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.optionname]}

class SIGOPTION(Base):
	__table__ = Table('SIGOPTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.optionname]}

class SITE(Base):
	__table__ = Table('SITE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid]}

class SITEAUTH(Base):
	__table__ = Table('SITEAUTH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.siteid]}

class SITEECOM(Base):
	__table__ = Table('SITEECOM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.siteid, __table__.c.vendor]}

class SKDACTION(Base):
	__table__ = Table('SKDACTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.actionname, __table__.c.objectname, __table__.c.skdobjectname, __table__.c.usewith]}

class SKDACTIVITY(Base):
	__table__ = Table('SKDACTIVITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.id, __table__.c.objectid, __table__.c.objectname, __table__.c.skdprojectid]}

class SKDACTIVITYQBE(Base):
	__table__ = Table('SKDACTIVITYQBE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class SKDAPPLETEXT(Base):
	__table__ = Table('SKDAPPLETEXT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.extname]}

class SKDCOMPLIANCE(Base):
	__table__ = Table('SKDCOMPLIANCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.enddate, __table__.c.skdprojectid, __table__.c.startdate]}

class SKDCOMPLIANCEWOLIST(Base):
	__table__ = Table('SKDCOMPLIANCEWOLIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.skdprojectid, __table__.c.workorderid]}

class SKDCONSTRAINT(Base):
	__table__ = Table('SKDCONSTRAINT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.deleted, __table__.c.fromactivityid, __table__.c.objectid, __table__.c.objectname, __table__.c.skdprojectid, __table__.c.toactivityid, __table__.c.type]}

class SKDCOST(Base):
	__table__ = Table('SKDCOST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contentuid]}

class SKDCOSTTEMP(Base):
	__table__ = Table('SKDCOSTTEMP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contentuid]}

class SKDDATAGROUP(Base):
	__table__ = Table('SKDDATAGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.skdobjectname]}

class SKDGVPREF(Base):
	__table__ = Table('SKDGVPREF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.projectname, __table__.c.userid]}

class SKDOBJECT(Base):
	__table__ = Table('SKDOBJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.objectname, __table__.c.skdobjectname]}

class SKDOBJECTMGR(Base):
	__table__ = Table('SKDOBJECTMGR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.objectname, __table__.c.purpose, __table__.c.skdobjectname]}

class SKDPMFORECAST(Base):
	__table__ = Table('SKDPMFORECAST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ltdpmcounter, __table__.c.pmnum, __table__.c.siteid, __table__.c.skdprojectid]}

class SKDPMFORECASTJP(Base):
	__table__ = Table('SKDPMFORECASTJP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ltdpmcounter, __table__.c.pmnum, __table__.c.siteid, __table__.c.skdprojectid]}

class SKDPROJECT(Base):
	__table__ = Table('SKDPROJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.name]}

class SKDPROJECTSHIFTS(Base):
	__table__ = Table('SKDPROJECTSHIFTS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.name, __table__.c.orgid, __table__.c.shiftnum]}

class SKDPROPERTY(Base):
	__table__ = Table('SKDPROPERTY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.propertyname, __table__.c.skdobjectname]}

class SKDPROPERTYMAP(Base):
	__table__ = Table('SKDPROPERTYMAP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.objectname, __table__.c.propertyname, __table__.c.skdobjectname]}

class SKDQUERY(Base):
	__table__ = Table('SKDQUERY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.name, __table__.c.objectname, __table__.c.queryname]}

class SKDRESERVATION(Base):
	__table__ = Table('SKDRESERVATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.objectid, __table__.c.objectname, __table__.c.skdactivityid, __table__.c.skdprojectid, __table__.c.skdresourceid]}

class SKDRESOBJECT(Base):
	__table__ = Table('SKDRESOBJECT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.activitygroup, __table__.c.resourceobjectname]}

class SKDRESOURCE(Base):
	__table__ = Table('SKDRESOURCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.id, __table__.c.objectid, __table__.c.objectname, __table__.c.skdprojectid]}

class SKDRESOURCEUSE(Base):
	__table__ = Table('SKDRESOURCEUSE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.objectid, __table__.c.objectname, __table__.c.refobjname, __table__.c.skdprojectid]}

class SKDRESOURCEVIEW(Base):
	__table__ = Table('SKDRESOURCEVIEW', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.viewname]}

class SKDUSERPROP(Base):
	__table__ = Table('SKDUSERPROP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.projectname, __table__.c.propertyname, __table__.c.skdobjectname, __table__.c.userid]}

class SLA(Base):
	__table__ = Table('SLA', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.slanum]}

class SLAASSETLOC(Base):
	__table__ = Table('SLAASSETLOC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.assettype, __table__.c.location, __table__.c.siteid, __table__.c.slanum]}

class SLACOMMITMENTS(Base):
	__table__ = Table('SLACOMMITMENTS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.commitmentid, __table__.c.slanum]}

class SLACONTRACT(Base):
	__table__ = Table('SLACONTRACT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractnum, __table__.c.slanum]}

class SLAKPI(Base):
	__table__ = Table('SLAKPI', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.kpiname, __table__.c.slanum]}

class SLARECORDS(Base):
	__table__ = Table('SLARECORDS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ownerid, __table__.c.ownertable, __table__.c.slanum]}

class SLROUTE(Base):
	__table__ = Table('SLROUTE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.slrouteid]}

class SLRTRAVELTIME(Base):
	__table__ = Table('SLRTRAVELTIME', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.slrtraveltimeid]}

class SMS(Base):
	__table__ = Table('SMS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.address, __table__.c.personid, __table__.c.smstype]}

class SOLUTION(Base):
	__table__ = Table('SOLUTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.solution]}

class SOLUTIONSPEC(Base):
	__table__ = Table('SOLUTIONSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.section, __table__.c.solution]}

class SOLUTIONSTATUS(Base):
	__table__ = Table('SOLUTIONSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.solutionstatusid]}

class SPAREPART(Base):
	__table__ = Table('SPAREPART', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.sparepartid]}

class SPLEXICONLINK(Base):
	__table__ = Table('SPLEXICONLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.safetylexiconid, __table__.c.siteid, __table__.c.spworkassetid]}

# class SPLITUSELINE(Base):
# 	__table__ = Table('SPLITUSELINE', metadata, autoload=True)
# 	__mapper_args__ = {'primary_key':[__table__.c.contentuid]}

class SPRELATEDASSET(Base):
	__table__ = Table('SPRELATEDASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.sprelatedassetid]}

class SPWORKASSET(Base):
	__table__ = Table('SPWORKASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.spworkassetid]}

class SYNONYMDOMAIN(Base):
	__table__ = Table('SYNONYMDOMAIN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.domainid, __table__.c.maxvalue, __table__.c.orgid, __table__.c.siteid, __table__.c.value]}

class TAGLOCK(Base):
	__table__ = Table('TAGLOCK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.taglockid]}

class TAGOUT(Base):
	__table__ = Table('TAGOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.tagoutid]}

class TAMITDPAHWM(Base):
	__table__ = Table('TAMITDPAHWM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tamitdpahwmid]}

class TAMITSWPRTNUM(Base):
	__table__ = Table('TAMITSWPRTNUM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ccid, __table__.c.partnumber]}

class TASKSCHEDULER(Base):
	__table__ = Table('TASKSCHEDULER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.servername, __table__.c.taskname]}

class TAX(Base):
	__table__ = Table('TAX', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.effective, __table__.c.orgid, __table__.c.taxcode, __table__.c.typecode]}

class TAXORDER(Base):
	__table__ = Table('TAXORDER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.tablename]}

class TAXTYPE(Base):
	__table__ = Table('TAXTYPE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.typecode]}

class TDTVERSION(Base):
	__table__ = Table('TDTVERSION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.language, __table__.c.pmpname, __table__.c.version]}

class TEMPLATESTATUS(Base):
	__table__ = Table('TEMPLATESTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.templatestatusid]}

class TERM(Base):
	__table__ = Table('TERM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.termuid]}

#Manually jigged as python does not like class as a field, surprisingly enough
class TICKET(Base):
	__table__ = Table('TICKET', metadata, autoload=True)
#	__mapper_args__ = {'primary_key':[__table__.c.class, __table__.c.ticketid]}
	__mapper_args__ = {'primary_key':[__table__.c.ticketid]}

#Manually jigged as python does not like class as a field, surprisingly enough
class TICKETSPEC(Base):
	__table__ = Table('TICKETSPEC', metadata, autoload=True)
#	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.class, __table__.c.section, __table__.c.ticketid]}
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.section, __table__.c.ticketid]}

#Manually jigged as python does not like class as a field, surprisingly enough
class TKOWNERHISTORY(Base):
	__table__ = Table('TKOWNERHISTORY', metadata, autoload=True)
#	__mapper_args__ = {'primary_key':[__table__.c.class, __table__.c.owndate, __table__.c.ticketid]}
	__mapper_args__ = {'primary_key':[__table__.c.owndate, __table__.c.ticketid]}

#Manually jigged as python does not like class as a field, surprisingly enough
class TKSERVICEADDRESS(Base):
	__table__ = Table('TKSERVICEADDRESS', metadata, autoload=True)
#	__mapper_args__ = {'primary_key':[__table__.c.class, __table__.c.ticketid]}
	__mapper_args__ = {'primary_key':[__table__.c.ticketid]}

class TKSTATUS(Base):
	__table__ = Table('TKSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tkstatusid]}

class TKTEMPLATE(Base):
	__table__ = Table('TKTEMPLATE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.templateid]}

#Manually jigged as python does not like class as a field, surprisingly enough
class TKTEMPLATESPEC(Base):
	__table__ = Table('TKTEMPLATESPEC', metadata, autoload=True)
#	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.class, __table__.c.section, __table__.c.templateid]}
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.section, __table__.c.templateid]}

class TKTEMPLTACTIVITY(Base):
	__table__ = Table('TKTEMPLTACTIVITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tktempltactivityid]}

class TKTEMPLTACTYSPEC(Base):
	__table__ = Table('TKTEMPLTACTYSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.refobjectid, __table__.c.refobjectname, __table__.c.templateid]}

class TLOAMASSETGRP(Base):
	__table__ = Table('TLOAMASSETGRP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tloamassetgrpid]}

class TLOAMDPAANCESTOR(Base):
	__table__ = Table('TLOAMDPAANCESTOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tloamdpaancestorid]}

class TLOAMDPAHWM(Base):
	__table__ = Table('TLOAMDPAHWM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tloamdpahwmid]}

class TLOAMFSNEVENTLISTENER(Base):
	__table__ = Table('TLOAMFSNEVENTLISTENER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.classname]}

class TLOAMFSNRUNSTATUS(Base):
	__table__ = Table('TLOAMFSNRUNSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mappingname]}

class TLOAMPRMDFLT(Base):
	__table__ = Table('TLOAMPRMDFLT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.defaultname]}

class TLOAMSOFTWARE(Base):
	__table__ = Table('TLOAMSOFTWARE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tloamsoftwareid]}

class TLOAMSWCATALOG(Base):
	__table__ = Table('TLOAMSWCATALOG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tloamswcatalogid]}

class TLOAMSWREL(Base):
	__table__ = Table('TLOAMSWREL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.tloamswrelid]}

class TOOLQUAL(Base):
	__table__ = Table('TOOLQUAL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.itemsetid, __table__.c.orgid, __table__.c.qualificationid]}

class TOOLTRANS(Base):
	__table__ = Table('TOOLTRANS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.siteid, __table__.c.tooltransid]}

class USERPREF(Base):
	__table__ = Table('USERPREF', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.userid, __table__.c.varname]}

# class USERPROFILECATS(Base):
# 	__table__ = Table('USERPROFILECATS', metadata, autoload=True)
# 	__mapper_args__ = {'primary_key':[__table__.c.category]}

class USERPURGL(Base):
	__table__ = Table('USERPURGL', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.userid]}

class VENDORSTATUS(Base):
	__table__ = Table('VENDORSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.vendorstatusid]}

class WARRANTYASSET(Base):
	__table__ = Table('WARRANTYASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetid, __table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum, __table__.c.warrantyassetid]}

class WARRANTYLINE(Base):
	__table__ = Table('WARRANTYLINE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.contractlinenum, __table__.c.contractnum, __table__.c.orgid, __table__.c.revisionnum]}

class WFACTION(Base):
	__table__ = Table('WFACTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.actionid, __table__.c.processname, __table__.c.processrev]}

class WFACTIVATION(Base):
	__table__ = Table('WFACTIVATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ownerid, __table__.c.ownertable, __table__.c.processname]}

class WFAPPTOOLBAR(Base):
	__table__ = Table('WFAPPTOOLBAR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.appname, __table__.c.toolbarsequence]}

class WFASGNGROUP(Base):
	__table__ = Table('WFASGNGROUP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.groupnum, __table__.c.nodeid, __table__.c.processname, __table__.c.processrev, __table__.c.wfid]}

class WFASSIGNMENT(Base):
	__table__ = Table('WFASSIGNMENT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assignid, __table__.c.nodeid, __table__.c.processname, __table__.c.processrev, __table__.c.wfid]}

class WFCALLSTACK(Base):
	__table__ = Table('WFCALLSTACK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.callseq, __table__.c.wfid]}

class WFCONDITION(Base):
	__table__ = Table('WFCONDITION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid, __table__.c.processname, __table__.c.processrev]}

class WFINPUT(Base):
	__table__ = Table('WFINPUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid, __table__.c.processname, __table__.c.processrev]}

class WFINSTANCE(Base):
	__table__ = Table('WFINSTANCE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wfid]}

class WFINTERACTION(Base):
	__table__ = Table('WFINTERACTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid, __table__.c.processname, __table__.c.processrev]}

class WFNODE(Base):
	__table__ = Table('WFNODE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid, __table__.c.processname, __table__.c.processrev]}

class WFNOTIFICATION(Base):
	__table__ = Table('WFNOTIFICATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.processname, __table__.c.processrev, __table__.c.uniqueid]}

class WFPROCESS(Base):
	__table__ = Table('WFPROCESS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.processname, __table__.c.processrev]}

class WFREVISION(Base):
	__table__ = Table('WFREVISION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.mainprocess, __table__.c.processname, __table__.c.revision]}

class WFSTART(Base):
	__table__ = Table('WFSTART', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid, __table__.c.processname, __table__.c.processrev]}

class WFSTOP(Base):
	__table__ = Table('WFSTOP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid, __table__.c.processname, __table__.c.processrev]}

class WFSUBPROCESS(Base):
	__table__ = Table('WFSUBPROCESS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid, __table__.c.processname, __table__.c.processrev]}

class WFTASK(Base):
	__table__ = Table('WFTASK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.nodeid, __table__.c.processname, __table__.c.processrev]}

class WFTRANSACTION(Base):
	__table__ = Table('WFTRANSACTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.transid]}

class WFWAITLIST(Base):
	__table__ = Table('WFWAITLIST', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.eventname, __table__.c.nodeid, __table__.c.processname, __table__.c.processrev]}

class WMASSIGNTMP(Base):
	__table__ = Table('WMASSIGNTMP', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wmassigntmpid]}

class WMMATCH(Base):
	__table__ = Table('WMMATCH', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wmmatchid]}

class WMMATCHCRW(Base):
	__table__ = Table('WMMATCHCRW', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wmmatchcrwid]}

class WOANCESTOR(Base):
	__table__ = Table('WOANCESTOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.ancestor, __table__.c.siteid, __table__.c.wonum]}

class WOCONTRACT(Base):
	__table__ = Table('WOCONTRACT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wocontractid]}

class WOGEN(Base):
	__table__ = Table('WOGEN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.runid, __table__.c.runorder, __table__.c.siteid]}

class WOHAZARD(Base):
	__table__ = Table('WOHAZARD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.hazardid, __table__.c.siteid, __table__.c.wonum, __table__.c.wosafetydatasource]}

class WOHAZARDPREC(Base):
	__table__ = Table('WOHAZARDPREC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.hazardid, __table__.c.precautionid, __table__.c.siteid, __table__.c.wonum, __table__.c.wosafetydatasource]}

class WOLOCKOUT(Base):
	__table__ = Table('WOLOCKOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wolockoutid]}

class WOMATSTATUSSYNC(Base):
	__table__ = Table('WOMATSTATUSSYNC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.itemnum, __table__.c.itemsetid, __table__.c.location, __table__.c.siteid]}

class WOMETER(Base):
	__table__ = Table('WOMETER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wometerid, __table__.c.wonum]}

class WOOWNERHISTORY(Base):
	__table__ = Table('WOOWNERHISTORY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.owndate, __table__.c.siteid, __table__.c.wonum]}

class WOPRECAUTION(Base):
	__table__ = Table('WOPRECAUTION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.precautionid, __table__.c.siteid, __table__.c.wonum, __table__.c.wosafetydatasource]}

class WORELEXT(Base):
	__table__ = Table('WORELEXT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class WORKLOG(Base):
	__table__ = Table('WORKLOG', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.worklogid]}

class WORKORDER(Base):
	__table__ = Table('WORKORDER', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class WORKORDERSPEC(Base):
	__table__ = Table('WORKORDERSPEC', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetattrid, __table__.c.section, __table__.c.siteid, __table__.c.wonum]}

class WORKPERIOD(Base):
	__table__ = Table('WORKPERIOD', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.calnum, __table__.c.orgid, __table__.c.shiftnum, __table__.c.workdate]}

class WORKPRIORITY(Base):
	__table__ = Table('WORKPRIORITY', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.priority, __table__.c.siteid]}

class WORKTYPE(Base):
	__table__ = Table('WORKTYPE', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.worktypeid]}

#Manually jigged as python does not like class as a field, surprisingly enough
class WORKVIEW(Base):
	__table__ = Table('WORKVIEW', metadata, autoload=True)
#	__mapper_args__ = {'primary_key':[__table__.c.class, __table__.c.recordkey, __table__.c.siteid]}
	__mapper_args__ = {'primary_key':[__table__.c.recordkey, __table__.c.siteid]}

class WOSAFETYLINK(Base):
	__table__ = Table('WOSAFETYLINK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wosafetylinkid]}

class WOSAFETYPLAN(Base):
	__table__ = Table('WOSAFETYPLAN', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class WOSERVICEADDRESS(Base):
	__table__ = Table('WOSERVICEADDRESS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}

class WOSTATUS(Base):
	__table__ = Table('WOSTATUS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wostatusid]}

class WOTAGLOCK(Base):
	__table__ = Table('WOTAGLOCK', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.taglockid]}

class WOTAGOUT(Base):
	__table__ = Table('WOTAGOUT', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.tagoutid, __table__.c.wonum, __table__.c.wosafetydatasource]}

class WOTASKRELATION(Base):
	__table__ = Table('WOTASKRELATION', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wotaskrelationid]}

class WPEDITSETTING(Base):
	__table__ = Table('WPEDITSETTING', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.orgid, __table__.c.status]}

class WPITEM(Base):
	__table__ = Table('WPITEM', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.wpitemid]}

class WPLABOR(Base):
	__table__ = Table('WPLABOR', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum, __table__.c.wplaborid]}

