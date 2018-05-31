def clean(file):
    with open("output.txt", "w") as wh:
        with open(file, "r") as fh:
            for line in fh:
                for char in line:
                    if char != "-":
                        wh.write(char)

if __name__ == "__main__":
    clean("p3/all_alignment.fasta")
