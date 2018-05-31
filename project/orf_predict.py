from Bio.Seq import Seq
import math
from collections import Counter

#Parse genome to get the sequence
def parse(genome_file):    
    with open(genome_file, 'r') as g:
        for line in g:
            if line.startswith(">"):
                continue
            else:
                return line.strip()

#Calculates general statistics for the nucleotide content of the genome. 
#Statistics can be output by adding print statements
#Output later reused by shannon entropy script to refine ORFs

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

#Finds all potential ORFs in all reading frames, that terminate in stop codon
#Efficiency of the script could be improved x3 if forward and reverse strands were processed simultaneously

def orfinder(genome_file):
    seq = parse(genome_file)
    revseq = str(Seq(seq).reverse_complement())
    genome_length = len(seq)

#Estimates the randomness of the global genomic dinucleotide content
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
    

#Concatenates the frames after retrieval

    seplist = []
    segment = ""
    for frame in scan:
        if frame == "*":
            seplist.append(segment)
            segment = ""
        segment = segment + frame

#Refinement script:
#Chooses the potential orfs starting with ATG
#Selects the fraction of ORFs which have more unexpected
#distribution of dinucleotides in relationship to whole genome

    orflist = []
    for chunk in seplist:
        fraglist = []
        entlist = []
        for ind in range(1, len(chunk)-2, 3):
            if chunk[ind] + chunk[ind+1] + chunk[ind+2] == "ATG":
                frag = chunk[ind:]
                if len(frag) > 75*3 and len(frag)%3 == 0:
                    fraglist.append(frag)

        if len(fraglist) > 0:            
            for gene in fraglist:
                ent = shannon(gene)
                entlist.append(abs(ent))
        else:
            continue

        entmax = entlist.index(max(entlist))
        if entlist[entmax] < glob_entropy + 0.135 and entlist[entmax] > glob_entropy:
            orflist.append(fraglist[entmax])

#Higher threshold of 0.135 somehat arbitrary but shows best performace
#Extremely low entropy fragments are usually repeated elements, centromeres, and rarely code for protein
#Extremely high entropy fragments are predicted Alanine/Leucine-rich sequences, also unlikely to code for protein
#70-77% ORFs in reference proteomes are found within 1 std dev above average

#Prints the ORFs to a file
    with open ("predicted_16_ent.txt", "w") as wh:

        orflen = len(orflist)
        for g in range(orflen):
            wh.write(">ORF_" + str(g) + "\n")
            wh.write(str(Seq(orflist[g]).translate()) + "\n")
    print("ORFs found:")        
    print(len(orflist))     


#Script for calculating entropy of sequences based on dinucleotide statistic
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
    genome_file = "fullgenomes/16.fa"
    global_probs = stats(genome_file)
    orfinder(genome_file)