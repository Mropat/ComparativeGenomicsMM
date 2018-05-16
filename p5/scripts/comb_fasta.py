import os

with open ("p5/dotter_mutual.fasta", "w") as wh:
    for file in os.listdir("p5/only_mutual/dotter/"):
        with open ("p5/only_mutual/dotter/" + file, "r") as fh:
            wh.write(">" + file[:-4]+ "\n" + fh.readline() + "\n")
