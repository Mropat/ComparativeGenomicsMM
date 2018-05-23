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
    
def reverse_complement(genome_file):
    seq = parse(genome_file)
    replaced = seq.replace("G", "c").replace("C", "g").replace("A", "t").replace("T", "a").upper()
    return replaced

def ORF_finder(genome_file):
    forward_strand = parse(genome_file)
    reverse_strand = reverse_complement(genome_file)
    reverse_strand = reverse_strand[::-1]
    fwd_1 = []
    fwd_2 = []
    fwd_3 = []
    rev_1 = []
    rev_2 = []
    rev_3 = []
    for j in range(0,len(forward_strand), 3):
        fwd_1.append(forward_strand[j:j+3])
        fwd_2.append(forward_strand[j+1:j+4])
        fwd_3.append(forward_strand[j+2:j+5])
        rev_1.append(reverse_strand[j:j+3])
        rev_2.append(reverse_strand[j+1:j+4])
        rev_3.append(reverse_strand[j+2:j+5])
        



reverse_complement("/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.dmessina.5/Comparative_Genomics/data/genomes2018/Grp4/04.fa.txt")
ORF_finder("/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.dmessina.5/Comparative_Genomics/data/genomes2018/Grp4/04.fa.txt")
#==============================================================================
# stats("/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.dmessina.5/Comparative_Genomics/data/genomes2018/Grp4/04.fa.txt")
#==============================================================================
