import csv

from sqlalchemy import and_

from dbconnect.tabledefs.LOCHIERARCHY import LOCHIERARCHY as lh

from dbconnect import session_scope

from dbconnect.usefulFunctions import get_persistent_columns_for_object as getper

dictlocs = {}
dictlevels = {}

level = 1
chunk_length = 1000

templist = []
firstline = []
fldlist = []
file_locs = []

site = 'M2'
inpath = '\\pch\\dataload\\raw\\'
infile = 'M2_locations.csv'
outpath = '\\pch\\dataload\\ready\\'
outfile = 'locations'
obsolete_loc = 'ZZ-OBSOLETE'
system = 'PRIMARY'
out_obs_file = 'M2_obsolete_locations.csv'

fl = ['EXTSYS1', 'AMIS_LOCHIER', None, 'EN']
sl = ['LOCATION_LOCATION', 'LOCATION_SITEID', 'LOCHIERARCHY_NEWPARENT', 'LOCHIERARCHY_PARENT', 'LOCHIERARCHY_SYSTEMID']

class loc:
    pass

class levels:
    locs = []

class lochier:
    pass

def get_locs(path, fname):
    global firstline, fldlist
    
    with open(path + fname, 'rb') as f:
        reader = csv.reader(f)
        rownum = 0
        for row in reader:
            #print row
            if rownum == 0:
                firstline = row
            if rownum == 1:
                fldlist = row
            if rownum > 1:
                thisloc = loc()
                for x in range(0,len(fldlist)):
                    mystr = row[x].decode('windows-1252').replace(u'\xa0', ' ')
                    mystr = mystr.replace(u'\xef\xbf\xbd', ' ')
                    setattr(thisloc, fldlist[x], mystr)
                dictlocs[thisloc.LOCATION] = thisloc
            rownum += 1
            
def build_levels():
    global level
    templist = []
    level += 1
    for lok, lov in dictlocs.iteritems():
        #print level
        theseparents = dictlevels.get(level - 1)
        #print theseparents
        
        #read parent location
        #print lov.PARENT
        if lov.PARENT in theseparents:
            #print lov.PARENT
            #print lov.LOCATION
            templist.append(lov.LOCATION) 
    if len(templist) >0:
        dictlevels[level] = templist
        return True
    else:
        return False
             
def create_level_1():
    global level
    for k, v in dictlocs.iteritems():
        #print k
        if v.PARENT == u'':
            #print k
            dictlevels[level]=[k]
            #level += 1

def break_files():
    global outpath, outfile, site
    for k,v in dictlevels.iteritems():
        fname = site + '_' + outfile + '_' + str(k) + '.csv'
        with open (outpath + fname, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(firstline)
            #print firstline
            writer.writerow(fldlist)
            for l in v:
                templist = []
                for fld in fldlist:
                    templist.append(getattr(dictlocs[l], fld))
                
                #print outlist
                writer.writerow(templist) 

def get_lochier():
    cols_lh = getper('lochierarchy')
    dictres = {}
    dict_parent = {}
    with session_scope() as session:
        res = session.query(lh).filter(and_(lh.siteid == site, ~lh.location.in_(file_locs))).all()
        for row in res:
            dict_parent[row.location] = row.parent
            thislh = lochier()
            for x in range(0, len(cols_lh)):
                setattr(thislh, cols_lh[x].lower(), getattr(row, cols_lh[x].lower()))
            dictres[row.location] = thislh
    delete_list = []
    #print dictres['09MED-DDP1255']
    #stop
    
    for location in dictres.keys():
        parent = dict_parent[location]
        if parent in dictres:
            #if location == '09MED-DDP1255':
                #print 'Location', location, 'with parent ', parent , ' found'
            if parent not in delete_list:
                delete_list.append(location)
    #print len(delete_list)
    for key in delete_list:
        del dictres[key]
    return dictres

def write_move_to_obsolete():
    with open(outpath + out_obs_file, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(fl)
        writer.writerow(sl)
        for lochier in dict_lochier_move.values():
            templist = []
            templist.append(lochier.location)
            templist.append(site)
            templist.append(obsolete_loc)
            templist.append(lochier.parent)
            templist.append(system)
            writer.writerow(templist)
        
if __name__ == '__main__':
    #Get locations from the fixed up locations file
    get_locs(inpath, infile)
    #print dictlocs
    #stop
    
    #Create simple list of all locations that are in the source file:
    file_locs = list(dictlocs.keys())
    #print file_locations
    #stop
    
    #Get lochierarchy entries for the relevant site
    dict_lochier_move = get_lochier()
    #print len(dict_lochier_move)
    #stop
    #print dict_lochier_move['10ENR-SRW'].parent
    #stop
    
    create_level_1()
    #print level, dictlevels[1]
    #stop
    while 1:
        if build_levels() == False:
            break
        #else:
        #    print level,dictlevels[level]
    break_files()
    
    write_move_to_obsolete()