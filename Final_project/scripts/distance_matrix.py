# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:11:06 2018

@author: u2353
"""
import numpy as np
import math

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
    GCcontent = ((gcontent + ccontent)/total)
    return GCcontent

 

def distance_matrix(g1, g2, g3, g4, g5):
    m = np.zeros((5,5))
    GCfreqs = [stats(g1), stats(g2), stats(g3), stats(g4), stats(g5)]
    distance_list = []
    temp_list = []
    print(GCfreqs)
    for i in range(len(GCfreqs)):

        temp_list.append(abs(GCfreqs[i]- (GCfreqs[i+1])))
        if i == 3:
            break
    print(temp_list)


if __name__ == "__main__":
    distance_matrix('04.fa.txt', '05.fa.txt', '08.fa.txt', '16.fa.txt', '34.fa.txt')