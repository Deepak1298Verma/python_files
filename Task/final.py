#print marksheet

def passFail(marks):
    '''check that candidate is pass or fail based on subject marks'''
    if marks >= 33:
        return("Pass")
    else:
        return("Fail")

def grade(marks):
    '''checks the grade of the candidate based on subject marks'''
    for i in range(len(marks)):
        print(i)
        if marks[i] >=90 and marks[i] <= 100:
            print("A")
        elif marks[i] >=80 and marks[i] < 90:
            print("B")
        elif marks[i] >=70 and marks[i] < 80:
            print("C")
        elif marks[i] >=60 and marks[i] < 70:
            print("D")
        elif marks[i] < 60:
            print("E")

school_name = input("Enter your school name --")
name = input("Enter your name -- ")
session = input("Enter the session -- ")
age = input("Enter the age -- ")
f_name = input("Enter father's name -- ")
roll_no = input("Enter roll_no of student -- ")
print("Marking will be done out of 100 ")

#list of subject and subject codes
subject = ['english', 'hindi', 'science', 'computer', 'social']
sub_code = ['M-01','M-02', 'M-03', 'M-04', 'M-05']

# ***********************************************************

#list will be updated based on inputs
theory_marks = []
pract_marks = []
total = []
grand_total = 0

# ***********************************************************

#marking done out of
out_of = [100, 100, 100, 100, 100]

#getting theory marks by user
for i in subject:
    if i == 'science' or i == 'computer':
        a = int(input("Enter the theory marks out of 75 "+ i))
        theory_marks.append(a)
    else:
        a = int(input("Enter theory marks out of 100 "+ i))
        theory_marks.append(a)
print(theory_marks)

# ***********************************************************

#getting practical marks by user only for science and computer
for i in subject:
    if i == 'science' or i == 'computer':
        b = int(input("Enter the practical marks out of 25 "+ i))
        pract_marks.append(b)
    else:
        pract_marks.append(0)
print(pract_marks)

#calculates the grand total marks(P + T) of candidate
for i, j in zip(theory_marks,pract_marks):
    total.append(i+j)
print(total)

for i in total:
    grand_total+=i
print(grand_total)

# ***********************************************************

#calculate percent based on grand total
percent = (grand_total*100) / 500
print(percent)


print('*************************************** Result ***************************************')
print("\t\t\t school_name")
print()
print(' Name ', name, "\t\t\t\t Session ", session)
print()
print(' Age ', age, "\t\t\t\t Roll Number ", roll_no)
print()
print(" Father's Name ", f_name)
print()
print('SUBJECTS     SUB_CODE      THEORY      PRACT.     TOTAL MARKS      OUT OF       GRADE')
print()

for a,b,c,d,e,f,g in zip(subject,sub_code,theory_marks, pract_marks, total, out_of, grade(total)):
    print(a,"        ", b,"        ", c,"        ", d,"        ", e,"        ", f, g)
    print()


print('  Grand Total : ', grand_total, "\t\t\t Percentage : ", percent)
print(grade(total))