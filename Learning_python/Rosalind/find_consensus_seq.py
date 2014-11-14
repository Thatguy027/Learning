# script takes in FASTA formated sequence data and identifes the sequence with the highest GC content

from sys import argv
import numpy as np
script, fasta = argv

DNA = open(fasta).read()
temp = DNA.split(">")
del temp[0]

temp1 = [0]*len(temp)

for i in range(0, len(temp)):
    temp1[i] = temp[i].partition("\n")[2]
    temp1[i] = temp1[i].replace("\n","")

temp2 = str()
combs = [0]*len(temp1[1])

for j in range(0, len(temp1[1])):
    for i in range(0, len(temp1)):
        temp2 += (temp1[i][j])
    combs[j] = temp2
    temp2 = str()

cons = str()
check = np.zeros(shape=(4,len(temp1[1])))

AL = [0]*len(temp1[1])
CL = [0]*len(temp1[1])
GL = [0]*len(temp1[1])
TL = [0]*len(temp1[1])


for i in range(0, len(combs)):
    A = float(combs[i].count('A'))
    check[0][i] = float(combs[i].count('A'))
    AL[i] = str(combs[i].count('A'))
    C = float(combs[i].count('C'))
    check[1][i] = float(combs[i].count('C'))
    CL[i] = str(combs[i].count('C'))
    G = float(combs[i].count('G'))
    check[2][i] = float(combs[i].count('G'))
    GL[i] = str(combs[i].count('G'))
    T = float(combs[i].count('T'))
    check[3][i] = float(combs[i].count('T'))
    TL[i] = str(combs[i].count('T'))
    if G > max([A,T,C]):
        cons += "G"
    elif  G == max([A,T,C]):
        cons += "G"
    elif C > max([A,T,G]):
        cons += "C"
    elif  C == max([A,T,G]):
        cons += "C"
    elif A > max([C,T,G]):
        cons += "A"
    elif A == max([G,T,C]):
        cons += "A"
    elif T > max([C,A,G]):
        cons += "T"
    elif T == max([A,G,C]):
        cons += "T"
    else:
        cons += "X"


print cons
print "A:",' '.join(AL)
print "C:",' '.join(CL)
print "G:",' '.join(GL)
print "T:",' '.join(TL)

print len(cons)
print len(temp1[1])
