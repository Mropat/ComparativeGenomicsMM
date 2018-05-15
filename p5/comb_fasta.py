import os

with open ("p5/vectors/combseqs.fasta", "w") as wh:
    for file in os.listdir("p5/vectors/combined"):
        with open ("p5/vectors/combined/" + file, "r") as fh:
            wh.write(">" + file[:-4]+ "\n" + fh.readline() + "\n")
