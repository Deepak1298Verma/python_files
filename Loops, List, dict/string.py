# from re import sub
# aa="GeekforGeeks"
# a1=[]
# for i in aa:
#     a1.append(i) #appending the string in list
# print(a1)
# a1.clear()
# print(a1)

# print(aa[::-1]) #reverse the string
# print(aa[2:8]) # string slicing

# n = "{2} {1} {0}".format("Morning","Good","hello")
# print(n)

# n="{1} is a great place to explore {0} has its own".format("It","Indore")    
# print(n)
# print(aa.startswith("G"))
# print(aa.capitalize())
# print(aa.split())

var="abbbaacccdda" #o/p = ab3ac3da
temp=var
aa=""
for i in range(len(temp)):
    if temp.count(temp[i]) == 3:
        aa.join(temp[i])
    print(aa)
