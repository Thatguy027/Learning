#!/bin/python
from sys import argv

script, Months, Lifespan = argv

#initialization
M = int(Months)
L = int(Lifespan)

n = [1,0]
nm = [0,1]
m = [0,1]
d = [0,0]
f = [1,1]

for i in range(2, M):
    nm.append(n[i-1])
    m.append(sum(nm[-L+1:]))
    n.append(m[i-1])
    if i < L :
        d.append(0)
    else:
        d.append(nm[i-L+1])
    f.append(f[i-1] + n[i] - d[i])

print f[M-1]

print n
print nm
print m
print d
