##lesson26

from classesPubg import Player
from classesPubg import Weapon
from classesPubg import Vehicle
from classesPubg import Map



player1=Player("Hadi")
player2=Player("Asraa")
player3=Player("Hiba")
player4=Player("Anas")

erangle=Map("Ernagl","8*8 km")

erangle.add_player(player1)
erangle.add_player(player2)
erangle.add_player(player3)
erangle.add_player(player4)

player1.move(10,23)

player2.move(20,23)

player3.move(10,10)

player4.move(10,-23)

player1.take_damage(40)

player2.take_damage(130)

player3.take_damage(12)

player4.take_damage(44)


## الوراثة
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname,self.lname)

x=Person("Hyma","Jamil")
x.printname()

class Student(Person) :
    def __init__(self,fname,lname):
      Person.__init__(self,fname,lname)  


y=Student("Asraa","Mohammad")
y.printname()


class Employee(Person) :
    def __init__(self,fname,lname):
      super().__init__(fname,lname)  


z=Employee("Hiba","Mohammad")
z.printname()



class Teacher(Person) :
    def __init__(self,fname,lname,sub):
      super().__init__(fname,lname)  
      self.subject_teach=sub  

    def printsub(self):
        print(self.subject_teach)
t=Teacher("Anas","Mohammad","Math")
t.printname()
t.printsub()


