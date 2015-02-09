from dbconnect.tabledefs.MAXATTRIBUTE import MAXATTRIBUTE as ma
from dbconnect.tabledefs.MAXTABLE import MAXTABLE as mt
from dbconnect.tabledefs.MAXSEQUENCE import MAXSEQUENCE as ms

from dbconnect import session_scope
from sqlalchemy import and_

dictbool = {0:False, 1:True, None:False}

def get_table_unique_col(tbname):
    '''
    Finds the unique column name for a given table
    '''
    with session_scope() as session:
        return [r[0] for r in session.query(mt.uniquecolumnname).filter(mt.tablename == tbname)][0]
    
def get_all_table_unique_col():
    '''
    Returns a dictionary of table names with their unique column name as the value
    '''
    dictunique = {}
    with session_scope() as session:
        res = session.query(mt.tablename, mt.uniquecolumnname).all()
        #print res
        for row in res:
            dictunique[row[0]] = row[1]
    return dictunique

def does_table_exist(tbname, schema = 'dbo', catalog = 'maxdb75'):
    '''
    Checks to see if a table exists
    '''
    thissql = "SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '%s' and TABLE_CATALOG = '%s' AND  TABLE_NAME = '%s'" % (schema, catalog, tbname) 
    with session_scope() as session:
        try:
            return dictbool[[r[0] for r in session.execute(thissql)][0]]
        except:
            return False

def get_persistent_columns_for_object(objname):
    '''
    Returns a dictionary of column names for the provided table with an empty
    string as the value
    '''
    idx = 0
    dictres = {}
    with session_scope() as session:
        res = session.query(ma.attributename).filter(and_(ma.objectname == objname, ma.persistent == 1)).all()
        for row in res:
            dictres[idx] = row.attributename
            idx += 1
    return dictres

def get_latest_sequence(p_tbname, p_sequencename):
    with session_scope() as session:
        return session.query(ms.maxreserved).filter(and_(ms.tbname == p_tbname, ms.sequencename == p_sequencename)).one()[0]
