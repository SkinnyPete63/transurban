from dbconnect import Base, metadata, Table

class MAXOBJECT(Base):
    __table__ = Table('MAXOBJECT', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.objectname]}

