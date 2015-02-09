from dbconnect import Base, metadata, Table

class JOBPLAN(Base):
    __table__ = Table('JOBPLAN', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.jpnum, __table__.c.orgid, __table__.c.pluscrevnum, __table__.c.siteid]}

