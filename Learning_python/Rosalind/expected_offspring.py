from sys import argv

#AA-AA
#AA-Aa
#AA-aa
#Aa-Aa
#Aa-aa
#aa-aa

script, dd, dh, dr, hh, hr, rr, offspring= argv

dd = float(dd)
dh = float(dh)
dr = float(dr)
hh = float(hh)
hr = float(hr)
rr = float(rr)

off = float(offspring)

# expected values
edd = dd*float(off) # 100% dominant
edh = dh*float(off) # 100% dominant
edr = dr*float(off) # 100% dominant
ehh = hh*(float(3)/float(4))*off # 75% dominant each child
ehr = hr*(float(2)/float(4))*off # 50% dominant each child
err = 0 # 0% dominant

expected = edd + edh + edr + ehh + ehr + err

print expected
