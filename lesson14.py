## lesson14


## ex1
# قم بتعيين القيم في القائمة الى أحرف كبيرة
cars=["bmw ", "aude" , "marcedecs "]
print("Ex1",cars)
cars=[x.upper() for x in cars]
print("Ex1",cars)

## ex2
## اضبط جميع الماركات الموجودة بالقائمة الى نوع واحد وهو سابا

cars=["bmw ", "aude" , "marcedecs "]
print("Ex2",cars)
cars=["سابا" for x in cars]
print("Ex2",cars)

## ex3
## تم الغاء وجود الودي ب ماركة جديدة سابا
## عدل على الطلب السابق
cars=["bmw ", "aude" , "marcedecs "]
print("Ex3",cars)
cars=[x if x != "aude" else "sapa" for x in cars]
print("Ex3",cars)


## ex4
## تم الغاء وجود الودي ب ماركة جديدة سابا
## عدل على الطلب السابق
cars=["bmw ", "aude" , "marcedecs "]
print("Ex4",cars)
cars=["sapa" if x =="aude" else x for x in cars]
print("Ex4",cars)

## ex5
## sort
## قم بترتيب العناصر الموجودة داخل قائمة ترتيبا أبجديا
cars=["bmw ", "aude" , "marcedecs "]
print("Ex5",cars)
cars.sort()
print("Ex5",cars)

## ex6
## sort
## قم بترتيب العناصر الموجودة داخل قائمة ترتيبا عدديا
steps=[1 ,6 ,4,3,5,2]
print("Ex6",steps)
steps.sort()
print("Ex6",steps)

## ex7
## sort
## قم بترتيب العناصر الموجودة داخل قائمة ترتيبا عدديا
##تنازليا
steps=[1 ,6 ,4,3,5,2]
print("Ex7",steps)
steps.sort(reverse=True)
print("Ex7",steps)


## ex8
## sort
##customize
## قم بفرز قائمة بناءا على مدى قرب الرقم من 50

def dist_50(n):
    return abs(n-50)


ages=[100,50,65,82,23,1]
print("Ex8",ages)
ages.sort(key = dist_50)
print("Ex8",ages)

ages.sort(reverse=True,key = dist_50)
print("Ex8",ages)


## ex9
## sort
##
grades=["good","Excellnt","bad","Middle","very good"]
print("Ex9",grades)
grades.sort()
print("Ex9",grades)


grades=["good","Excellnt","bad","Middle","very good"]
print("Ex9",grades)
grades.sort(key = str.lower)
print("Ex9",grades)

##ex10
## عكس الترتيب
grades=["good","Excellnt","bad","Middle","very good"]
print("Ex10",grades)
grades.reverse()
print("Ex10",grades)


##ex11
##نسخ القائمة
grades=["good","Excellnt","bad","Middle","very good"]
print("Ex11",grades)
grades_copy=grades.copy()
print("Ex11",grades_copy)

##ex12
##الربط القائمة
grades=["good","Excellnt","bad"]
grades2=["Middle","very good"]
grades3=grades+grades2
print("Ex12",grades3)
