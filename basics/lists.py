thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
#indices
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-2])
print(thislist[-2:-4])
#change
thislist[1]="big banana"
print(thislist)
#loop
for x in thislist:
    print(x)
#check
if "cherry" in thislist:
    print("yes")
#length of list
print(len(thislist))
#add items
thislist.append("added at last")
print(thislist)
thislist.insert(2,"at indices add")
print(thislist)
#remove items
thislist.pop()
print(thislist)
thislist.remove("kiwi")
print(thislist)
del thislist[0]
print(thislist)
#clear
thislist.clear()
print(thislist)
#copy list
thislist=["a","b","c","d"]
print(thislist)
mycopy=thislist.copy()
#list2=list1 makes only reference
print(mycopy)
mycopy2=list(thislist)
print(mycopy2)
#join
list3=thislist+mycopy
print(list3)
list3.extend(mycopy2)
print(list3)
list3.sort()
print(list3)
list3.reverse()
print(list3)
"""
['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
banana
mango
['cherry', 'orange', 'kiwi']
['apple', 'banana', 'cherry', 'orange']
['cherry', 'orange', 'kiwi', 'melon', 'mango']
['orange', 'kiwi']
[]
['apple', 'big banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
apple
big banana
cherry
orange
kiwi
melon
mango
yes
7
['apple', 'big banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'added at last']
['apple', 'big banana', 'at indices add', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'added at last']
['apple', 'big banana', 'at indices add', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
['apple', 'big banana', 'at indices add', 'cherry', 'orange', 'melon', 'mango']
['big banana', 'at indices add', 'cherry', 'orange', 'melon', 'mango']
[]
['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd']
['d', 'd', 'd', 'c', 'c', 'c', 'b', 'b', 'b', 'a', 'a', 'a']
"""