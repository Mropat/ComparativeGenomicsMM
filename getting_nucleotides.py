def parsing_output(inputfile):
    '''takes nucleotides from peptide nucleotide file'''
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
parsing_output('proteins_nucleotides34.txt')
