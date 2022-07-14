from collections import Counter

a = [1,1,1,1,2,3,3,4,4,4]
a1 = Counter(a)
print(a1)
print(type(a1))

b = 'AAABCCCCCDDEFF'
b2 = Counter(b)
print(b2)
for i in b2:
    print(i , b2[i])

lis = ['P', 'y', 't', 't', 'h', 'o', 'o', 'n', 'n', ' ', 'C', 'u', 'e', 'r', 's']
z1 = Counter(lis)
 
for i in z1:
    print(i, z1[i], end=" ")
