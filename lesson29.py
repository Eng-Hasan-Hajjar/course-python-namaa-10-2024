### lesson 29
# modules


import my_mudule as mx

mx.left29("Sar")
a=mx.person1["age"]
print(a)


import platform
x=platform.system()
print(x)


y=dir(mx)
print(y)


y=dir(platform)
print(y)



from my_mudule import person2
d=person2["country"]
print(d)


x=min(5,10,22)
y=max(5,10,22)
print(x)
print(y)


o=abs(-6)
print(o)


p=pow(4,2)
print(p)

import math
print(dir(math))

k=math.sqrt(64)
print(k)

u=math.ceil(1.4)
u2=math.floor(1.4)
print(u,u2)

o=math.pi 
print(o)

s=math.sin(0)
print(s)


### try except
## try except else finally

try:
    print(hh)
except:
    print("exception")   
 

try:
    print("hh")
except:
    print("exception")   
 
try:
    print("hh")
except:
    print("exception")   
else:
    print("else section") 


try:
    print("hh")
    knbl
except:
    print("exception")   
else:
    print("else section") 






try:
    print("hh")
    knbl
except:
    print("exception")   
else:
    print("else section") 
finally:
    print("finally section")




try:
    print("hh")
 
except:
    print("exception")   
else:
    print("else section") 
finally:
    print("finally section")



try:
  f = open("demofile.txt","a")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
