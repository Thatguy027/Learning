# script takes in FASTA formated sequence data and identifes the sequence with the highest GC content

from sys import argv
script, fasta = argv

DNA = open(fasta).read()
temp = DNA.split(">")
del temp[0]

temp1 = [0]*len(temp)
header = [0]*len(temp)
combs = [0]*len(temp)

for i in range(0, len(temp)):
    print i
    temp1[i] = temp[i].partition("\n")[2]
    temp1[i] = temp1[i].replace("\n","")
    temp1[i] = (float(temp1[i].count('G')) + float(temp1[i].count('C'))) / float(len(temp1[i]))
    header[i] = temp[i].partition("\n")[0]
    combs[i] = '\n'.join([header[i],str(temp1[i]*100)])

for i in range(0,len(temp)):
    if temp1[i] == max(temp1):
        print combs[i]
    else:
        print "you suck"
