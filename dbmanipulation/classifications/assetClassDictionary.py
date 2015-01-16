from dbconnect import session_scope
from sqlalchemy import and_
from dbconnect.tabledefs.CLASSSTRUCTURE import CLASSSTRUCTURE
import csv

basedict = {}
parentdict = {}
totaldict = {}
descdict = {}
def gp(baseid, id, mystr):
    newstr = mystr
    #print "Running gp "
    if parentdict[id] is not None:
        #print "Parent of " + id + " is " + parentdict[id] 
        #print basedict[parentdict[id]]
        newstr =  basedict[parentdict[id]] + " \\ " + newstr 
        #print newstr
        gp(baseid, parentdict[id], newstr)
    else:
        #print "It's none"
        totaldict[baseid] = newstr
#         return "This is it"
    #return newstr
    
with session_scope() as session:
    myres = session.query(CLASSSTRUCTURE).filter(and_(CLASSSTRUCTURE.orgid == None, ~CLASSSTRUCTURE.classificationid.in_(['ASSETS2', 'TEST_ASSET', 'LAND']))).all()
    for cs in myres:
        basedict[cs.classstructureid] = cs.classificationid
        parentdict[cs.classstructureid] = cs.parent
        descdict[cs.classstructureid] = cs.description
    #print basedict
    #print parentdict
    #print '6961'
    #gp('6961', '6961', basedict['6961'])
    #print totaldict
    
    for k,v in basedict.iteritems():
        if parentdict[k] is not None:
            gp(k, k, basedict[k] )
            #print thisp
            
with open("classhier.csv", "wb") as f:
    writer = csv.writer(f)  
    for k, v in  totaldict.iteritems():
        mylist = [k,v,descdict[k]]
        writer.writerow(mylist)