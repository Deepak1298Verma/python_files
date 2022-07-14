class aar:

    dict1 = {'brand': None, 'model': None,'year' : None}

    @classmethod
    def set_brand(cls, brand):
        cls.dict1.update({'brand': brand})
        return cls
        
    @classmethod
    def set_model(cls, model):
        cls.dict1.update({'model':model})
        return cls

    @classmethod
    def set_year(cls, year):
        cls.dict1.update({'year': year})
        return cls

    import pdb; pdb.set_trace()
    @classmethod
    def make(cls):
        print(cls.dict1.values())


# car.set_brand('Maruti')
# car.set_model('baleno')
# car.set_year('2022')
# car.make()
# car.set_brand('avc').set_model('abc').set_year('22').make()