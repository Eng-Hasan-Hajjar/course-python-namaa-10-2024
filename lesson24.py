
##lesson 24
##lambda
## lambda arguments : expression
##ex1
x=lambda a : a + 1

print(x(3))

##ex2
x=lambda a ,b : a * b

print(x(3,4))

##ex3
x=lambda a ,b,c : a + b + c 

print(x(3,4,3))


##ex4
def my_func(n):
    return lambda a:a*n
x=my_func(2) 

print(x(3))
print(x(4))


##ex5
def my_func(n):
    return lambda a:a*n
x=my_func(3) 

print(x(3))
print(x(4))


##ex5
sum = lambda a,b:a+b
print(sum(5,3))


##ex6
numbers=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda x:x%2==0,numbers))
print(evens)

