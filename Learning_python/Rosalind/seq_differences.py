from sys import argv

script, string = argv

DNA = open(string).read()

DNA = DNA.split("\n")

DNA = DNA[:-1]

seq1 = DNA[0]
seq2 = DNA[1]

counter = 0

for i in range(0, len(seq1)):
    if seq1[i] != seq2[i]:
        counter = counter +1
    else:
        counter = counter

print counter
