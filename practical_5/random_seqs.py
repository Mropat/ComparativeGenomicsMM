import random
import sys
number=int(sys.argv[1])
length=int(sys.argv[2])

aas="ARNDCEQGHILKMFPSTWYV"

def r20():
    return random.randrange(20)
with open('random_seq_dic.txt', 'w') as w:
    for i in range(number):
        s=""
        for j in range(length):
            s+=aas[r20()]

        w.write(str(i) + ' ' + s + '\n')
#print(dic)

