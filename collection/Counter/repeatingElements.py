from collections import Counter

# aa = Counter(p = 4, q = 2, r = 0, s = 1 )
# print(list(aa.elements()))

# Write a Python program to find the most common elements and their counts of a specified text. Go to the editor
s = "lkseropewdssafsdfafkpwessss"
# lis = []
# for i in string:
#     lis.append(i)
print(Counter(s).most_common(4))
print(Counter(s).setdefault(s,"abcd"))
