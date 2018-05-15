import sys
dic_file = open(sys.argv[1], 'r')
gene_order = open(sys.argv[2], 'r')
outfile = sys.argv[3]

dic = {}

for rand_seq in dic_file:
    number_seq = rand_seq.split(' ')
    dic[number_seq[0]] = number_seq[1].strip()
        
pseudoproteome = []
def pseudogenome(gene_order):
        
    with open(outfile, 'w') as w:
        for line in gene_order:
            line = line.strip()
            #print(dic[int(line)])
            
            w.write(dic[line])
pseudogenome(gene_order)
