from Bio import SeqIO


def get_fancy_keys(record):
    index = record.id.find("_")
    return record.id[index+1:]


def genomes(filename):
    dict4 = SeqIO.to_dict(SeqIO.parse("p4/04.fa", "fasta"),
                          key_function=get_fancy_keys)
    dict5 = SeqIO.to_dict(SeqIO.parse("p4/05.fa", "fasta"),
                          key_function=get_fancy_keys)
    dict8 = SeqIO.to_dict(SeqIO.parse("p4/08.fa", "fasta"),
                          key_function=get_fancy_keys)
    dict16 = SeqIO.to_dict(SeqIO.parse(
        "p4/16.fa", "fasta"), key_function=get_fancy_keys)

    with open(filename, "r") as fh:
        counter = 0
        for line in fh.readlines():
            id4, id5, id8, id16 = line.strip().split(" ")
            id4, id5, id8, id16 = id4[3:], id5[3:], id8[3:], id16[3:]

            seq4, seq5, seq8, seq16 = dict4[id4].seq, dict5[id5].seq, dict8[id8].seq, dict16[id16].seq
            counter += 1
            with open("p4/clusters/"+str(counter)+".fasta", "w") as wh:
                wh.write(">Bradyrhizobium_"+id4 + "\n" + str(seq4) + "\n" + ">Chlamydia_"+id5 + "\n" + str(seq5) + "\n" +
                         ">Dictyoglomus_"+id8 + "\n" + str(seq8) + "\n" + ">Rhodopirellula_"+id16 + "\n" + str(seq16) + "\n")


if __name__ == "__main__":
    genomes("concat_instersect.txt")
