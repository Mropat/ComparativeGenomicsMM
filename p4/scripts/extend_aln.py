from Bio import AlignIO
import os


def extended(files):
    for n in range(4):
        org = ""
        metalist = ""
        for file in os.listdir(files):
            alignment = AlignIO.read(files+"/" + file, "fasta")
            org = alignment[n].id.split("_")[0]
            metalist = metalist + str(alignment[n].seq.strip())
        with open ("10_metagenes.fasta", "a") as wh:
            wh.write(">"+org + "\n" + metalist + "\n")

if __name__ == "__main__":          
        extended("p4/10seq")
