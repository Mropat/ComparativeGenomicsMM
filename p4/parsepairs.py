def pairs(file):
    with open (file, "r")as fh:
        for line in fh:
            orf = line[3:11]
            print(orf)


if __name__ == "__main__":
    pairs("parsed05.txt")