
##lesson 24
##lambda
## lambda arguments : expression
##ex1
x=lambda a : a + 1

print(x(3))

##ex2
x=lambda a ,b : a * b

print(x(3,4))

##ex3
x=lambda a ,b,c : a + b + c 

print(x(3,4,3))


##ex4
def my_func(n):
    return lambda a:a*n
x=my_func(2) 

print(x(3))
print(x(4))


##ex5
def my_func(n):
    return lambda a:a*n
x=my_func(3) 

print(x(3))
print(x(4))


##ex6
sum = lambda a,b:a+b
print(sum(5,3))


##ex7
numbers=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda x:x%2==0,numbers))
print(evens)


##ex8
words = ["apple", "banana", "kiwi", "watermelon", "cherry"]

# ترتيب الكلمات حسب طولها باستخدام lambda
sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)


##ex9
students=[
    {'name':'Hasan','age':50},
        {'name':'Hyma','age':120},
            {'name':'Hashem','age':90},
              {'name':'Huda','age':75}
]
sorted_student=sorted(students,key= lambda x:x['age'])
print(sorted_student)

##المصفوفات
"""array[5] x = {1,2,3,4,5}
x[2]
"""
## import NumPy
cars=["Ford", "bmw","Volvo"]
print(cars[0])
print(type(cars))

###oop
## create class
class My_Class:
    x=5
##create object
obj1=My_Class()
print(obj1.x)


class Car:
    num_doors = 4



car1=Car()
car2=Car()


print(car1.num_doors)

print(car2.num_doors)




class Car:
    def __init__(self,doors):
      self.num_doors = doors



car1=Car(4)
car2=Car(2)


print(car1.num_doors)

print(car2.num_doors)





##مثال اخر
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


person1=Person("Hadi","22")
person2=Person("Hadi2","23")
print(person1.name)      
print(person1.age) 
print(person1)
print(person2.name)      
print(person2.age)  





class Person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"name is : {self.name} and age is: {self.age}"

person1=Person2("Hadi","22")
person2=Person2("Hadi2","23")
print(person1.name)      
print(person1.age)    
print(person1) 
print(person2.name)      
print(person2.age)  

