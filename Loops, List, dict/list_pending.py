list1=[{"Name":"Jack", "age":18, "salary":18000},{"Name":"john", "age":22, "salary":20000},{"Name":"Jhonny", "age":20, "salary":15000},{"Name":"Daniel", "age":26, "salary":25000}]

for i in range(len(list1)):
    if list1[i]["salary"] > 18000:
        print(list1[i])

for i in range(len(list1)):
    if list1[i]["age"] >= 20:
        print(list1[i]["Name"])

cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As"
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah"
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad"
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac"
           ]
print(len(cards))

phonebook = {"bob": 7387,"alice": 3719,"jack": 7052}

# print(cards[-5:-1])

# if "2s" in cards:
    # print("present")

cards[4]="Hello"
# print(cards)

cards[12:49]="Empty"
print(cards)

data=["indore", "Delhi"]
data1=['Pune', "Mumbai"]
# data.extend(data1)
car=["Tata","Suzuki","Honda"]
# car.remove("Tata")
# car.pop(1)
# car.pop()
# car.insert(0, "Honda")
# car.insert(1, "Tata")
# del car[1]
# # del car
# car.clear()
# print(car)

# [print(car[i]) for i in range(len(car))]
[print(i) for i in range(len(car)) if car[i] == "Honda"]