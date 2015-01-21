import csv
import xlrd
import copy

inpath = '\\pch\\M2\\raw\\'
outpath = '\\pch\\dataload\\ready\\'
errorpath = '\\pch\\dataload\\errors\\'
infile = '\\assets.xlsx'
topfile = 'assets_top.csv'
otherfile = 'assets_other.csv'
notmappedfile = 'asset_move_to_dummy.csv'

site = 'M2'

wb = xlrd.open_workbook(inpath + infile)
wsa = wb.sheet_by_name('Assets')
wsm = wb.sheet_by_name('map')
wsd = wb.sheet_by_name('default')

fldlist = {}
assets_top = {}
assets_other = {}
assetmap = {}
notmapped = {}
#assetid = 80000
l1 = ['EXTSYS1','AMIS_ASSET_R01', '', 'EN']
holdinglocation = 'DUMMY'

class m2asset:
    pass


defasset = m2asset()

def newloc():
    global wsm, assetmap
    
    num_rows = wsm.nrows - 1
    
    curr_row = 0
    while curr_row <= num_rows:
        assetmap[wsm.cell_value(curr_row, 0)] = wsm.cell_value(curr_row, 1)
        curr_row += 1

def get_flds():
    global wsa, fldlist
    num_cols = wsa.ncols -1
    #print num_cols
    curr_col = 0
    while curr_col <= num_cols:
        fldlist[curr_col] = wsa.cell_value(1, curr_col)
        curr_col += 1
        
def create_default():
    global defasset, wsd
    
    num_cols = wsd.ncols - 1
    
    curr_col = 0
    
    while curr_col <= num_cols:
        setattr(defasset, wsd.cell_value(0, curr_col), wsd.cell_value(1, curr_col))
        curr_col += 1
        
def get_assets():
    global assets_top, assets_other, wsa, defasset, assetmap, notmapped, assetid, holdinglocation
    num_rows = wsa.nrows - 1
    curr_row = 2
    
    while curr_row <= num_rows:
        thisasset = copy.copy(defasset)
        
        for k,v in fldlist.iteritems():
            if v in ['ASSET_ASSETID', 'ASSET_CHANGEBY', 'ASSET_CHANGEDATE', 'ASSET_HIERARCHYPATH']:
                setattr(thisasset, v, '')
            elif v in ['ASSET_LOCATION']:
                try:
                    setattr(thisasset, v, assetmap[thisasset.ASSET_ASSETNUM])
                except KeyError:
                    setattr(thisasset, v, None)
            elif v in ['ASSET_NEWSITE', 'ASSET_SITEID']:
                setattr(thisasset, v, site)
            else:
                setattr(thisasset, v, wsa.cell_value(curr_row, k))
        #thisasset.ASSET_ASSETID = assetid
        #assetid += 1
        #thisasset.DISPLAYSEQUENCE = ds
        #ds += 1
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
        
def fixlist(mylist):
    for index, item in enumerate(mylist):
        if type(item) is float :
            mylist[index] = "%.*f" % (0, item )
    return mylist

def loadfile(dictry, fname):
    global fldlist, l1
    templist = []
    with open(outpath + site + '_' + fname, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(l1)
        for x in range(0, len(fldlist)):
            templist.append(fldlist[x])
        writer.writerow(templist)
        for v in dictry.values():
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

if __name__ == '__main__':
    newloc()
    #print assetmap['TMU-88']
    get_flds()
    #print fldlist
    create_default()
    #print defasset.PERSONID
    get_assets()
    #print notmapped
    #print assets
    #print assets['AIR-CTRL0002'].AS_DESCRIPTION
    #output_errors()
    loadfile(assets_top, topfile)
    loadfile(assets_other, otherfile)
    loadfile(notmapped, notmappedfile)