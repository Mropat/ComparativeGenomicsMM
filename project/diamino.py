from collections import Counter


filename = "project/Ref.proteomes/rhodo.fasta"

proteome = []
diaminos = {}
with open(filename , "r") as fh:
    for line in fh:
        if line.startswith(">"):
             continue
        else:
            proteome.append(line.strip())

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

with open("diaminos.txt", "a") as wh:
    wh.write(str(filename) + "\n" + str(diaminos) + "\n")
