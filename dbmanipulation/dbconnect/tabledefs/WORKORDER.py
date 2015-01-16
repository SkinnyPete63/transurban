from dbconnect import Base, metadata, Table

class WORKORDER(Base):
    __table__ = Table('WORKORDER', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.siteid, __table__.c.wonum]}
