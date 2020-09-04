import numpy as np
#search 
print("numpy search")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0) #even number indices

print(x) 

#find sorted place

arr = np.array([1,5,7,9])
x=np.searchsorted(arr,[2,5,8,10])
print(x)
"""
(array([1, 3, 5, 7]),)
[1 1 3 4]
"""
print("numpy sort")
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))  #copy , original unchanged
print(arr)

#2d sort
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr)) 

"""
numpy sort
[0 1 2 3]
[3 2 0 1]
[[2 3 4]
 [0 1 5]]
"""

print("filter")
arr= np.array([1,2,3,0,5])
x=[False,False,True,False,True]
newAr=arr[x]
print(newAr)

x=arr%2==0 #even values
newArr=arr[x]
print(newArr)

"""
numpy sort
[0 1 2 3]
[3 2 0 1]
[[2 3 4]
 [0 1 5]]
filter
[3 5]
[2 0]
"""





print("random")

print(np.random.randint(100)) #0-100
print(np.random.rand()) #0-1
#generate random array with 5 elements
x=np.random.randint(100, size=(5))

print(x) 
# 2d array with 3 rows each 5ele
x = np.random.randint(100, size=(3, 5))

print(x) 

#random from given choices
from numpy import random
x = random.choice([3, 5, 7, 9])

print(x) 
#array generation
x = random.choice([3, 5, 7, 9],size=(3,5))

print(x) 