# -*- coding: utf-8 -*-
import chardet 

#with open("\\pch", "rb")as f:
#    pass

inpath = "\\pch"
infile = "oddchar.txt"
#rawdata=open(inpath + "\\" + infile,"r").read()
#print chardet.detect(rawdata)

with open(inpath + "\\" + infile, "rb") as f:
    for line in f:
        #myline = line.decode('windows-1252').replace(u'\xef', '').replace(u'\xbf', '').replace(u'\xbd', '')
        myline = line.decode('windows-1252').replace(u'\xef\xbf\xbd', ' ')
        #myline = line.replace(u'\xef', ' ')
        #myline = myline.encode('unicode')
        print myline