# -*- coding: utf-8 -*-
import xlrd
import copy
import csv

from Sites.generic import get_def_asset

class asset:
    pass

segs = ['SEG01', 'SEG02S', 'SEG02N', 'SEG03S', 'SEG03N', 'SEG04']

wb = xlrd.open_workbook('\\pch\\I95\\Light_Poles.xlsx')
wsd = wb.sheet_by_name('Default')


def get_light_poles(lda):
    global segs, wb
    for seg in segs:
        ws = wb.sheet_by_name(seg)
        num_rows = ws.nrows - 1
    
if __name__ == '__main__':
    da = get_def_asset(wsd)
    get_light_poles(da)