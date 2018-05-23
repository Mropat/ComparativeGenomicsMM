import sys
def compute_gc(genome_file):
    '''Computes GC content in genome file'''    
    with open(genome_file, 'r') as g:
        sequence = []
        lines = g.readlines()
        for line in lines:
            if '>' not in line:
                sequence.extend(line)
        total = (len(sequence))
        gcontent = (sequence.count("G"))
        ccontent = (sequence.count("C"))
        undefined = (sequence.count("N"))
        gccontent = ((gcontent + ccontent)/total)
        print('Total nucleotides =' + ' ' + str(total))
        print('GC-content =' + ' ' + str(gccontent)) 
        print('Undefined nucleotides:' + ' ' + str(undefined))
compute_gc(sys.argv[1])
