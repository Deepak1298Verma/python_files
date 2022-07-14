inp=[12, 35, 9, 56, 24]
size=len(inp)
temp=inp[0]
inp[0]=inp[size-1]
inp[size-1]=temp
print(inp)

inp = [23, 65, 19, 90]
size=len(inp)
inp[0], inp[2] = inp[2], inp[1]
print(inp)

inp.sort(reverse=True)
print(inp)

inp=["Indore","delhi","Pune"]
inp.sort(key=str.lower)
print(inp)
#--copy List------
data=inp.copy()
print(data)

data1=list(inp)
print(data1)

#--------------------------Reverse a list in Python------------------------------#
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

#----------------------Turn every item of a list into its square----------------------#
numbers = [1, 2, 3, 4, 5, 6, 7]
newlist=[i*i for i in numbers]
print(newlist)
#--------------------Concatenate two lists in the following order-------------------#
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
    for j in list2:
        print(i+j,end=" ,")
#--------------------Remove empty strings from the list of strings-----------------#
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)