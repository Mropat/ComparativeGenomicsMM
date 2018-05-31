
# Optional:
# Run this script on output of ortholog_sets.py or on paired hits output by XML parser (parse_xml.py)
# Creates cluster file with id's for hits present only in all 4 proteomes

def unified_dict (file1, file2, file3):

    unidict = {}

    for file in file1, file2, file3:
        with open (file) as fh:
            for line in fh.readlines():
                pairs = line.strip().split(" ")
                if str(pairs[0]) + "_" + str(pairs[1]) not in unidict:
                    unidict[str(pairs[0]) + "_" + str(pairs[1])] = [str(pairs[2]) + "_" + str(pairs[3])]
                elif str(pairs[0]) + "_" + str(pairs[1]) in unidict:
                    unidict[str(pairs[0]) + "_" + str(pairs[1])].append(str(pairs[2]) + "_" + str(pairs[3]))


    with open ("concat_instersect_nonmutual_all.txt", "w") as wh:
        for key, val in unidict.items():
#                if len(val) == 3:
                wh.write(key + " " +" ".join(val) + "\n")



if __name__ == "__main__":
    unified_dict("p4/parsed_blasts/parsed05.txt", "p4/parsed_blasts/parsed08.txt", "p4/parsed_blasts/parsed16.txt")