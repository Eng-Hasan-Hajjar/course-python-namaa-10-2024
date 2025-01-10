
#ex1
class Animal:
  def __init__(self,name):
    self.name=name
  #abstract method  
  def speak(self):
    raise NotImplementedError("subclass must implement abstract method")
    #pass
  def move(self):
    print(f"{self.name} is moving")

    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

    def speak(self):
        print(f"{self.name} says woof") 

    def fetch(self):
        print(f"{self.name} is fetching the ball")


my_dog=Dog("Buddy","white")

my_dog.move()
my_dog.speak()
my_dog.fetch()

#ex2
class Animal:
  def __init__(self,name):
    self.name=name
  #abstract method  
  def speak(self):
    raise NotImplementedError("subclass must implement abstract method")
    #pass
  def move(self):
    print(f"{self.name} is moving")

class Mammal(Animal):
    def __init__(self,name,fur_color):
        super().__init__(name)
        self.fur_color=fur_color

    def describe(self):
        print(f"{self.name}  mammal + {self.fur_color} color ")


class Dog(Mammal):
    def __init__(self,name,breed,fur_color):
        super().__init__(name,fur_color)
        self.breed=breed

    def speak(self):
        print(f"{self.name} says woof") 

    def fetch(self):
        print(f"{self.name} is fetching the ball")



my_dog=Dog("Buddy","white","black")

my_dog.move()
my_dog.describe()
my_dog.speak()
my_dog.fetch()


# تعدد الأشكال
x="Asraa Hiba Anas Hadi"
print(len(x))
my_tuple=("Asraa" ,"Hiba", "Anas", "Hadi")
print(len(my_tuple))


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Sail!")             

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Fly!")             


car1=Car("BMW","Mu")
boat1=Boat("boatbrand","boatModel")
plane1=Plane("planebrand","planemodel")

for x in (car1 ,boat1 ,plane1 ):
    x.move()




class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
       pass


class Car(Vehicle):
 
    def move(self):
        print("Drive!")

class Boat(Vehicle):
    def move(self):
        print("Sail!")             

class Plane(Vehicle):
    def move(self):
        print("Fly!")             



car1=Car("BMW","Mu")
boat1=Boat("boatbrand","boatModel")
plane1=Plane("planebrand","planemodel")

for x in (car1 ,boat1 ,plane1 ):
    print(x.brand)
    print(x.model)
    x.move()
