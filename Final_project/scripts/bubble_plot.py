# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:06:53 2018

@author: u2353
"""

import matplotlib.pyplot as plt
filename = "04_prot.fasta"

proteome = []
diaminos = {}
with open(filename , "r") as fh:
    for line in fh:
        if line.startswith(">"):
             continue
        else:
            proteome.append(line.strip()[:-1])

dia_counter = 0

for seq in proteome:
    dia_count = len(seq)-1
    dia_counter += dia_count

    for aac in range(dia_count):
        diamino = seq[aac] + seq[aac+1]
        if diamino in diaminos:
            diaminos[diamino] += 1
        else:
            diaminos[diamino] = 1


for key in diaminos:
    diaminos[key] = diaminos[key]/dia_counter
print(diaminos)


AA_x_axis = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
AA_y_axis = AA_x_axis[::-1]
#plt.scatter(AA_x_axis, AA_y_axis)
#plt.show()
keys = []
value =[]    
for k, v in sorted(diaminos.items()):
    keys.append(k)
    value.append(v)
x = []
y = []
print(keys)
for i in keys:
    x.append(i[0])
    x.append(i[1])
plt.scatter(x, y)
    
