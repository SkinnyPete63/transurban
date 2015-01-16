from dbconnect import Base, metadata, Table

class LOCHIERARCHY(Base):
    __table__ = Table('LOCHIERARCHY', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.parent, __table__.c.siteid, __table__.c.systemid]}

