from dbconnect import Base, metadata, Table

class APPLICATIONAUTH(Base):
    __table__ = Table('APPLICATIONAUTH', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.app, __table__.c.groupname, __table__.c.optionname]}
