

class Animal:
    def __init__(self, name, family, color, sound):
        self.name = name
        self.family = family
        self.color = color
        self.sound = sound

    def display_characteristics(self):
        return (f"Name: {self.name}\n"
                f"family: {self.family}\n"
                f"Color: {self.color}\n"
                f"Sound: {self.sound}")

animal = Animal(name="jaguar", family="tigers", color="black", sound="Roar")

print(animal.display_characteristics())


#ex1
class Person:
    def __init__(sdd,name,age):
        sdd.name=name
        sdd.age=age


person1=Person("Hadi","22")
person2=Person("Hadi2","25")

print(person1.name)      
print(person1.age) 

##ex2
person1.age=24
print(person1.age) 

##ex3
del person1.age

###print(person1.age)
print(person2.age) 
##ex4
del person2
###print(person2) 


##ex5
class u:
    pass



##pubg

class Player:
    def __init__(self,name,health=120):
        self.name=name
        self.health=health
        self.inventory=[]
        self.position=(0,0)

    def move(self,x,y):
        self.position=(x,y)
        print(f"{self.name} moved to position {self.position}") 

    def take_damage(self,damage):
        self.health-=damage
        if self.health<=0:
            print(f"{self.name} has been eliminated!")
        else:
            print(f"{self.name} took {damage} damage, {self.health} health remaining")

    def pick_up_weapon(self,weapon):
        self.inventory.append(weapon)
        print(f"{self.name} picked up {weapon}")


class Weapon:
    def __init__(self,name,damage):
        self.name=name
        self.damage=damage
    def __str__(self):
        return self.name


akm=Weapon("AKM",49)
m416=Weapon("M416",42)


class Vehicle:
    def __init__(self,typee,max_speed,healh=100):
        self.type=typee
        self.max_speed=max_speed
        self.healh=healh

    def drive(self,destination):
        print(f"Driving {self.type} to {destination} at max speed of {self.max_speed}km/h")

    def take_damage(self,damage):
        self.healh-=damage
        if self.healh<=0:
            print(f"{self.type} has been destroyed!")
        else:
            print(f"{self.type} took {damage} damage, {self.healh} health remaining")
   

buggy=Vehicle("Buggy",80)
buggy.drive("shcool")
buggy.take_damage(20)


class Map:
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.players=[]
        self.vehicles=[]
    def add_player(self,player):
        self.players.append(player)
        print(f"{player.name} "))    


