# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:56 2018

@author: u2353
"""
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def translate_fasta(fastafile, outfile):
    with open(outfile, "w") as O:
        for record in SeqIO.parse(fastafile, "fasta"):
            sequences = record.seq
            aa_seqs = sequences.translate()
            aa_record = SeqRecord(aa_seqs, id=record.id, description="")        
            SeqIO.write(aa_record, O, "fasta")
            
if __name__ == "__main__":
    translate_fasta('04.fasta', '04_prot.fasta')
    translate_fasta('05.fasta', '05_prot.fasta')
    translate_fasta('08.fasta', '08_prot.fasta')
    translate_fasta('16.fasta', '16_prot.fasta')
    translate_fasta('34.fasta', '34_prot.fasta')