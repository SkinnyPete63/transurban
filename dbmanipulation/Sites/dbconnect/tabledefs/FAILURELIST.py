from dbconnect import Base, metadata, Table

class FAILURELIST(Base):
    __table__ = Table('FAILURELIST', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.failurelist, __table__.c.orgid]}

