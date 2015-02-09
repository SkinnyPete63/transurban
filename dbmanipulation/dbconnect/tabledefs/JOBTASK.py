from dbconnect import Base, metadata, Table

class JOBTASK(Base):
    __table__ = Table('JOBTASK', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.jobtaskid]}

