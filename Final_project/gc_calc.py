def parse(genome_file):
    
    with open(genome_file, 'r') as g:
        seq = ""
        for line in g:
            if '>' not in line:
                seq += line
    return seq
    
def stats(genome_file):
    seq = parse(genome_file)
    gcontent = (seq.count("G"))
    ccontent = (seq.count("C"))
    undefined = (seq.count("N"))
    total = (len(seq)-undefined)
    gccontent = ((gcontent + ccontent)/total)
    listofDI = ["AG", "AA", "AC", "AT","CG", "CA", "CC", "CT","GG", "GA", "GC", 
    "GT", "TG", "TA", "TC", "TT" ]       
    for di in listofDI:        
        print("{} content = {}".format(di, seq.count(di)/(total-1)))    
    print('Total nucleotides(excluding undefined) =' + ' ' + str(total))
    print('Undefined nucleotides:' + ' ' + str(undefined))        
    print('GC-content =' + ' ' + str(gccontent)) 
        
stats("/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.dmessina.5/Comparative_Genomics/data/genomes2018/Grp4/04.fa.txt")