import csv

dictlocs = {}
dictlevels = {}
level = 1
templist = []

firstline = []
fldlist = []

site = 'M2'
inpath = '\\pch\\M2'
outpath = '\\pch\\dataload\\ready\\'
outfile = 'locations'

class loc:
    pass

class levels:
    locs = []

def get_locs(path, fname):
    global firstline, fldlist
    
    with open(path + '\\' + fname, 'rb') as f:
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
               
if __name__ == '__main__':
    path = '\\pch\\M2'
    fname = 'locations.csv'
    get_locs(path, fname)
    #print dictlocs
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