def parsing_output(inputfile):
    '''takes nucleotides from peptide and nucleotide file'''
    combined = open(inputfile)
    read_lines = combined.readlines()
    nucleotides = ['a','t','c','g']
    outputfile = open('nucleotides34.txt', 'w')
    for line in read_lines:
        if line.endswith('bp\n'):
                outputfile.write(line)
        for x in nucleotides: 
            if line.startswith(x):
                outputfile.write(line)
    outputfile.close()   


def getridofheader(file):
    '''gets only peptide sequences from genscan output'''
    file = open(file)
    read_lines = file.readlines()
    ofile = open('peptides34.txt','w')
    for lines in read_lines[1252:]:
        print(lines)
        ofile.write(lines)
    ofile.close()

if __name__ == '__main__':
parsing_output('proteins_nucleotides34.txt')
getridofheader('proteins34.txt')
