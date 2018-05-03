def getridofheader(file):
    file = open(file)
    read_lines = file.readlines()
    ofile = open('peptides34.txt','w')
    for lines in read_lines[1252:]:
        print(lines)
        ofile.write(lines)
getridofheader('proteins34.txt')
