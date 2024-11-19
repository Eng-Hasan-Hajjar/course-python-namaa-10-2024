##ahmed*1
#aziz*43
# Asraa* 64
#heba*61
#Amal*1
#sara *1
##abdmalake*8
## hadi *7

## anas * 6


##lesson13

## for
##  اطبع العناصر  الموجودة في قائمة
## ex1
my_laptops=["hp", "Asus","mac","lenevo"]

for name_lap in my_laptops:
    print(name_lap)

## ex2
my_laptops=["hp", "Asus","mac","lenevo"]
print(my_laptops)

## ex3
## طباعة جميع العناصر من خلال رقم الفهرس

my_laptops=["hp", "Asus","mac","lenevo"]

for i in range(len(my_laptops)):
    print(len(my_laptops))
    print(i,my_laptops[i])


##ex4
## اطبع جميع العناصر باستخدام حلقة while 

my_laptops=["hp", "Asus","mac","lenevo"]
i=0
while i < len(my_laptops):
    print(i,my_laptops[i])
    i +=  1  ## i = i + 1

##ex5
## short hand - for 

my_laptops=["hp", "Asus","mac","lenevo"]
[print(x) for x in my_laptops]

student_names=["Hiba","Anas","Asraa"]
for v in student_names:
    print(v)
[ print(v) for v in student_names]


##ex6
mycars=["bmw","marcedes","aud","sapa"]
chipcar=[]
for u in mycars:
    if "sapa" == u :
        chipcar.append("sapa")
print(chipcar)        



##ex7
mycars=["bmw","marcedes","aud","sapa", "sapa v3"]
chipcar=[]
for u in mycars:
    if "sa" in u :
        chipcar.append("sapa")
print(chipcar)        



##ex8
mycars=["bmw","marcedes","aud","sapa", "sapa v3"]
chipcar=[]
for u in mycars:
    if "sama" in u :
        chipcar.append("sapa")
print(chipcar)        


##ex9
mycars=["bmw","marcedes","aud","sapa", "sapa v3"]
chipcar=[n for n in mycars if  "sa" in n ]
print(chipcar)


##ex10
mycars=["bmw","marcedes","aud","sapa"]
expencar=[n for n in mycars if  "sa" not in n ]
print(expencar)


##ex11
mycars=["bmw","marcedes","aud","sapa"]
expencar=[n for n in mycars if  "sapa" != n ]
print(expencar)


##ex12
mycars=["bmw","marcedes","aud","sapa"]
ourcar=[n for n in mycars ]
print(ourcar)

##ex13
newlist=[c for c in range(10)]
print(newlist)


##ex14
newlist=[c for c in range(10) if c < 5]
print(newlist)


"""
##anas
import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    label = tk.Label(popup, text="Thanks for Accepting")
    label.pack(padx=20, pady=20)

def move_button(event):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    no_button.place(x=x, y=y)

root = tk.Tk()
root.title("instagram: @pythonlearnerr")
root.geometry("400x400")

question_label = tk.Label(root, text="Do you like me?")
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Yes", command=show_popup)
yes_button.pack()

no_button = tk.Button(root, text="No")
no_button.pack()

no_button.bind("<Enter>", move_button)

root.mainloop()

"""

