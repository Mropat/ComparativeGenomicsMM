import pickle 

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

    pickle.dump(dict_05, open("pickle16rev.sav", "wb"))

if __name__ == "__main__":
    parse("p4/blast_out/ref16rev.xml")
