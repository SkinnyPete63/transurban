import csv

with open("pmlong_full.txt", "rb") as f:
    reader = csv.reader(f, csv.excel_tab)
    with open("pmlong_full_fixed.txt", "wb") as fo:
        writer = csv.writer(fo)
        for row in reader:
            #print "*" + row[0][:1] + "*"
            if row[0][:1] <> " ":
                #print row[0]
                planno = row[0]
            outstr = [planno, row[1]]
            writer.writerow(outstr)