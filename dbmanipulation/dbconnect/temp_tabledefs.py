from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session
from dbconnect.parameters import *
import base64

decpass = base64.b64decode(dbpass)

connectstring = 'mssql+pyodbc://' + dbuser + ':' + decpass + '@' + dbserver + '/' + db + ';Trusted_Connection=Yes' 
Base = declarative_base()
engine = create_engine(connectstring)
metadata = MetaData(bind=engine)
session = create_session(bind=engine)

class ASSET(Base):
	__table__ = Table('ASSET', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.assetnum, __table__.c.siteid]}

class LOCATIONS(Base):
	__table__ = Table('LOCATIONS', metadata, autoload=True)
	__mapper_args__ = {'primary_key':[__table__.c.location, __table__.c.siteid]}

