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
    seq_rev = seq.reverse_complement()
    translated = str(seq.translate()).split("*") + str(seq[1:].translate()).split("*") + str(seq[2:].translate()).split("*") + str(
        seq_rev.translate()).split("*") + str(seq_rev[1:].translate()).split("*") + str(seq_rev[2:].translate()).split("*")

    translated_long = []

    for frag in translated:
        for ind, char in enumerate(frag):
            if char == "M":
                frag_pla = frag[ind:]
                if len(frag_pla) > 40 and len(frag_pla) < 3000:
                    translated_long.append(frag_pla)
                    break
    print(len(set(translated_long)))
    print(translated_long[:100])


if __name__ == "__main__":
    genome_file = "fullgenomes/05.fa"
    orfinder(genome_file)
