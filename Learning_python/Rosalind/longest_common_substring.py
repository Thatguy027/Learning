import sys, re, itertools
from sys import argv
import numpy as np
script, fasta = argv


file = open(fasta).read()
temp = file.split(">")
del temp[0]

dna = [0]*len(temp)

for i in range(0, len(temp)):
    dna[i] = temp[i].partition("\n")[2]
    dna[i] = dna[i].replace("\n","")

minest = min(dna,key=len)

subs = str()
length = 0

for j in range(0, len(minest)):
    for i in range(j+length, len(minest)):
        matching = len([s for s in dna if minest[j:i] in s])
        if matching == len(dna) and len(minest[j:i]) > len(subs):
                subs= minest[j:i]
                length = len(subs)
    if len(minest)-len(subs)<j:
        break

print subs
