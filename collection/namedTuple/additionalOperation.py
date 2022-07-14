from collections import namedtuple
from tokenize import Name

emp = namedtuple('details','Name, dept, id, salary')

#assigning values
e1 = emp('John', 'developer', '4521', '25000')
e2 = emp('Jack', 'tester', '1265', '40000')

#replace method
# e1 = e1._replace(salary, '20000')
# print(e1)

#getting fields
e2 = print(str(e2._fields))