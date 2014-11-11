from sys import argv

script, string = argv

DNA = open(string).read()

DNA = DNA.replace("\r","")
DNA = DNA.replace("\n","")

dna = list(DNA)

print "Length of sequence: ", len(DNA)

for i in range(0,len(dna)):
    if dna[i] == 'T':
        dna[i] = 'U'
    else:
        dna[i] = dna[i]

dna = ''.join(dna)

print "DNA = ", DNA
print "RNA = ", dna
