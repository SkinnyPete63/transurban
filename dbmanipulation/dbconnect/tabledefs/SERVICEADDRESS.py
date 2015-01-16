from dbconnect import Base, metadata, Table

class SERVICEADDRESS(Base):
    __table__ = Table('SERVICEADDRESS', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.addresscode, __table__.c.orgid]}

