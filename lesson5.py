##ahmed*1
#aziz*12
# Asraa*14
#heba*20
#Amal*1
#sara *1
##abdmalake*2
## hadi *1


##lesson5

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

##ex1 
#int 
y=5
print(type(y))

##ex2
#string
name="aziz"
print(name,type(name))

#ex3
#float
x=3.2
print(x)
print(type(x))

##ex4
##complex
x=5+3j
print(x,type(x))

#ex5
h=-6j
k=0+8j
o=2+0j
print(type(h),type(k),type(o))

##ex6
##list
L=["Hiba","Ali", "mariam","Ahmad"]
print(L)
print(type(L))
# {}  [] ()

#ex7
laptops=["hp","asus","msi","mac","lenevo"]
print(laptops,type(laptops))

#ex8
#tuple
laptops=("hp","asus","msi","mac","lenevo")
print(laptops,type(laptops))
#ex9
#set
laptops={"hp","asus","msi","mac","lenevo"}
print(laptops,type(laptops))
#ex10
#dict
## key:value
laptops={"hp":100,"asus":125,"msi":250,"mac":600,"lenevo":300}
print(laptops,type(laptops))


#ex11
#bool
## True - False
issuny=True
checkin=False
print("issuny= ",issuny,type(issuny),"checkin= ",checkin,type(checkin))

#ex12
#nontype
b=None
print(b,type(b))

## ex13
idname=str(5689742)
print(idname,type(idname))

##ex14
ma=complex(2)
print(ma,type(ma))

#ex15
avg1=float(83.6)
avg2=float(90)
print(avg1,type(avg1),avg2,type(avg2))
## ex16
family=list(("father","mother","sons"))
family2=["father","mother","sons"]

print(family,type(family),family2,type(family2))

##ex17
subjects=tuple(("math","lang","history"))
print(subjects,type(subjects))
subjects=("math","lang","history")
print(subjects,type(subjects))


##hiba
#homework1
print("#homework1- Hiba")

X=float(input("please enter the first number is :"))
Z=str(input("please enter the  process  is: "))
Y=float(input("please enter the second number is :"))

if Z=="+" :
    print(X+Y)
elif  Z=="-" :
  print(X-Y)
elif Z=="*":
  print(X*Y)
elif Z=="/":
  print(X/Y)
else:
  print("wrong: please choose (+ - * /)")


##Asraa
#homework1
print("#homework1- Asraa ")

x = input("Enter x value: ")
y = input("Enter y value: ")
print(type(x))
sum = float(x) + float(y)
print("The summation is ", sum)



##Aziz
#homework1
# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main program
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print(add(num1, num2))
    elif operator == '-':
        print(subtract(num1, num2))
    elif operator == '*':
        print(multiply(num1, num2))
    elif operator == '/':
        print(divide(num1, num2))
    else:
        print("Invalid operator")

# Run the calculator
calculator()
