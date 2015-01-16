import csv
from dbconnect.tabledefs.ASSETS import ASSET
from dbconnect.tabledefs.CLASSSTRUCTURE import CLASSSTRUCTURE
from dbconnect import session_scope 
from sqlalchemy import and_

class classification():
    pass

dictclasses = {}
dictenthier = {}
dictentclass = {}
assetlist = []

def get_path(cs):
    path = ''
    path = ' \ ' + dictclasses[cs].classificationid
    parent = dictclasses[cs].parent
    while 1:
        #print path
        cs = parent
        path = ' \ ' + dictclasses[cs].classificationid + path
        parent = dictclasses[cs].parent
        if parent is None:
            
            path = path[3:]
            return path
        
def get_class_id(cs):
    return dictclasses[cs].classificationid
        
def get_cs_parent(cs):
    return dictclasses[cs].parent
    
def get_asset_cs(assetnum, siteid):
    '''
    Gets one assets classstructureid
    '''
    with session_scope() as session:
        return session.query(ASSET.classstructureid).filter(and_(ASSET.siteid == siteid, ASSET.assetnum == assetnum)).one()[0]
        

def get_classDict():
    '''
    Creates a dictionary of all classstructureid's and their associated attributes
    '''
    global dictclasses
    with session_scope() as session:
        classifications = session.query(CLASSSTRUCTURE.classstructureid, CLASSSTRUCTURE.classificationid, CLASSSTRUCTURE.parent, CLASSSTRUCTURE.siteid).all()
        
        for c in classifications:
            thisc = classification()
            setattr(thisc, 'classstructureid', c[0])
            setattr(thisc, 'classificationid', c[1])
            setattr(thisc, 'parent', c[2])
            setattr(thisc, 'siteid', c[3])
            dictclasses[c[0]] = thisc
            #print dictclasses['1008'].classificationid
            #stop

def get_ent_asset_hierarchy():
    '''
    Creates a dictionary of the enterprise hierarchy
    '''
    global dictenthier
    with session_scope() as session:
        bl = session.query(CLASSSTRUCTURE.classstructureid).filter(and_(CLASSSTRUCTURE.siteid == None, CLASSSTRUCTURE.haschildren == 0)).all()
        for c in bl:
            
            dictenthier[dictclasses.get(c[0]).classificationid] = get_path(c[0])
    
def get_ent_class():
    '''
    Creates a dictionary of the enterprise classificationid's and their classstructure ids.
    Used to look up the enterprise classstructureid for any given classificationid
    '''
    global dictentclass    
    with session_scope() as session:
        #bl = session.query(CLASSSTRUCTURE.classstructureid, CLASSSTRUCTURE.classificationid).filter(and_(CLASSSTRUCTURE.siteid == None, CLASSSTRUCTURE.haschildren == 0)).all()
        bl = session.query(CLASSSTRUCTURE.classstructureid, CLASSSTRUCTURE.classificationid).filter(CLASSSTRUCTURE.siteid == None).all()
        for c in bl:
            dictentclass[c[1]] = c[0]


def get_assets(siteid, numrows = 100):
    global assetlist
    with session_scope() as session:
        assetlist = [r[0] for r in session.query(ASSET.assetnum).filter(ASSET.siteid == siteid).limit(numrows).all()]

def map_classes(siteid):
    notfound = []
    for a in assetlist:
        thiscl = dictclasses[get_asset_cs(a, siteid)].classificationid
        if thiscl not in dictentclass:
            if thiscl not in notfound:
                notfound.append(thiscl)
    print notfound        
            
if __name__ == '__main__':
    siteid = 'LCT'
    #get_assets(siteid)
    #get_path('6542', siteid)
    
    get_classDict()
    #print dictclasses['1016'].classificationid
    #print get_path('1016')
    #get_ent_asset_hierarchy()
    
    get_ent_class()
    #print dictentclass
    #mycl = get_asset_cs('1881', siteid)
    #print mycl, dictentclass.get(mycl)
    
    get_assets(siteid)
    map_classes(siteid)
    #print assetlist