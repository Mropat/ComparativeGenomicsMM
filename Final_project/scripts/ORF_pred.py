def parse(genome_file):
    
    with open(genome_file, 'r') as g:
        seq = ""
        for line in g:
            if '>' not in line:
                seq += line
    return seq
     
    
def reverse_complement(genome_file):
    seq = parse(genome_file)
    replaced = seq.replace("G", "c").replace("C", "g").replace("A", "t").replace("T", "a").upper()
    return replaced

def frame_finder(genome_file):
    forward_strand = parse(genome_file)
    reverse_strand = reverse_complement(genome_file)
    reverse_strand = reverse_strand[::-1]
    fwd_1 = []
    fwd_2 = []
    fwd_3 = []
    rev_1 = []
    rev_2 = []
    rev_3 = []
    for j in range(0,len(forward_strand), 3):
        fwd_1.append(forward_strand[j:j+3])
        fwd_2.append(forward_strand[j+1:j+4])
        fwd_3.append(forward_strand[j+2:j+5])
        rev_1.append(reverse_strand[j:j+3])
        rev_2.append(reverse_strand[j+1:j+4])
        rev_3.append(reverse_strand[j+2:j+5])
    forward_frames = []
    forward_frames.append(fwd_1)
    forward_frames.append(fwd_2)
    forward_frames.append(fwd_3)
    reverse_frames = []
    reverse_frames.append(rev_1)
    reverse_frames.append(rev_2)
    reverse_frames.append(rev_3)
    #print(len(forward_frames))
   # print(len(reverse_frames))
    return forward_frames, reverse_frames

def ORFs(genome_file):
    forward = frame_finder(genome_file)[0]
    reverse = frame_finder(genome_file)[1]
    forward_ORFs = []    
    for frame in forward:
        #print(frame)
        for codon in range(len(frame)):
            #print(codon)            
            if frame[codon] == "ATG":
                
                ORF = []
                for j in range(codon, len(frame)):
                    ORF.extend(frame[j])
                    if frame[j] == "TAG" or frame[j] == "TAA" or frame[j] == "TGA":
                        break
                forward_ORFs.append(ORF)
    print(len(forward_ORFs))


if __name__ == "__main__":
    ORFs("/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.dmessina.5/Comparative_Genomics/data/genomes2018/Grp4/04.fa.txt")    
   
