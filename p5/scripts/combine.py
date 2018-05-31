import pickle

indict = pickle.load(open("p5/ndict.sav", "rb"))

with open ("p5/only_mutual/16_order.txt", "r") as fh:
    for line in fh.readlines():
        line_nr = line.strip()

        with open ("p5/only_mutual/16orderseq.txt", "a") as wh:
            wh.write(indict[int(line_nr)])