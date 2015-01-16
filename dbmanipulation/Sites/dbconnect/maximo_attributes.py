from dbconnect import session_scope, MAXATTRIBUTE
from sqlalchemy import and_

def all_attributes():
    with session_scope() as session:
        attributelist = session.query(MAXATTRIBUTE).filter(MAXATTRIBUTE.objectname == tbname)
    
        for attribute in attributelist:
            print attribute.objectname, attribute.attributename, attribute.persistent, attribute.primarykeycolseq

def primary_cols(tbname):
    with session_scope() as session:
        primarylist = session.query(MAXATTRIBUTE).filter(MAXATTRIBUTE.objectname == tbname, MAXATTRIBUTE.primarykeycolseq <> None).all()
        mapargs = "__mapper_args__ = {'primary_key':["
        primary_cols = []
        #print primarylist.__dict__
        if len(primarylist) >0:
            for attribute in primarylist:
                if attribute.attributename.lower() == "class":
                    pass
                else:
                    mapargs = mapargs + "__table__.c." + attribute.attributename.lower() + ", "
            mapargs = mapargs[:-2] + "]}"
            return mapargs
        else:
            return None
        
    
def max_data_types(obj, fldlist):
    with session_scope() as session:
        typecon ={"ALN":"string", "DECIMAL":"float", "GL":"string", "DURATION":"float", "SMALLINT":"integer", "DATETIME":"datetime", "TIME":"datetime",
                  "BLOB":"string", "LOWER":"string", "CRYPTO":"string", "FLOAT":"float", "DATE":"datetime", "UPPER":"string", "CRYPTOX":"string",
                  "BIGINT":"integer", "AMOUNT":"float", "YORN":"bool", "INTEGER":"integer", "CLOB":"string", "LONGALN":"string"}
        typedict = {}
        cols = session.query(MAXATTRIBUTE).filter(obj == obj).all()
        for col in cols:
            if col.attributename in fldlist:
                typedict[col.attributename] = typecon[col.maxtype]
            
        return typedict
    
def get_sameas(colname, tblist):
    mydict = {}
    tlist = []
    with session_scope() as session:
        mysame = session.query(MAXATTRIBUTE).filter(and_(MAXATTRIBUTE.sameasattribute == colname, MAXATTRIBUTE.persistent == 1, MAXATTRIBUTE.objectname.in_(tblist))).all()
        
        for c in mysame:
            if c.objectname in mydict:
                tlist = mydict[c.objectname]
            else:
                tlist = []
                
            tlist.append(c.attributename)
            mydict[c.objectname] = tlist
            mydict["LOCATIONS"] = ["LOCATION"]
        return mydict

def get_sameas_one_table(tbname, colname):
    mydict = {}
    tlist = []
    with session_scope() as session:
        mysame = session.query(MAXATTRIBUTE).filter(and_(MAXATTRIBUTE.sameasattribute == colname, MAXATTRIBUTE.persistent == 1, MAXATTRIBUTE.objectname == tbname)).all()
        
        for c in mysame:
            if c.objectname in mydict:
                tlist = mydict[c.objectname]
            else:
                tlist = []
                
            tlist.append(c.attributename)
            mydict[c.objectname] = tlist
        return mydict

    
if __name__ == "__main__":
    tbname = 'CLASSSTRUCTURE'
    primary_cols(tbname)
    
