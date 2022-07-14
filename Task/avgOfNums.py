from odoo import models, fields

class TestModel(models.Model):
    __name = 'test.model'
    name = fields.Char(string='Name', Required = True)
    dob = fields.date(string = 'dob', Required=True, help="Date of birth")
    
ob1 = TestModel()
a = ob1.name('Deepak')
aa = ob1.dob('21/04/2022')
print(a)
print(aa)