class car:

    def __init__(self):
        self.b = None
        self.m = None
        self.y = None

    def brand(self,b):
        self.b = b
        return self

    def model(self, m):
        self.m = m
        return self

    def year(self, y):
        self.y = y
        return self
    
    import pdb; pdb.set_trace()
    def make(self):
        print(self.b, self.m, self.y)

