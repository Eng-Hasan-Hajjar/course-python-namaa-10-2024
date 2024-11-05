##ahmed*1
#aziz*26
# Asraa* 55
#heba*56
#Amal*1
#sara *1
##abdmalake*8
## hadi *6


##lesson10
"""
## homework Asraa

# Asking the user to enter a sentence to perform a different operations on it
sentence = input("Please enter a sentence: ")

# 1. Print the sentence in lowercase and uppercase
print("Sentence in lowercase: ", sentence.lower())
print("Sentence in uppercase: ", sentence.upper())
## ممتاز 1 

# 2. Calculate the length of the sentence (including spaces)
length_of_sentence = len(sentence)
print("Length of the sentence (including spaces):", length_of_sentence)
## ممتاز

# 3. Calculate the number of characters (including spaces)
num_characters = length_of_sentence
print("Number of characters (including spaces):", num_characters)
## جيد 


# 4. Calculate the number of characters (excluding spaces)
num_characters = len(sentence.replace(" ", ""))
print("Number of characters (excluding spaces):", num_characters)
## ممتاز


# 5. Calculate the number of words
num_words = len(sentence.split())
print("Number of words:", num_words)

# 6. Get the first and last characters of the sentence
first_char = sentence[0]
last_char = sentence[-1]
print("First character:", first_char)
print("Last character:", last_char)

# 7 Ask the user to enter a number then re-print our sentence with the number times
number = int(input("Enter a number: "))

for i in range(number):
    print(sentence,"\n")

# 8. Finding the vowels and consonants characters
vowels = "aeiou"
vowel_number = 0
consonant_number = 0

sentence_lower = sentence.lower()


for char in sentence_lower:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:
            vowel_number += 1 ## vowel_number = vowel_number + 1
            
        else:
            consonant_number += 1

# Print the counts
print("Number of vowels:", vowel_number)
print("Number of consonants:", consonant_number)


# 9. Extracting characters at even and odd positions
even_chars = sentence[1::2]
odd_chars = sentence[0::2]

print("Characters at even positions:", even_chars)
print("Characters at odd positions:", odd_chars)

# 10. Asking the user to enter a password then check its strength
password = input("Enter your password: ")

# Check for conditions
has_lower = False
has_upper = False
has_digit = False
has_special = False

# Loop through each character in the password to check the conditions
for char in password:
    if char.islower():
        has_lower = True
    elif char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True


if has_lower and has_upper and has_digit and has_special:
    print("Good password")
else:
    print("Weak password")





# homework Hiba

txt=input("Enter your names and age = ")
low=txt.lower()
upp=txt.upper()
l=len(txt)
print(low)
print(upp)
print(l)
print("the first letter is : " + txt[0])
print("the last letter is : " + txt[-1])
odd_positions=""
for i in range(len(txt)):
    if i % 2 == 0:
        odd_positions += txt[i]
print("Characters at odd positions:", odd_positions)
even_positions = ""
for i in range(len(txt)):
    if i % 2 != 0:
        even_positions += txt[i]

print("Characters at even positions:", even_positions)
n = int(input("Enter the number of repetitions: "))

repeated_text = txt * n
print("Repeated text:", repeated_text)


password = input("أدخل كلمة مرور قوية: ")
has_upper = False
has_lower = False
has_symbol = False
symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char in symbols:
        has_symbol = True
if has_upper and has_lower and has_symbol:
    print("كلمة المرور قوية.")
else:
    print("كلمة المرور ليست قوية.").


    """


 ## القيم البوليانية
 # False True
 # 
 # 
a=10

b= 9
if a < b :
    print("True")
else :
     print("False")

print(bool("Hello"))
print(bool(25))

print(bool(a))
print(bool(" "))
print(bool(""))


print(bool(0))

d=[]
print(bool(d))

d=[1,2,3]
print(bool(d))


def my_func():
    return True

print(my_func())   


def my_func():
    return 10

print(my_func())   


def my_func():
    return False
if my_func():
    print("yes")   
else :
    print("no")

## المعاملات

## 
# الحسابية 
## + / * - % ** //
a= 10
b= 15
def sum(k,l):
    c= k+l 
    return c 

print(sum(a,b))

print(a+b)

## % 
a= 10
b=2
print(a/b)
print(a%b)

a= 11
b=2
print(a/b)
print(a%b)
c=666

if c%2 == 0:
    print("even")

else :
    print("odd")    


if c%2 :
    print("odd")

else :
    print("even")    


a=2
b=3
print(b**a)



a=13
b=3
print(b//a)
print(a//b)
print(a/b)
print(a%b)

## الاسناد 

## =   +=    -=   *=   %=     //=

a=3
print(a)
a+=3 ## a=a+3
print(a)
a*=2  ## a=a*2
print(a)


# معاملات المقارنة

## ==   !=   >   <   <=   >= 

b=4
g=7
if b != g :
    print("b != g")
else :
    print("b=g")

##LOGICAL OPERATORS
##  and or not 

f=10
g= 12
if f>11 or g <6:
    print("true")

if f>11 and g <6:
    print("true")



sentence = input("Please enter a sentence: ")

#extra work calculation of alphapitc charachter only

count = 0
for char in sentence:
    if char.isalpha():
        count += 1
print("Length of the sentence (only alphaptic charachters) is :", count)

