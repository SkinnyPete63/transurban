# -*- coding: utf-8 -*-
'''
Raw data provided in excel spreadsheet required locations to be 01, 02 etc, 
but excel stores as 1, 2 etc.  This routine fixes that up.

On first data load, ? appearing in data.  These were non-breaking spaces
so added decode and replace to get rid of those.

26-Nov-14
More odd characters, removed
'''
import csv
import chardet    


inpath = "\\pch\\M2"
infile = "locations_raw.csv"
outfile = "locations.csv"
fldlist = []
locations = {}
header = ['EXTSYS1', 'AMIS_LOCATIONS', None,'EN']
#rawdata=open(inpath + "\\" + infile,"r").read()
#print chardet.detect(rawdata)

   
class m2loc:
    pass



with open(inpath + "\\" + infile, "rb") as f:
    reader = csv.reader(f)
    rownum = 0
    for row in reader:
        if rownum == 1:
            secondline = row
        if rownum > 0:
            if rownum == 1:
                fldlist = row
            else:
                thisloc = m2loc()
                for x in range(0,len(fldlist)):
                    #print chardet(row[x])
                    #Gets rid of non-breaking spaces
                    mystr = row[x].decode('windows-1252').replace(u'\xa0', ' ')
                    mystr = mystr.replace(u'\xef\xbf\xbd', ' ')
                    setattr(thisloc, fldlist[x], mystr)
                #adjust for excel storing 01 as 1 etc
                if len(thisloc.LOCATION) == 1:
                    thisloc.LOCATION = '0' + str(thisloc.LOCATION)
                #adjust for excel storing 01 as 1 etc
                if len(thisloc.PARENT) == 1:
                    thisloc.PARENT = '0' + str(thisloc.PARENT)
                locations[rownum] = thisloc
                #print locations
                #stop
            #print row
        rownum += 1
        
#write the output file
with open(inpath + "\\" + outfile, "wb") as f:
    #first and second lines taken directly from input file
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(secondline)
    for k,v in locations.iteritems():
        templist = []
        for x in range(0, len(fldlist)):
            templist.append(getattr(v, fldlist[x]))
        writer.writerow(templist)
        