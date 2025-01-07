

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
   


class Map:
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.players=[]
        self.vehicles=[]
    def add_player(self,player):
        self.players.append(player)
        print(f"{player.name} ")    
