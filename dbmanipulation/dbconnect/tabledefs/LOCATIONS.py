from dbconnect import Base, metadata, Table

class LOCATIONS(Base):
    __table__ = Table('LOCATIONS', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.siteid]}

