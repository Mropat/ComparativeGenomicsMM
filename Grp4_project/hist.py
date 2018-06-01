# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:38:29 2018

@author: u2353
"""
from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np


def making_array(file):
    seqs = []
    lengths = []        
    for record in SeqIO.parse(file, "fasta"):
        sequences = record.seq
        #print(record)
        #seq = seq+str(sequences)
        seqs.append(str(sequences))
    #print(seqs[0])
    for i in seqs:
        lengths.append(len(i))
        
    
    x = np.asarray(lengths)
    return x

def plotting(f1, f2, f3, f4, f5):
    l = [making_array(f1),  making_array(f2), making_array(f3), making_array(f4), making_array(f5)]
    #print(l)    
    #x = np.stack(l)  
    colors = ['red', 'purple', 'lime', 'blue', 'pink']
    species = ['B. japonicum', 'C. trachomatis', 'D. turgidum', 'R. baltica', 'S. cervisiae']

    plt.hist(l, bins=20, histtype='step', color=colors, label=species, linewidth=1.5)
    plt.legend(prop={'size': 10})
    plt.xlabel('Protein length (#AA)')
    plt.ylabel('Frequency')
    plt.show()
    #print(seqs)
    
plotting('../data/predicted_04_ent.txt', '../data/predicted_05_ent.txt', '../data/predicted_08_ent.txt', '../data/predicted_16_ent.txt', '../data/yeast_pred.fasta')
