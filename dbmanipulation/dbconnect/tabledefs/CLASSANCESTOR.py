from dbconnect import Base, metadata, Table

class CLASSANCESTOR(Base):
    __table__ = Table('CLASSANCESTOR', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.ancestor, __table__.c.classstructureid]}
