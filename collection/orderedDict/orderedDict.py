from collections import OrderedDict

od = OrderedDict()
od[0] = "A"
od[1] = "C"
od[2] = "E"
od[3] = "G"
od[4] = "I"
od[5] = "K"
od[6] = "M"
od[7] = "O"
od[8] = "Q"
od[5] = "Z"
for i in od:
    print(i, od[i])
print()
ndict = {}
ndict[0] = "A"
ndict[1] = "B"
ndict[3] = "C"
ndict[4] = "D"
ndict[5] = "E"

for i in ndict:
    print(i,ndict[i])
print()
ndict[4] = "Z"

for i in ndict:
    print(i,ndict[i])

