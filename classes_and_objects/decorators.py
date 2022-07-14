# def add(a, b):
#     c = a+b
#     return c

# add1 = add
# del add
# # print(add(2,3))
# print(add1(4,5))

# def decor(func):
#     def inner():
#         print('inside inner func')
#         func()
#         print('inner func end')

# @decor
# def disp():
#     print('out of decorator')

# disp()

# def decor(func):
#     def inner():
#         print('before decorators')
#         func()
#         print('after decorators')
#     return inner

# @decor
# def ordinary():
#     print('ordinary function')

# aa = ordinary()
# print(aa)

#divide a / b

# def decor1(func):
#     def inner():
#         a = func()
#         multi = a * 5
#         return multi
#     return inner

# def decor2(func):
#     def inner():
#         b = func()
#         add = b + 5
#         return add
#     return inner

# def num():
#     return 10

# a = num()
# print(a)

# res = decor1(num)
# print(res())

# result = decor2(decor1(num))
# print(result())

def decor1(func):
    def inner(a, b):
        print(' the division of a nd b is ')
        if b == 0:
            print("Cannot divide ")
            return

        return func(a,b)
    return inner

@decor1
def divide(a, b):
    print(a/b)

divide(8, 0)