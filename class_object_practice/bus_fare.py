class Vehicle:

    #constructor
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    #parent method 
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    #method overridden by child class
    def fare(self):
        total_amount = self.capacity * 100
        final_amount = total_amount + (total_amount * 10) / 100
        return final_amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

aa = isinstance(School_bus, Vehicle)
print(aa)