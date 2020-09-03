#math
import math
#built in math
print(min(1,5,3,0))
print(max(1,5,3,0))
print(abs(-9.8))
print(pow(2,6))
"""
0
5
9.8
64
"""
print(math.sqrt(36))
print(math.ceil(1.4))
print(math.floor(1.4))
print(math.pi)
#https://www.w3schools.com/python/module_math.asp
"""
6.0
2
1
3.141592653589793
"""

#json 
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 

"""
Python 	JSON
dict 	Object
list 	Array
tuple 	Array
str 	String
int 	Number
float 	Number
True 	true
False 	false
None 	null
"""
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 

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
  ]
}

print(json.dumps(x))

#format
print(json.dumps(x, indent=4))
#seperators
print(json.dumps(x, indent=4, separators=(". ", " = ")))

#order
print(json.dumps(x, indent=4, sort_keys=True))
"""
{"name": "John", "age": 30}
["apple", "bananas"]
["apple", "bananas"]
"hello"
42
31.76
true
false
null
30
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
{
    "name" = "John". 
    "age" = 30. 
    "married" = true. 
    "divorced" = false. 
    "children" = [
        "Ann". 
        "Billy"
    ]. 
    "pets" = null. 
    "cars" = [
        {
            "model" = "BMW 230". 
            "mpg" = 27.5
        }. 
        {
            "model" = "Ford Edge". 
            "mpg" = 24.1
        }
    ]
}
{
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": false,
    "married": true,
    "name": "John",
    "pets": null
}
"""
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
y = re.search("Spain", txt)

print(x) 
print(y)
"""
None
<re.Match object; span=(12, 17), match='Spain'>
"""
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) 
#['The', 'rain', 'in', 'Spain']
x = re.split("\s", txt, 1)
print(x) 
#['The', 'rain in Spain']
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) 
#The9rain9in9Spain
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) 
#<re.Match object; span=(5, 7), match='ai'>