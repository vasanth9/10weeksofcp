#functions
def function1():
    print("hurrah")
function1()
function1()
#arguments
def fun2(a1):
    print("youtube "+a1)
fun2("twitter")
fun2("instagram")

#arbitarty arguments *
def func3(*a1):
    print(a1[2])
func3("iron man","captian marvel","hanuman")
""" 
hurrah
hurrah
youtube twitter
youtube instagram
hanuman
""" 
#keyword args
def fun4(a1,a2,a3):
    print("a3 is",a3)
fun4(a1="arjun",a2="krishna",a3="raavan")

# arbitary keyword **kwargs

def fun5(**a):
    print("a3 is",a["a3"])
fun5(a1="arjun",a2="krishna",a3="raavan")



#default args
def fun6(name="Neon"):
    print("my name is "+name)
    
fun6()
fun6("Stark")

#return
def fun7(r):
    return 3.14*r*r
print(fun7(10))

#pass
def func8():
    pass
func8()
"""
a3 is raavan
a3 is raavan
my name is Neon
my name is Stark
314.0
"""
#lambda
x= lambda y:y*y

print(x(3))

x= lambda a,b:a*b
print(x(2,8))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

""" 
9
16
33
"""
