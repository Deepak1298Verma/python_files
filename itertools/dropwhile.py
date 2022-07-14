from itertools import dropwhile
import itertools

lis = [2,3,4,5,6,7,8,9,11,12,13]

print(list(itertools.dropwhile(lambda x: x % 2 == 0, lis)))