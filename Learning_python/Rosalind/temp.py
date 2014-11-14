import sys, re, itertools
from sys import argv
import numpy as np
script, fasta = argv


file = open(fasta).read()
temp = file.split(">")
del temp[0]

dna = [0]*len(temp)
sub = [0]*len(temp)
header = [0]*len(temp)

for i in range(0, len(temp)):
    dna[i] = temp[i].partition("\n")[2]
    dna[i] = dna[i].replace("\n","")

longest = max(dna,key=len)

subs = []

def find_kmers(string, kmer_size):

      kmers = []

      for i in range(0, len(string)-kmer_size+1):
           kmers.append(string[i:i+kmer_size])
      return kmers


subs = []
for i in range(len(longest)):
    t = find_kmers(longest, i)
    subs.append(list(set(t)))

del subs[0]

matches = []

for j in range(len(subs)):
    temp = len(subs[j])
    matching = [0]*temp
    while max(matching) <100:
        for i in range(temp):
            matching[i] = len([s for s in dna if subs[j][i] in s])
            break
