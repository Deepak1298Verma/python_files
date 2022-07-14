# class X:
#     pass

# class Y:
#     pass

# class Z:
#     pass

# class A(X,Y):
#     pass

# class B(Y, Z):
#     pass

# class M(A, B, Z):
#     pass

# print(M.mro())


# 5
# 2 3 6 6 5

n = int(input())
arr = map(int, input().split())
lis1 = list(arr)

lis1.sort(reverse=True)
print(lis1[1])
