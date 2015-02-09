from dbconnect import Base, metadata, Table

class MAXSEQUENCE(Base):
    __table__ = Table('MAXSEQUENCE', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.name, __table__.c.tbname]}

