import csv

content = []
plans = {}
class plan:
    pass

def get_rows():
    global content
    with open('\\pch\\CML\\PM_long.txt', 'rb') as f:
        content = [x.split('\t') for x in f.readlines()] 
        
def make_plan():
    global content
         

def fixlist(mylist):
    for item, val in enumerate(mylist):
        mylist[item] = val.lstrip(',').strip(' ').replace('\r', '').replace('\n', '')
    return mylist
    
def makeld():
    global plans
    plannum = 1
    thisplan = plan()
    for item, val in enumerate(content):
        if val[0] is None or val[0] == '':
            if val[7] == '':
                pass
            else:
                thisplan.LD.append(val[7])
        else:
            plans[plannum] = thisplan
            plannum += 1
            thisplan = plan()
            thisplan.PLANNO = val[0]
            thisplan.TASKLIST = val[5]
            thisplan.VER = val[6]
            thisplan.LD = [val[7]]
    plans[plannum] = thisplan
            #print val[0]
        #for it, text in enumerate(val):
            #pass

def makeoutput():
    with open('\\pch\\CML\\ld.csv', 'wb') as f:
        writer = csv.writer(f)
        outstr = []
        for k,v in plans.iteritems():
            if k==1:
                pass
            else:
                outstr=[v.PLANNO, v.TASKLIST, v.VER]
                outstr.append('\n'.join(v.LD))
                writer.writerow(outstr)
                #outstr.extend('\n'.join(v.LD))
            #print outstr
if __name__ == '__main__':
    get_rows()
    for item, val in enumerate(content):
        content[item] = fixlist(val)
    #print content
    makeld()
    #print plans[2].LD
    makeoutput()