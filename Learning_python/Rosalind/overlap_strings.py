# code takes dna strings from FASTA format and asks:
# is the substring of length "ss" at the end of one sequence at the start of another
# if it is, then link the two sequences by header name
from sys import argv
import numpy as np
script, fasta, ss = argv

ss = int(ss)

file = open(fasta).read()
temp = file.split(">")
del temp[0]

dna = [0]*len(temp)
sub = [0]*len(temp)
header = [0]*len(temp)

for i in range(0, len(temp)):
    dna[i] = temp[i].partition("\n")[2]
    dna[i] = dna[i].replace("\n","")
    sub[i] = dna[i][-ss:]
    header[i] = temp[i].partition("\n")[0]

for j in range(0, len(dna)):
    for i in range(0, len(dna)):
        if sub[j] == dna[i][:ss] and header[j] != header[i]:
            print header[j], header[i]
