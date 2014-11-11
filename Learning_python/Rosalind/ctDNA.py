from sys import argv

script, string = argv

DNA = open(string).read()

print DNA

print "Length of sequence: ", len(DNA)

A = 0
G = 0
T = 0
C = 0
X = 0

for i in range(0,len(DNA)):
    if DNA[i] == 'A':
        A = A +1
    elif DNA[i] == 'G':
        G = G +1
    elif DNA[i] == 'C':
        C = C +1
    elif DNA[i] == 'T':
        T = T +1
    else:
        X = X +1

print "A = ", A
print "G = ", G
print "T = ", T
print "C = ", C
print "X = ", X
