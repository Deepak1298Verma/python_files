#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
# decorator
def decor(func):
    def inner():
        print('area calculation ')
        func()
    return inner

class circle:

    #class variable
    pie = 3.14

    # constructor
    def __init__(self, radius):
        self.radius = radius

    # finding area
    def area(self):
        area = circle.pie * self.radius * self.radius
        return area

    # circumference
    def circum(self):
        circum = 2 * circle.pie * self.radius
        return circum


# ob1 = circle(12)
# ob1.area()
# ob1.circum()

ob1 = circle(12)
print(f'the area of circle with radius {ob1.radius} is {ob1.area()}')

print(f'the circumference of circle with radius {ob1.radius} is {ob1.circum()}')


class reactangle(circle):

    def __init__(self, length, breadth):
        self.len = length
        self.bre = breadth

    # decorator
    def decor(func):
        def inner():
            print('area calculation ')
            func()
        return inner
    
    def area(self):
        area = 2 * (self.len + self.bre)
        return area

aa = reactangle(25, 12)
aa.decor()
            
        
