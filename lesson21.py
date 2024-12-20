##Asraa
students_grades = {
         "Asraa": {"Math": 85, "Science": 90, "English": 98},
         "Ali": {"Math": 72, "Science": 88, "English": 95},
         "Ahmed": {"Math": 90, "Science": 85, "English": 92}
     }

for student, subjects in students_grades.items():
    total = 0
    count = 0
    for subject, grade in subjects.items():
        total += grade
        count += 1
    average = total / count
    print(f"{student}'s average grade: {average:.2f}")


# طباعة جدول الضرب من 1 إلى 5
for i in range(1, 6):  # الحلقة الخارجية: تمثل الصفوف
    for j in range(1, 6):  # الحلقة الداخلية: تمثل الأعمدة
        print(f"{i * j:2}",end="     ")  # طباعة ناتج الضرب بتنسيق مرتب
    print()  # الانتقال إلى السطر التالي بعد انتهاء الحلقة الداخلية   

## functions
# انشاء تابع
#ex1

def my_func():
    print("nice deploma")

#استدعاء تابع
#ex2

def my_func():
    print("nice deploma")

my_func()

### parameters
##Arguments
##ex2
def my_func_name(fname):
    print(fname + " Brijawi")

my_func_name("Anas")   
my_func_name("Samer")   
my_func_name("Gamal")    

##ex3
def my_func_name_student(fname,lname):
    print(fname + lname)

my_func_name_student("Anas","Gamal")   
my_func_name_student("Samer","Anas")   
my_func_name_student("Gamal","Jan")    

##ex4

def my_func_prepar(*students):
    print("the name of student present :", students[2])


my_func_prepar("Anas","Asraa","Hiba","Hadi")

my_func_prepar("Anas","Asraa","Hiba","Hadi","Ahmad")


##ex5

def my_func_4(student2,student1,student3,student4):
    print("the name of student present :", student1)


#my_func_4(student1="Anas",student2="Asraa",student3="Hiba",student4="Hadi")
my_func_4("Anas","Asraa","Hiba","Hadi")

##ex6

def my_func_4(student2,student1,student3,student4):
    print("the name of student present :", student1)


my_func_4(student1="Anas",student2="Asraa",student3="Hiba",student4="Hadi")

  
##ex7

def my_func_4(**students):
    print("the name of student present :", students["student1"])


my_func_4(student1="Anas",student2="Asraa",student3="Hiba",student4="Hadi")

##ex8

def my_func_4(studentsname="Hasan"):
    print("the name of student present :", studentsname)


my_func_4()
  