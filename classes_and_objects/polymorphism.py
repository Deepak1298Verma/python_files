class parrot():

    #creating Functions
    def fly(self):
        print('parrot can fly')

    def swin(self):
        print("parrot can't swim")

class penguin():

    #creating functions
    def fly(self):
        print("penguin can't fly")
    
    def swin(self):
        print('penguin can swin')

def flying_test(bird):
    bird.fly()

#creating objects
ob1 = parrot()
ob2 = penguin()

#using common interface in many forms
flying_test(ob1)
flying_test(ob2)
