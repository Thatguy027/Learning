from sys import argv

script, string = argv

revDNA = list(string[::-1])
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
