##ahmed*1
#aziz*26
# Asraa*40
#heba*41
#Amal*1
#sara *1
##abdmalake*8
## hadi *6


##lesson9

## strings 

## index
##ex1
txt= "Welcome to my Home."
print(txt.index("to"))


##ex2
txt= "Welcome to my Home."
#print(txt.index("حخسهفهخ"))


# string.index(value,start,end)
##ex3
txt= "Welcome to my Home."
print(txt.index("to",2,13))

## string.find(value,start, end )
##ex4
txt= "Welcome to my Home."
print(txt.find("to"))


##ex5
txt= "Welcome to my Home."
print(txt.find("fun"))

if txt.find("jojo") == -1 :
    print("not found")


##ex6
txt= "Welcome to my Home."
print(txt.find("my",1,12))

if txt.find("my") == -1 :
    print("not found")
else :
    print(" found")


## isalpha()
##ex7
##home1
txt= "WelcometomyHome"
print("ex7",txt.isalpha())

if txt.isalpha() :
    print("true")
else :
    print(" false")



## isdigit()
##ex8

txt= "1233"
print(txt.isdigit())

if txt.isdigit() :
    print("true")
else :
    print(" false")


##ex9

txt= "1233.55"
print(txt.isdigit())

if txt.isdigit() :
    print("true")
else :
    print(" false")

## islower()

##ex10
txt= "Welcome to my Home"
print(txt.islower())

if txt.islower() :
    print("true")
else :
    print(" false")



##ex11
#home2
txt= "Welcome to my Home"
txt=txt.lower()
print("ex11",txt)
print(txt.islower())

if txt.islower() :
    print("true")
else :
    print(" false")


##ex12

txt= "Welcome to my Home 13245679 4654"

print("ex12",txt.islower())


##ex13

txt= "welcome to my home 13245679 4654"

print("ex13",txt.islower())


##ex14

txt= " 13245679 4654"

print("ex14",txt.islower())


##isupper()
##ex15

txt= "HELLOW"

print("ex15",txt.isupper())

##join()
## قم بربط جميع العناصر الموجودة في 
# tuple
#  في سلسلة باستخدام حرف 
# #


##ex16

my_tuple= ("hp","asus","del")
txt="#".join(my_tuple)
print("ex16",txt)


###aziz
##replace(oldValue,newValue)
##ex17
text = "welcome to my home"
result = text.replace(" ", "3").isalpha()
print(result)  
print(text.replace(" ", "3"))



##ex18
text = "welcome to my home"
result = text.replace("home", "office")
print("ex18",result)  



##ex19
text = "home welcome to my home welcome to my home"
result = text.replace("home", "office",1)
print("ex19",result)  


##partition()

## ابحث عن كلمة 
##البيت  home
# #وارجع 
# ##tuple  


##ex20
text = "welcome to my home welcome to my "
result = text.partition("home")
print("ex20",result)  


##ex21
text = "welcome to my home welcome to my home welcome to my  "
result = text.partition("home")
print("ex21",result)  


##ex22
text = "welcome to my  welcome to my  welcome to my  "
result = text.partition("home")
print("ex22",result)  


##ex23
text = "home welcome to my  welcome to my  welcome to my  "
result = text.partition("home")
print("ex23 ",result)  

