from sys import argv

script, n, k = argv

#initialization
n = int(n)
k = int(k)
spop = 1
mpop = [0]*n

for i in range(0, n):
    if i < 2:
        mpop[i] = spop
    else:
        mpop[i] = mpop[i-1]+mpop[i-2]*k

print mpop
