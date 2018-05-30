# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:36:17 2018

@author: u2353
"""
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis


def parse(genome_file):
    
    with open(genome_file, 'r') as g:
        seq = ""
        for line in g:
            if '>' not in line:
                seq += line
    return seq
    
def DNA_stats(genome_file):
    seq = parse(genome_file)
    gcontent = (seq.count("G"))
    ccontent = (seq.count("C"))
    undefined = (seq.count("N"))
    total = len(seq)
    gccontent = ((gcontent + ccontent)/(total-undefined))
    listofDI = ["AG", "AA", "AC", "AT","CG", "CA", "CC", "CT","GG", "GA", "GC", 
    "GT", "TG", "TA", "TC","TT"]       
    print('Total nucleotides(excluding undefined) =' + ' ' + str(total-undefined))
    print('Undefined nucleotides:' + ' ' + str(undefined))        
    print('GC-content =' + ' ' + str(gccontent))
    print('Dinucleotide contents:')
    for di in listofDI:        
        #print("{} content = {}".format(di, seq.count(di)/(total-1-2* undefined)))    
        print(seq.count(di)/(total- 2*undefined-1))

def protein_stats(proteome_file):
    seq = ""    
    for record in SeqIO.parse(proteome_file, "fasta"):
        sequences = record.seq 
        seq = seq+str(sequences)
    s = ProteinAnalysis(str(seq))
    dic = s.get_amino_acids_percent()

    for k, v in sorted(dic.items()):
        print(k, dic[k])

def di_aa(proteome_file):
    
    
if __name__ == "__main__":    
    
    protein_stats("04_prot.fasta")
    protein_stats("05_prot.fasta")
    protein_stats("08_prot.fasta")
    protein_stats("16_prot.fasta")
    protein_stats("34_prot.fasta")