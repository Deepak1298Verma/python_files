class Car:

    #class variable
    specs = 'vehicles'

    #instance variables

    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year

    def color(self, colour):
        self.colour = colour
    
#object creation
ob1 = Car('swift', 'maruti', 2020)
ob2 = Car('SUV', 'mahindra', 2022)
ob3 = Car('verna', 'hyundai', 2021)

ob1 = Car.color("blue")
ob2 = Car.color("black")
ob3 = Car.color("grey")

print(ob1.__class__.specs) #calling class variable
print(ob1.name, ob1.brand, ob1.year)  #calling instance variables

print(ob2.__class__.specs) #calling class variable
print(ob2.name, ob2.brand, ob2.year) # calling instance variables

print(ob3.__class__.specs) #calling class variable
print(ob3.name, ob3.brand, ob3.year) # calling instance variables


    

