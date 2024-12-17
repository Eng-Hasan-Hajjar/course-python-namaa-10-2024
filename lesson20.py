## condition
## A==B
## B!=N
## A< k
## D>m
## t>= h
##ex1
a=16
b=8
if a>b:
    print("ex1","true")

##ex2
a=6
b=8
if a>b:
    print("ex2","true a>b")
elif a == b:
    print("ex2","true a==b")


##ex3
a=6
b=8
if a>b:
    print("ex3","true a>b")
elif a < b:
    print("ex3","true a<b")
else:
    print("ex3","true a=b")
##ex4
a=6
b=8
if a>b:
    print("ex4","true a>b")
else:
    print("ex4","true a<=b")

##ex5
a=6
b=8
if a<b: print("ex5","true a<b")
   

##ex6
a=6
b=8
print("ex6","true a<b") if a<b else print("ex6","true a>=b")
   
##ex7
a=8
b=8
print("ex7","true a<b") if a<b else print("ex7","true a>b") if a>b else print("ex7","a=b")

##ex8
a=9
b=10
c=13
if a>b and a<c:
    print("ex8","true")

if a>b or a<c:
    print("ex8","true")

if not a<c:
    print("ex8","not true")


##ex9
d=14
if d>10:
    print("ex9","d>10")
    if d>20:
        print("ex9","d>20")
    else:
        print("ex9","d<20")

##ex10
a=b=20
if a > b:
    pass


#Hiba
math = 70
paython = 80
if math>60 and paython>70:
    print("exelent")
    if "":
        print("The student will be honored")
    
#هادي
# Input: Enter the age of a person
age = int(input("Enter your age: "))

# Check age group using if-elif-else
if age < 13:  
    print("You are a Child.")
elif 13 <= age <= 19:  
    print("You are a Teenager.")
else:  
    print("You are an Adult.")
        
#Asraa
salary = int(input("please enter your salary in USD: "))
base = 400
limit = 900
if salary <= base:
     print("your salay is low")
elif salary > base and salary < limit:
     print("your salay is medium")
else:
     print("your salay is high")
#Enes
word = "apple"
if len(word) > 3:
    print("The word has more than 3 letters")
    if len(word) > 5:
        print("The word has more than 5 letters")
    else:
        print("The word has 5 or fewer letters")



##loop
# for
# while
#ex11 
i=0
while i<6:
    print("ex11 while",i)
    i+=1   
#ex12 
i=0
while i<6:
    print("ex12 while",i)
    if i==3:
        break
    i+=1   
#ex13 
i=0
while i<6:
    i+=1   
    
    if i==3:
        continue
    print("ex13 while",i)
#ex14 
i=0
while i<6:
    print("ex14 while",i)
    i+=1   
else:
    print("else with while")   


##for loop
##ex15
types_car=["santafeh","hunda","toyta"]
for c in types_car:
    print(c)

x="salary"
for i in x:
    print(i)
##ex16
types_car=["santafeh","hunda","toyta"]
for c in types_car:

    print(c)
    if c ==  "hunda":
        break

##ex17
types_car=["santafeh","hunda","toyta"]
for c in types_car:
    if c ==  "hunda":
        continue
    print(c)

##ex18

for c in range(7):
    if c == 0:
        continue
    print(c)
##ex19

for c in range(2,22,2):
    print(c)                         
##ex20

for c in range(2,22,2):
    print(c)  
else : print("finish")                          

##ex20

for c in range(2,22,2):
  pass

##ex21
adj=["red","big"]
fruits=["apple","banana","3"]
for x in adj:
    for y in fruits:
        print(x,y)
##ex22
adj=[1,2]
fruits=[3,4,5]
for x in adj:
    for y in fruits:
        print(x,y)

