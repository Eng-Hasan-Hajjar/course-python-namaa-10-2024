##ahmed*1
#aziz*3
# Asraa*6
#heba*7
#Amal*1
#sara *1
##abdmalake*1
## hadi *1


##lesson4

##ex1 
engIT="Asraa"

math='Hiba'

print("engIT type:",type(engIT))
print("math type:",type(math))

##ex2
IT="Asraa"
it="Hiba"
print("IT type:",type(IT),IT)
print("it type:",type(it),it)



##ex3
IT="Asraa"
it="Hiba"
IT="Hadi"
print("##ex3:IT type:",type(IT),IT)
print("##ex3:it type:",type(it),it)


## قواعد اسماء المتغيرات
#ex4
myvar="Hasan"

my_var="Ha_san"

_my_var="_Hasan"

myVar="Hasan"

MYVAR="HASAN"

myvar2="Hasan"

##EX5
## incorrect names of variables
##   5myvar="Hasan"
## my-var="Hasan"
## my var="Hasan"

myVarName="Hasan"

## الاسناد المتعدد للمتحولات
x,y,z="orange","red","black"

print(x)
print(y)
print(z)

## اسناد قيمة واحدة لثلاثة متحولات
x=y=z="orange"

print(x)
print(y)
print(z)

## القوائم
##lists
colors=["orange","red","black"]
x,y,z=colors

print(x)
print(y)
print(z)


## print
print(x,y,z) ## orange red black


print(x+y+z) ## orangeredblack

## link of two strings
v=x+y
print(v) ##orangered

v=x+" "+y
print(v)
#orange red

##ex8
fname="Hiba "
lname="Alhenesh"


fullname=fname+lname
print("fullname:",fullname)


##ex9
x=5
y=10
c=x+y
print("x=5,y=10,","x+y=",c)

##ex10
x=int(5)
y=str(10)
##c=x+y
print("x=5,y=10,","x+y=",x,y)

## global variables
print(engIT)

## functions
##  print(c2)  ## error

def myfunc():
    x2=5
    y2=10
    global c2
    c2=x2+y2
    print("func: x2=5,y2=10,","x2+y2=",c2)
## print(c2) ## error
myfunc()    

print(c2)


## أنواع البيانات
## int
## str
# float
## complex الأعداد العقدية الأعداد المركبة
## list
##tuple
## dict
## set
## bool
## non type


## ex10
x=2+3j
x=5j
x=2+0j
