### Asraa
first_set = {1, 2, 3, 4, 5, 6}
second_set = {4, 5, 6, 7, 8, 9}

print(first_set.difference(second_set))
print(first_set - second_set)

print(first_set.symmetric_difference(second_set))
print(first_set ^ second_set)


##ex1
first_set = {1, 2, 3, 4, 5, 6}
first_set.add(12)
print(first_set)



##Anas
# تعريف المجموعتين
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# حساب التقاطع
intersection = A.intersection(B)  # يمكن أيضًا استخدام A & B

# طباعة النتيجة
print("The intersection of sets A and B is:", intersection)

#حساب التقاطع:
intersection = A.intersection(B) 
intersection = A & B 
#يتم استخدام الدالة intersection() المدمجة في Python لحساب العناصر المشتركة بين المجموعتين.
#يمكن بدلاً من ذلك استخدام الرمز & كاختصار لحساب التقاطع.


###

# تعريف المجموعتين
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# حساب الاتحاد
union = A.union(B)  # يمكن أيضًا استخدام A | B

# طباعة النتيجة
print("The union of sets A and B is:", union)


#ex2
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.update(B)
print(A)
##ex3
A = {1, 2, 3, 4}
for x in A:
    print(x)

##ex4
names={"Anas","Asraa","Hiba","Hadi","Hasan"}
ages={20,20,26,66,43}

names_ages=names.union(ages)

print("Ex4",names_ages)

##ex5
names_students={"Anas","Asraa","Hiba","Hadi","Hasan"}
names_employee={"Anas2","Asraa2","Hiba2","Hadi","Hasan"}

#names=names_students & names_employee
names=names_students.intersection(names_employee) 
print("Ex5",names)

##ex6
names_students={"Anas","Asraa","Hiba","Hadi","Hasan"}
names_employee={"Anas2","Asraa2","Hiba2","Hadi","Hasan"}

#names=names_students & names_employee  --- home symoble
names_students.intersection_update(names_employee) 
print("Ex6",names_students)

##ex7
names_students={"Anas","Asraa","Hiba","Hadi","Hasan"}
names_employee={"Anas2","Asraa2","Hiba2","Hadi","Hasan"}

#names=names_students & names_employee  --- home symoble
names=names_students.symmetric_difference(names_employee) 
print("Ex7",names)


##ex8
names_students={"Anas","Asraa","Hiba","Hadi","Hasan"}
names_employee={"Anas2","Asraa2","Hiba2","Hadi","Hasan"}

#names=names_students & names_employee  --- home symoble
names_students.symmetric_difference_update(names_employee) 
print("Ex8",names_students)

## dict
#ex9
## key:value
details={
"name":"Ahmad",
"age":33
}
print("ex9",type(details))


##ex10

salary={"Ahmad":700 ,"Ali":500,"Gamal":800}
print("ex10","Ali",salary["Ali"])
print("ex10",type(salary))


##ex11

salary={"Ahmad":700 ,"Ali":500,"Ali":400,"Gamal":800}
print("ex11","Ali",salary["Ali"])
##ex12
salary={"Ahmad":700 ,"Ali":500,"Gamal":800}
print("ex12",len(salary))

##ex13
ide={"name":"salem" ,"age":500,"male":True,"region":["Turkey","Istanbul"]}
print("ex13",ide)

##ex14
ide = dict ({ "name":"salem" ,"age":500,"male":True })
print("ex14",ide)

##ex15
ide = dict ({ "name":"salem" ,"age":500,"male":True })
name= ide["name"]
print("ex15",name)


salary={"Ahmad":700 ,"Ali":500,"Ali":400,"Gamal":800}
print("ex15","Ali",salary)