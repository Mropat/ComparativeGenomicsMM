
def unified_dict (file1, file2, file3):

    unidict = {}

    for file in file1, file2, file3:
        with open (file) as fh:
            for line in fh.readlines():
                pairs = line.strip().split(" ")
                if pairs[0] not in unidict:
                    unidict[pairs[0]] = [pairs[1]]
                elif pairs[0] in unidict:
                    unidict[pairs[0]].append(pairs[1])


    with open ("concat_instersect.txt", "w") as wh:
        for key, val in unidict.items():
                if len(val) == 3:
                    wh.write(key + " " +" ".join(val) + "\n")



if __name__ == "__main__":
    unified_dict("intersect5.txt", "intersect8.txt", "intersect16.txt")