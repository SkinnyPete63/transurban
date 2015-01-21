import datetime
import sys
import xlrd

from dbconnect.tabledefs.MAXATTRIBUTE import MAXATTRIBUTE as ma
from dbconnect.tabledefs.CLASSSTRUCTURE import CLASSSTRUCTURE as cs
from dbconnect.tabledefs.CLASSANCESTOR import CLASSANCESTOR as ca
from dbconnect import session_scope
from sqlalchemy import distinct, and_

tablelist = ['classancestor', 'classification', 'classspec', 'classspecusewith', 'classstructure', 'classusewith']
table_actions = {}

entasset = []
dictentasset = {}
check_tables = []

inpath = '\\pch\\dataload\\raw\\'
outsqlpath = '\\pch\\dataload\\sql_scripts\\'
outsqlfile = 'update_classifications.sql'

class Classification:
    def __init__(self, csid, classif, desc, level, map):
        self.csid = csid
        self.classif = classif
        self.desc = desc
        self.level = level
        self.map = map
    
def get_tables_with_sameasattribute(attrib):
    with session_scope() as session:
        return session.query(ma.objectname, ma.attributename).filter(and_(ma.sameasattribute == attrib, ~ma.objectname.in_(tablelist))).all()

def drop_backup_table(tbname):
    if 'backup' not in tbname:
        raise Exception('Tried to delete a non backup table')
        return False
    with session_scope() as session:
        thissql = 'drop table ' + tbname
        session.execute(thissql)
        return True

def backup_action_success(tbname, bu_tablename):
    if tbname in table_actions:
        thislist = table_actions.get(tbname)
        thislist.append('Table backed up to ' + bu_tablename)
        table_actions[tbname] = thislist
    else:
        table_actions[tbname] = ['Table backed up to ' + bu_tablename]
    
def backup_action_failed(tbname):
    if tbname in table_actions:
        thislist = table_actions.get(tbname)
        thislist.append('Table backup failed')
        table_actions[tbname] = thislist
    else:
        table_actions[tbname] = ['Table backup failed']

def backup_table(tbname):
    bu_tablename = tbname + '_backup_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    with session_scope() as session:
        thissql = 'SELECT * INTO ' + bu_tablename + ' FROM ' + tbname
        try:
            session.execute(thissql)
            backup_action_success(tbname, bu_tablename)
        except:
            backup_action_failed(tbname)

def backup_list_of_tables(tblist):
    this_function_name = sys._getframe(  ).f_code.co_name
    try:
        assert isinstance(tblist, list)
        for tb in tblist:
            backup_table(tb)
    except AssertionError:
        raise Exception('Exception in ' + this_function_name + '.\n\tPassed something other than a list')
    
def drop_all_backups_for_table(tbname):
    thissql = "SELECT * FROM information_schema.tables where table_name like '%" + tbname + "%backup%'"  
    #print thissql
    with session_scope() as session:
        tblist = session.execute(thissql)
        for table in tblist:
            drop_backup_table(table[2])

def get_children(parent):
    res = []
    try:
        assert isinstance(parent, str)
        with session_scope() as session:
            res.extend([r[0] for r in session.query(cs.classstructureid).filter(cs.parent == parent).all()])
            if len(res) > 0:
                return True, res
            else:
                return False, res
    except AssertionError:
        raise Exception('Tried to get children from a non string')
            
def get_entasset_list():
    with session_scope() as session:
        return [r[0] for r in session.query(ca.classstructureid).filter(ca.ancestor == '6717').distinct().all()]
         
def make_mapping(thislist):
    for csid in thislist:
        if csid in entasset:
            #print csid, thislist
            thislist.remove(str(csid))
            print csid, thislist
            stop
            dictentasset[csid] = thislist
            return
    
def read_spreadsheet():
    wb = xlrd.open_workbook(inpath + 'classifications.xlsx')
    colmap = {0:2, 1:3, 2:7, 3:9, 4:11}
    
    for x in range (0,5):
        ws = wb.sheet_by_name('Level ' + str(x))
        num_rows = ws.nrows - 1
        curr_row = 1
        while curr_row <= num_rows:
            if ws.cell_value(curr_row, colmap[x]) <>'':
                make_mapping([r.strip() for r in str(ws.cell_value(curr_row, colmap[x])).split(',')])
#                make_mapping()
            curr_row += 1
        #print dictentasset
        
def write_file_from_list(path, filename, list):
    with open(path + filename, "w") as f:
        for line in list:
            f.write(line)
            
def create_sql_statements():
    sqllist = []
    for k, v in dictentasset.iteritems():
        if len(v) > 0:
            for tc in check_tables:
                sqlstr = "Update " + tc[0] + " set " + tc[1] + " = '" + str(k) + "' where " + tc[1] + " in " + str(tuple(v)) + "\n"
                sqllist.append(sqlstr)
    write_file_from_list(outsqlpath, outsqlfile, sqllist)

if __name__ == '__main__':
    #backup all tables
    #backup_list_of_tables(tablelist)
    
    #get list of tables and columns that use classstructureid
    check_tables = get_tables_with_sameasattribute('classstructureid')
    #print check_tables
    
    #Make a list of the ENTASSET hierarchy entries
    entasset = get_entasset_list()
    
    #Make a dictionary of entasset classification with mapping from spreadsheet
    read_spreadsheet()
    
    #Construct sql statement
    create_sql_statements()

