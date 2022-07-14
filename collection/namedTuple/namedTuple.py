from collections import namedtuple

# a = namedtuple('details', 'name, Idnumber, course, year')
# s = a('John', '4526', 'MCA', '2022')
# # print(s)

# aa = namedtuple('courses','Name, Details')
# ss = aa("computer Science", "Java Technology")
# # print(ss)

#creating namedTuple
emp = namedtuple('details','Name, dept, id, salary')

#assigning values
e1 = emp('John', 'developer', '4521', '25000')
e2 = emp('Jack', 'tester', '1265', '40000')
print(e1, e2)

#accessing the namedTuple
#by indexes
print("The name and salary of e1 is : "+ e1[0]+' and '+e1[3])

#by keys
print("the name and dept of e1 and e2 are : "+ e1.Name + " "+ e1.dept+ " and "+" "+ e2.Name +" "+ e2.dept)

#by getattr() method
print('The name and id of e1 is :'+ getattr(e1, 'Name') +' and '+ getattr(e1, 'id') )
