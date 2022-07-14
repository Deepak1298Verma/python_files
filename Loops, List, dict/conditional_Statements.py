# for i in range(1,11):
#     print(i)

# ---------Pattern----------
# for i in range(1,6):
#     for j in range(1,i+1):
#         # print(i,j)
#         print(j, end=" ")
#     print()

# --------sum of natural numbers----------
# var=int(input("Enter value"))
# sum=0
# for i in range(1, var+1):
#     sum+=i
# print(sum)   

# --------tables by method-------
# def table(num):
#     for i in range(1,11):
#         print(num, " X ", i, " = ", num*i)
# table(10)
# table(2)

# Display numbers from a list using loop
# aa = [12, 75, 150, 180, 145, 525, 50]
# for i in aa:
#     if i > 500:
#         break
#     if i > 150:
#         continue
#     elif i % 5==0:
#         print(i)

# Count the total number of digits in a number
# aa=int(input("Enter value"))
# count=0
# while aa!=0: //checking condition

    # aa=aa//10 //performing floor division and updating the quotient

    # count+=1 //increasing the count
# print(count)

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()

# ------------reversing the list------------
# aa = [10, 20, 30, 40, 50]
# size=len(aa)-1
# aa1=[]
# for i in range(size,-1,-1):
#     aa1.append(aa[i])
# print(aa1)

# display prime number in specified range
a=int(input("First"))
b=int(input("second"))
for num in range(a,b+1,1):
    for i in range(2,num,1):
        if num%i == 0:
            break
    else:
        print(num, end=" ")

# Display Fibonacci series up to 10 terms
# num1, num2 = 0,1
# n=int(input("Value"))
# for i in range(n):
#     print(num1, end=" ")

#     res = num1 + num2
#     num1 = num2
#     num2 = res

# find factorial
# n=int(input("Value")) 
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(1,len(my_list),2):
#     print(my_list[i])

# n=int(input("Value"))
# for i in range(1,n+1):
#     res = i*i*i
#     print("the cube of ", i, "is ", res)

# pattern
# for i in range(1,7,1):
#     for j in range(1,i):
#         print("*", end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(i,1,-1):
#         print("*", end=" ")
#     print()
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *