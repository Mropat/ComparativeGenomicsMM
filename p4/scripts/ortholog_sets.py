

def ortholog_pairs(file, filerev):
    
    set_for = set()
    set_rev = set()

    with open (file, "r") as fh_fw:
        for line in fh_fw.readlines():
            pairs_for = line.strip().split(" ")
            set_for.add(str(pairs_for[0]+"_"+pairs_for[1]+" "+pairs_for[2]+"_"+pairs_for[3]))
                
    with open (filerev, "r") as fh_rv:
        for line in fh_rv.readlines():
            pairs_rev = line.strip().split(" ")
            set_rev.add(str(pairs_rev[2]+"_"+pairs_rev[3]+" "+pairs_rev[0]+"_"+pairs_rev[1]))

    with open ("intersect16.txt", "w") as wh:
        interlist = list(set_for.intersection(set_rev))
        for pair in interlist:
            wh.write(pair + "\n")


if __name__ == "__main__":
    ortholog_pairs("p4/parsed_blasts/parsed16.txt", "p4/parsed_blasts/parsed16rev.txt")