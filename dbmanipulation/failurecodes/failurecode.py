from dbconnect.tabledefs.FAILURECODE import FAILURECODE
import csv
from dbconnect import session_scope

with session_scope() as session:
    maxfail = session.query(FAILURECODE.failurecodeid).all()
    maxval = int(str(max(maxfail)[0]))
    
with open("failurecode.csv", "rb") as f:
    reader = csv.reader(f)
    for row in reader:
        maxval = maxval+1
        sqlstr = "insert into failurecode(failurecode, description, orgid, failurecodeid, langcode, hasld) values ('" + row[0] + "', '" + row[1] + "', 'AML', " + str(maxval) + ", 'EN', 0)"
        print sqlstr