#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#accessing
print(thisdict["model"])
print(thisdict.get("model"))
#change
thisdict["year"]=2000
print(thisdict)
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
Mustang
Mustang
{'brand': 'Ford', 'model': 'Mustang', 'year': 2000}
"""
#loop
print("keys:")
for x in thisdict:
    print(x)
print("values:")
for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)
for x,y in thisdict.items():
    print(x,y)

"""
keys
brand
model
year
values
Ford
Mustang
2000
Ford
Mustang
2000
brand Ford
model Mustang
year 2000
"""
#check
if "model" in thisdict:
    print("yes")
print(len(thisdict)) 
#add
thisdict["color"]="white"
print(thisdict)
#remove 
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["year"]
print(thisdict)
del thisdict
#entire deleted
"""
yes
3
{'brand': 'Ford', 'model': 'Mustang', 'year': 2000, 'color': 'white'}
{'brand': 'Ford', 'year': 2000, 'color': 'white'}
{'brand': 'Ford', 'year': 2000}
{'brand': 'Ford'}
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) 

#copy
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
mydict2 = dict(thisdict)
print(mydict2) 
"""
{}
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
"""

#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily)
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 
print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}