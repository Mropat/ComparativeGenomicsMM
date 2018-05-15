


geneOrderList = []
with open ("p4/genomes/16.fa", "r") as aHandle:
    lines = aHandle.readlines ()
    for aLine in lines:
	    aLine = aLine.strip()	
	    if aLine.startswith (">"):
		    aLine = aLine.split('.fa.txt')
		    first = aLine[0].split('/')
		    second = aLine[1]
		    geneOrderList.append (first[1] + second)


partOfCluster = {}

with open ("concat_instersect_all.txt", "r") as bHandle:
    lines = bHandle.readlines ()
    id = 0

    for aLine in lines:

	    aLine = aLine.strip()
	    words = aLine.split (" ")

	    for aWord in words:

		    if aWord not in partOfCluster:
			    partOfCluster [aWord] = id

	    id = id + 1

# put together
with open ("p5/16_order_line.txt", "w") as wh:
    for aGene in geneOrderList:

	    if aGene in partOfCluster:

		    wh.write(str(partOfCluster[aGene]) + " ")