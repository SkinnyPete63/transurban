from dbconnect import Base, metadata, Table

class FAILURECODE(Base):
    __table__ = Table('FAILURECODE', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.failurecode, __table__.c.orgid]}

