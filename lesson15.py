#lesson 15
##Asraa
##sum
my_list = [10, 20, 30, 45, 56]
total_sum = sum(my_list)
print("sum element of list",total_sum)
##max
my_list = [49, 170, 726, 99, 111]
maximum = max(my_list)
print("max element of list",maximum)
##min
my_list = [47, 17, 29, 19, 100]
minimum = min(my_list)
print("min element of list",minimum)
##index
my_list = [10, 20, 30, 20, 40, 50]
index = my_list.index(20, 2, 5)
print("index element of list",index)
##copy
original_list = [10, 20, 30]
copied_list = original_list.copy()
print("copy element of list",copied_list)

"""
##Anas
# round() تُستخدم لتقريب الأرقام العشرية إلى عدد محدد من المنازل العشرية.

number = float(input("enter float number \n")) #يعرض رسالة للمستخدم تطلب إدخال رقم عشري
number2 = int(input("enter round step \n")) #يعرض رسالة للمستخدم تطلب إدخال عدد صحيح يحدد عدد المنازل العشرية للتقريب.
RN = float(round(number , number2)) #تستخدم الدالة round() لتقريب الرقم الموجود في number إلى عدد المنازل العشرية المحدد في number2.
print(RN)  #يتم طباعة القيمة النهائية المخزنة في المتغير RN (الرقم بعد التقريب) على الشاشة.

"""
## tuples
##ex1 
myTuple=("drinks","food","sweets")
print(myTuple)
##ex2
myTuple=tuple(("drinks","food","sweets"))
print(myTuple)
##ex3
myTuple=tuple(("drinks","food","sweets","drinks","food","sweets",))
print(myTuple)

##ex4
myTuple=tuple(("drinks","food","sweets","drinks","food","sweets",))
print(len(myTuple))

##ex5
myTuple=("drinks")
print(myTuple)
print(type(myTuple))

##ex6
myTuple=tuple(("drinks"))
print(myTuple)
print(type(myTuple))

##ex7
myTuple=tuple(("drinks",))
print(myTuple)
print(type(myTuple))

##ex8
myTuple=("drinks",)
print(myTuple)
print(type(myTuple))

##ex9
myTuple=("drinks","food","sweets")
myTuple2=(8 , 12 , 13 , 9)
myTuple3=(True , False)
myTuple4=("drinks",3,True)
print(myTuple)
print(type(myTuple))
print(myTuple2)
print(type(myTuple2))
print(myTuple3)
print(type(myTuple3))
print(myTuple4)
print(type(myTuple4))

##ex10
myTuplelist=["drinks"]
print(myTuplelist)
print(type(myTuplelist))


##ex11
myTuple=("drinks","food","sweets")
print(myTuple[1])
print(type(myTuple))



##ex12
myTuple=("drinks","food","sweets")
print(myTuple[-1])
print(type(myTuple))




##ex13
myTuple=("drinks","food","sweets")
print(myTuple[0:2])
print(type(myTuple))



##ex14
myTuple=("drinks","food","sweets")
print(myTuple[0:len(myTuple)])
print(type(myTuple))


##ex15
myTuple=("drinks","food","sweets")
print(myTuple[0:])
print(type(myTuple))



##ex16
myTuple=("drinks","food","sweets")
print(myTuple[:2])
print(type(myTuple))



##ex17
myTuple=("drinks","food","sweets")
print(myTuple[-2:-1])
print(type(myTuple))


myTuple = ("drinks", "food", "sweets")

if "sweet" in myTuple:
    print("Yes, 'sweet' is in myTuple")
else:
    print("No, 'sweet' is not in myTuple")

tuple_rest = ("drinks", "food", "sweets")

if "food" in tuple_rest:
    print("The word 'food' exists in the tuple.")
else:
    print("The word 'food' is not in the tuple.")


for i in range(len(myTuple)):
    if myTuple[i] == "sweets":
        print("sweets is found")
    else:
        print("sweets not found")



my_tuple = (1, 2, 3, 4, 5)

if 3 in my_tuple:
    print("3 exists in the tuple")
else:
    print("3 does not exist in the tuple")


## update for tuple
##ex18
myTuple=("drinks","food","sweets")
myTuple=("drinks","food","sweets2")
print(myTuple)

##ex19
myTuple=("drinks","food","sweets")
mylist=list(myTuple)
print(myTuple)
mylist[2]="sweets2"

print(mylist)


myTuple=tuple(mylist)

print(myTuple)

##ex20
myTuple=("drinks","food","sweets")
mylist=list(myTuple)
print(myTuple)
mylist.append("sweets2")
print(mylist)
myTuple=tuple(mylist)
print(myTuple)

##ex21
myTuple=("drinks","food","sweets")
mytuple2=("sweets2",)
myTuple+=mytuple2
print(myTuple)

##ex22
myTuple=("drinks","food","sweets","sweets2")
mylist=list(myTuple)
print(myTuple)
mylist.remove("sweets2")
print(mylist)
myTuple=tuple(mylist)
print(myTuple)

##ex23
myTuple=("drinks","food","sweets","sweets2")
del myTuple

##ex24
myTuple=("drinks","food","sweets","sweets2")
mylist=list(myTuple)
print(myTuple)
mylist.clear()
print(mylist)
myTuple=tuple(mylist)
print(myTuple)


### اسمك

## منصب الوظيفة 
## حساب الغيت هب 
## حساب اللينكد اين
### رقمك

##################
# الملخص 
# الخبرات
## التعليم + شهادات
## المهارات
## اللغات