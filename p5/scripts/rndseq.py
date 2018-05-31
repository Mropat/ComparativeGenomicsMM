
import random
import pickle

number=5000
length=20
aas="ARNDCEQGHILKMFPSTWYV"
def r20():
    return random.randrange(20)

ndict = {}
for i in range(number):
    s=""
    for j in range(length):
        s+=aas[r20()]
    ndict [i] = s

pickle.dump(ndict, open("p5/ndict.sav", "wb"))