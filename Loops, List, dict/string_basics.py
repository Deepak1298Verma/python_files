from operator import index


var="abcdefghij"

#print(var[2:8])
data=[]
#travesing on string
for i in var:
    data.append(i)
#print(data)
#length of the string
#print(len(var))

var="Today, is a, good day"
print(var.split(","))
print(var.index("good"))

var="i am john and marks are {2} in subject {0} and {1}"
# print(var.format("maths","science", 90))
# print(var.capitalize())
# print(var.casefold())
# print(var.center(18))