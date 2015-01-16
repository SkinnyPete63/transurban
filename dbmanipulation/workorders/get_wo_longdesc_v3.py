import csv
wodict = {}

with open("WO_Long_Text_Delta.TXT", "rb") as f:
    #reader = csv.reader(f, csv.excel_tab)
    for row in f:
        #print row
        #stop
        splits = row.split('|')
        wonum = splits[1]
        
        #print wonum
        if wonum in wodict:
            l1 = splits[4].strip()
            l2 = splits[5].strip()
            l3 = splits[6].strip()
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
            if len(splits[4].strip()) == 0:
                pass
            else:
                wodict[wonum][1] = splits[4].strip() + "\n"
            if len(splits[5].strip()) == 0:
                pass
            else:
                wodict[wonum][2] = splits[5].strip() + "\n"
            if len(splits[6].strip()) == 0:
                pass
            else:
                wodict[wonum][3] = splits[6].strip() + "\n"
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

