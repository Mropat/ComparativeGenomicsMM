#Deprecated:
#Script that concatenates the XML parser output dicts into cluster files
#Reference genome orf id is used as key to retrieve hit ids and print them together

import pickle

def conc():
    file5 = pickle.load(open("pickle5.sav","rb"))
    file8 = pickle.load(open("pickle8.sav","rb"))
    file16 = pickle.load(open("pickle16.sav","rb"))
    with open ("concatenate.txt", "w") as wh:
        for key, val in file5.items():
            if key in list(file8.keys()):
                if key in list(file16.keys()):                  
                    wh.write("04_"+key + " 05_" + file5[key] + " 08_" + file8[key] + " 16_" + file16[key] + "\n")
    #Resulting file is a file containing all clusters

if __name__ == "__main__":
    conc()