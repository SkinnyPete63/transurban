import xlrd
from dbconnect.tabledefs.LOCHIERARCHY import LOCHIERARCHY

from dbconnect import session_scope

from sqlalchemy import and_

#import logging
#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

inpath = '\\pch\\M2\\raw\\'
infile = 'Locations.xls'

wb = xlrd.open_workbook(inpath + infile)
ws = wb.sheet_by_name('locations')

num_rows = ws.nrows - 1

curr_row = 2

m2locs = {}

def same_parent(l, p):
    global m2locs
    dbp = m2locs.get(l)
    if dbp == p:
        return True
    else:
        return False
    
def location_exists(l):
    global m2locs
    if l in m2locs:
        return True
    else:
        return False
    
def check_locs():
    global curr_row, ws
    while curr_row <= num_rows:
        #print ws.cell_value(curr_row, 0), ws.cell_value(curr_row, 8)
        l = ws.cell_value(curr_row, 0)
        p = ws.cell_value(curr_row, 8)
        if location_exists(l):
            if not same_parent(l, p):
                print 'Different parent: ' + l
            if location_exists(p):
                pass
            else:
                print 'Parent does not exist: ' + p
        else:
            print 'Location does not exist: ' + l
        curr_row += 1

def get_locations():
    global session, m2locs
    
    with session_scope() as session:
        locs = session.query(LOCHIERARCHY.location, LOCHIERARCHY.parent).filter(LOCHIERARCHY.siteid == 'M2').all()
        #print locs
        #exit
        
        for l in locs:
            m2locs[l[0]] = l[1]
    #print m2locs
    #print len(m2locs)
    
if __name__ == '__main__':
    get_locations()
    check_locs()