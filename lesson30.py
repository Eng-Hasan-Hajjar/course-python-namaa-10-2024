#lesson30
##file handling

file_v=open("txt_lesson30.txt")
file_v=open("txt_lesson30.txt","r")
## r
## a
file_a=open("txt_lesson302.txt","a")

## w
file_w=open("txt_lesson303.txt","w")

## x
## file_x=open("txt_lesson302.txt","x")## خط
##t
file_w=open("txt_lesson303.txt","rt")

##ex1
file1=open("txt_lesson30.txt","r")
print(file1.read())

## file1=open("المسار الكامل لاي  ملف","r")

##ex2
file1=open("txt_lesson30.txt","r")
print(file1.read(30)) 

##ex3
file1=open("txt_lesson30.txt","r")
print(file1.readline()) 

print(file1.readline()) 
print(file1.readline())


##ex4
file1=open("txt_lesson30.txt","r")
for x in file1:
    print(x)

file1.close()

