from Sites.CrossSite.createOutputFiles import loc, levels, get_locs, build_levels, create_level_1, break_files

source_path = '\\pch\\dataload\\raw\\'
dest_path = '\\pch\\dataload\\ready\\'
site = 'LCTNEW'
org = 'CMPL'
#output_file = 'locations'
output_file = 'locations_existing'
#sourcefile = 'lct_location_lvl_1_to_3.csv'
sourcefile = 'lctnew_locations_all.csv'
header = ['EXTSYS1', 'AMIS_LOCATIONS', None,'EN']

firstline = []
fldlist = []
level = 1
dictlocs = {}
dictlevels = {}

if __name__ == '__main__':
    dictlocs, fldlist = get_locs(source_path, sourcefile, site, org)
    dictlevels = create_level_1()
    while 1:
        result, dictlevels, level = build_levels(dictlocs, dictlevels, level)
        #print result
        if result == False:
            break

    #build_levels(dictlocs, dictlevels)
    #print dictlevels
    break_files(header, dest_path, output_file, site, fldlist)