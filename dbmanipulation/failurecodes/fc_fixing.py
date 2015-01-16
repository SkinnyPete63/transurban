from dbconnect import session_scope
from dbconnect.tabledefs.WORKORDER import WORKORDER
from dbconnect.tabledefs.FAILURECODE import FAILURECODE
from dbconnect.tabledefs.FAILURELIST import FAILURELIST
from sqlalchemy import and_, not_

fclist = []
with session_scope() as session:
    fcs = session.query(FAILURELIST).filter(and_(FAILURELIST.parent == None, FAILURELIST.orgid == 'TUCML')).all()
    for fc in fcs:
        fclist.append(fc.failurecode)
    #print fclist
    
    #edwo = session.query(WORKORDER).filter(and_(WORKORDER.siteid == 'ED', WORKORDER.failurecode.in_(fclist))).all()
    edwo = session.query(WORKORDER).filter(and_(WORKORDER.siteid == 'ED', not_(WORKORDER.failurecode.in_(['ELECTRONIC', 'ELECTRICAL', 'MECHANICAL', 'STRUCTURE', 'LANDSCAPING', 'PAVEMENT', 'HYDRAULIC'])))).one()
    for rec in edwo:
        print rec.wonum