#lesson18


## Asraa
##First Part lists
#First Part lists
# 1. Create a list of five cities, then add a new city to the list.
cities = ["New York", "London", "Tokyo", "Sydney", "Paris"]
print("Original list of cities:", cities)
cities.append("Dubai")
print("Updated list of cities:", cities)

# 2. Remove an element from a list containing numbers from one to ten.
numbers = list(range(1, 11))
print("\nOriginal list of numbers:", numbers)
numbers.remove(5)  # Removes the number 5
print("List after removing the number 5:", numbers)

# 3. Reverse the elements in the list of numbers.
numbers.reverse()
print("\nReversed list of numbers:", numbers)

# 4. Find the summation of elements in the list containing numbers from one to ten.
numbers_sum = sum(numbers)
print("\nSummation of the elements in the list:", numbers_sum)

# 5. Create two lists and merge them into one list.
list1 = ["apple", "banana", "cherry"]
list2 = ["orange", "grape", "watermelon"]
merged_list = list1 + list2
print("\nMerged list:", merged_list)

#Second Part Tuples

# 1. Create a tuple with five types of fruits, then add a new fruit to the tuple.
fruits = ("apple", "banana", "cherry", "orange", "grape")
print("Original tuple of fruits:", fruits)

fruits_list = list(fruits)
fruits_list.append("mango")
fruits = tuple(fruits_list)
print("Updated tuple of fruits:", fruits)

# 2. Convert the tuple to a list and then back to a tuple.
fruits_list = list(fruits)
print("\nTuple converted to list:", fruits_list)
fruits_tuple = tuple(fruits_list)
print("List converted back to tuple:", fruits_tuple)

# 3. Create a tuple containing even numbers from 1 to 20, then print the last number in the tuple.
even_numbers = tuple(range(2, 21, 2))
print("\nTuple of even numbers from 1 to 20:", even_numbers)
print("Last number in the tuple:", even_numbers[-1])

# 4. Check if a specific number exists in the tuple or not.
number_to_check = 10
if number_to_check in even_numbers:
    print(f"\n{number_to_check} exists in the tuple.")
else:
    print(f"\n{number_to_check} does not exist in the tuple.")

# 5. Create a tuple containing occurrences of a number, then check how many times the number occurs.
numbers_tuple = (3, 5, 3, 7, 3, 8, 9, 3)
specific_number = 3
count = numbers_tuple.count(specific_number)
print(f"\nThe number {specific_number} occurs {count} times in the tuple.")

#Third part sets
# 1. Create two sets of numbers and find their intersection.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print("Intersection:", intersection)

# 2. Find the union of these two sets.
union = set1.union(set2)
print("\nUnion:", union)

# 3. Remove an element from a set.
set1.remove(3)  # Removing the element 3 from set1
print("\nSet 1 after removing element 3:", set1)

# 4. Create two sets and find out if one of them is a subset of the other.
subset1 = {4, 5}
subset2 = {4, 5, 6, 7, 8}
is_subset = subset1.issubset(subset2)
print("Is Subset 1 a subset of Subset 2?", is_subset)

# 5. Create a set with duplicate elements, then remove the duplicates.
set_with_duplicates = {1, 2, 3, 3, 4, 4, 5}
set_without_duplicates = set(set_with_duplicates)  # Sets automatically remove duplicates
print("\nSet with duplicates:", set_with_duplicates)
print("Set after removing duplicates:", set_without_duplicates)

#Fourth Part dictionaries

# 1. Create a dictionary with names of students as keys and their ages as values, then add a new student.
students = {"Asraa": 29, "Ali": 27, "Ahmed": 25}
print("Original dictionary:", students)
students["Mariem"] = 23  # Adding a new student
print("Updated dictionary:", students)

# 2. Remove a student from the dictionary.
students.pop("Ali")  # Removing the student "Bob"
print("\nDictionary after removing 'Bob':", students)

# 3. Check if a specific student exists in the dictionary.
student_to_check = "Asraa"
if student_to_check in students:
    print(f"\n{student_to_check} exists in the dictionary.")
else:
    print(f"\n{student_to_check} does not exist in the dictionary.")

# 4. Create a dictionary with numbers from 1 to 5 as keys and their squares as values.
squares = {x: x**2 for x in range(1, 6)}
print("\nDictionary of numbers and their squares:", squares)

# 5. Convert the keys to values and values to keys in a dictionary.
inverted_dictionary = {value: key for key, value in squares.items()}
print("\nInverted dictionary (keys as values and values as keys):", inverted_dictionary)


##ُانس
print("*******list*******")
country_list = ["istanbul", "bursa", "izmir", "ankara", "adana"]
city = "diyarbakir"
country_list.append(city)
print(country_list)


numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.pop(2)
print(numbers)


country_list.reverse()
print(country_list)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = sum(numbers)
print(total_sum)


list1 = ["BMW", "MERCEDES", "AUDI", "LAMBORGHINI"]
list2 = ["PORSCHE", "ROLLS ROYCE", "RANGE ROVER"]
list1.extend(list2)
print(list1)


############################################################
print("*******tuples*****")

fruits = ("banana" , "apple" , "Orange" , "avocado")
fruits = fruits + ("pomegranate",)
print(fruits)


my_list = [1,2,3,4,5]
my_tuple = tuple(my_list)
print(my_tuple)
my_new_list = list(my_tuple)
print(my_new_list)


my_tuple = tuple(range(2, 21, 2))
print(my_tuple[-1])


numbers = (1,2,3,4,5,6,7,8,9,10,5,8,9)
element = 4
if element in numbers:
    print("the number in the numbers")
else:
    print("its not in numbers")


my_tuple = (10, 20, 30, 20, 40, 20, 50)
element = 20
count = my_tuple.count(element)
print(f"{element} , {count}")


######################################################
print("*******Dictonaries*****")
students = {
    "ahmed": 20,
    "meryem": 22,
    "mustafa": 19
}
students["sara"] = 21
print(students)


del students["meryem"]
print(students)


if "muhammed" in students:
    print("yes muhammed in the students")
else:
    print("muhammed not in students")

# X 
squares = {}
for x in range(1, 6):
    squares[x] = x**2
print(type(squares))
print(squares)

# X 
original_dict = {
    "ahmed": 20,
    "aziz": 22,
    "aras": 19
}
reversed_dict = {value: key for key, value in original_dict.items()}
print(reversed_dict)


####################################################
print("*******SETS******")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common_elements = set1 & set2
print(common_elements)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
sets = set1.union(set2)
print(sets)


country = {"italy" , "dubai" , "qatar" , "fransa"}
country.remove("qatar")
print(country)


set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
is_subset = set_a.issubset(set_b)
print(is_subset)


my_set = {1, 2, 2, 3, 4, 4, 5}
print(my_set)

#finished :)

##هبة
fruits=("banana","apple","orange","mango")
print(fruits)
fruits=list(fruits)
print(fruits)


even_numbers = (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
print("Even numbers:", even_numbers)
if 32 in even_numbers:
    print("The number 32 is found")
else:
    print("The number 32 is not found")

 # تعريف الـ tuple
data_tuple = (1, 2, 3, 4, 2, 3, 5, 6, 3)
for x in data_tuple :
    if data_tuple.count(x) > 1:
       repeared_items= x
       print("repeared items" ,x)
    else:
       print("not found")  



city=["Hama","homs","alepo","damascuse","idlep"]
print(city)
city.append("latakia")
print(city)
city.reverse()
print(city)
city2=["daraa","tartus"]
city.extend(city2)
print(city)


numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  
print(numbers)
numbers.pop(2)
print(numbers)
numbers_sum = sum(map(int, numbers))  
print(numbers_sum)       


students_ages = {
    "أحمد": 20,
    "ليلى": 22,
    "سارة": 19,
    "محمد": 21
    }

print("قاموس الطلاب:", students_ages)
# حذف طالب
del students_ages["محمد"]

print("القاموس بعد الحذف:", students_ages)

reversed_dict = dict(zip(students_ages.values(), students_ages.keys()))
print("القاموس المعكوس:", reversed_dict)

squares_dict = {}
for num in range(1, 6): 
    squares_dict[num] = num ** 2 
print("قاموس المربعات:", squares_dict)
# إنشاء مجموعتين
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common_elements = set1 & set2  
print("العناصر المشتركة بين المجموعتين:", common_elements)

merged_set = set1 | set2
print("Marged set is: ", merged_set)


##ex1

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career_name= career["3"]
print("ex1",career_name)

##ex2

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career_name= career.get("3")
print("ex2",career_name)

##ex3

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career_keys= career.keys()
print("ex3",career_keys)


##ex4

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career["5"]="chef"
career_keys= career.keys()
print("ex4",career_keys)


##ex5

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career["5"]="chef"
career_values= career.values()
print("ex5",career_values)


##ex6

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career["5"]="chef"
career_elements= career.items()
print("ex6",career_elements)


##ex7

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career["5"]="chef"
if "6" in career:
    print("ex7","6 exit in dict")
else :
    print("ex7","6 not exit in dict")


##ex8

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career["1"]="chef"

print("ex8",career)



##ex9

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career.update({"1":"chef"})

print("ex9",career)

##ex10

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career.pop("1")

print("ex10",career)


##ex11

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
del career["1"]

print("ex11",career)



##ex12

career={"1":"doctor","2":"eng","3":"teacher","4":"security"}
career.popitem()

print("ex12",career)

