from Bio.Seq import Seq

def parse(genome_file):    
    with open(genome_file, 'r') as g:
        for line in g:
            if line.startswith(">"):
                continue
            else:
                return Seq(line.strip())


def orfinder(genome_file):
    seq = parse(genome_file)

    scan = ""
    for ind in range (0, len(seq)-3,  3):
        codon = seq[ind] + seq[ind+1] + seq[ind+2]
        if codon == "ATG":
            scan = scan + "*" + codon
        elif codon == any(["TAA", "TAG", "TGA"]):
            scan = scan + codon + "*"
        else:
            scan = scan + codon

    seplist = []
    separate = scan.split("*")
    for chunk in separate:
        if chunk.startswith("ATG") and chunk.endswith(("TAA", "TAG", "TGA")):
            seplist.append(chunk)
    print (seplist)
        
 

if __name__ == "__main__":
    genome_file = "fullgenomes/34.fa"
    orfinder(genome_file)
