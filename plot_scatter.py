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
            plt.scatter(np.log(k),np.log(v))
        plt.show()    
plotting_prep('B_japonicum.txt')
