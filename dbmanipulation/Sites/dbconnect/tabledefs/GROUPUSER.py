from dbconnect import Base, metadata, Table

class GROUPUSER(Base):
    __table__ = Table('GROUPUSER', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.groupname, __table__.c.userid]}

