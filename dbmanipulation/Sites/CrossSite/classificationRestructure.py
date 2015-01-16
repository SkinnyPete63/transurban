from dbconnect.tabledefs.MAXATTRIBUTE import MAXATTRIBUTE as ma
from dbconnect import session_scope
import datetime
import sys

tablelist = ['classancestor', 'classification', 'classspec', 'classspecusewith', 'classstructure', 'classusewith']
table_actions = {}


class Classification:
    def __init__(self, csid, classif, desc, level, map):
        self.csid = csid
        self.classif = classif
        self.desc = desc
        self.level = level
        self.map = map
    
def get_tables_with_sameasattribute(attrib):
    with session_scope() as session:
        return session.query(ma.objectname, ma.attributename).filter(ma.sameasattribute == attrib).all()

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
    
if __name__ == '__main__':
    #backup all tables
    backup_list_of_tables(tablelist)
    
    #Make a dictionary of the ENTASSET hierarchy entries
    
    #get list of tables and columns that use classstructureid
    #check_tables = get_tables_with_sameasattribute('classstructureid')
    #backup_list_of_tables(['classstructure'])
    #print table_actions
