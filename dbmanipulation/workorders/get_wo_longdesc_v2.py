import csv
wodict = {}

c1s = 51
c1e = 123

c2s = 126
c2e = 198

c3s = 200
c3e = 308

with open("WO_Long_Text_Delta.TXT", "rb") as f:
    reader = csv.reader(f, csv.excel_tab)
    for row in reader:
        wonum = row[0][1:10]
        
        #print wonum
        if wonum in wodict:
#            l1 = row[0][51:153].strip()
#            l2 = row[0][155:258].strip()
#            l3 = row[0][259:360].strip()
            l1 = row[0][c1s:c1e].strip()
            l2 = row[0][c2s:c2e].strip()
            l3 = row[0][c3s:c3e].strip()
            myld1 = wodict[wonum][1]
            myld2 = wodict[wonum][2]
            myld3 = wodict[wonum][3]
            if len(l1) == 0:
                pass
            else:
                myld1 = myld1 + l1 + "\n"
                wodict[wonum][1] = myld1
            if len(l2) == 0:
                pass
            else:
                myld2 = myld2 + l2 + "\n"
                wodict[wonum][2] = myld2
            if  len(l3) == 0:
                pass
            else:
                myld3 = myld3 + l3 + "\n"
                wodict[wonum][3] = myld3
            
        else:
#             print wodict
#             print row[0]
            wodict[wonum] = {1:"", 2:"", 3:""}
            if len(row[0][c1s:c1e].strip()) == 0:
                pass
            else:
                wodict[wonum][1] = row[0][c1s:c1e].strip() + "\n"
            if len(row[0][c2s:c2e].strip()) == 0:
                pass
            else:
                wodict[wonum][2] = row[0][c2s:c2e].strip() + "\n"
            if len(row[0][c3s:c3e].strip()) == 0:
                pass
            else:
                wodict[wonum][3] = row[0][c3s:c3e].strip() + "\n"
#print wodict
 
 
with open("wo_long.csv", "wb") as of:
    writer = csv.writer(of)
    tempstring = ""
    for k,v in wodict.iteritems():
        #print k
        #print v
        tempstring = ""
        for k1, v1 in v.iteritems():
            #print v1
            tempstring = tempstring + v1
        outstring = [k, tempstring]
        writer.writerow(outstring)
         
##print wodict

