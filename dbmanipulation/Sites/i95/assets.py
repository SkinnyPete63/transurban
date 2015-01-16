# -*- coding: utf-8 -*-
import xlrd
import copy
import csv
from i95_generic import fix_MM

class asset:
    pass

defass = asset()
header = []
fieldlist = []
bridgecols = {}
dictbridge = {}
signcols = {}
dictsigns = {}
dictlp = {}

lpatts = {1:'LUMIS', 2:'LUMWATT', 3:'MTHEIGHT'}
intlist = ['DESIGNLIFE', 'LINEARASSETSPECID']
boolist = ['AUTOWOGEN', 'CHANGEPMSTATUS', 'CHILDREN', 'CONTINUOUS', 'DISABLED', 'INHERITEDFROMITEM', 'ISCALIBRATION', 'ISLINEAR', 'ISRUNNING', 'ITEMSPECVALCHANGED', 'MAINTHIERCHY', 'MANDATORY', 'MOVED', 'PLUSCISCONTAM', 'PLUSCISINHOUSECAL', 'PLUSCISMTE', 'PLUSCPMEXTDATE', 'PLUSCSOLUTION', 'REMOVEFROMACTIVEROUTES', 'REMOVEFROMACTIVESP', 'RETURNEDTOVENDOR', 'ROLLTOALLCHILDREN', 'TLOAMPARTITION', 'TOTALCOST', 'YTDCOST', 'DISPLAYSEQUENCE']
smintlist = []
specflds = ['ASSPEC_ASSETATTRID', 'ASSPEC_LINEARASSETSPECID', 'ASSPEC_MESRUNITID', 'ASSPEC_NUMVALUE', 'ASSPEC_ORGID', 'ASSPEC_SECTION']

wb = xlrd.open_workbook('Assets.xlsm')
wsb = wb.sheet_by_name('Bridges')
wss = wb.sheet_by_name('Static')
wssg = wb.sheet_by_name('Signs')

outpath = '\\pch\\dataload\\ready\\'
site = 'I95'
fname = 'assets.csv'

def confirm():
    return True
    myinput = raw_input("Have you copied the source file (type Yes to confirm - case sensitive!)")
    if myinput == "Yes":
        #print "Exiting......."
        return True
    else:
        return False

def get_def_asset():
    global defass, wb, wss, boolist, intlist
    
    num_cells = wss.ncols

    #print ws.cell_value(0,0)
    defass = asset()
    for x in range(0, num_cells):
        #print ws.cell_value(0,x)
#        if wss.cell_value(0,x) in boolist or wss.cell_value(0,x) in intlist:
            #print 'boolean or integer - ', wss.cell_value(0,x)
#            setattr(defass, wss.cell_value(0,x), int(wss.cell_value(1,x)))
        if wss.cell_value(1,x) in['0.0', '1.0']:
            #print '0.0 or 1.0 - ', wss.cell_value(1,x)
            setattr(defass, wss.cell_value(0,x), int(wss.cell_value(1,x)))
        else:
            #print 'other type - ', wss.cell_value(0,x)
            setattr(defass, wss.cell_value(0,x), wss.cell_value(1,x))

def get_header():
    global header, wss
    
    num_cells = 4

    for x in range(0, num_cells):
        #print x, ws.cell_value(5, x)
        header.append(wss.cell_value(10, x))
    return True
 
def get_cols(ws, row):
    tempcols = {}
    num_cells = ws.ncols
    for x in range(0, num_cells):
        tempcols[x]=(ws.cell_value(row,x))
    return tempcols

def get_bridges():
    global defass, wsb, dictbridge, bridgecols, boolist, intlist
    #print "On entry - ", defass.ASSETNUM
    
    num_rows = wsb.nrows
#    num_rows = 2
    num_cells = wsb.ncols
    
    curr_row = 1
    while curr_row < num_rows:
        #print curr_row
        tb = copy.copy(defass)
        #print "In loop - ", tb.ASSETNUM
        for x in range(0, num_cells):
            #print ws.cell_value(curr_row,x)
            if wsb.cell_value(0,x) in boolist or wsb.cell_value(0,x) in intlist:
                setattr(tb, bridgecols[x], int(wsb.cell_value(curr_row,x)))
            elif wsb.cell_value(0,x) in ['0.0', '1.0']:
                setattr(tb, bridgecols[x], int(wsb.cell_value(curr_row,x)))
            else:
                setattr(tb, bridgecols[x], wsb.cell_value(curr_row,x))
        dictbridge[wsb.cell_value(curr_row,1)] = tb
        
        curr_row += 1
    return True

def get_signs():
    global defass, wssg, dictsigns, signcols, boolist, intlist
    
    num_rows = wssg.nrows
    #print num_rows
    num_cells = wssg.ncols
    #print num_cells
    curr_row = 3
    while curr_row < num_rows:
        #print curr_row
        tb = copy.copy(defass)
        #print wssg.cell_value(curr_row,0).decode('windows-1252').replace(u'\u2010', '')
        for x in range(0, num_cells):
            if signcols[x] == 'CUST_PERSONID':
                if wssg.cell_value(curr_row,x) is not None:
                    setattr(tb, 'CUST_ISCUSTODIAN', 1)
            if wssg.cell_value(1,x) in boolist or wssg.cell_value(1,x) in intlist:
                setattr(tb, signcols[x], int(wssg.cell_value(curr_row,x)))
            else:
                setattr(tb, signcols[x], wssg.cell_value(curr_row,x))
                
        dictsigns[wssg.cell_value(curr_row,0).decode('ISO-8859-2')] = tb
        
        curr_row += 1
    return True
    
def get_fields():
    global wss, fieldlist
    
    for x in range(0, wss.ncols):
        fieldlist.append(wss.cell_value(0,x))
    return True

def write_file():
    
    global defass, fieldlist, dictbridge, outpath, fname, site
    with open(outpath + site + '_' + fname, "wb")as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(fieldlist)
        for k, v in dictbridge.iteritems():
            templist = []
            for fld in fieldlist:
                if getattr(v,fld) in[0.0, 1.0]:
                    templist.append(int(getattr(v,fld)))
                else:
                    templist.append(getattr(v,fld))
            writer.writerow(templist)
        for k, v in dictsigns.iteritems():
            templist = []
            for fld in fieldlist:
                if getattr(v,fld) in[0.0, 1.0]:
                    templist.append(int(getattr(v,fld)))
                else:
                    templist.append(getattr(v,fld))
            writer.writerow(templist)
        for k, v in dictlp.iteritems():
            templist = []
            for fld in fieldlist:
                if getattr(v,fld) in[0.0, 1.0]:
                    templist.append(int(getattr(v,fld)))
                else:
                    templist.append(getattr(v,fld))
            writer.writerow(templist)


def get_light_poles():
    global defass, wb, dictlp, lpatts, specflds
    segs = ['SEG01', 'SEG02S', 'SEG02N', 'SEG03S', 'SEG03N', 'SEG04']
    attcount = 1
    for seg in segs:
        ws = wb.sheet_by_name(seg)
        num_rows = ws.nrows
        #num_rows = 2
        curr_row = 1
        while curr_row < num_rows:
            for x in range(1,4):
                thisasset = copy.copy(defass)
                thisasset.ASSET_LOCATION = 'MM' + str(fix_MM(ws.cell_value(curr_row, 1)))
                thisasset.ASSET_ASSETNUM = ws.cell_value(curr_row, 0)
                thisasset.ASSET_HIERARCHYPATH = 'ENTASSET \ ME \ LIGHTING \ LIGHTPOLE'
                thisasset.ASSET_FAILURECODE = 'ELECTRICAL'
                thisasset.ASSET_DESCRIPTION = 'Light Pole'
                thisasset.ASSPEC_ASSETATTRID = lpatts[x]
                thisasset.ASSPEC_NUMVALUE = ws.cell_value(curr_row, x + 1)
                thisasset.ASSPEC_ORGID = 'I95'
                thisasset.ASSPEC_LINEARASSETSPECID = 0
                dictlp[attcount] = thisasset
                attcount += 1
            curr_row += 1
    #print dictlp
        
if __name__ == "__main__":
    if not confirm():
        pass
    else:
        get_def_asset()
        bridgecols = get_cols(wsb,0)
        get_bridges()
        signcols = get_cols(wssg, 1)
        #print signcols
        get_signs()
        #print dictsigns
        get_light_poles()
        get_header()
        get_fields()
        #print fieldlist
        write_file()
        #print mh 
        #print md["BR001"].DESCRIPTION, md["BR001"].MM, md["BR001"].LOCATION