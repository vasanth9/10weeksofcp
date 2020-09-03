#classes and objects
""" 
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
""" 
class myclass:
    x=5
p1=myclass()
print(p1.x)
"""
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print("my name is",self.name)
p1=Person("vasanth",19)
print(p1.name,"  ",p1.age)
p1.printname()
#change values
p1.age=40
print(p1.age)
#del
del p1.age
print(p1)
print(p1.name)
""" print(p1.age) gives error age was deleted
Traceback (most recent call last):
  File "classesandobjects.py", line 32, in <module>
    print(p1.age)
AttributeError: 'Person' object has no attribute 'age'
"""
del p1 #object deletion
"""
5
vasanth    19
my name is vasanth
40
<__main__.Person object at 0x7f3d8d87d8e0>
vasanth
"""
#inheritance

class Student(Person):
  def __init__(self, name, age, year):
    super().__init__(name, age)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.name, "to the class of", self.graduationyear) 

s1=Student("Amulya",18,2038)
s1.welcome()
#Welcome Amulya to the class of 2038