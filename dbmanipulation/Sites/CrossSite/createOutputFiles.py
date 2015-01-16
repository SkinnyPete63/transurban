import csv

dictlocs = {}
dictlevels = {}
templist = []
fldlist = []

class loc:
    pass

class levels:
    locs = []

def get_locs(path, fname, siteid, orgid):
    fldlist = []
    
    with open(path + '\\' + fname, 'rb') as f:
        reader = csv.reader(f)
        rownum = 0
        for row in reader:
            if rownum == 1:
                fldlist = row
            if rownum > 1:
                thisloc = loc()
                for x in range(0,len(fldlist)):
                    mystr = row[x].decode('windows-1252').replace(u'\xa0', ' ')
                    mystr = mystr.replace(u'\xef\xbf\xbd', ' ')
                    setattr(thisloc, fldlist[x], mystr)
                thisloc.SITEID = siteid
                thisloc.ORGID = orgid
                dictlocs[thisloc.LOCATION] = thisloc
            rownum += 1
    return dictlocs, fldlist
            
def build_levels(inlocs, inlevels, level = 1):
    templist = []
    level += 1
    for lok, lov in inlocs.iteritems():
        #print level
        theseparents = inlevels.get(level - 1)
        #print theseparents
        
        #read parent location
        #print lov.PARENT
        if lov.PARENT in theseparents:
            #print lov.PARENT
            #print lov.LOCATION
            templist.append(lov.LOCATION) 
    #print level, len(templist)
    if len(templist) >0:
        inlevels[level] = templist
        return (True, inlevels, level)
    else:
        return (False, inlevels, level)
    
def create_level_1():
    for k, v in dictlocs.iteritems():
        #print k
        if v.PARENT == u'':
            #print k
            dictlevels[1]=[k]
            #level += 1
    return dictlevels

def break_files(header, outpath, outfile, site, fldlist):
    for k,v in dictlevels.iteritems():
        fname = site + '_' + outfile + '_' + str(k) + '.csv'
        with open (outpath + fname, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            #print firstline
            writer.writerow(fldlist)
            for l in v:
                templist = []
                for fld in fldlist:
                    templist.append(getattr(dictlocs[l], fld))
                
                #print outlist
                writer.writerow(templist) 
               
