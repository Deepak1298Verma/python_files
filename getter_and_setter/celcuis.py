class temp:

    def __init__(self, temp = 0):
        self.set_temp(temp)

    def to_farenheit(self):
        return (self.celcius * 1.8) + 32

    def get_temp(self):
        print('getting value.......')
        return self.celcius

    def set_temp(self, value):
        print('setting value........... ')
        if value < -273:
            print("not possible")
        self.celcius = value

    #   creating the property of class
    temp = property(get_temp, set_temp)

human = temp(37)

print(human.get_temp())

print(human.to_farenheit())

print(human.set_temp(-300))