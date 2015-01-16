from dbconnect import Base, metadata, Table

class CLASSSTRUCTURE(Base):
    __table__ = Table('CLASSSTRUCTURE', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.classstructureid]}

