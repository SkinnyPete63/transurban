from dbconnect import Base, metadata, Table

class MAXATTRIBUTE(Base):
    __table__ = Table('MAXATTRIBUTE', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.attributename, __table__.c.objectname]}
