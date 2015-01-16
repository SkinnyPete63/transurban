import chardet    

inpath = "\\pch\\workspace\\dbmanipulation\\Sites\\i95"
infile = "Assets.xlsm"
rawdata=open(inpath + "\\" + infile,"r").read()
print chardet.detect(rawdata)
