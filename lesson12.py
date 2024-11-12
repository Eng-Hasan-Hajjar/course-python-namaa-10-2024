##ahmed*1
#aziz*43
# Asraa* 63
#heba*61
#Amal*1
#sara *1
##abdmalake*8
## hadi *7

## anas * 6


##lesson12

## اسبقية المشغل (المعاملات)
#Ex1
x=5 * 2 + 7 * 3
print("ex1",x)


## ()
## **
## +x ,-x , ~x
## * , / ,  // ,  %
## + - 
## & 
## ^ 
## |
## == , != , > , < , <= , >= 


## not
## and
## or

#ex2
x = 5 
y = 7
z = x ** y + (x - y ) * 2
print("ex2",z)

### list
## القوائم

my_laptops=["hp", "Asus"]

##create list
## ex3
my_laptops=["hp", "Asus"]
print("Ex3,", my_laptops)

## ex4
my_laptops=list(("hp", "Asus"))
print("Ex4,", my_laptops)

## ex5
my_laptops=["hp", "Asus","hp","lenevo"]
print("Ex5,", my_laptops)


## ex6
my_laptops=["hp", "Asus","hp","lenevo"]
print("Ex6,",len(my_laptops) )

## ex7
my_laptops=["hp", "Asus","lenevo"]
my_laptops_is_good=[True,False,True]
my_laptops_price=[1 ,2,33,5,99]
print("Ex7,",my_laptops)
print("Ex7,",my_laptops_price)
print("Ex7,",my_laptops_is_good)

## ex8
my_laptop=["hp",550 , True]

print("Ex8,",my_laptop)

## ex9
my_laptop=["hp",550 , True]

print("Ex9,",type(my_laptop))


## ex10
my_laptops=["hp", "Asus","lenevo"]

print("Ex10,",my_laptops[1])


## ex11
my_laptops=["hp", "Asus","lenevo"]

print("Ex11,",my_laptops[-1])


## ex12
my_laptops=["hp", "Asus","lenevo","Toshiba","mac","msi","LG","samsung","monster"]

print("Ex12,",my_laptops[1:4])


## ex13
my_laptops=["hp", "Asus","lenevo","Toshiba","mac","msi","LG","samsung","monster"]

print("Ex13,",my_laptops[0:4])
## ex14
my_laptops=["hp", "Asus","lenevo","Toshiba","mac","msi","LG","samsung","monster"]

print("Ex14,",my_laptops[:4])


## ex15
my_laptops=["hp", "Asus","lenevo","Toshiba","mac","msi","LG","samsung","monster"]

print("Ex15,",my_laptops[4:])

## التحقق من وجود عنصر في القائمة

#Ex16
my_laptops=["hp", "Asus","lenevo","Toshiba","mac","msi","LG","samsung","monster"]
if "mac" in my_laptops:
    print("Ex16,","mac exict")


#Ex17
my_laptops=["hp", "Asus","lenevo","Toshiba","mac","msi","LG","samsung","monster"]
my_laptops[6]="Dell"
print("Ex17,",my_laptops[6])


#Ex18
my_laptops=["hp", "Asus","lenevo","Toshiba","mac","msi","LG","samsung","monster"]
my_laptops[0:3]=["Hp"]
print("Ex18,",my_laptops)


#Ex19
my_laptops=["Hp","Toshiba","mac","msi","LG","samsung","monster"]
my_laptops[0:1]=["hp", "Asus","lenevo"]
print("Ex19,",my_laptops)


#Ex20
my_laptops=["Hp","Toshiba","mac","msi","LG","samsung","monster"]
my_laptops.insert(2,"Dell")
print("Ex20,",my_laptops)


#Ex21
my_laptops=["Hp","Toshiba","mac","msi","LG","samsung","monster"]
my_laptops.append("Dell")
print("Ex21,",my_laptops)

#Ex22
my_laptops=["Hp","Toshiba","mac"]
print("Ex22,",my_laptops)
my_laptops2=["msi","LG","samsung","monster"]
print("Ex22,",my_laptops2)
my_laptops.extend(my_laptops2)
print("Ex22,",my_laptops)


#Ex23
my_laptops=["Hp","Toshiba","mac"]
print("Ex23,",my_laptops)
my_laptops2=("msi","LG","samsung","monster")
print("Ex23,",my_laptops2)
my_laptops.extend(my_laptops2)
print("Ex23,",my_laptops)



#Ex24
my_laptops=["Hp","Toshiba","mac"]
my_laptops.remove("mac")
print("Ex24,",my_laptops)



#Ex25
my_laptops=["Hp","Toshiba","mac","Hp","Toshiba","mac"]
my_laptops.remove("mac")
print("Ex25,",my_laptops)

#Ex26
my_laptops=["Hp","Toshiba","mac","Hp","Toshiba","mac"]
my_laptops.pop(2)
print("Ex26,",my_laptops)


#Ex27
my_laptops=["Hp","Toshiba","mac","Hp","Toshiba","mac"]
my_laptops.pop()
print("Ex27,",my_laptops)


#Ex28
my_laptops=["Hp","Toshiba","mac","Hp","Toshiba","mac"]
del my_laptops
#print("Ex28,",my_laptops)

#Ex29
my_laptops=["Hp","Toshiba","mac","Hp","Toshiba","mac"]
del my_laptops[0]

print("Ex29,",my_laptops)


#Ex30
my_laptops=["Hp","Toshiba","mac","Hp","Toshiba","mac"]
my_laptops.clear()
#my_laptops=[]
print("Ex30,",my_laptops)



x=8
y=4
z=3+x/y%2
w = x-2 and x/2
print("the result is ", z , w)




A = 10
B = 3
C = A ** B + (A + B) / 2 - (A * B)

print(C)




















