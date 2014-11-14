
from sys import argv

script, peptide = argv

amino_weight = {
    'A':  71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G':  57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,   # you omitted leutine?
    'M': 131.04049,
    'N': 114.04293,
    'P':  97.05276,
    'Q': 128.05858,   # you omitted glutamine?
    'R': 156.10111,
    'S':  87.03203,
    'T': 101.04768,
    'V':  99.06841,
    'W': 186.07931,
    'Y': 163.06333
}

def splitCount(s, count):
     return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]


aa = splitCount(peptide,1)
print aa

for i in range(0, len(aa)):
    aa[i] = amino_weight[aa[i]]

print sum(aa)
