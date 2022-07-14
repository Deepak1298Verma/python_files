class marksheet:

    #list of subject and subject codes
    sub_code = [' M-01','       M-02', ' M-03', 'M-04', '       M-05']
    subject = ['English', 'Hindi', 'Science', 'Computer', 'Social']
    theory_marks = []
    pract_marks = []
    total = []
    grand_total = 0
    out_of = [100, 100, 100, 100, 100]
    grade = []

    def __init__(self):
        self.get_info()
        self.get_th_marks()
        self.get_pract_marks()
        self.get_total()
        self.show_info()
        self.cal_perc_and_remarks()
        
    def get_info(self):
        self.school_name = input("Enter the school name -- ")
        self.name = input("Enter the name -- ")
        self.age = int(input("Enter the age --"))
        self.std = input("Enter the class -- ")
        self.session = input("Enter the session -- ")
        self.rno = input("Enter the roll number -- ")

    def get_th_marks(self):
        for i in marksheet.subject:
            if i == 'Science' or i == 'Computer':
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

    def get_pract_marks(self):
        for i in marksheet.subject:
            if i == 'Science' or i == 'Computer':
                b = int(input("Enter the practical marks out of 25 --"+ i +" -- "))
                while True:
                    if b <= 25 and b >= 0:
                        marksheet.pract_marks.append(b)
                        break
                    b = int(input("Invalid Marks, Please Renter Again "))
            else:
                marksheet.pract_marks.append(0)

    def get_total(self):
        for i, j in zip(marksheet.theory_marks,marksheet.pract_marks):
            marksheet.total.append(i+j)
        self.cal_grade()
        for i in marksheet.total:
            marksheet.grand_total+=i
        self.cal_perc_and_remarks()

    def cal_grade(self):
            for i in range(len(marksheet.total)):
                if marksheet.total[i] >=90 and marksheet.total[i] <= 100:
                    a = "A"
                    marksheet.grade.append(a)
                elif marksheet.total[i] >=80 and marksheet.total[i] < 90:
                    a = "B"
                    marksheet.grade.append(a)
                elif marksheet.total[i] >=70 and marksheet.total[i] < 80:
                    a = "C"
                    marksheet.grade.append(a)
                elif marksheet.total[i] >=60 and marksheet.total[i] < 70:
                    a = "D"
                    marksheet.grade.append(a)
                elif marksheet.total[i] >= 33 and marksheet.total[i] < 60:
                    a = "E"
                    marksheet.grade.append(a)
                else:
                    a = "F"
                    marksheet.grade.append(a)

    def cal_perc_and_remarks(self):
        self.percent = (marksheet.grand_total*100) / 500
        count = 0
        for i in range(len(marksheet.grade)):
            if marksheet.grade[i] == "F":
                count+=1
                if count == 0:
                    return "PASS"
                elif count <= 2:
                    return "SUPPLEMENTRY"
                elif count > 2:
                    return "FAIL"

    def show_info(self):
        print('\n ********************************************** Result **************************************************')
        print("\t\t\t\t\t ", self.school_name, "\n")
        print(' Name ', self.name, "\t\t\t\t\t\t\t\t Session ", self.session, "\n")
        print(' Age ', self.age, "\t\t\t\t\t\t\t\t Roll Number ", self.rno, "\n")
        print(" Class ", self.std, "\n")
        print('SUBJECTS \t SUB_CODE \t THEORY \t PRACT. \t TOTAL MARKS \t OUT OF \t GRADE  \n')
        for a,b,c,d,e,f,g in zip(marksheet.subject, marksheet.sub_code, marksheet.theory_marks, marksheet.pract_marks, marksheet.total, marksheet.out_of, marksheet.grade):
            print(a,"\t", b,"\t\t",c,"\t\t",d,"\t\t",e,"\t\t",f,"\t\t",g,"\n")
        print('\n Grand Total : ', marksheet.grand_total, "\t\t Percentage : ", format(self.percent,".2f"),"\t\t Remarks : ", self.cal_perc_and_remarks())

A = marksheet()