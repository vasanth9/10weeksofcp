#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple=("banana","apple","choclate","P","u","r")
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:4])
print(thistuple[-4:-1])
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#thistuple[1]="rp" not possible
print(thistuple)
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 
#loop
for u in x:
    print(u)
"""
('banana', 'apple', 'choclate', 'P', 'u', 'r')
apple
r
('choclate', 'P')
('choclate', 'P', 'u')
('banana', 'apple', 'choclate', 'P', 'u', 'r')
('apple', 'kiwi', 'cherry')
apple
kiwi
cherry
"""
#check

if "kiwi" in x:
    print("yes")
#length
print(len(x))

#del
del x
#print(x) deleted
#join two tuples
z=("r","p","l")
d=("o","y","i")
s=z+d
print(s)
"""
yes
3
('r', 'p', 'l', 'o', 'y', 'i')
"""
