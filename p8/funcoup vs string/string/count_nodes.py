from collections import Counter

idlist = []
with open ("p8/funcoup vs string/string/string_interactions.tsv", "r") as fh:
    for line in fh:
        idlist.append(line.strip().split("\t")[0])
        idlist.append(line.strip().split("\t")[1])
print(Counter(idlist))
        
