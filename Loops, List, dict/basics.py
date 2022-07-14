# #Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
# a=0
# for i in range(0,10,1):
#     print("Current Number ", i,"Previous Number ",a ,"Sum ", i+a)
#     a=i

str = "pynative"
for i in range(len(str)):
    if i % 2 == 0:
        print(str[i], end=" ")
data=[]
for i in str:
    data.append(i)