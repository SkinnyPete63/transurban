import sys
import copy
import datetime

from dbconnect import session_scope
from dbconnect.usefulFunctions import get_persistent_columns_for_object as getper
from dbconnect.usefulFunctions import get_latest_sequence as gls
from dbconnect.tabledefs.JOBPLAN import JOBPLAN as jp
from dbconnect.tabledefs.MAXSEQUENCE import MAXSEQUENCE as ms
from dbconnect.tabledefs.JOBTASK import JOBTASK as jt

from sqlalchemy import and_

from usefulFunctions import sqldate_format
sqlLeadIn = "begin transaction \nbegin try\n\t"
sqlLeadOut = "\tcommit transaction\nend try\nbegin catch\n\trollback transaction\n\tDECLARE @Msg NVARCHAR(MAX)\n\tSELECT @Msg=ERROR_MESSAGE()\n\tRAISERROR('Error Occured: %s', -1, -1, @msg) WITH LOG\nend catch"

dictJPrevs = {}
dictJPLatest = {}
cols_jp = {}
cols_jt = {}
allTasks = {}
revisionComment = 'Lead in and out tasks added'
newJPStatus = 'ACTIVE'
updatedJPStatus = 'REVISED'
pendingJPStatus = 'PNDREV'
changeby = 'MAXADMIN'

nextjpid = 0
outSQLPath = '\\pch\\dataload\\sql_scripts\\'
outjpfile = '010_jobplan_insert.sql'
outAllFile = '100_jobplan_all.sql'
dictChangedJPFields = {'pluscstatusdate':sqldate_format(), 'pluscchangedate':sqldate_format(), 'pluscchangeby':changeby, 'status':updatedJPStatus}

class jobplan:
    pass

class jobtask:
    pass

def xstr(s):
    if s is None:
        return ''
    else:
        return str(s)
    
def get_jprevs(p_sitelist):
    '''
    returns a dictionary of jobplan numbers with a list of all the revisions
    as the value
    '''
    dictres = {}
    with session_scope() as session:
        res = session.query(jp.jpnum, jp.pluscrevnum, jp.siteid).filter(jp.siteid.in_(p_sitelist)).all()
        for row in res:
            if row.siteid in dictres:
                if row.jpnum in dictres[row.siteid]:
                    dictres[row.siteid][row.jpnum].append(row.pluscrevnum)
                else:
                    dictres[row.siteid][row.jpnum] = [row.pluscrevnum]
            else:
                dictres[row.siteid] = {row.jpnum:[]}
                dictres[row.siteid][row.jpnum] = [row.pluscrevnum]
    return dictres

def get_single_latest_jp_details(p_siteid, p_jpnum):
    '''
    Returns a jobplan instance populated with the data from the latest
    revision of the provided jobplan number
    ''' 
    thisjp = jobplan()
    with session_scope() as session:
        res = session.query(jp).filter(and_(jp.jpnum == p_jpnum, jp.pluscrevnum == max(dictJPrevs[p_siteid][p_jpnum]))).one()
        for x in range(0, len(cols_jp)):
            #print cols_jp[x].lower()
            setattr(thisjp, cols_jp[x].lower(), getattr(res, cols_jp[x].lower()))
        
        return thisjp
      
def get_all_latest_jp_details(p_jpnums):
    '''
    Returns a dictionary of all sites, containing a dictionary of all jobplan objects
    as the value
    '''
    try:
        assert isinstance(p_jpnums, dict)
    except AssertionError:
        raise Exception('Exception occurred.\n\tReceived something other than a dictionary')

    dictres = {}
    for site, jobplans in p_jpnums.iteritems():
        if site in dictres:
            for jp in jobplans.keys():
                dictres[site][jp] = get_single_latest_jp_details(site, jp)
        else:
            dictres[site] = {}
            for jp in jobplans.keys():
                dictres[site][jp] = get_single_latest_jp_details(site, jp)
    #print dictres
    #stop
    return dictres

def create_new_jobplans(p_jpdict):
    resdict = {}
    
    def update_new_jp(p_siteid, p_jp):
        global nextjpid
        jpUpdate = copy.copy(p_jp)
        jpUpdate.jobplanid = nextjpid
        nextjpid += 1
        jpUpdate.pluscchangeby = changeby
        jpUpdate.pluscchangedate = sqldate_format()
        jpUpdate.pluscrevcom = revisionComment 
        #print dictJPrevs[jpn]
        
        jpUpdate.pluscrevnum = max(dictJPrevs[p_siteid][jpn]) + 1
        #print  max(dictJPrevs[jpn]) + 1
        
        jpUpdate.pluscstatusdate = sqldate_format()
        jpUpdate.status = newJPStatus
        return jpUpdate

    
    for site, jobplans in p_jpdict.iteritems():
        if site in resdict:
            for jpn, jp in jobplans.iteritems():
                resdict[site][jpn] = update_new_jp(site, jp)
        else:
            for jpn, jp in jobplans.iteritems():
                resdict[site] = {jpn:{}}
                resdict[site][jpn] = update_new_jp(site, jp)
            
    return resdict

def create_jobplan_update_output(p_jpnum):
    jpdetail = dictJPLatest[p_jpnum]
#     jpdetail.pluscstatusdate = sqldate_format()
#     jpdetail.pluscchangedate = sqldate_format()
#     jpdetail.pluscchangeby = changeby
#     jpdetail.status = 'REVISED'
    strUpdate = "\tupdate jobplan set "
    for col, val in dictChangedJPFields.iteritems():
        strUpdate = strUpdate + col + " = " + chr(39) + val + chr(39) + ", "
    strUpdate = strUpdate.rstrip(', ') + " where jpnum = '" + p_jpnum + "' and pluscrevnum = '" + str(jpdetail.pluscrevnum) + "' and siteid = '" + jpdetail.siteid + "';\n"
    return strUpdate
        
def create_jobplan_insert_output(p_jpnum):
    fldstring = '('
    valstring = '('
    jpdetail = dictJPNew[p_jpnum]
        
    for x in range(0, len(cols_jp)):
        fldstring = fldstring + cols_jp[x] + ','
        if type(getattr(jpdetail, cols_jp[x].lower())) is datetime.datetime:
            thisval = sqldate_format(getattr(jpdetail, cols_jp[x].lower()))
        else:
            thisval = getattr(jpdetail, cols_jp[x].lower())
        valstring = valstring + chr(39) + xstr(thisval) + chr(39) + ','
    fldstring = fldstring.rstrip(',') + ')'
    valstring = valstring.rstrip(',') + ')'
    thissql = 'insert into jobplan %s values %s;\n' % (fldstring, valstring)
    return thissql
    #with open(outsqlpath + outjpfile, 'w') as f:

def create_pluscjpstatus_output(p_jpnum):
    global nextpluscjpstatusid
    strsql = ""
    strinsert = "\tinsert into pluscjpstatus (jpnum, jprevnum, status, changeby, changedate, orgid, siteid, pluscjpstatusid) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');\n"
    jpold = dictJPLatest[p_jpnum]
    jpnew = dictJPNew[p_jpnum]
    strsql = strinsert % (jpnew.jpnum, jpnew.pluscrevnum, pendingJPStatus, changeby, sqldate_format(), jpnew.orgid, jpnew.siteid, nextpluscjpstatusid) 
    nextpluscjpstatusid += 1
    strsql = strsql + strinsert % (jpold.jpnum, jpold.pluscrevnum, updatedJPStatus, changeby, sqldate_format(), jpold.orgid, jpold.siteid, nextpluscjpstatusid)
    nextpluscjpstatusid += 1
    strsql = strsql + strinsert % (jpnew.jpnum, jpnew.pluscrevnum, newJPStatus, changeby, sqldate_format(), jpnew.orgid, jpnew.siteid, nextpluscjpstatusid)
    nextpluscjpstatusid += 1
    return strsql
    
    
    
def create_output(p_dictin):
    try:
        assert isinstance(p_dictin, dict)
    except AssertionError:
        raise Exception('Exception occurred.\n\tReceived something other than a dictionary')
        sys.exit()
    with open(outSQLPath + outAllFile, 'w') as f:  
        for jpnum in p_dictin.keys():
            sqlstring = sqlLeadIn
            sqlstring = sqlstring + create_jobplan_insert_output(jpnum)
            sqlstring = sqlstring + create_jobplan_update_output(jpnum)
            sqlstring = sqlstring + create_pluscjpstatus_output(jpnum)
            #add other sql strings here for other operations
            sqlstring = sqlstring + sqlLeadOut
            f.write(sqlstring)

def get_one_set_job_tasks(p_siteid, p_jpnum, p_jprevnum):
    '''
    Returns a dictionary with the data for tasks for the jpnum and revnum provided
    keyed on the tasknum
    '''
    dictres = {}
    with session_scope() as session:
        res = session.query(jt).filter(and_(jt.siteid == p_siteid, jt.jpnum == p_jpnum, jt.pluscjprevnum == p_jprevnum)).all()
        for row in res:
            thisjt = jobtask()
            for x in range(0, len(cols_jt)):
                setattr(thisjt, cols_jt[x].lower(), getattr(row, cols_jt[x].lower()))
            dictres[thisjt.jptask] = thisjt
    return dictres
            
def create_new_tasklist(p_dict):
    try:
        assert isinstance(p_dict, dict)
    except AssertionError:
        raise Exception('Exception occurred.\n\tReceived something other than a dictionary')
    
    def strip_lead_in_tasks(p_dict):
        dict_temp = p_dict
        striplist = [r for r in range(0,101)]
        for key in p_dict.keys():
            if key in striplist:
                del dict_temp[key]
        return p_dict
    
    dictres = {}
    for site, jobplan in p_dict.iteritems():
        for jpnum, revs in jobplan.iteritems():
            revnum = max(revs)
            #print site, jpnum, revnum
            #stop
            newjp = allTasks[site][jpnum][revnum]
            #print newjp
            #stop
            if site == 'LCT':
                newjp = strip_lead_in_tasks(newjp)
            print jpnum, newjp[160].description
            stop
        
    
    return dictres

def create_all_jobtasks():
    '''
    This is a bit of a mind blower.  Fetches every single job task and arranges
    them in a dictionary thus;
        {'site':{'jobplan':{jprevnum:{jptask:jobtaskobject}}}}
    '''
    def create_task(p_row):
        thistask = jobtask()
        for x in range(0, len(cols_jt)):
            setattr(thistask, cols_jt[x].lower(), getattr(p_row, cols_jt[x].lower()))
        return thistask 
    
    dictres = {}
    with session_scope() as session:
        res = session.query(jt).all()
        for row in res:
            try:
                dictres[row.siteid][row.jpnum][row.pluscjprevnum][row.jptask] = create_task(row)
            except KeyError:
                try:
                    dictres[row.siteid][row.jpnum][row.pluscjprevnum] = {row.jptask:{}}
                    dictres[row.siteid][row.jpnum][row.pluscjprevnum][row.jptask] = create_task(row)
                except KeyError:
                    try:
                        dictres[row.siteid][row.jpnum] = {row.pluscjprevnum:{}}
                        dictres[row.siteid][row.jpnum][row.pluscjprevnum][row.jptask] = create_task(row)
                    except KeyError:
                        try:
                            dictres[row.siteid] = {row.jpnum:''}
                            dictres[row.siteid][row.jpnum] = {row.pluscjprevnum:{}}
                            dictres[row.siteid][row.jpnum][row.pluscjprevnum][row.jptask] = create_task(row)
                        except KeyError:
                            #print dictres
                            raise 
    return dictres

if __name__ == '__main__':
    #Fetch all job tasks
    allTasks = create_all_jobtasks()
    #print allTasks['LCT']['EL0104'][5]
    #stop
    
    #get columns for job plan
    cols_jp = getper('jobplan')
    cols_jt = getper('jobtask')
    #print cols_jt
    #stop
    
    #get list of all jobplans for list of sites
    dictJPrevs = get_jprevs(['LCT'])
    #print dictJPrevs
    #stop
    
    
    #dictJPLatest = get_all_latest_jp_details(dictJPrevs)
    dictJPLatest = get_all_latest_jp_details({'LCT':{'EL0104': [0, 1, 2, 3, 4, 5]}})
    #print dictJPLatest['LCT']['EL0104']
    #stop
    
    #Get the latest jobplan id
    nextjpid = gls('JOBPLAN', 'JOBPLANSEQ') + 1
    nextpluscjpstatusid = gls('PLUSCJPSTATUS', 'PLUSCJPSTATUSSEQ') + 1
    #Create updated jobplans
    #dictJPNew = create_new_jobplans(dictJPLatest)
    
    dictJPNew = create_new_jobplans(dictJPLatest)
    #print dictJPNew['LCT']['EL0104'].pluscrevnum
    #stop
    
    #get latest job tasks
    #tasklist = get_all_job_tasks(dictJPrevs)
    tasklist = create_new_tasklist(dictJPrevs)
    print tasklist['LCT']['EL0104'][101].description
    stop
    #Create output file for inserting new Jobplans
    #create_output(dictJPrevs)
    create_output(testdict)
    
    #Don't forget to update the jobplanid and PLUSCJPSTATUSSEQ in maxsequence