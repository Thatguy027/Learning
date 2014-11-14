# calculate the probability of dominant offspring
k = 23 # homozygous dominant
m = 19 # heterozygous
n = 19 # homozygous recessive
inds = float(k) + float(m) + float(n)

probDom = (float(k)/inds) + (float(m)/inds)*float(k)/(inds-1) + ((float(m)/inds)*((float(m)-1)/(inds-1))*.75 )+ ((float(m)/inds))*((float(n))/(inds-1))*.5 + ((float(n)/inds))*((float(k))/(inds-1)) + ((float(n)/inds))*((float(m))/(inds-1))*.5

print probDom
