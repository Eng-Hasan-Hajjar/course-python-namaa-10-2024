##ahmed*1
#aziz*12
# Asraa*21
#heba*24
#Amal*1
#sara *1
##abdmalake*6
## hadi *1


##lesson6
## Assraa
"""
def area_perimeter_of_rectangle():
    l = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    your_choice = input("Enter what do you want to calculate ? area R or perimeter P : ")
    if your_choice == "R":
       area = l * w
       return area
    if your_choice == "P":
       perimeter = 2 * (l + w)
       return perimeter

    else:
        print("wrong choice")


def area_perimeter_of_circle():
    r = float(input("Enter the radius of the circle: "))
    pi = 3.14 # Approximate value of pi
    your_choice = input("Enter what do you want to calculate ? area R or perimeter P : ")
    if your_choice == "R":
       area = pi * r ** 2
       return area
    if your_choice == "P":
       perimeter = 2 * pi * r
       return perimeter

    else:
        print("wrong choice")


def area_perimeter_of_square():
    length = float(input("Enter the length of the square: "))
    your_choice = input("Enter what do you want to calculate ? area R or perimeter P : ")
    if your_choice == "R":
       area = length ** 2
       return area
    if your_choice == "P":
       perimeter = 4 * length
       return perimeter

    else:
      print("wrong choice")


def area_perimeter_of_right_triangle():
    c1 = float(input("Enter the c1 of the right triangle: "))
    c2 = float(input("Enter the c2 of the right triangle: "))
    h = (c1 ** 2 + c2 ** 2) ** 0.5
    your_choice = input("Enter what do you want to calculate ? area R or perimeter P : ")
    if your_choice == "R":
       area = 0.5 * c1 * c2
       return area
    if your_choice == "P":
       perimeter = c1 + c2 + h
       return perimeter
    else:
        print("wrong choice")


print("Choose the shape you want to calculate the area and perimeter of it: ")
print("1. Rectangle\n2. Circle\n3. Square\n4. Right Triangle")


your_selection = int(input("Enter the number corresponding to the shape: "))

if your_selection == 1:
        calculation = area_perimeter_of_rectangle()
        print("The result is : ", calculation)
elif your_selection == 2:
        calculation = area_perimeter_of_circle()
        print("The result is : ", calculation)
elif your_selection == 3:
        calculation = area_perimeter_of_square()
        print("The result is : ", calculation)
elif your_selection == 4:
        calculation = area_perimeter_of_right_triangle()
        print("The result is : ", calculation)
else:
        print("Invalid choice. Please choose a valid shape.")
"""
"""
##Hiba
print("✓✓Find the area and circumference of the circle ...  ")
r=float(input("please  Enter the radius of the circle : " ))
pi=3.14
s=pi*r*r ## r**2
l=2*pi*r
print(" the area is : ", s, )
print("the circumference " , l )
print("✓✓find the area of right teiangle... ")
a=float(input("the first side is : "))
b=float(input("the Height is : " ))
s2= 1/2*a*b
print(" The area of ​​a right triangle is :  ", s2)
print("✓✓find the area of the square ....")
d=float(input("the first side is : "))
c=float(input("the second side is : " ))
s3=d*c
print (" The area of ​​a  square is :  ", s3)
print("✓✓find the area of the rectangular... ")
f=float(input("the first side is : " ))
n=float(input("the second side is : " ))
s4=f*n
print(" The area of a rectangular is :" ,s4)        
"""
"""
#abd malek
import math

def main():
    print("1. Circle  2. Triangle  3. Rectangle  4. Square")
    choice = input("Choose (1-4): ")

    if choice == '1':
        r = float(input("Radius: "))
        print(f"Area: {math.pi * r**2:.2f}, Perimeter: {2 * math.pi * r:.2f}")
    elif choice == '2':
        b = float(input("Base: "))
        h = float(input("Height: "))
        print(f"Area: {0.5 * b * h:.2f}, Perimeter: {b + h + math.hypot(b, h):.2f}")
    elif choice == '3':
        l = float(input("Length: "))
        w = float(input("Width: "))
        print(f"Area: {l * w:.2f}, Perimeter: {2 * (l + w):.2f}")
    elif choice == '4':
        s = float(input("Side: "))
        print(f"Area: {s**2:.2f}, Perimeter: {4 * s:.2f}")
    else:
        print("Invalid choice!")


main()

"""
"""
import math
x=math.sqrt(4)
print(x)
x=dir(math)
print(x)
"""

##الأعداد في البايثون

##ex1
x=5
n=555
g=12345678912346
v=-3332
print(type(x))
print(type(n))
print(type(g))
print(type(v))

##ex2
x=5.3
n=555.0
g=12345678912346.3
v=-3332.56
print(type(x))
print(type(n))
print(type(g))
print(type(v))


k=35e3
print(k,type(k))


k2=35E5
print(k2,type(k2))

k3=-35E100
print(k3,type(k3))


##ex3
g1=5+7j
g2=5+0j
g3=5j
g4=-9j

print(g1,type(g1))
print(g2,type(g2))
print(g3,type(g3))
print(g4,type(g4))

## casting
x=1    ##int
y=2.8    ## flaot

z=2j    ##complex
## convert from int to float
a=float(x)

print(a,type(a)) ##1.0

## convert from float to int
b=int(y)

print(b,type(b)) ##2

c=complex(x)
print(c,type(c))

#p=int(z)
#print(p,type(p)) ##error

##random number
import random
print(random.randrange(1,10))

print(dir(random))

##ex5
x=int(1)
y=int(2.8)
z=int("3")

print(x,type(x))
print(y,type(y))
print(z,type(z))


## z=int("3.5")

z=float("3.5")
print(z,type(z))
z=float("3")
print(z,type(z))


##ex6
x=str("hasan")
y=str(3)
z=str(3.5)
print(x,type(x))
print(y,type(y))
print(z,type(z))



import math 
from turtle import*
def hearta(k):
     return 15*math.sin(k)**3
def heartb(k):
      return 12*math.cos(k)-5*\
      math.cos(2*k)-2*\
      math.cos(3*k)-\
      math.cos(4*k)
speed(1000)
bgcolor("black")
for i in range(6000):
      goto(hearta(i)*20,heartb(i)*20)
      for j in range(5):
            color("blue")
done()