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
    
    g1_dist = []
    g2_dist = []
    g3_dist = []
    g4_dist = []
    g5_dist = []
    for i in range(len(GCfreqs)):
        g1_dist.append(math.sqrt((GCfreqs[0]-GCfreqs[i])**2)*100)
        g2_dist.append(math.sqrt((GCfreqs[1]-GCfreqs[i])**2)*100)
        g3_dist.append(math.sqrt((GCfreqs[2]-GCfreqs[i])**2)*100)
        g4_dist.append(math.sqrt((GCfreqs[3]-GCfreqs[i])**2)*100)
        g5_dist.append(math.sqrt((GCfreqs[4]-GCfreqs[i])**2)*100)

    distance_list = [g1_dist] + [g2_dist] + [g3_dist] + [g4_dist] + [g5_dist]
    m = np.asarray(distance_list)
    print(m)
    
    
if __name__ == "__main__":
    distance_matrix('04.fa.txt', '05.fa.txt', '08.fa.txt', '16.fa.txt', '34.fa.txt')