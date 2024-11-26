

#anas

# رجع العنصر الأكبر المثال tuple (إذا كانت جميع العناصر قابلة للمقارنة).
my_tuple = (1, 2, 3, 4)
print(max(my_tuple))  #4
#min رجع العنصر الاصغر المثال 
my_tuple = (1, 2, 3, 4)
print(min(my_tuple))  # 1
#الوصف: تُستخدم لحساب عدد المرات التي يظهر فيها عنصر معين داخل الـ tuple.
my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))  # 3
print(my_tuple.count(5))  # 0

##Asraa
my_tuple = (10, 20, 30, 45, 56)
total_sum = sum(my_tuple)
print(total_sum)

my_tuple = (49, 170, 726, 99, 111)
maximum = max(my_tuple)
print(maximum)

my_tuple = (47, 17, 29, 19, 100)
minimum = min(my_tuple)
print(minimum)

my_tuple = (10, 20, 30, 20, 40, 50)
index = my_tuple.index(20, 2, 5)
print(index)




#ex1
## تفريغ الصف
fruits=("apple","orange")
(yellow,orange1)=fruits

print("Ex1",fruits)
print("Ex1",yellow)
print("Ex1",orange1)



#ex2
## تفريغ الصف
fruits=("apple","orange","banana","watermelon","peach")
(yellow,orange,*colors)=fruits

print("Ex2",fruits)
print("Ex2",yellow)
print("Ex2",orange)
print("Ex2",colors)


#ex3
## تفريغ الصف
fruits=("apple","peach","banana","watermelon","orange")
(yellow,*colors,orange)=fruits

print("Ex3",fruits)
print("Ex3",yellow)
print("Ex3",colors)
print("Ex3",orange)


#ex4
## تفريغ الصف
titles=("functions","2 quadratics","logarithms","Exponention")
(d1,d2,*d3)=titles

print("Ex4",titles)
print("Ex4",d1)
print("Ex4",d2)
print("Ex4",d3)



#ex5
## تفريغ الصف
titles=("functions","logarithms","Exponention","2 quadratics")
(d1,*d2,d3)=titles

print("Ex5",titles)
print("Ex5",d1)
print("Ex5",d2)
print("Ex5",d3)


##ex6 
titles=("functions","logarithms","Exponention","2 quadratics")
for i in range(len(titles)):
    print(titles[i])

for x in titles:
    print(x)


##Asraa
my_tuple = ("apple", "banana", "cherry", "peach")
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

##Anas
cars = ("bmw", "mercedes", "audi", "volvo")

# متغير لتمثيل الفهرس
index = 0
# استخدام حلقة while للطباعة
while index < len(cars):
    print(cars[index])
    index += 1 

##hiba
titles=("functions","logarithms","Exponention","2 quadratics")
i=0
while i < len(titles):
    print(titles[i])
    i+=1   

#ex7 
# 
# link between
# tow tuples
# 
titles1=("functions","2 quadratics")    
titles2=("logarithms","Exponention")
titles=titles1 + titles2
print(titles)


##ex8
tuple1=(1,2,3)
dtuple=tuple1*2
print(dtuple)

###المجموعات
##set
#Ex9
subjects={"math","programming","IT","electical"}
print(subjects)



subjects=set(("math","programming","IT","electical"))
print(subjects)

#ex10
subjects={"math","programming","IT","electical","math","programming","IT","electical"}
print(subjects)
#ex11
subjects={"math","programming","IT",True,0 ,False, 2}
print(subjects)

##ex12
subjects={"math","programming","IT"}
print(len(subjects))

##ex13
subjects={"math","programming","IT"}
numbers={1,2,3}
bool_hh={True,True}
defren={"math","programming","IT",True,0 ,False, 2}

##ex14
subjects={"math","programming","IT"}
for x in subjects:
    print(x)
print(len(subjects))


##ex15
subjects={"math","programming","IT"}
print("IT" in subjects)

###ex16
subjects={"math","programming","IT"}
subjects.add("elct")
print(subjects)

##ex17
subjects={"math","programming","IT"}
subjects2={"math2","programming2","IT2"}
subjects.update(subjects2)
print(subjects)


##ex18
subjects={"math","programming","IT"}
subjects2=["math2","programming2","IT2"]
subjects.update(subjects2)
print(subjects)

##ex19
subjects={"math","programming","IT"}

subjects.remove("IT")
print(subjects)

##ex20
subjects={"math","programming","IT"}

subjects.discard("IT2")
print(subjects)

##ex21
subjects={"math","programming","IT"}

x= subjects.pop()
print(x)
print(subjects)

##ex22
subjects={"math","programming","IT"}

subjects.clear()


#del subjects
print(subjects)


## +  -