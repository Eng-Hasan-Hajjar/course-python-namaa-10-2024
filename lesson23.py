## lesson23

##ex1
def my_fuc(country="Syria"):
    print("I am from "+ country)

my_fuc()

my_fuc("Iraq")
my_fuc("Eygpt")

#ex2
def my_fuc2(fruits):
    for x in fruits:
        print(x)


fruits222=["banana","orange","apple"]  
my_fuc2(fruits222)   

#ex3
def my_fuc3(x):

    print("this text befor return")
    return 5 * x
   


max2=my_fuc3(5) 
print(max2)


print(my_fuc3(3)) 



#ex4
def my_fuc4():
    v="this text befor return" 
    return v
   
max2=my_fuc4() 
print(max2)
print(my_fuc4()) 

##ex5
def my_fun5():
    pass



#ex6
def my_fun6(x,/):
    print(x)

my_fun6(3)    

def my_fun6(x):
    print(x)

my_fun6(3)
##ex7
def my_fun7(x):
    print(x)

my_fun7(x=3)

""" خطأ
def my_fun7(x,/):
    print(x)

my_fun7(x=3)

"""
#ex8
def my_fun8(*,x):
    print(x)

my_fun8(x=5)


""" خطأ
def my_fun8(*,x):
    print(x)

my_fun8(5)
"""

##ex9
def my_func9(a,b,/,*,c,d):
    print(a+b+c+d)

my_func9(1,2,c=3,d=4)    


###االتعاودية
###الشرط
## حالة أساسية
##ex10
##  n! = n * (n-1) * (n-2) *.......*3*2*1
## 5! = 5 * 4 *3 * 2 * 1=120
## 4! = 4 * 3*2*1=24
## 3! = 3*2*1 =6
## 2! = 2 * 1 =2
## 1! = 1
## 0! = 1

def fact(n):
    
    i="tick"
    if n > 0 :
       
        print(i)
        return n * fact(n-1)
    else :
        return 1

## fact(2)
## 2 * fact(1)
## 2 * 1 * fact(0)
## 2 * 1* 1
print(fact(2))

## fact(3)
## 3 * fact(2)
## 3 * 2 * fact(1)
## 3 * 2 * 1 * fact(0)
## 3 * 2 * 1* 1


print(fact(3))
