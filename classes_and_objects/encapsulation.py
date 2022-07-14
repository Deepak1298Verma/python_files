class encapsulation:

    def __init__(self):
        self.__maxprice = 900
        print(self.__maxprice)

    def displayPrice(self):
        print(self.__maxprice)
    
    def setPrice(self, price):
        self.__maxprice = price

ob = encapsulation()
ob.displayPrice()
ob.__maxprice = 1000
ob.displayPrice()
ob.setPrice(1000)
ob.displayPrice()

del ob
print(ob)