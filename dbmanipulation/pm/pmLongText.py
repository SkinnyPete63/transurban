import csv
import sys
#print type(sys.maxsize)
csv.field_size_limit(int(sys.maxint))

class pm:
    linecount = 0
    
    def __init__(self, mpno = "", mptext = "", mitem = "", itext = "", tltype = "", tlgroup = "", grpcount = "", lt={}):
        self.mpno = mpno
        self.mptext = mptext
        self.mitem = mitem
        self.itext = itext
        self.tltype = tltype
        self.tlgroup = tlgroup
        self.grpcount = grpcount
        self.lt = lt
        

def test():
    mystr = "000030013764"
    print mystr[:1]
#     mypm = pm()
#     listlen = len(mypm.lt)
#     mypm.lt[listlen + 1] = "stuff"
#     listlen = len(mypm.lt)
#     mypm.lt[listlen + 1] = "morestuff"
#     
#     #print mypm.lt
#         
def read_pms():
    pmdict = {}
    mypm = pm()
    with open("pmlong_full.txt", "rb") as f:
        #dialect = csv.Sniffer().sniff(f.read(1024))
        #f.seek(0)
        reader = csv.reader(f, csv.excel_tab)
        rowcount = 0
        templt = {}
        for row in reader:
            #print len(row)
            if row[0][:1] <> " ":
                pmdict[mypm.tlgroup] = mypm
                mypm.lt = templt
                templt = {}
                #print "*" + row[0][:1] + "*"
                mypm = pm(mpno = row[0], mptext = row[1], mitem = row[2], tlgroup = row[5])
                #print "found one"
            else:
                listlen = len(templt)
                #print len(row)
                #print row
                templt[listlen + 1] = row[7]
            rowcount += 1
            
        pmdict[mypm.tlgroup] = mypm
        mypm.lt = templt
        #print mypm.lt
        #print mypm.tlgroup
        return pmdict

def output_pms(inDict):
    mystr = ""
    with open("pmoutput.csv", "wb") as f:
        writer = csv.writer(f) 
        for k,v in inDict.iteritems():
            mystr = ""
            if k <> '':
                print v.lt
                for x in range(1,len(v.lt)):
                    mystr = mystr + v.lt[x] + "\n"
                templist = [k, mystr]
                writer.writerow(templist)
        
if __name__ == "__main__":
    pmlist = read_pms()
    output_pms(pmlist)