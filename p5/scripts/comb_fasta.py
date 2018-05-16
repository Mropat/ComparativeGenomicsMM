import os

with open ("p5/combseqs.fasta", "w") as wh:
    for file in os.listdir("p5/all_orf/dotter/"):
        with open ("p5/all_orf/dotter/" + file, "r") as fh:
            wh.write(">" + file[:-4]+ "\n" + fh.readline() + "\n")
