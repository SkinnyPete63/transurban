import csv
wodict = {}

c1s = 51
c1e = 123

c2s = 126
c2e = 198

c3s = 200
c3e = 308
with open("WO_Long_Text_Delta.TXT", "rb") as f:
    reader = csv.reader(f)
    for row in reader:
        wonum = row[0][1:10]
        
        #print wonum
        if wonum in wodict:
#            if len(row[0][51:153].strip()) == 0:
            if len(row[0][c1s:c1e].strip()) == 0:
                pass
            else:
                myld1 = wodict[wonum][1]
#                if row[0][51:153].strip() in myld1:
                if row[0][c1s:c1e].strip() in myld1:
                    pass
                else:
#                    myld1 = myld1 + row[0][51:153].strip() + "\n"
                    myld1 = myld1 + row[0][c1s:c1e].strip() + "\n"
                    wodict[wonum][1] = myld1
#            if len(row[0][155:258].strip()) == 0:
            if len(row[0][c2s:c2e].strip()) == 0:
                pass
            else:
                myld2 = wodict[wonum][2]
#                if row[0][155:258].strip() in myld2:
                if row[0][c2s:c2e].strip() in myld2:
                    pass
                else:
#                    myld2 = myld2 + row[0][155:258].strip() + "\n"
                    myld2 = myld2 + row[0][c2s:c2e].strip() + "\n"
                    wodict[wonum][2] = myld2
#            if len(row[0][259:360].strip()) == 0:
            if len(row[0][c3s:c3e].strip()) == 0:
                pass
            else:
                myld3 = wodict[wonum][3]
#                if row[0][259:360].strip() in myld3:
                if row[0][c3s:c3e].strip() in myld3:
                    pass
                else:
#                    myld3 = myld3 + row[0][259:360].strip() + "\n"
                    myld3 = myld3 + row[0][c3s:c3e].strip() + "\n"
                    wodict[wonum][3] = myld3
            
        else:
#             print wodict
#             print row[0]
            wodict[wonum] = {1:"", 2:"", 3:""}
#            if len(row[0][51:153].strip()) == 0:
            if len(row[0][c1s:c1e].strip()) == 0:
                pass
            else:
#                wodict[wonum][1] = row[0][51:153].strip() + "\n"
                wodict[wonum][1] = row[0][c1s:c1e].strip() + "\n"
#            if len(row[0][155:258].strip()) == 0:
            if len(row[0][c2s:c2e].strip()) == 0:
                pass
            else:
#                wodict[wonum][2] = row[0][155:258].strip() + "\n"
                wodict[wonum][2] = row[0][c2s:c2e].strip() + "\n"
#            if len(row[0][259:360].strip()) == 0:
            if len(row[0][c3s:c3e].strip()) == 0:
                pass
            else:
#                wodict[wonum][3] = row[0][259:360].strip() + "\n"
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

