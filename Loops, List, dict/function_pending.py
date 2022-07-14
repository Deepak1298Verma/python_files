def stud(name, age, year, course="MCA"):
    print(name, " ",course, " ", age, " ", year)

# stud("Deepak",18,2022) #//if parameter is not provided then by default will be use_default_colors
# stud("Deepak", "25", "2020") #//if paramenter is provided it will override it.
stud("Deepak", year="2020", course="BE", age=18)

# multiple args
def name(*stud):

    for i in stud:
        print("Hello", i)
name("Deepak", "Rohit","Kundan")
