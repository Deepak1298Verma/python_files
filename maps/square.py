import array as arr
from functools import reduce
from re import I


# numbers=(1,2,3,4,5)
# #function declaration
# def square(num):
#     return num * num

# #map function call
# res = map(square,numbers)

# #assigning to list
# final_res = set(res)
# print(final_res)    

# #  Write a Python program to triple all numbers of a given list of integers. Use Python map

# numbers=(1,3,5,7,9)

# def cube(num):
#     """function for cube"""
#     return num * num * num

# #map function call
# result = map(cube, numbers)

# #coverting to list
# final_result = list(result)
# print(final_result)

# aa = lambda x: x * x
# print(aa(5))

# # Write a Python program to add three given lists using Python map and lambda.
# lis1 = [1,2,3]
# lis2 = [4,5,6]
# lis3 = [7,8,9]

# res = map(lambda n1, n2, n3 : n1+n2+n3, lis1, lis2, lis3)
# print(list(res))

# # Write a Python program to listify the list of given strings individually using Python map.
# aa="abcdefghijklmnopqrstuvwxyz"
# # function declaration
# def list_conversion(string):
#     list=[]
#     for i in string:
#         list.append(i)
#     print(list)

# #map function calling
# res = map(list_conversion,aa)

# #converting to list
# final = list(res)
# print(final)

# res = list(map(list, aa))
# print(res)

# lis1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# lis2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = map(lambda n1, n2 : n1 ** n2, lis1, lis2)

# print(list(res))

# # Write a Python program to square the elements of a list using map() function.

# Original_List = [4, 5, 2, 9]

# res = map(lambda x : x * x, Original_List )

# print(list(res))

# chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}

# def changeCases(s):
#     return str(s).lower(), str(s).upper()

# res = map(changeCases, chrars)

# print(set(res))

# nums1 = [6, 5, 3, 9]
# nums2 = [0, 1, 7, 7]
# #function call
# def add_sub(x,y):
#     return x+y, x-y
# #map function call
# res = map(add_sub,nums1,nums2)
# #converting to list
# print(list(res))

# # convert list of integers and tuple of integers in a list of string
# l1 = [1,2,3,4]
# t1 = (5,6,7,8)

# #map function call
# res_list = list(map(str, l1))
# res_tuple = tuple(map(str, t1))
# print(res_list)
# print(res_tuple)

# student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
# name = map(lambda x: x[0], student_data)
# print(list(name))
# dob = map(lambda x: x[1], student_data)
# print(list(dob))
# weight = map(lambda x: x[2], student_data)
# print(list(weight)) 

# num = arr.array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])  
# n = len(num)
# def positive_negative(nums):
#     n1 = n2 = n3 =0
#     for i in nums:
#         if nums[i] > 0:
#             n1 += 1
#         elif nums[i] < 0:
#             n2 += 1
#         else:
#             n3 += 1
#     return n1/n, n2/n, n3/n 

# res = list(map(int, num))
# final = positive_negative(res)
# print(final)
# aa=0
# def add(arr):
#     for i in arr:
#         aa = aa + i
#     print(aa)

# add(num)
# # res = list(map(int, num))
# # final_res = sum(res)
# print(final_res)

aa1 = [36,12,24,48,-65,0,42,-20,-45,48,12,0]
aa2 = [7,14,21,28]

lam = map(lambda n1: n1, aa1)
l1 = list(lam)
print(l1)
l1.sort(reverse=True)
print(l1)
s1 = set(l1)
print(s1)

st = "Today is a good day"

# fil = filter(lambda n1: len(st), st)
# fil = filter(lambda n1: n1 == 'o', st)
# fil = filter(lambda n1: n1 < 0, aa1)

# print(list(fil))

red = reduce(lambda n1, n2: n1+n2, aa2)
print(red)

