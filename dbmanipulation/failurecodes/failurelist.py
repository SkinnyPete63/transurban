from dbconnect.tabledefs.FAILURELIST import FAILURELIST
import csv
from dbconnect import session_scope

with session_scope() as session:
    maxfail = session.query(FAILURELIST.failurelist).all()
    maxval = int(str(max(maxfail)[0]))
    #print maxval
    
parentdict = {}
with open("failurelist.csv", "rb") as f:
    
    reader = csv.reader(f)
    for row in reader:
        maxval = maxval+1
        if row[4] == None or row[4] == "":
            myparent = 'null'
        else:
            if row[4] not in parentdict:
                parentdict[row[4]] = maxval - 1
                myparent = maxval - 1
            else:
                myparent = str(parentdict[row[4]])
        sqlstr = "insert into failurelist(failurelist, failurecode, parent, type, orgid) values ('" + str(maxval) + "', '" + row[1] + "', " + str(myparent) + ", '" + row[3] + "', 'AML')"
        print sqlstr
        
print parentdict