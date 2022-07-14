from collections import ChainMap
from curses import keyname

aa = {1:'delhi', 2:'pune'}
bb = {3:'mumbai', 4:'kochi'}
cc = ChainMap(aa,bb)
print(cc)

# add a new dict again in old one
dd = {5:'banglore', 6: 'jaipur'}
cc = cc.new_child(dd)
print(cc)

