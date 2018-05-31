# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:38:29 2018

@author: u2353
"""
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import matplotlib.pyplot as plt
import numpy as np

seq = ""
seqs = []
lengths = []        
for record in SeqIO.parse('../data/yeast_pred.fasta', "fasta"):
    sequences = record.seq
    #print(record)
    #seq = seq+str(sequences)
    seqs.append(str(sequences))
print(seqs[0])
for i in seqs:
    lengths.append(len(i))
    

x = np.asarray(lengths)
print(x)
plt.hist(x, bins=20)
plt.xlabel('Protein length (#AA)')
plt.ylabel('Frequency')
plt.show()
#print(seqs)