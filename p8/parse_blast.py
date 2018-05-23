

chromo_set = set()

with open ("p8/blast/pred34inyeast.txt", "r") as fh:
    for line in fh:
        if "sp|" in line:
            get_line = line.rstrip().split("_YEAST")
            chromo_set.add(get_line[0].split("|")[2])

largest_overlap = list()
with open ("p8/experiments.txt", "r") as fh2:
    maxlen = 0
    for line in fh2:        
        expset = set(line.strip().split(" "))
        if len(chromo_set.intersection(expset)) > maxlen:
            maxlen = len(chromo_set.intersection(expset))
            print(maxlen)
            if len(largest_overlap) < 2:
                largest_overlap.append(list(expset))
            else:
                if len(largest_overlap[1]) > len(largest_overlap[0]):
                    largest_overlap[0] = list(expset)
                else:
                    largest_overlap[1] = list(expset)

with open ("overlapsets.txt", "w") as wh:
    for e in largest_overlap:
        wh.write(" ".join(e) + "\n")

