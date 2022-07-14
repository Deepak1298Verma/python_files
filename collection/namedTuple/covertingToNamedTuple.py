from collections import namedtuple

#namedtuple creation
emp = namedtuple('details', 'Name, city')

#list
my_list = ['Jhonny','Delhi']

#converting list to namedTuple
e1 = emp._make(my_list)
print(e1)

my_dict = {'Name':'John', 'city':'kolkata'}

#converting dict to namedTuple
e2 = emp(**my_dict)
print(e2)

e_dict = e2._asdict()
print(e_dict)