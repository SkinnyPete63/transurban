import csv
import xlrd
import copy

from sqlalchemy import and_
from Sites.dbconnect import session_scope
from Sites.dbconnect.tabledefs.MAXSEQUENCE import MAXSEQUENCE as ms
class asset:
    pass

defasset = asset()

def newloc(wsm):
    '''
    Returns a dictionary of assets mapped to their new locations
    '''
    assetmap = {}
    num_rows = wsm.nrows - 1
    
    curr_row = 0
    while curr_row <= num_rows:
        try:
            assert isinstance(wsm.cell_value(curr_row, 0), float)
            assetmap[str(int(wsm.cell_value(curr_row, 0)))] = wsm.cell_value(curr_row, 1)
        except:
            assetmap[wsm.cell_value(curr_row, 0)] = wsm.cell_value(curr_row, 1)
        curr_row += 1
    #print assetmap['6589']
    #stop
    return assetmap

def get_flds(wsa):
    fldlist = {}
    num_cols = wsa.ncols -1
    #print num_cols
    curr_col = 0
    while curr_col <= num_cols:
        fldlist[curr_col] = wsa.cell_value(1, curr_col)
        curr_col += 1
    return fldlist

def create_default(wsd):
    defasset = asset()
    
    num_cols = wsd.ncols - 1
    
    curr_col = 0
    
    while curr_col <= num_cols:
        setattr(defasset, wsd.cell_value(0, curr_col), wsd.cell_value(1, curr_col))
        curr_col += 1
    return defasset

def get_max_assetid():
    with session_scope() as session:
        return session.query(ms.maxreserved).filter(ms.sequencename == 'ASSETIDSEQ').one()[0]
    
def get_assets(wsa, defasset, assetmap, holdinglocation, fldlist, site):
    #print assetmap['2810']
    #stop
    assets_top = {}
    assets_other = {}
    notmapped = {}
    num_rows = wsa.nrows - 1
    curr_row = 2

    while curr_row <= num_rows:
        thisasset = copy.copy(defasset)
        
        for k,v in fldlist.iteritems():
            if v in ['ASSET_ASSETID', 'ASSET_CHANGEBY', 'ASSET_CHANGEDATE', 'ASSET_HIERARCHYPATH']:
                setattr(thisasset, v, '')
            elif v in ['ASSET_LOCATION']:
                try:
                    if type(wsa.cell_value(curr_row, 1)) is float:
                        setattr(thisasset, v, assetmap[str(int(wsa.cell_value(curr_row, 1)))])
                    else:
                        setattr(thisasset, v, assetmap[wsa.cell_value(curr_row, 1)])
                except KeyError:
                    #print 'map not found for asset ' + str(wsa.cell_value(curr_row, 1))
                    #print type(wsa.cell_value(curr_row, 1))
                    #print assetmap
                    #stop
                    setattr(thisasset, v, None)
            elif v in ['ASSET_NEWSITE', 'ASSET_SITEID']:
                setattr(thisasset, v, site)
            else:
                setattr(thisasset, v, wsa.cell_value(curr_row, k))
        if thisasset.ASSET_PRIORITY == 0 : thisasset.ASSET_PRIORITY = 1
        
        if thisasset.ASSET_LOCATION == None:
            thisasset.ASSET_LOCATION = holdinglocation
            notmapped[thisasset.ASSET_ASSETNUM] = thisasset
        else:
            if thisasset.ASSET_PARENT == '' or thisasset.ASSET_PARENT == None:
                assets_top[thisasset.ASSET_ASSETNUM] = thisasset
            else:
                assets_other[thisasset.ASSET_ASSETNUM] = thisasset
        
        curr_row += 1
    
    return assets_top, assets_other, notmapped

def output_errors():
    global notmapped, site
    with open(errorpath + site + '_' + 'not_mapped.csv', 'wb') as f:
        writer = csv.writer(f)
         
        for k, v in notmapped.iteritems():
            writer.writerow([k])

def fixlist(mylist):
    for index, item in enumerate(mylist):
        if type(item) is float :
            mylist[index] = "%.*f" % (0, item )
    return mylist

def loadfile(fldlist, l1, outpath, site, dict, fname):
    templist = []
    with open(outpath + site + '_' + fname, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(l1)
        writer.writerow(fldlist.values())
        for k,v in dict.iteritems():
            templist = []
            for x in range(0, len(fldlist)):
                if getattr(v, fldlist[x]) in [0.0, 1.0]:
                    templist.append(int(getattr(v, fldlist[x])))
                else:
                    templist.append(getattr(v, fldlist[x]))
            fl = fixlist(templist)
            try:
                writer.writerow(fl)
            except UnicodeEncodeError:
                print fl

