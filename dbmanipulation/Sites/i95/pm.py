import xlrd
import csv

from fileFunctions.fileFunc import list_services

pmfld = ['LEADTIME', 'DESCRIPTION', 'FREQUENCY', 'FREQUNIT', 'JPNUM', 'LOCATION', 'NEXTDATE', 
         'PERSONGROUP', 'PMNUM', 'PRIORITY', 'SITEID', 'STATUS', 'WOSTATUS', 'WORKTYPE',
         'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY',
         'INTERVAL', 'JPS_JPNUM', 'JPS_ORGID']
line1 = ['EXTSYS1', 'AMIS_PM', '', 'EN']
wstat = 'WSCH'
st = 'DRAFT'
si = 'I95'
pri = 3
loc = 'i95'
lt = 0
wt = 'PM'
dy = 1
org = 'TUI95'

pmdict = {}
services = {}
    
class pm:
    pass

def fix_pmnum(pm):
    splitty = pm.split('-')
    if len(splitty[2]) == 1:
        return splitty[0] + '-' + splitty[1] + '-' + '0' + splitty[2]
    else:
        return pm
    
def countseq(curr_row):
    global ws
    count = 0
    for x in range(2,11):
        if ws.cell_value(curr_row, x) == 'X':
            count += 1
    return count

def jpseq(curr_row):
    global ws
    if countseq(curr_row) > 1:
        print ws.cell_value(curr_row, 0)

def createPMs():
    global wb, ws
    
    wb = xlrd.open_workbook('insp.xlsx')
    #print wb.sheet_names()
    ws = wb.sheet_by_name('Sheet1')
    
    num_rows = ws.nrows - 1
    num_cells = ws.ncols - 1
    
    curr_row = 4
    while curr_row < num_rows:
        curr_row += 1
        if ws.cell_type(curr_row, 1) == 0:
            pass
        else:
            this_pm = pm()
            pmnum = fix_pmnum(ws.cell_value(curr_row, 0))
            for att in pmfld:
                setattr(this_pm, att, '')
            this_pm.PMNUM = pmnum
            this_pm.FREQUNIT = ws.cell_value(curr_row, 12)
            this_pm.FREQUENCY = int(ws.cell_value(curr_row, 13))
            this_pm.DESCRIPTION = services[ws.cell_value(curr_row, 1)]
            this_pm.LEADTIME = lt
            this_pm.JPNUM = pmnum
            this_pm.LOCATION = loc
            this_pm.WOSTATUS = wstat
            this_pm.STATUS = st
            this_pm.SITEID = si
            this_pm.PRIORITY = pri
            this_pm.MONDAY = dy
            this_pm.TUESDAY = dy
            this_pm.WEDNESDAY = dy
            this_pm.THURSDAY = dy
            this_pm.FRIDAY = dy
            this_pm.SATURDAY = dy
            this_pm.SUNDAY = dy
            jpseq(curr_row)
            #INTERVAL
            #JPS_JPNUM
            this_pm.JPS_ORGID = org
            #print row[0]
            pmdict[this_pm.PMNUM] = this_pm
    #print pmdict
    #     curr_cell = -1
    #     while curr_cell < num_cells:
    #         curr_cell += 1
    #         cell_type = ws.cell_type(curr_row, curr_cell)
    #         cell_value = ws.cell_value(curr_row, curr_cell)
    #         print '    ', cell_type, ':', cell_value
    #         #print cell_type
    
    with open("pm_out.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerow(line1)
        writer.writerow(pmfld)
        for k, v in pmdict.iteritems():
            ol =[]
            for fld in pmfld:
                ol.append(getattr(v, fld))
            writer.writerow(ol)
            
if __name__ == '__main__':
    services = list_services('\\pch\\workspace\\dbmanipulation\\Sites\\i95', 'services.csv')
    #print services
    createPMs()