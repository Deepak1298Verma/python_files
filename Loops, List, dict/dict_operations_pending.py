
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
data = ["Name", "class", "Stream"]
res_dict=dict(zip(keys, values))
# print(res_dict)
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3=dict1.copy()
dict3.update(dict2)

# print(dict3)
# print(dict3.values())
# print(dict3.keys())

# dict3.clear()
# print(dict3)

dict4=dict3.copy()
# print(dict4)

# print(dict4.fromkeys(dict1, dict2))

# print(dict1.items())

# print(dict4.pop("Ten","Twenty"))

# print(dict4)
# print(dict4.popitem())
# print(dict4)

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# # print(sampleDict["class"]["student"]["marks"]["history"])


# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# res=dict.fromkeys(employees,defaults)
# # print(res)

# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# # for i in sample_dict:
# #     if sample_dict[i] == 200:
#         # print(i)
#         # print("present")

# if 200 in sample_dict.values():
#     # print("present")

# # sample_dict = {
# #     "name": "Kelly",
# #     "age": 25,
# #     "salary": 8000,
# #     "city": "New york"
# # }

# # # Keys to remove
# # keys = ["name", "salary"]

# data={"name":"kelly", "age":25, "salary":8000, "city":"NewYork"}
# var=[]
# var.append({"name": data["name"], "Salary":data["salary"]})
# print(var)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
data1=[]
for i in keys:
    sample_dict.pop(i)
print(sample_dict)