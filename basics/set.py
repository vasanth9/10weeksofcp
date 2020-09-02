#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset) 
for x in thisset:
  print(x) 

print("banana" in thisset) 

"""
{'banana', 'cherry', 'apple'}
banana
cherry
apple
True
"""
#add
thisset.add("orange")

print(thisset) 
#update
thisset.update(["orange", "mango", "grapes"])

print(thisset) 
#length
print(len(thisset))

#remove
thisset.remove("mango")
print(thisset)
thisset.discard("orange")
print(thisset)
#discard() doesn't raise erroe while remove raises an error
"""
{'cherry', 'orange', 'banana', 'apple'}
{'mango', 'banana', 'apple', 'grapes', 'cherry', 'orange'}
6
{'banana', 'apple', 'grapes', 'cherry', 'orange'}
{'banana', 'apple', 'grapes', 'cherry'}
"""

thisset.pop()
print(thisset)
thisset.clear()
print(thisset)
thisset = {"apple", "banana", "cherry"}

del thisset
try:
    print(thisset) 
except :
    print("deleted")
"""
{'grapes', 'banana', 'apple'}
set()
deleted
"""
#join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) 
"""
{1, 'a', 2, 3, 'c', 'b'}
{1, 'a', 2, 3, 'c', 'b'}
"""

"""
add()                        	Adds an element to the set
clear()	                        Removes all the elements from the set
copy()                       	Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()                	Returns a set, that is the intersection of two other sets
intersection_update()       	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()                	Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()            	        Removes the specified element
symmetric_difference()       	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()                        	Return a set containing the union of sets
update()	                    Update the set with the union of this set and others
"""