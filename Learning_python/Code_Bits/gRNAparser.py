from sys import argv
import csv

script, file, cutoff = argv

with open(file) as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)

cutoff = float(cutoff)

print cutoff

goodRNAS = []

for i in range(1, len(d)):
    if float(d[i][3]) > cutoff:
        print float(d[i][3]) > cutoff
        print float(d[i][3])
        goodRNAS.append(d[i])
    else:
        goodRNAS = goodRNAS

print goodRNAS
