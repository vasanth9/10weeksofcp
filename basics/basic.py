#python comments
"""hello there,
this is how you comment multiple lines
in python
use #for single line comments
"""
print("hello world!")
#hello world!

#variables
x=10
y="python code"
print(x,y)
#10 python code
x="orange"
print(x)
#orange

x,y,z="orange",10,"games"
print(x,y,z)
#orange 10 games
print(x+z)
#orangegames

#basics of python 

#global varable
def func():
    print("global"+x)

func()
#globalorange
def func2():
    x="aravind"
    print("local"+x)
func2()
#localaravind
print(x)
#orange
def func3():
    global x
    x="changed"
    print("func3"+x)
func3()
#func3changed
print(x)
#changed
"""
datatypes:

Text Type: 	        str
Numeric Types: 	    int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	    dict
Set Types: 	        set, frozenset
Boolean Type: 	    bool
Binary Types:    	bytes, bytearray, memoryview
"""
print(type(x))
#<class 'str'>
x=100
print(type(x))
#<class 'int'>
x=False
print(type(x))
#<class 'bool'>
x=[100,"200"]
print(type(x))
#<class 'list'>
#setting to specific types
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry")) 	
x = tuple(("apple", "banana", "cherry")) 	
x = range(6) 	
x = dict(name="John", age=36) 
x = set(("apple", "banana", "cherry")) 
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

import random
print(random.randrange(1,10))
#displays a random number between 1 to 10
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
"""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#strings ....
#strings are arrays

a="Hello World"
print(a[1])
#e
print(a[2:5])
#llo
print(a[-5:-2])
#wor
print(len(a))
#11
a="         Arav  ind            "
print(a+"end")
#         Arav  ind            end
print(a.strip()+"end")
#Arav  indend
a="Arjun Reddy"
print(a.lower())
#arjun reddy
print(a.upper())
#ARJUN REDDY
print(a.split(" "))
#['Arjun', 'Reddy']
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
#True


#\' 	Single Quote 	
#\\ 	Backslash 	
#\n 	New Line 	
#\r 	Carriage Return 	
#\t 	Tab 	
#\b 	Backspace 	
#\f 	Form Feed 	
#\ooo 	Octal value 	
#\xhh 	Hex value

"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle() 	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

print(bool(False),bool(None),bool(0),bool(""),bool(()),bool([]),bool({}))

#False False False False False False False



