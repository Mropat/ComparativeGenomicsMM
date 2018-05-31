from Bio.Seq import Seq
import math
from collections import Counter
import matplotlib.pyplot as plt

def parse(genome_file):    
    with open(genome_file, 'r') as g:
        for line in g:
            if line.startswith(">"):
                continue
            else:
                return line.strip()

def stats(genome_file):
    
    seq = Seq(parse(genome_file))
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

    return dinuc_dict



def orfinder(genome_file):
    seq = parse(genome_file)
    revseq = str(Seq(seq).reverse_complement())
    genome_length = len(seq)
    glob_entropy = shannon(seq)
    print(glob_entropy)

    scan = []
    for ind in range (0, genome_length-2,  3):
        codon = seq[ind] + seq[ind+1] + seq[ind+2]
        if codon in (["TAA", "TAG", "TGA"]):
            scan.append("*")
        else:
            scan.append(codon)
    scan.append("*")

    for ind in range (1, genome_length-2,  3):
        codon = seq[ind] + seq[ind+1] + seq[ind+2]
        if codon in (["TAA", "TAG", "TGA"]):
            scan.append("*")
        else:
            scan.append(codon)
    scan.append("*")

    for ind in range (2, genome_length-2,  3):
        codon = seq[ind] + seq[ind+1] + seq[ind+2]
        if codon in (["TAA", "TAG", "TGA"]):
            scan.append("*")
        else:
            scan.append(codon)
    scan.append("*")

    for ind in range (0, genome_length-2,  3):
        codon = revseq[ind] + revseq[ind+1] + revseq[ind+2]
        if codon in (["TAA", "TAG", "TGA"]):
            scan.append("*")
        else:
            scan.append(codon)
    scan.append("*")

    for ind in range (1, genome_length-2,  3):
        codon = revseq[ind] + revseq[ind+1] + revseq[ind+2]
        if codon in (["TAA", "TAG", "TGA"]):
            scan.append("*")
        else:
            scan.append(codon)
    scan.append("*")

    for ind in range (2, genome_length-2,  3):
        codon = revseq[ind] + revseq[ind+1] + revseq[ind+2]
        if codon in (["TAA", "TAG", "TGA"]):
            scan.append("*")
        else:
            scan.append(codon)
    scan.append("*")
    
    seplist = []
    segment = ""
    for frame in scan:
        if frame == "*":
            seplist.append(segment)
            segment = ""
        segment = segment + frame

    orflist = []
    for chunk in seplist:
        fraglist = []
        entlist = []
        for ind in range(1, len(chunk)-2, 3):
            if chunk[ind] + chunk[ind+1] + chunk[ind+2] == "ATG":
                frag = chunk[ind:]
                if len(frag) > 75*3 and len(frag) < 800*3 and len(frag)%3 == 0:
                    fraglist.append(frag)

        if len(fraglist) > 0:            
            for gene in fraglist:
                ent = shannon(gene)
                entlist.append(abs(ent))
        else:
            continue

        entmax = entlist.index(max(entlist))
        if entlist[entmax] < 4.05 and entlist[entmax] > glob_entropy:
            orflist.append(fraglist[entmax])

    print (len(orflist))


    with open ("predicted_08.txt", "w") as wh:

        orflen = len(orflist)
        for g in range(orflen):
            wh.write(">ORF_" + str(g) + "\n")
            wh.write(str(Seq(orflist[g]).translate()) + "\n")
    print(orflist[0])       



def shannon(gene):
       
    local_dict = {}
    dinuc_list = ["AT", "AG", "AC", "CT", "CG", "CA", "TA",
                        "TC", "TG", "GA", "GC", "GT", "AA", "TT", "CC", "GG"]
    for i in dinuc_list:
        local_dict[i] = 0

    for ind in range(len(gene)-1):
        dinucleotide = gene[ind] + gene[ind+1]
        if dinucleotide in local_dict:
            local_dict[dinucleotide] += 1

    for key in local_dict:
        local_dict[key] = local_dict[key]/ (len(gene)-1)

    entropy = -sum((local_dict[key] * math.log2(global_probs[key])) for key in local_dict)

    return entropy

      
 

if __name__ == "__main__":
    genome_file = "fullgenomes/08.fa"
    global_probs = stats(genome_file)
    orfinder(genome_file)