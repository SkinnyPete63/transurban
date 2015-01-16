from Sites.CrossSite.assetMove import newloc, get_flds, create_default, get_assets, loadfile
import xlrd

inpath = '\\pch\\dataload\\raw\\'
outpath = '\\pch\\dataload\\ready\\'
errorpath = '\\pch\\dataload\\errors\\'
infile = 'lct_assets_lvl_1_to_3.xlsx'
topfile = 'assets_top.csv'
otherfile = 'assets_other.csv'
notmappedfile = 'asset_move_to_dummy.csv'

site = 'LCTNEW'

wb = xlrd.open_workbook(inpath + infile)
wsa = wb.sheet_by_name('Assets')
wsm = wb.sheet_by_name('map')
wsd = wb.sheet_by_name('default')

fldlist = {}
assetmap = {}

l1 = ['EXTSYS1','AMIS_ASSET_R01', '', 'EN']
holdinglocation = 'DUMMY'



if __name__ == '__main__':
    assetmap = newloc(wsm)
    #print assetmap
    fldlist = get_flds(wsa)
    #print fldlist
    
    defasset = create_default(wsd)
    #print defasset.ASSET_NEWSITE
    assets_top, assets_other, notmapped = get_assets(wsa, defasset, assetmap, holdinglocation, fldlist, site)
    #print notmapped
    loadfile(fldlist, l1, outpath, site, assets_top, topfile)