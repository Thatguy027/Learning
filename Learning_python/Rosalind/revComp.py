from sys import argv

script, string = argv

DNA = open(string).read()

DNA = DNA.replace("\r","")
DNA = DNA.replace("\n","")

revDNA = list(DNA[::-1])
revComp = revDNA

end = len(revDNA)

for i in range(0,end):
    if revComp[i] == 'A':
        revComp[i] = 'T'
    elif revComp[i] == 'T':
        revComp[i] = 'A'
    elif revComp[i] == 'G':
        revComp[i] = 'C'
    elif revComp[i] == 'C':
        revComp[i] = 'G'
    else:
        revComp[i] = revComp[i]

revComp = ''.join(revComp)

print revComp
