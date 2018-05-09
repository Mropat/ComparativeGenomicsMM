# this script takes the output of a blast run
# and outputs a file with the best hits between genomes in the format:
#reference_proteome ref_seq  target proteome target-seq


import sys
import re
from Bio.Blast import NCBIXML

blastOutputXMLFile = sys.argv [1]

referenceProteome = sys.argv [2]

targetProteome = sys.argv [3]

blastOutputXMLHandle = open (blastOutputXMLFile)

listOfBlastRecords = NCBIXML.parse (blastOutputXMLHandle)

for aSingleBlastRecord in listOfBlastRecords:

	for i in range (len (aSingleBlastRecord.alignments)):

		description = aSingleBlastRecord.descriptions [i]
		alignment = aSingleBlastRecord.alignments [i]		
		print  referenceProteome + ' ' + alignment.hsps [0].query + ' '+ targetProteome +  ' ' + alignment.hsps [0].sbjct

