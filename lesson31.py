

## json files

## JavaScript Object Notation
## deep seek


import json
x='{"name":"Jamil","age":25,"city":"Aleppo"}'
print(type(x))
y=json.loads(x)
print(y)
print(type(y))
print(y["age"])

#from python into json
u={
"name":"Jamil",
"age":25,
"city":"Aleppo"

}

y=json.dumps(u)
print(y)
print(type(y))
## from objects into json strings
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(type(json.dumps(42)))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


##
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ],

}

print(json.dumps(x))
print(type(json.dumps(x)))

print(json.dumps(x,indent=2))

print(json.dumps(x,indent=4,separators=(".","=")))