##ahmed*1
#aziz*22
# Asraa*35
#heba*37
#Amal*1
#sara *1
##abdmalake*8
## hadi *4


##lesson8

## strings 


## تنسيق السلاسل 
##ex1
age= 35
txt = "My name Ahmad ,I am " + str(age)
print(txt)

## ex2 
## format()
age= 35
txt = "My name Ahmad ,I am {}" 
print(txt.format(age))

## ex3 

## format()
quantity= 4
item_no=1200
price=50

my_order = "you take {} pieces of item no {} for {} price"

print(my_order.format(quantity,item_no,price))


## ex4 

## format()
quantity= 4
item_no=1200
price=50

my_order = "you take {2} pieces of item no {0} for {1} price"

print(my_order.format(item_no,price,quantity))


## ex5

txt="  \"Tesla\" is a good car"
print(txt)

txt="  'Tesla' is a good car"
print(txt)


txt="  'Tesla' \n is a good car"
print(txt)



txt="  'Tesla' \t\t is a good car"
print(txt)



txt='it\'s right'
print(txt)

## Asraa 
example1 = "hello, and welcome to my home."

x = example1.capitalize()

print (x)

example2 = "I love lemon , lemon are my favorite fruit"

y = example2.count("lemon")

print(y)

example3 = "Hello, welcome to my home."

z = example3.index("welcome")

print(z)
## Hiba

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

text = "Hello, how are you? Hello again!"
count_hello = text.count("Hello")
print(count_hello)

#aziz
text = "Hello, World!"
print(text.split(","))

text = "Hello, World!"
print(text.upper()) 
print(text.lower())



##Aziz 

"""
import difflib

# دالة لتحويل الجملة إلى كلمات صغيرة
def lower_super_space(sentence):
    return sentence.lower().split()

# قائمة الأفعال المساعدة
auxiliary_verbs = ['is', 'am', 'are', 'was', 'were', 'has', 'have', 'had', 'will', 'would', 'shall', 'should', 'can', 'could', 'may', 'might', 'be', 'been']

# قائمة الضمائر
pronouns = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 
            'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves',
            'my', 'your', 'his', 'her', 'its', 'our', 'their']

# قائمة كلمات الزمن
time_words = ['yesterday', 'today', 'tomorrow', 'now']

# قائمة الكلمات الصحيحة لتصحيح الأخطاء الإملائية
common_words = ['go', 'went', 'want', 'wanted', 'see', 'saw', 'read', 'reading']

# دالة لتصحيح الأخطاء الإملائية
def correct_spelling(word):
    closest_matches = difflib.get_close_matches(word, common_words + time_words)
    return closest_matches[0] if closest_matches else word

# دالة لتحليل وتصحيح الجملة
def analyze_and_correct_sentence(sentence):
    words = lower_super_space(sentence)  # تحويل الجملة إلى كلمات صغيرة
    
    subject = None
    verb = None
    aux_verb = None
    obj = None
    time_word = None
    corrections = []  # قائمة التصحيحات
    
    # تحليل الكلمات بحثًا عن الفاعل، الفعل، والمفعول
    for i, word in enumerate(words):
        corrected_word = correct_spelling(word)  # تصحيح الأخطاء الإملائية
        if corrected_word != word:
            corrections.append(f"Corrected '{word}' to '{corrected_word}'")

        if corrected_word in pronouns and not subject:
            subject = corrected_word  # تحديد الفاعل
        elif corrected_word in auxiliary_verbs and not aux_verb:
            aux_verb = corrected_word  # تحديد الفعل المساعد
        elif corrected_word.isalpha() and not verb:
            verb = corrected_word  # تحديد الفعل الرئيسي
        elif corrected_word in time_words:
            time_word = corrected_word  # تحديد كلمة الزمن
        elif verb and not obj:
            obj = corrected_word  # تحديد المفعول

    # التحقق من النتائج النهائية
    if corrections:
        print("Corrections:")
        for correction in corrections:
            print(correction)

    # عرض الجملة المحللة
    print(f"Main Clause: {' '.join(words)}")
    print(f"- Subject: '{subject if subject else 'None'}' (This is the person or thing doing the action)")
    print(f"- Main Verb: '{verb if verb else 'None'}' (This is the main action in the sentence)")
    if obj:
        print(f"- Object: '{obj}' (This is the thing receiving the action)")
    if time_word:
        print(f"- Time word: '{time_word}' (This indicates the time of the action)")

    # تحقق من الجملة الصحيحة
    if subject is None or verb is None:
        print("The sentence seems incomplete or incorrect. Make sure it includes both a subject and a verb.")

# برنامج تفاعلي لتعليم الطلاب
while True:
    sentence = input("Enter your sentence (or type 'exit' to stop): ")
    if sentence.lower() == 'exit':
        break
    analyze_and_correct_sentence(sentence)
"""




##Hiba
"""
def analyze_sentence(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    subject = ""
    auxiliary_verb = ""
    main_verb = ""
    if len(words) >= 3:
        subject = words[0]
        auxiliary_verb = words[1]
        main_verb = words[2]      
    elif len(words) == 2:
        subject = words[0]
        main_verb = words[1]
    elif len(words) == 1:
        main_verb = words[0]
    print("النتائج:")
    if subject:
        print(f"الفاعل: {subject}")
    else:
        print("لم يتم العثور على فاعل واضح في الجملة.")
    
    if auxiliary_verb:
        print(f"الفعل المساعد: {auxiliary_verb}")
    
    if main_verb:
        print(f"الفعل الرئيسي: {main_verb}")
    else:
        print("لم يتم العثور على فعل رئيسي في الجملة.")
    if not subject or not main_verb:
        print("يبدو أن الجملة قد تكون غير كاملة أو تحتوي على خطأ نحوي.")
sentence = input("أدخل جملة باللغة الإنجليزية: ")
analyze_sentence(sentence)
"""
"""
##Asraa 

statement = input("Please enter an English statement with a correct form: ")

#spliting the statement into words
words = statement.lower()
words = statement.split()

#varaibles with ever possible construction of the statement
subject = ""
verb = ""
object = ""
adjective =""
adverb = ""
time_adverb = ""
article = ""
helping_verb = ""
preposition = ""

#The list or database that will help in identify the construction
articles = ["a", "an", "the"]
helping_verbs = ["is", "are", "was", "were"]
verbs = ["eat", "play", "run", "write", "read", "jump", "sing", "walk", "go"]
adjectives = ["pretty", "slow", "happy", "sad", "clever", "polite"]
adverbs = ["quickly", "slowly", "happily", "sadly", "loudly", "easily"]
time_adverbs = ["today", "tomorrow", "yesterday", "tonight", "everyday"]
prepositions = ["to", "from", "on", "in", "above", "below"]

#The program

for word in words:
    if word in articles:
        article = word
        print("The article is : " , article)
    elif word in helping_verbs:
        helping_verb = word
        help_verb_index = words.index(helping_verb)
        subject = words[help_verb_index - 1]
        print("The subject is : ", subject)
        print("The helping_verb is : " , helping_verb)
    elif word in prepositions:
        preposition = word
        print("The preposition is : " , preposition)
    elif word in verbs:
        verb = word
        verb_index = words.index(verb)
        subject = words[verb_index - 1]
        print("The subject is : ", subject)
        print("The verb is : " , verb)
    elif word in adjectives:
        adjective = word
        print("The adjective is : " , adjective)
    elif word in adverbs:
        adverb = word
        print("The adverb is : " , adverb)
    elif word in time_adverbs:
        time_adverb = word
        print("The time_adverb is : " , time_adverb)
        break
    else:
        if words.index(word) > 0:
          object = word
          print("The object is : ", object)


"""

