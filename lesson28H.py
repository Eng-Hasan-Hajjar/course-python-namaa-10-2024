#class (الفئة):
#هو قالب (template) أو مخطط (blueprint) لإنشاء كائنات (objects).

#object (الكائن):
#يتم إنشاؤه بناءً على القالب الذي يحدده  الكلاس class.


class Car: 
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def print_details(self):
        print(f"car details  year:{self.year} model:{self.model} brand:{self.brand}")

my_car=Car(2022,"Model M4","BMW")

my_car.print_details()

#عرف عن init
#عند إنشاء كائن باستخدام Person("Ali", 25):
#يتم استدعاء _init_ تلقائيًا.
#يتم تعيين "Ali" إلى الخاصية name و 25 إلى الخاصية age.


class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age   
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Ali", 25)
person2 = Person("Sara", 30)

person1.display_details() 
person2.display_details()


class Car:
    def __init__(self,make,model,color,year):

        self.make=make
        self.model=model
        self.color=color
        self.year=year

    def info_display(self):
        print(f"\ncar details")
        print(f"make: {self.make}")
        print(f"model:{self.model}")
        print(f"color:{self.color}")
        print(f"year: {self.year}")

my_car2 = Car(make="toyota" , model="corolla" , color="white" , year="2023\n") 
my_car2.info_display()



class BankAccount:
    def __init__(self,number_account,balance=0.0):
        self.number_account=number_account
        self.balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"deposit: {amount:.2f} new balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self , amount):
        if amount > 0:
            if amount <= self.balance:
               self.balance -= amount
               print(f"withdraw: {amount:.2f} new balance: {self.balance:.2f}")
            else:
                print("Insufficient funds")
        else:
            print("Withdraw amount must be positive.")

account = BankAccount(number_account=123456, balance=1000.0)


account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.deposit(-200)
account.withdraw(-300)


class Animal:
    def speak(self):
        print("this is an animal")

class Dog(Animal):
    def speak(self):
        print("woof woof ")

animal = Animal()
animal.speak()

dog = Dog()
dog.speak()



class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def disiplay_details(self):
        print(f"name: {self.name} , salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary,depertmant):
        super().__init__(name , salary)
        self.depertmant=depertmant

    def disiplay_details(self):
        super().disiplay_details()
        print(f"depertmant:{self.depertmant}")

employee1 = Employee("anas" , 5000)
employee1.disiplay_details()

print()

maanger1 = Manager("sara" , 4500 , "IT")
maanger1.disiplay_details()



# 1. Classes
# Class: is a scheme for creating objects. Classes define the structure and behavior of the objects,
# including the properties (attributes) and actions (methods) that the objects can have.
#Object: in Python is a thing created from a class. It represents a specific example of that class and
# has its own data (called attributes) and actions (called methods).

#1.1
class Car:
    def __init__(self, brand, model, year):

        self.brand = brand
        self.model = model
        self.year = year

    def display_car(self):
        # A method to print a greeting
        print(f"The car information is: the brand {self.brand} , the model {self.model} , and the year {self.year} ")


car1 = Car("Honda", "new" , 2024)

# Call the greet method on the object
car1.display_car()


# 1.2
#The __init__ method in Python is a special method used to initialize an object when it is created.
# It acts as the constructor of the class and is automatically called when you create a
# new instance of the class.
class Person:
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Creating objects of the Person class
person1 = Person("Ahmed", 25)
person2 = Person("Asraa", 30)

#1.3
class BankAccount:
    def __init__(self, account_number, balance=0):
        # Initialize account attributes
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # Add the amount to the balance
        if amount > 0:
            self.balance += amount
            print(f" The New balance: ${self.balance}")
        else:
            print("you should enter positive amount")

    def withdraw(self, amount):
        # Subtract the amount from the balance
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"The New balance: ${self.balance}")
            else:
                print("You dont have enough balance.")
        else:
            print("you should input positive amount.")

# Create a BankAccount object
customer = BankAccount(account_number="123456789", balance=500)

# Call deposit and withdraw methods
customer.deposit(200)  # Deposit $200
customer.withdraw(100)  # Withdraw $100
customer.withdraw(700)  # Attempt to withdraw more than the balance

#2.Inheritance
#Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows one class
# (called the child class or subclass) to acquire the properties and behaviors of another class
# (called the parent class or superclass). the advantages of it:
#Code Reusability: It promotes the reuse of existing code by enabling a new class to inherit the
# functionality of an existing class, reducing redundancy.
#Hierarchical Relationships: It establishes a hierarchical relationship between classes.
#Extensibility: The child class can add new properties and methods or override existing ones to
# customize or extend functionality.


class Animal:
    def speak(self):
        print("This is an animal")

class Dog(Animal):
    def speak(self):
        print("Wolf wolf")

animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

#2.1

class Employee:
    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def display_info(self):
        # A method to print a greeting
        print(f"The employee information is: the name {self.name} , and the salary is  {self.salary} ")


class Manager(Employee):
    def __init__(self, name, salary, department):
       super().__init__(name,salary)
       self.department = department

    def display_info(self):
        # A method to print a greeting
        print(f"The employee information is: the name {self.name} , the salary is  {self.salary} , and the department is {self.department}  ")


employee1 = Employee("Ahmed Ali", 1000)
manager1 = Manager("Asraa Ali", 900 ,"IT Department")

employee1.display_info()
manager1.display_info()

#2.2

class Shape:
    def area(self):
        print("No area")


class Rectangular(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        area = self.width * self.length
        print(f"The area of the rectangle is: {area}")

shape1 = Shape()
shape1.area()

rect1 = Rectangular(5, 10)
rect1.area()

#Polymorphism means "many shapes" — it allows objects of different types to be treated the same way,
# but they can behave differently when you call a method on them.
#In simple terms: Polymorphism lets different classes have methods with the same name, but they can do
# different things.

#1
class Cat:
    def speak(self):
        print("Meow")

class Bird:
    def speak(self):
        print("Chirp")

def animal_speak(animal):
    animal.speak()

cat = Cat()
bird = Bird()

animal_speak(cat)   # Output: Meow
animal_speak(bird)  # Output: Chirp

#2.1

class Vehicle:
    def fuel(self):
        print("Vehicle uses fuel")

class Car(Vehicle):
    def fuel(self):
        print("This car do not need fuel")

class Bike(Vehicle):
    def fuel(self):
        print("This bike uses fuel")

vehicle1 = Vehicle()
vehicle1.fuel()

car1= Car()
car1.fuel()
bike1= Bike()
bike1.fuel()

#2.2

class Cat:
    def speak(self):
        print("Meow Meoo")

class Dog:
    def speak(self):
        print("Wooh wooh")

class Bird:
    def speak(self):
        print("Chirp Chirp")

cat1=Cat()
dog1=Dog()
bird1=Bird()

for x in (cat1 ,dog1 ,bird1 ):
    x.speak()

#another homework

class Car:
    def _init_(self, year, model, brand):
        self.year = year
        self.model = model
        self.brand = brand

my_car = Car(2025, "Model S", "Tesla")
print(f"Car Details: Brand: {my_car.brand}, Model: {my_car.model}, Year: {my_car.year}")


class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(f"Name: {person1.name}, Age: {person1.age}")

class Animal:
    def _init_(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

print(dog.make_sound())
print(cat.make_sound())


class BankAccount:
    def _init_(self, balance, number_account):
        self.balance = balance
        self.number_account = number_account

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"

account = BankAccount(1000, "123456789")
print(account.deposit(500))
print(account.withdraw(300))
print(account.withdraw(1500))


class Car:
    def _init_(self, year, model, brand):
        self.year = year
        self.model = model
        self.brand = brand

    def info_display(self):
        return f"Car Details: Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

my_car = Car(2025, "Model S", "Tesla")
print(my_car.info_display())


class Animal:
    def _init_(self, name):
        self.name = name

    def speak(self):
        print(f"This is an animal named {self.name}")

class Dog(Animal):
    def _init_(self, name, breed):
        super()._init(name)  # استدعاء دالة __init_ في الصنف الأساسي
        self.breed = breed

    def speak(self):
        print(f"Woof! Woof! This is a {self.breed} dog named {self.name}")

# إنشاء كائنات واختبار الدوال
animal = Animal("Lion")
dog = Dog("Buddy", "Golden Retriever")

animal.speak()  # يطبع: This is an animal named Lion
dog.speak()     # يطبع: Woof! Woof! This is a Golden Retriever dog named Buddy

class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def _init_(self, name, salary, department):
        super()._init(name, salary)  # استدعاء دالة __init_ في الصنف الأساسي
        self.department = department

# إنشاء كائنات واختبار الطباعة
employee = Employee("Ali", 5000)
manager = Manager("Sarah", 8000, "HR")

# طباعة التفاصيل
print(f"Employee: Name: {employee.name}, Salary: {employee.salary}")
print(f"Manager: Name: {manager.name}, Salary: {manager.salary}, Department: {manager.department}")


