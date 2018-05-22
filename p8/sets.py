

chromo_set = set()

with open ("chr14.fasta", "r") as fh:
    for line in fh:
        if line.startswith(">sp|"):
            get_line = line.strip().split("_")
            chromo_set.add(get_line[0].split("|")[2])

largest_overlap = list()
with open ("experiments.txt", "r") as fh2:
    maxlen = 0
    for line in fh2:
        expset = set(line.strip().split(" "))
        if len(chromo_set.intersection(expset)) > maxlen:
            maxlen = len(chromo_set.intersection(expset))
            if len(largest_overlap) < 2:
                largest_overlap.append(list(expset))
            else:
                if len(largest_overlap[1]) > len(largest_overlap[0]):
                    largest_overlap[0] = list(expset)
                else:
                    largest_overlap[1] = list(expset)

with open ("overlapsets_STRING.txt", "w") as wh:
    for e in largest_overlap:
        wh.write("\n".join(e) + "\n"+ "\n")
