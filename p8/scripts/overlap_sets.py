

chromo_set = set()

with open ("p8/blast/34inyiest.txt", "r") as fh:
    for line in fh:
        if "sp|" in line:
            get_line = line.rstrip().split("_YEAST")
            chromo_set.add(get_line[0].split("|")[4])

with open ("p8/overlapsets_genscan.txt", "w") as wh:
    with open ("p8/experiments.txt", "r") as fh2:
        for line in fh2:        
            expset = set(line.strip().split(" "))
            overlen = len(chromo_set.intersection(expset))
            wh.write("----------------" + "\n")
            wh.write("Overlapping genes:" + "\n")
            wh.write(" ".join(chromo_set.intersection(expset)) +"\n")
            wh.write("Length of overlap:"  + str(overlen) + "\n")
            wh.write("Full set:" + "\n")
            wh.write(" ".join(expset) + "\n" + "\n")
