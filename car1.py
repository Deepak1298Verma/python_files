
class Car1(object):

    def __init__(self):
        self.b = None
        self.m = None
        self.y = None

    def brand(self, b):
        self.b = b
        # print(self.b)
        return self
    
    def model(self,m):
        self.m = m
        # print(self.m)
        return self

    def year(self, y):
        self.y = y
        # print(self.y)
        return self
        
    def make(self):
        print(self.b, self.m, self.y)
print(dir(Car1))