class marksheet:

    def __init__(self):
        self.basic_inputs()

    def basic_inputs(self, school_name, name, age, session, father_name, roll_no):
        self.school_name = school_name
        self.name = name
        self.age = age
        self.session = session
        self.father_name = father_name
        self.roll_no = roll_no

    def subjects(self):
        self.subject = ['english', 'hindi', 'science', 'computer', 'social']
        self.sub_code = ['M-01','M-02', 'M-03', 'M-04', 'M-05']

    def grade(self, marks):
        final_grade = []
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

    def passFail(marks):
        '''check that candidate is pass or fail based on subject marks'''
        if marks >= 33:
            return("Pass")
        else:
            return("Fail")
    
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
        
    def gettheorymarks(self):
        self.subjects()
        theory_marks = []
        for i in self.subject:
            if i == 'science' or i == 'computer':
                a = int(input("Enter the theory marks out of 75 "+ i +" -- "))
                while True:
                    if a <= 75 and a >= 0:
                        theory_marks.append(a)
                        break
                    a = int(input("Invalid Marks, Please Renter Again "))
            else:
                a = int(input("Enter theory marks out of 100 -- "+ i +" -- "))
                while True:
                    if a <= 100 and a >= 0:
                        theory_marks.append(a)
                        break
                    a = int(input("Invalid Marks, Please Renter Again "))

