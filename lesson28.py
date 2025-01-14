##leeson28
##scope

def my_func():
    x=300
    print(x)
my_func()    




def my_func():
    x=300
    def my_inner_func():
        print(x)
    my_inner_func()
    
my_func()  

######
y=300
def mu_func():
    print(y)
mu_func()
print(y)    



####
z=300
def mu_func():
    z=150
    print(z)
mu_func()
print(z) 

####
z=300
def mu_func():
    global z
    z=150
    print(z)
mu_func()
print(z) 



####

def mu_func1():
    z=300
    def mu_func2():
        nonlocal z
        z=130
        print(z)
    mu_func2() 
    return z   
k=mu_func1()
print(k) 




