

chromo_set = set()

with open ("blast/34inyiest.txt", "r") as fh:
    for line in fh:
        if "sp|" in line:
            get_line = line.rstrip().split("|")
            chromo_set.add(get_line[4].split("_YEAST")[0])


with open ("experiments.txt", "r") as fh2:
    for line in fh2:
        expset = set(line.strip().split(" "))
        print(chromo_set.intersection(expset))
