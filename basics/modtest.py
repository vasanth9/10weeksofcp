import mymodule
print(mymodule.greeting("vasanth"))
print(mymodule.person)
#alias
import mymodule as mx
print(mx.person["Age"])

#import from module
from mymodule import person
print(person["goal"])