from curses.ascii import isdigit


var="foo-ba12r-13"
# num = "1234567890"
# var2 = ""
# for i in var:
#     if i not in num:
#         var2+=i
# print(var2)
 
for i in range(len(var)):
    if var[i].isdigit():
        continue
    else:
        print(var[i], end=" ")
 