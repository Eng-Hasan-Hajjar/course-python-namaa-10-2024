# lesson 19


##ex1
## loop with dict
colors_dict={"red": "#195621" ,"green":"#123456",
 "blue":"#ffff10","white":"#ffffff","black":"#000000"}
for x in colors_dict:
    print("ex1", x)


##ex2
## loop with dict
colors_dict={"red": "#195621" ,"green":"#123456",
 "blue":"#ffff10","white":"#ffffff","black":"#000000"}
for x in colors_dict:
    print("ex2",colors_dict[x] )    

    
##ex3
## loop with dict print values 2th method
colors_dict={"red": "#195621" ,"green":"#123456",
 "blue":"#ffff10","white":"#ffffff","black":"#000000"}
for x in colors_dict.values():
    print("ex3",x )   


##ex4
## loop with dict print keys 2th method
colors_dict={"red": "#195621" ,"green":"#123456",
 "blue":"#ffff10","white":"#ffffff","black":"#000000"}
for x in colors_dict.keys():
    print("ex4",x )   


##ex5
## loop with dict print keys and values
colors_dict={"red": "#195621" ,"green":"#123456",
 "blue":"#ffff10","white":"#ffffff","black":"#000000"}
for x in colors_dict.items():
    print("ex5",x ) 


##ex6
## loop with dict print keys and values
colors_dict={"red": "#195621" ,"green":"#123456",
 "blue":"#ffff10","white":"#ffffff","black":"#000000"}
for x,y in colors_dict.items():
    print("ex6",x,y )   

##ex7
## copy of dict
colors_dict={"red": "#195621" ,"green":"#123456",
 "blue":"#ffff10","white":"#ffffff","black":"#000000"}
copy_colors_dict=colors_dict.copy()
print("ex7",copy_colors_dict )  

##ex8
## copy of dict 2th method
colors_dict={"red": "#195621" ,"green":"#123456",
 "blue":"#ffff10","white":"#ffffff","black":"#000000"}
copy_colors_dict=dict(colors_dict) 
print("ex8",copy_colors_dict )
          

##ex9   
# ## القواميس المتداخلة
myfamily={
"father":{"age":35,"tall":170}    ,
"mather":  {"age":40,"tall":180}   ,
"Ahmad":   {"age":20,"tall":180}  ,
"Hyma":    {"age":16,"tall":170} ,
"Samer":   {"age":11,"tall":150}  ,
} 

print("ex9",myfamily)

##ex10
print("ex10",myfamily["Hyma"])

##ex11
print("ex11",myfamily["Hyma"]["age"])

##ex12   
# ## القواميس المتداخلة
member1={"age":35,"tall":170}
member2={"age":40,"tall":180}
member3={"age":20,"tall":180}
member4={"age":16,"tall":170}
member5= {"age":11,"tall":150}

myfamily={
    "father":  member1  ,
    "mather":  member2   ,
    "Ahmad":   member3  ,
    "Hyma":    member4 ,
    "Samer":   member5 ,
} 
print("ex12",myfamily)

## ex13
myfamily.clear()
print("ex13",myfamily)
##ex14
##fromkeys
x=('key1','key2','key3')
y=0
d_dict=dict.fromkeys(x,y)
print("ex14",d_dict)

##ex15
##fromkeys
x=('key1','key2','key3')
y=('key1','key2','key3')
d_dict=dict.fromkeys(x,y)
print("ex15",d_dict)

##ex16
##fromkeys
x=('key1','key2','key3')

d_dict=dict.fromkeys(x)
print("ex16",d_dict)