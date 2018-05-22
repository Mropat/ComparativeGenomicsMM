
import gzip

with gzip.open("/home/maria/Desktop/ComparativeGenomicsMM/p8/protein.links.v10.txt.gz", "rb") as fh:
    processing = "null"
    for line in fh:
        line = line.decode('utf-8').strip()

        if line.startswith(processing):
            continue

        elif line.startswith("4932"):
            with open("4932.txt", "a") as wh5:
                wh5.write(line + "\n")

        elif line.startswith("224911"):
            with open("224911.txt", "a") as wh1:
                wh1.write(line + "\n")

        elif line.startswith("243090"):
            with open("243090.txt", "a") as wh4:
                wh4.write(line + "\n")

        elif line.startswith("272561"):
            with open("272561.txt", "a") as wh2:
                wh2.write(line + "\n")

        elif line.startswith("515635"):
            with open("515635.txt", "a") as wh3:
                wh3.write(line + "\n")
        else:
            processing = line.split(".")[0]
            if int(processing) > 515635:
                break
            print(processing)


