import pickle

# Script that parses XML output and saves a dict with orf ids:
# This is not a Biopython parser and is a very specific to the exact input and output formats we used in this lab
# Query id is saved as key and hit id is saved as value.
# We also save a list of id pairs with organism identifier all parsed from XML output

def parse(file):
    with open("p4/parsed_blasts/parsed16rev.txt", "w") as wh:
        dict_05 = {}
        with open(file, "r") as fh:
            line_list = fh.readlines()
            for i, line in enumerate(line_list):
                if "<Iteration_query-def>" in line:
                    query = line.strip()
                    if "<Hit>" in line_list[i+3]:
                        match = line_list[i+6].strip()
                        dict_05[query[33:-22]] = match[21:-10]
                        wh.write(query[23:25] + " " + query[33:-22] +
                                 " " + match[11:13]+" " + match[21:-10] + "\n")
                        # We save a list of id pairs with organism identifier

    pickle.dump(dict_05, open("pickle16rev.sav", "wb"))
# Dicts are used as input in concatenate.py to create clusters (only when not generating mutual top hit lists)


if __name__ == "__main__":
    parse("p4/blast_out/ref16rev.xml")
