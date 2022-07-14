# from functools import reduce

# scores = [75, 65, 80, 95, 50]

# def add(a, b):
#     print(f"{a} and {b} and the sum {a}+{b}")
#     return a+b

# # res = reduce(add, scores)
# res = reduce(lambda a,b : a+b, scores)
# print(res)

from ankit import add

print(add(2,5))