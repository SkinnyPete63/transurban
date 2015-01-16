import csv
dictservs = {}
def list_services(path, fname):
    with open(path + '\\' + fname, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            #print row
            dictservs[row[0]] = row[1]
        
    return dictservs

if __name__ == '__main__':
    pass
    #mydict = list_services('\\pch\\workspace\\i95', 'services.csv')
    #print mydict