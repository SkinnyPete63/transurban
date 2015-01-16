import csv
from dbconnect.tabledefs.ASSETS import ASSET
from dbconnect import session_scope 
from sqlalchemy import and_

fp = "\\pch\\file_checking\\"
fn = "Asset_details.csv"
coldict = {}
assetdict = {}
concol = {"AS_DESCRIPTION":"DESCRIPTION", "AS_DESCRIPTION_LD":"DESCRIPTION_LONGDESCRIPTION", "AS_ITEMNUM":"ITEMNUM", \
          "AS_ITEMSETID":"ITEMSETID","AS_LOCATION":"LOCATION","AS_SITEID":"SITEID","AS_STATUS":"STATUS", \
          "AS_STATUSDATE":"STATUSDATE", "AS_ORGID":"ORGID", "AS_MANUFACTURER":"MANUFACTURER", "AS_NEWSITE":"NEWSITE", \
          "AS_BASEMEASURUTID": "BASEMEASURUTID"}

class asset:
    pass


def create_coldict():
    with open (fp + fn, "rb") as f:
        reader = csv.reader(f)
        rownum = 0
        c = 0
        r=reader.next()
        r=reader.next()
        for col in r:
            if col[0:3] == "AS_":
                coldict[c] = concol[col].lower()
                #print col
            elif col == "ORGID":
                coldict[c] = "MISSORGID"
            else:
                coldict[c] = col.lower()
            c += 1
    return coldict

def create_file_asset(data):
    a = asset()
    cn = 0
    for c in data:
        if c is None or c == '':
            c = 0
        setattr(a, coldict[cn], c)
        cn += 1
    assetdict[getattr(a,coldict[0])] = a
    
def get_file_assets():
    with open (fp + fn, "rb") as f:
        reader = csv.reader(f)
        rownum = 0
        for row in reader:
            if rownum > 1:
                create_file_asset(row)
                #print assetdict['1000'].DESCRIPTION

                #stop
            rownum += 1

def db_asset_local(dbasset):
    la = asset()
    for k, v in coldict.iteritems():
        try:
            myval = getattr(dbasset, v)
            if myval is None or myval == '':
                myval = 0
            setattr(la, v, myval)
        except AttributeError:
            pass
    return la


def get_db_asset(assetno):
    with session_scope() as session:
        thisasset = db_asset_local(session.query(ASSET).filter(and_(ASSET.assetnum == assetno, ASSET.siteid == 'CML')).one())
     
    return thisasset


def check_details(da, fa):
    print da.assetnum
    for k, v in coldict.iteritems():
        
        v=v.lower()
        try:
            if str(getattr(da, v)) <> str(getattr(fa,v)):
                if v in ['budgetcost', 'invcost', 'midlifecost', 'purchaseprice', 'replacecost', 'totalcost', 'totdowntime', \
                         'totunchargedcost', 'unchargedcost', 'ytdcost']:
                    if int(getattr(da, v)) <> int(getattr(fa,v)):
                        print v, getattr(da, v), getattr(fa,v)
                #print type(getattr(da, v)),type(getattr(fa, v))
                else:
                    print v, getattr(da, v), getattr(fa,v)
        except AttributeError:
            pass
            
def check_each():
    for k, v in assetdict.iteritems():
        #print v.__dict__
        with session_scope() as session:
            db_asset = get_db_asset(k)
            #print v.assetnum
            check_details(db_asset, v)
            #print k, db_asset.description
            stop


if __name__ == "__main__":
    cd = create_coldict()
    #print cd
    
    get_file_assets()
    #print assetdict['3724'].autowogen
    #stop
    check_each()
    
    