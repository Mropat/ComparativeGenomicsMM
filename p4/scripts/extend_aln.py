from Bio import AlignIO
import os

# Creates a meta alignment sequence from all files found in specified folder

def meta_alignment(my_dir):
    for n in range(4):
        org = ""
        metalist = ""
        for file in os.listdir(my_dir):
            alignment = AlignIO.read(my_dir+"/" + file, "fasta")
            org = alignment[n].id.split("_")[0]
            metalist = metalist + str(alignment[n].seq.strip())
        with open ("10_metagenes.fasta", "a") as wh:
            wh.write(">"+org + "\n" + metalist + "\n")

if __name__ == "__main__":          
        meta_alignment("p4/10seq")
