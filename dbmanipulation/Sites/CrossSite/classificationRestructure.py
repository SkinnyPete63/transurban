import datetime
import sys
import xlrd
import os

from dbconnect.tabledefs.MAXATTRIBUTE import MAXATTRIBUTE as ma
from dbconnect.tabledefs.MAXOBJECT import MAXOBJECT as mo
from dbconnect.tabledefs.CLASSSTRUCTURE import CLASSSTRUCTURE as cs
from dbconnect.tabledefs.CLASSANCESTOR import CLASSANCESTOR as ca
from dbconnect.tabledefs.MAXTABLE import MAXTABLE as mt
from dbconnect.usefulFunctions import get_all_table_unique_col
from dbconnect import session_scope
from sqlalchemy import distinct, and_
from Sites.CrossSite.usefulFunctions import string_from_date

tablelist = ['classancestor', 'classification', 'classspec', 'classspecusewith', 'classstructure', 'classusewith']
table_actions = {}

entasset = []
droptables = []
tablesnokey = []
dicttablecols = {}
dictentasset = {}

inpath = '\\pch\\dataload\\raw\\'
outsqlpath = '\\pch\\dataload\\sql_scripts\\'
outsqlfile = '030_update_classifications.sql'
outBackupTables = '020_backup_tables.sql'
outClassBackupTables = '010_class_backup_tables.sql'
classMapFile = 'classification_mapping.xlsx'

initFileList = [outsqlfile, outBackupTables, outClassBackupTables]

def check_for_data(t, c):
    '''
    Checks for data in a specific table column combination
    '''
    thissql = 'select count(1) from %s where %s is not null' % (t, c)
    with session_scope() as session:
        res = [r[0] for r in session.execute(thissql)][0]
        if res > 0:
            return True
        else:
            return False
    
def make_table_column_dict(tclist):
    '''
    tclist is a list of tuples with two entries, table and column name. This
    routine checks to see if there are any values in the table column 
    combination and creates a dictionary of table names with a list of column names
    as the dictionary value if there are
    '''
    dicttc = {}
    for e in tclist:
        if check_for_data(e[0], e[1]):
            templist = []
            #Does the table name already exist in the dictionary
            if e[0] in dicttc:
                #It does, so get the list of column names
                templist = dicttc[e[0]]
                #Is the field name already in the list
                if e[1] not in templist:
                    #If not, add it to the list
                    templist.append(e[1])
                    #Update the dictionary with the new list
                    dicttc[e[0]] = templist
            #The table name is not already in the dictionary
            else:
                dicttc[e[0]] = [e[1]]
    return dicttc
                
def get_tables_with_sameasattribute(attrib):
    '''
    returns a dictionary containing table names and a list of columns which
    are identified in maxattribute as being the same as 
    '''
    with session_scope() as session:
        return make_table_column_dict(session.query(ma.objectname, ma.attributename).filter(and_(ma.persistent == 1, ma.sameasattribute == attrib, ~ma.objectname.in_(tablelist), ma.objectname.in_(session.query(mo.objectname).filter(and_(mo.isview == 0, mo.persistent == 1))))).all())

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

def backup_table(fpath, fname, tbname):
    bu_tablename = tbname + '_backup'
    thissql = 'SELECT * INTO %s FROM %s;\n' % (bu_tablename, tbname) 
    if not os.path.isfile(fpath + fname):
        with open(fpath + fname, 'w') as f:
            f.write(thissql)
    else:
        with open(fpath + fname, 'a') as f:
            f.write(thissql)


def backup_list_of_tables(fpath, fname, tblist):
    
    try:
        assert isinstance(tblist, list)
    except AssertionError:
        raise Exception("Exception occurred.\n\tReceived something other than a list")
    
    
    for tb in tblist:

        bu_table = tb + '_backup'

        mysql = "SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '%s' and TABLE_CATALOG = '%s' AND  TABLE_NAME = '%s'" % ('dbo', 'maxdb75', bu_table)    
        with session_scope() as session:
            try:
                res = [r[0] for r in session.execute(mysql)][0]
                rename_backup_table(outsqlpath, outClassBackupTables, bu_table)
                backup_table(outsqlpath, outClassBackupTables, tb)
            except IndexError:
                #print mysql
                backup_table(outsqlpath, outClassBackupTables, tb)

            



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
            
def get_entasset_list(ancest):
    with session_scope() as session:
        return [r[0] for r in session.query(ca.classstructureid).filter(ca.ancestor == ancest).distinct().all()]
         
def make_mapping(thislist):
    for csid in thislist:
        if csid in entasset:
            #print csid, thislist
            thislist.remove(str(csid))
            #print csid, thislist
            
            dictentasset[csid] = thislist
            return
    
# def read_spreadsheet():
#     
#     #wb = xlrd.open_workbook(inpath + 'classifications.xlsx')
#     wb = xlrd.open_workbook(inpath + classMapFile)
#     colmap = {0:2, 1:3, 2:7, 3:9, 4:11}
#     
#     for x in range (0,5):
#         ws = wb.sheet_by_name('Level ' + str(x))
#         num_rows = ws.nrows - 1
#         curr_row = 1
#         while curr_row <= num_rows:
#             if ws.cell_value(curr_row, colmap[x]) <>'':
#                 make_mapping([r.strip() for r in str(ws.cell_value(curr_row, colmap[x])).split(',')])
# #                make_mapping()
#             curr_row += 1
#         #print dictentasset
def read_mapping():
    dictres = {}
    wb = xlrd.open_workbook(inpath + classMapFile)
    
    ws = wb.sheet_by_name('Sheet1')
    num_rows = ws.nrows - 1
    curr_row = 1
    while curr_row <= num_rows:
        if ws.cell_value(curr_row, 1) is None or ws.cell_value(curr_row, 1) == '':
            pass
        else:
            try:
                if type(ws.cell_value(curr_row, 1)) is float:
                    #print "This is a float: ", ws.cell_value(curr_row, 1)
                    dictres[str(int(ws.cell_value(curr_row, 0)))] = [str(int(ws.cell_value(curr_row, 1)))]
                    #print dictentasset[int(ws.cell_value(curr_row, 0))]
                else:
                    #print "So this should be a list: ", ws.cell_value(curr_row, 1)
                    dictres[str(int(ws.cell_value(curr_row, 0)))] = ws.cell_value(curr_row, 1).split(',')
                    #print dictentasset[int(ws.cell_value(curr_row, 0))]
            except IndexError:
                print ws.cell_value(curr_row, 0), ws.cell_value(curr_row, 1)
            #print dictentasset[int(ws.cell_value(curr_row, 0))] 
        curr_row += 1
    return dictres

def write_file_from_list(path, filename, inlist):
    with open(path + filename, "w") as f:
        for line in inlist:
            f.write(line)
            
def create_update_sql_statements(dictin):
    sqllist = []
    for k, v in dictentasset.iteritems():
        if len(v) > 0:
#             for tc in check_tables:
#                 sqlstr = "Update " + tc[0] + " set " + tc[1] + " = '" + str(k) + "' where " + tc[1] + " in " + str(tuple(v)) + "\n"
#                 sqllist.append(sqlstr)
            for table, cols in dictin.iteritems():
                for column in cols:
                    if len(v) == 1:
                        vallist = "= '" + v[0] + "'"
                    else:
                        vallist = "in " + str(tuple(v))
                    sqlstr = "Update %s set %s = '%s' where %s %s\n" % (table, column, str(k), column, vallist)
                    sqllist.append(sqlstr)
    write_file_from_list(outsqlpath, outsqlfile, sqllist)

def rename_backup_table(fpath, fname, tbname):
    newname = tbname + '_' + string_from_date()
    thissql = "EXEC sp_rename '%s', '%s';\n" % (tbname, newname)
    
#    if not os.path.isfile(outsqlpath + outBackupTables):
    if not os.path.isfile(fpath + fname):
        with open(fpath + fname, 'w') as f:
            f.write(thissql)
    else:
        with open(fpath + fname, 'a') as f:
            f.write(thissql)

def write_backup_table(table, bu_table, cols):
    tempstr = ""
    unique_col = dictunique[table]
    whereclause = ''
    try:
        tempstr = unique_col + ', '
        whereclause = 'where '
        for column in cols:
            whereclause = whereclause + column + ' is not null or'
        whereclause = whereclause.rstrip(' or')
        for column in cols:
            tempstr = tempstr + column + ', '
        tempstr = tempstr.rstrip(', ')
        thissql = "select %s into %s from %s %s;\n" % (tempstr, bu_table, table, whereclause)
        if not os.path.isfile(outsqlpath + outBackupTables):
            with open (outsqlpath + outBackupTables, 'w') as f:
                f.write(thissql)
        else:
            with open (outsqlpath + outBackupTables, 'a') as f:
                f.write(thissql)
    except:
        tablesnokey.append(table)
        
    
def backup_affected_columns(indict):
    '''
    Creates a backup table of each table that could be affected with just the
    columns that may be altered
    '''
    if os.path.isfile(outsqlpath + outBackupTables):
        os.remove(outsqlpath + outBackupTables)
    for table, cols in indict.iteritems():
        bu_table = table + '_csid_backup'
        mysql = "SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '%s' and TABLE_CATALOG = '%s' AND  TABLE_NAME = '%s'" % ('dbo', 'maxdb75', bu_table)
        
        with session_scope() as session:
            try:
                res = [r[0] for r in session.execute(mysql)][0]
                rename_backup_table(outsqlpath + outBackupTables, bu_table)
                write_backup_table(table, bu_table, cols)
            except IndexError:
                #print mysql
                write_backup_table(table, bu_table, cols)
                
        for column in cols:
            pass


def create_delete_sql_statements():
    pass

def clean_whitespace_dict(indict):
    cleandict = {}
    for k, v in indict.iteritems():
        cleandict[k] = [r.strip().encode('UTF8') for r in v]
    return cleandict

def init_script_files(p_path, p_filelist):
    for fname in p_filelist:
        with open(p_path + fname, "wb") as f:
            f.write('')
            
if __name__ == '__main__':
    #Initialise script files
    init_script_files(outsqlpath, initFileList)
    
    #backup all tables that define the class structures
    backup_list_of_tables(outsqlpath, outClassBackupTables, tablelist)
    #stop
    
    #get dict of table unique columns
    dictunique = get_all_table_unique_col()
    #print dictunique
    #stop
    
    #get list of tables and columns that use classstructureid
    dicttablecols = get_tables_with_sameasattribute('classstructureid')
    #print dicttablecols
    #stop
    
    #Backup the columns from the tables that may get changed
    #backup_affected_columns(dicttablecols)
    #print tablesnokey
    #stop
    
    #Make a list of the ENTASSET hierarchy entries
    #entasset = get_entasset_list('6717')
    
    #Make a dictionary of entasset classification with mapping from spreadsheet
    dictentasset = clean_whitespace_dict(read_mapping())
    #print dictentasset
    #for k, v in dictentasset.iteritems():
    #    print k,v
    #stop
    #Construct sql statements to update values
    create_update_sql_statements(dicttablecols)
    
    #Construct sql statements to delete redundant entries in classification
    #defintition tables
    create_delete_sql_statements()

