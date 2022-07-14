# list1 = [1, 2, 3] 

# def multiply(num):
#     prod = 1
#     for i in range(len(list1)):
#         prod = prod * list1[i]
#     return prod

# res = map(multiply,list1)

# print(set(res))


subject = ['english', 'hindi', 'science', 'computer', 'social']
lis1 = []
def grade(marks):
    for i in range(len(marks)):
        if marks[i] >=90 and marks[i] <= 100:
            a = "A"
            lis1.append(a)
        elif marks[i] >=80 and marks[i] < 90:
            a = "B"
            lis1.append(a)
        elif marks[i] >=70 and marks[i] < 80:
            a = "C"
            lis1.append(a)
        elif marks[i] >=60 and marks[i] < 70:
            a = "D"
            lis1.append(a)
        elif marks[i] >= 33 and marks[i] < 60:
            a = "E"
            lis1.append(a)
        else:
            a = "F"
            lis1.append(a)

lis = [95, 15, 10, 10, 65]
grade(lis)
# print(lis1)


def remarks(value):
    count = 0
    for i in range(len(value)):
        if value[i] == "F":
            count+=1
    if count == 0:
        print("pass")
    elif count <= 2:
        print("You got supplementary")
    elif count > 2:
        print("Fail")

            
    print(count)

remarks(lis1)






















# def avgmarks(aa):
#     sum = 0
#     for i in aa:
#         sum += i
#     sum = sum / 5
#     return sum
