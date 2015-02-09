from dbconnect import Base, metadata, Table

class MAXTABLE(Base):
    __table__ = Table('MAXTABLE', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.tablename]}
