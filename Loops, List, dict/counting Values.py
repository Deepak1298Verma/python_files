# n=int(input())
# count=0
# while n!=0:
#     #performing floor division to reduce the digit
#     n=n//10
#     #count the value everytime in the loop
#     count=count+1
    
# print(count)

var="abbbaacccdda" #o/p = ab3ac3da
data=[]
for i in range(len(var)):
    data.append(var[i])
newlist=[]
for i in range(len(data)):
    if "a" in data[i]:
        newlist.append(data[i])
    if "d"in data[i]:
        newlist.append(data[i])
print(newlist)
string=""
for i in newlist:
    string+=i
print(string)

aa = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
# for i in aa:
#     if "a" in i:
#         newlist.append(i)


#list comprehension
newlist = [i for i in aa if "a" in i]
print(newlist)
    