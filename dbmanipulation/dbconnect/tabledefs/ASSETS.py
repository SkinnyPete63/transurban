from dbconnect import Base, metadata, Table

class ASSET(Base):
    __table__ = Table('ASSET', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.siteid]}
