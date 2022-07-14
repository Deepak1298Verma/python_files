#print marksheet

class marksheet:

        #list will be updated based on inputs
        theory_marks = []
        pract_marks = []
        total = []
        grand_total = 0

        #list of subject and subject codes
        subject = ['english', 'hindi', 'science', 'computer', 'social']
        sub_code = ['M-01','M-02', 'M-03', 'M-04', 'M-05']

        # User Inputs

        def __init__(self):

            self.school_name = input("Enter your school name --")
            self.name = input("Enter your name -- ")
            self.session = input("Enter the session -- ")
            self.age = input("Enter the age -- ")
            self.f_name = input("Enter father's name -- ")
            self.roll_no = input("Enter roll_no of student -- ")
            print("Marking will be done out of 100 ")

            self.marks = int(input("enter the marks"))

            
            
ob = marksheet()

def passFail(marks):
    '''check that candidate is pass or fail based on subject marks'''
    if marks >= 33:
        return("Pass")
    else:
        return("Fail")


final_grade = []
def grade(marks):
    for i in range(len(marks)):
        if marks[i] >=90 and marks[i] <= 100:
            a = "A"
            final_grade.append(a)
        elif marks[i] >=80 and marks[i] < 90:
            a = "B"
            final_grade.append(a)
        elif marks[i] >=70 and marks[i] < 80:
            a = "C"
            final_grade.append(a)
        elif marks[i] >=60 and marks[i] < 70:
            a = "D"
            final_grade.append(a)
        elif marks[i] >= 33 and marks[i] < 60:
            a = "E"
            final_grade.append(a)
        else:
            a = "F"
            final_grade.append(a)

def remarks(value):
    count = 0
    for i in range(len(value)):
        if value[i] == "F":
            count+=1
    if count == 0:
        return "pass"
    elif count <= 2:
        return "supp"
    elif count > 2:
        return "Fail"


# ***********************************************************

#marking done out of
out_of = [100, 100, 100, 100, 100]

# ***********************************************************

#getting theory marks by user
for i in marksheet.subject:
    if i == 'science' or i == 'computer':
        a = int(input("Enter the theory marks out of 75 "+ i +" -- "))
        while True:
            if a <= 75 and a >= 0:
                marksheet.theory_marks.append(a)
                break
        a = int(input("Invalid Marks, Please Renter Again "))
    else:
        a = int(input("Enter theory marks out of 100 -- "+ i +" -- "))
        while True:
            if a <= 100 and a >= 0:
                marksheet.theory_marks.append(a)
                break
            a = int(input("Invalid Marks, Please Renter Again "))           


#getting practical marks by user only for science and computer
for i in marksheet.subject:
    if i == 'science' or i == 'computer':
        b = int(input("Enter the practical marks out of 25 --"+ i +" -- "))
        while True:
            if b <= 25 and b >= 0:
                marksheet.pract_marks.append(b)
                break
            b = int(input("Invalid Marks, Please Renter Again "))
    else:
        marksheet.pract_marks.append(0)
# print(pract_marks)

# ***********************************************************

#calculates the grand total marks(P + T) of candidate
for i, j in zip(marksheet.theory_marks,marksheet.pract_marks):
    marksheet.total.append(i+j)
# print(total)

for i in marksheet.total:
    marksheet.grand_total+=i
# print(grand_total)

# ***********************************************************

#calculate percent based on grand total
percent = (marksheet.grand_total*100) / 500
# print(percent)

print('*************************************** Result ***************************************')
print("\t\t\t\t\t ", marksheet.school_name)
print()
print(' Name ', marksheet.name, "\t\t\t\t\t\t Session ", marksheet.session)
print()
print(' Age ', marksheet.age, "\t\t\t\t\t\t Roll Number ", marksheet.roll_no)
print()
print(" Father's Name ", marksheet.f_name)
print()
print('SUBJECTS     SUB_CODE      THEORY      PRACT.     TOTAL MARKS      OUT OF       GRADE ')
print()


# ***********************************************************
grade(marksheet.total)

for a,b,c,d,e,f,g in zip(marksheet.subject, marksheet.sub_code, marksheet.theory_marks, marksheet.pract_marks, marksheet.total, out_of, final_grade):
    print(a,"         ", b,"         ", c,"         ", d,"         ", e,"         ", f,"         ", g)
    print()

# ***********************************************************

print('  Grand Total : ', marksheet.grand_total, "\t\t Percentage : ", format(percent,".2f"),"\t\t Remarks : ", remarks(final_grade))