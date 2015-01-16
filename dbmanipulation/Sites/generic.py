class asset:
    pass

numlist = ['DESIGNLIFE', 'ISCALIBRATION', 'ISLINEAR', 'ISRUNNING']

def get_def_asset(wss):
    defass = asset()
    wss, numlist
    
    num_cells = wss.ncols

    #print ws.cell_value(0,0)
    defass = asset()
    for x in range(0, num_cells):
        #print ws.cell_value(0,x)
        if wss.cell_value(0,x) in numlist:
            setattr(defass, wss.cell_value(0,x), int(wss.cell_value(1,x)))
        else:
            setattr(defass, wss.cell_value(0,x), wss.cell_value(1,x))
            
    return defass