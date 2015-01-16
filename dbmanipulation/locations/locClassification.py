import csv

classdict = {'civil drainage':6909, 'civil roadside':6927, 'civil structure':6930, 'ettm cabinet':6910, 'ettm control':6908, \
             'ettm datacomm':6911, 'ettm instrument':6919, 'ettm security':7100, 'ettm signage':6929, 'ettm surveil':6931, \
             'ettm tolling':6932, 'ettm voicecom':6935, 'landscape gardens':6913, 'landscape graffiti':6915, 'landscape hardsurf':6916, \
             'me airqual':6914, 'me equipment':7108, 'me firesys':6912, 'me highvolt':6917, 'me hvac':6918, 'me lighting':6920, \
             'me lowvolt':6921, 'me plant':6924, 'me power':6925, 'me pumping':6926, 'me security':6936, 'me ups':6933, 'me vent':6934, \
             'pavement marking':6922, 'pavement other':6923, 'pavement roadway':6928, 'ettm surveil aid':7074, 'civil structure bridges':6951, 
             'civil structure retain':6985, 'civil structure building':6949, 'me firesys deluge':6957, 'me lighting des':6961, \
             'ettm signage lus':7114, 'civil structure tunn':7115, 'ettm surveil cctv':6952, 'civil roadside displan':7116, \
             'ettm voicecom firepho':6964, 'civil groundwater':7117, 'ettm voicecom mets':6975, 'civil roadside gates':7113, \
             'landscape':6728, 'ettm signage alus':7075, 'me vent damper':6958, 'civil roadside fencing':7118, 'civil drainage pldb':6980, \
             'civil roadside sign':6991}

with open("\\pch\\SQL files\\location classification rules.sql", "rb") as f:
    reader = csv.reader(f)
    sqlcount = 0
    templist = []
    sqllist = {}
    for row in reader:
        #print row
        if len(row) > 0:
            if row[0][0:2] == "--":
                pass
                #print row[0]
            else:
                templist.append(row[0])
        else:
            sqllist[sqlcount] = templist
            templist = []
            sqlcount += 1
        
for k, v in sqllist.iteritems():
    outstring = ""

    if len(v) > 0:
        #print v
        try:
            if v[3][0:3] == "and":
                
                myid = classdict[v[4]]
                outstring = "update locations set classstructureid = '" + str(myid) + "' " + v[1] + " " + v[2] + " and siteid = 'CML';"
                print outstring
            else:
                myid = classdict[v[3]]
                outstring = "update locations set classstructureid = '" + str(myid) + "' " + v[1] + " and siteid = 'CML';"
                print outstring
                
        except KeyError, IndexError:
            print v
            stop
#print sqllist