# -*- coding: utf-8 -*-
import xlrd
orgs = ['TUCML', 'AML', 'TUI95', 'CMPL', 'TUM2']
fc = {}
fl = {}
#print fc['TRIPPED']
curr_row = 0

strfc = "insert into failurecode(failurecode, description, orgid, failurecodeid, langcode, hasld) values('%s', '%s', '%s', %s, 'EN', 0);\n"
strfl = "insert into failurelist(failurelist, failurecode, parent, type, orgid) values (%s, '%s', %s, '%s', '%s');\n"
delfc = "delete from failurecode where orgid = '%s';\n"
delfl = "delete from failurelist where orgid = '%s';\n"
iters = 0

outpath = '\\pch\\dataload\\sql_scripts\\'

fcnum = 1000
flnum = 1000

wb = xlrd.open_workbook('Failure Codes New Hierarchy.xlsx')
wsfl = wb.sheet_by_name('Failurelist')
wsfc = wb.sheet_by_name('Failurecode')

for x in range (0,49):
    fc[int(wsfc.cell_value(x, 0))] = [wsfc.cell_value(x, 1), wsfc.cell_value(x, 2)]
    
#print fc[1048]

for x in range (2,99):
    try:
        fl[int(wsfl.cell_value(x, 1))] = [wsfl.cell_value(x, 2), int(wsfl.cell_value(x, 5)), wsfl.cell_value(x, 6)]
    except ValueError:
        fl[int(wsfl.cell_value(x, 1))] = [wsfl.cell_value(x, 2), None, None]

with open(outpath + "fcupdate.txt", "wb") as f:
    for o in orgs:
        f.write(delfc % (o))
        f.write('')
        f.write(delfl % (o))
        f.write('') 
        for k,v in sorted(fc.iteritems()):
            #print fl[1019]
            try:
                #pass
                f.write(strfc % (fc[k][0], fc[k][1], o, fcnum ))
            except (TypeError, UnicodeEncodeError):
                print 'Oops'
                print fc[k]
            fcnum += 1
        print 
        print
        for k,v in sorted(fl.iteritems()):
            try:
                f.write(strfl % (k + (iters * 1000), v[0], v[1] + (iters * 1000), v[2], o))
            except TypeError:
                f.write((strfl % (k + (iters * 1000), v[0], 'null', 'null',o)).replace("'null'", "null"))
        
        iters += 1
            