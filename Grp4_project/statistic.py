from collections import Counter
from Bio.Seq import Seq

#Calculates general nucleotide statistics on a genome

def parse(genome_file):
    with open(genome_file, 'r') as g:
        for line in g:
            if line.startswith(">"):
                continue
            else:
                return Seq(line.strip())


def stats(genome_file):

    seq = parse(genome_file)
    nucleotide_stat = Counter(seq)
    genome_length = len(seq)

    gc_fraction = (nucleotide_stat["G"] + nucleotide_stat["C"]
                   ) / (genome_length - nucleotide_stat["N"])
    amb_fraction = nucleotide_stat["N"] / genome_length

    dinuc_dict = {}
    dinuc_list = ["AT", "AG", "AC", "CT", "CG", "CA", "TA",
                  "TC", "TG", "GA", "GC", "GT", "AA", "TT", "CC", "GG"]

    for i in dinuc_list:
        dinuc_dict[i] = 0

    for ind in range(genome_length-1):
        dinucleotide = seq[ind] + seq[ind+1]
        if dinucleotide in dinuc_dict:
            dinuc_dict[dinucleotide] += 1

    for key in dinuc_dict:
        dinuc_dict[key] = dinuc_dict[key]/ (genome_length-1)

    print(dinuc_dict)
    print(gc_fraction)
	print(nucleotide_stat)


if __name__ == "__main__":
    genome_file = "fullgenomes/34.fa"
    stats(genome_file)
