import csv
pmdict = {}

with open("pmlong_full_fixed.txt", "rb") as f:
    reader = csv.reader(f, csv.excel_tab)
    for row in reader:
        pmnum = row[0]
        print pmnum
        if pmnum in pmdict:
            myld = pmdict[pmnum]
            myld = myld + row[1] + "<br />"
            pmdict[pmnum] = myld
        else:
            pmdict[pmnum] = row[1] + "<br />"


with open("pm_long2.csv", "wb") as of:
    writer = csv.writer(of)
    for k,v in pmdict.iteritems():
        #print v
        outstring = [k,v]
        writer.writerow(outstring)
        
##print wodict

