import collections
import matplotlib.pyplot as plt
import itertools
import numpy as np

def plotting_prep(filename):
    nodes = list()
    cnt = collections.Counter()
    with open(filename, 'r') as f:
        f = f.readlines()
        for line in f:
            line = line.split(' ')
            nodes.append(line[0])
        for i in nodes:
            cnt[i] += 1    
        freq = {key: len(list(value)) for key, value in itertools.groupby(sorted(cnt.values()))}
        for k, v in freq.items():
            plt.scatter(k,v,c='red')
        ax = plt.axes()
        ax.set_xscale("log")
        ax.set_yscale("log")
        plt.xlabel('node degree')
        plt.ylabel('frequency')
        plt.title(filename)
        plt.show()    
plotting_prep('B_japonicum.txt')
plotting_prep('C_trachomatis.txt')
plotting_prep('D_turgidum.txt')
plotting_prep('R_baltica.txt')
plotting_prep('S_cerevisiae.txt')
