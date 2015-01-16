from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from dbconnect.parameters import development as env
from dbconnect.parameters import prod as env

import base64
from contextlib import contextmanager
from sqlalchemy import Table, MetaData

Base = declarative_base()


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()



decpass = base64.b64decode(env['dbpass'])
decserv = base64.b64decode(env['dbserver'])
decuser = base64.b64decode(env['dbuser'])
decdb = base64.b64decode(env['db'])

#use this with trusted connection
#connectstring = 'mssql+pyodbc://' + decuser + ':' + decpass + '@' + decserv + '/' + decdb + ';Trusted_Connection=Yes'
connectstring = 'mssql+pyodbc://' + decuser + ':' + decpass + '@' + decserv + '/' + decdb 
# an Engine, which the Session will use for connection
# resources
engine = create_engine(connectstring)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

metadata = MetaData(bind=engine)

class MAXOBJECT(Base):
    __table__ = Table('MAXOBJECT', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.objectname]}
    
class MAXATTRIBUTE(Base):
    __table__ = Table('MAXATTRIBUTE', metadata, autoload=True)
    __mapper_args__ = {'primary_key':[__table__.c.objectname, __table__.c.attributename]}