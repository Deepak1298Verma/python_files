# Create a Class with instance attributes

class vehicle:

    #class variable
    specs = 'white'

    #constructor
    def __init__(self, name, avg, mileage):
        self.name = name
        self.avg = avg
        self.mileage = mileage

    def show(self):
        print(self.name, self.avg, self.mileage)

    def seating_limit(self, seating):
        self.seating = seating
        print('color : ', vehicle.specs, 'vehicle name : ', self.name, 'speed : ', self.avg, 'mileage : ', self.mileage)


#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Bus(vehicle):
    
    #method overridden by child class
    def seating_limit(self, capacity = 50): 
        print('color : ', vehicle.specs, '   vehicle name : ', self.name, '   speed : ', self.avg, '   mileage : ', self.mileage)

ob1 = Bus('Volvo', 180, 12)
ob1.seating_limit()

ob2 = Bus('Audi', 240, 18)
ob2.seating_limit()
