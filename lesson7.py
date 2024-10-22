##ahmed*1
#aziz*15
# Asraa*26
#heba*30
#Amal*1
#sara *1
##abdmalake*8
## hadi *3


##lesson7

## strings

print("Hello world")


name ="Aziz"
print(name)


lesson7="""
today lesson7
test string
more examples
"""

print(lesson7)



lesson72='''
today lesson7
test string
more examples
'''

print(lesson72)


## string === array
## x=[1 , 2 ,3]

name_student="Hiba"
print(name_student[0])
print(name_student[1])
print(name_student[2])
print(name_student[3])

## for 
for x in name_student:
    print(x)


for x in "Hadi - Abd":
    print(x)


## طول السلسلة

names="Hadi - Abd"
print("names",names,"length :",len(names))

len_of_names=len(names)
print(len_of_names ,type(len_of_names))

## التحقق من وجود كلمة معينة ضمن النص
statement="Mariam is studing"
if "Mariam" in statement:
    print("Mariam name is exit")
else :
    print("Mariam name not is exit")

if "Hiba" in statement:
    print("Hiba name is exit")
else :
    print("Hiba name not is exit")  

print("Mariam" in statement)       

print("Mariam" not in statement)     
print("Aziz" not in statement) 


## تقطيع السلاسل
statement="Mariam is studing"
subject=statement[0:6]
print(subject)

ax_verb=statement[7:9]
print(ax_verb)

main_verb=statement[10:17]
print(main_verb)


## from start of string
statement="Mariam is studing"

print(statement[:6])

## to end of string

print(statement[6:])

## الفهرسة السلبية

statement="Mariam is studing "

print(statement[-6:-1])

## التعديل على السلاسل

a= "Hello, World!"
print(a.upper())



a= "Hello, World!"
print(a.lower())

## ازالة المسافة الفارغة بنهاية السلسلة في حال وجودها
a= "Hello, World!      "
print(a.strip())


a= """Hello, World!    



  """
print(a)

## استبدال السلسلة
a= "Hello, World!"
print(a.replace("H","J"))
print(a.replace("w","J"))

print(a.replace("Hello","****"))


## تقسيم السلسلة
a= "Hello, World!"
print(a.split(","))


##دمج السلاسل
a="Hello "
b="world"
c=a + b

print(c)
