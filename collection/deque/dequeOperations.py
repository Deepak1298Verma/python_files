from collections import deque

aa = '124dfre'
a1 = deque('124edfree')
#appending the value
a1.appendleft("A")
a1.append("X")
print(a1)

#removing the value
item = a1.pop()
item = a1.popleft()
print(a1)

#get information related to item
print(a1.index("4"))
print(a1.count("e"))

#insert and delete from deque
a1.insert(5,"Z")
a1.remove("e")
print(a1)

