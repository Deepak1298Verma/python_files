#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
from curses.ascii import isdigit


def isDivisible(num1, num2):
    for i in range(num1, num2+1, 1):
        if i % 5 == 0 and i % 7 == 0:
            print(i, end=" ")
# isDivisible(1500,2700)

#Write a Python program to convert temperatures to and from celsius, fahrenheit
def isClecius(temp):
    far = temp * 1.8 + 32
    print(far)
def isfarenheit(temp):
     cel = (temp - 32) * 5/9 
     print(cel)
# isClecius(60), isfarenheit(140)

aa="abc13abc"
lis=[]
for i in aa:
    # lis.append(i)
    if i == isdigit(aa):
        i.replace(i," ")
print(aa)

for i in range(len(lis)):
    if lis[i] == isdigit(aa):
        lis.pop(i)
# print(lis)