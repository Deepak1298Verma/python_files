import itertools
from mmap import ACCESS_WRITE
import operator as op

lis1 = ['m','u','m']
lis2 = ['b','a','i']
lis3 = [1,3,5,7,9]

print(list(itertools.accumulate(lis3,op.add)))
print(list(itertools.accumulate(lis3,op.mul)))
# print(list(itertools.accumulate(lis3,op.pow(lis3,2))))
print(list(itertools.chain(lis1, lis2, lis3)))
print(list(itertools.chain(lis1,lis2)))