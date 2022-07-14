class car:

    def __init__(self):
        print("This is parent class")

    def color(self):
        print('parent class color')

    def model(self):
        print('parent class model')

class maruti(car):

    def __init__(self):
        super().__init__()
        print('child class const.')
    
    def color(self):
        print('child class color')

    def version(self, year):
        self.year = year
        print(year)

ob1 = maruti()
print(ob1.color)
print(ob1.version(2022))
print(ob1.model)


class ploygon:

    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [input("Enter the sides ") for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [int(input("Enter the sides "+ str(i+1)) for i in range(self.n))]

    def disp_sides(self):
        for i in range(self.n):
            print("side ", i+1 , " is " , self.sides[i])

ob = ploygon(3)
ob.disp_sides()
